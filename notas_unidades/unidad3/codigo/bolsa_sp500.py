"""Modulo de la dinamica "La bolsa del S&P 500" de 2_estadistica_y_datos.md
(seccion 4.4).

Cada mesa, una pareja, saca con reemplazo 20 papelitos de una bolsa con 50
rendimientos anuales que imitan los 98 del S&P 500 (1928-2025). Las
instrucciones y los calculos estan a la vista en el notebook bolsa_sp500.ipynb:
la parte 1 estima
con los primeros 4 papelitos de cada mesa, con sus 20 y con los de todo el
grupo juntos, y la parte 2 ilustra la convergencia con muestras simuladas.
Este modulo define la bolsa, imprime la hoja de papelitos, valida las
respuestas, simula una clase y dibuja las graficas del notebook.

La bolsa discretiza los datos (BOLSA): cada papelito lleva el centro de un
intervalo de 10 puntos, y hay tantos de cada valor como anios cayeron en ese
intervalo, a escala de 50. Su media y su desviacion estandar se conocen, asi
que cada estimacion del grupo se compara con la verdad.

Uso desde la linea de comandos (desde la raiz del repo), solo para la hoja:
    python notas_unidades/unidad3/codigo/bolsa_sp500.py papelitos [salida.pdf]

Los datos se registran en una celda del notebook, en un diccionario: cada
mesa y sus 20 rendimientos en por ciento, en el orden en que salieron, como
{"mesa_1": [-5, 15, 25, 35, ...], "mesa_2": [...]}.
"""
import argparse
import os

import matplotlib
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from scipy.stats import norm

NAVY = "#1E2761"
GOLD = "#C9A227"
GRAY = "#5B6482"
LGRAY = "#A6ADC7"
BODY = "#27314D"
RED = "#C0392B"

plt.rcParams["font.family"] = "Calibri"

CODIGO_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PAPELITOS = os.path.join(CODIGO_DIR, "..", "..", "..", "practicas", "unidad3",
                             "papelitos_bolsa_sp500.pdf")
# Centro de cada intervalo de 10 puntos y cuantos papelitos lo llevan. Los 98
# anios escalados a 50 dan 0.5, 1.0, 1.5, 3.1, 7.1, 7.7, 10.7, 9.2, 6.6, 2.0 y
# 0.5 papelitos de -45% a +55%; el redondeo conserva un papelito de -45%, como
# 1931, y deja la media en 11.8%, la desviacion en 19.4% y 26% de perdidas,
# frente a 11.86%, 19.30% y 26.5% en los datos.
BOLSA = {-45: 1, -35: 1, -25: 1, -15: 3, -5: 7, 5: 7, 15: 12, 25: 9, 35: 7, 45: 2}
N_PAPELITOS = 20  # la muestra de cada mesa
N_INICIO = 4  # los primeros papelitos, con los que se estima primero
SIMULACIONES = 10_000
SEMILLA = 2026


def bolsa():
    """Los 50 papelitos, en por ciento, de menor a mayor."""
    return np.repeat(list(BOLSA), list(BOLSA.values())).astype(float)


def verdad(b):
    """Los parametros de la bolsa, la poblacion de la dinamica."""
    orden = np.sort(b)
    return {"media": b.mean(), "sigma": b.std(), "n": len(b),
            "var95": orden[int(np.ceil(0.05 * len(b))) - 1], "p_perder": np.mean(b < 0)}


def _formato(x):
    return f"{x:+g}%".replace("-", "−")


def papelitos(salida):
    """Una hoja tamanio carta con los 50 papelitos en una cuadricula de 5 x 10,
    con el signo y el porcentaje en letra grande. Se imprime una copia por
    bolsa."""
    b = bolsa()
    columnas, filas = 5, 10
    fig = plt.figure(figsize=(8.5, 11))
    fig.text(0.5, 0.975, "La bolsa del S&P 500: recorta por las líneas punteadas",
             ha="center", va="center", fontsize=12, color=GRAY)
    ax = fig.add_axes([0.04, 0.03, 0.92, 0.92])
    ax.set_xlim(0, columnas)
    ax.set_ylim(filas, 0)
    ax.axis("off")
    for k in range(columnas + 1):
        ax.axvline(k, color=LGRAY, lw=0.8, ls="--")
    for k in range(filas + 1):
        ax.axhline(k, color=LGRAY, lw=0.8, ls="--")
    for i, x in enumerate(b):
        fila, col = divmod(i, columnas)
        ax.text(col + 0.5, fila + 0.5, _formato(x), ha="center", va="center", fontsize=30,
                fontweight="bold", color=RED if x < 0 else NAVY)
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    fig.savefig(salida)
    plt.close(fig)
    print(f"papelitos: {os.path.normpath(salida)}  ({len(b)} valores; imprime una copia por bolsa)")


def simular_clase():
    """Una clase ficticia de 15 mesas, para probar el notebook antes de la
    sesion, en el mismo formato que la celda de captura. Trae dos casos que la
    validacion debe atender: una muestra con 19 valores y un valor que no esta
    en la bolsa."""
    b = bolsa()
    rng = np.random.default_rng(SEMILLA)
    datos = {f"mesa_{k}": [float(x) for x in rng.choice(b, N_PAPELITOS)] for k in range(1, 16)}
    datos["mesa_4"] = datos["mesa_4"][:19]  # registro 19 valores
    datos["mesa_6"][0] /= 10  # registro su primer valor con el punto corrido
    return datos


def _decimas(x):
    """Los rendimientos en decimas de punto, como enteros, para compararlos sin
    errores de redondeo."""
    return np.round(10 * np.asarray(x)).astype(int)


def validar(datos, b):
    """Recorre los datos registrados, avisa de las muestras que no tienen
    N_PAPELITOS valores (y las deja fuera) y de los valores que no estan en la
    bolsa, que suelen ser errores de captura (se conservan). Un error de signo
    no se detecta, porque cada valor de la bolsa tiene su negativo. Devuelve
    una lista de muestras con sus valores como arreglo."""
    validas = []
    en_bolsa = set(_decimas(b).tolist())
    for mesa, valores in datos.items():
        if len(valores) != N_PAPELITOS:
            print(f"AVISO {mesa}: tiene {len(valores)} valores y deben ser {N_PAPELITOS};"
                  " se omite hasta que lo corrija")
            continue
        raros = [v for v, d in zip(valores, _decimas(valores)) if d not in en_bolsa]
        if raros:
            print(f"AVISO {mesa}: {', '.join(_formato(v) for v in raros)} no esta en la"
                  " bolsa; revisa la captura")
        validas.append({"mesa": mesa, "valores": np.array(valores, dtype=float)})
    return validas


def _mostrar(fig):
    fig.tight_layout()
    plt.show()


def _estilo(ax, xlabel=None, porcentaje_x=True):
    ax.tick_params(colors=GRAY, labelsize=10)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_color(LGRAY)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=11, color=GRAY)
    if porcentaje_x:
        ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(100, decimals=0))


def _titulo(ax, texto):
    ax.set_title(texto, fontsize=12.5, color=NAVY, fontweight="bold", loc="left", pad=10)


def fig_distribucion(todas, b=None):
    """El histograma de todos los papelitos que saco el grupo; con la bolsa,
    encima el de los 50 papelitos."""
    bordes = np.arange(-50, 51, 10)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.hist(todas, bins=bordes, density=True, color=NAVY, alpha=0.85, edgecolor="white",
            linewidth=2, label=f"el grupo ({len(todas)} papelitos)")
    if b is not None:
        ax.hist(b, bins=bordes, density=True, histtype="step", color=GOLD, lw=2.6,
                label=f"la bolsa ({len(b)} papelitos)")
    ax.set_yticks([])
    ax.legend(loc="upper left", fontsize=9.5, frameon=False, labelcolor=BODY)
    _estilo(ax, "Rendimiento anual")
    _titulo(ax, "Todos los papelitos del grupo")
    _mostrar(fig)


def fig_medias(tabla):
    """Las medias de cada mesa en dos franjas: con sus primeros 4 papelitos
    arriba y con los 20 abajo, con su dispersion y su cociente."""
    rng = np.random.default_rng(SEMILLA)
    fig, ax = plt.subplots(figsize=(10, 4.2))
    disp = {}
    for y, n in ((1, N_INICIO), (0, N_PAPELITOS)):
        medias = tabla[f"media_{n}"].to_numpy()
        disp[n] = medias.std(ddof=1)
        ax.scatter(medias, y + rng.uniform(-0.15, 0.15, len(medias)), s=40, color=NAVY,
                   edgecolor="white", zorder=3)
        ax.text(0.01, y + 0.3, f"con {n} papelitos: dispersión {disp[n]:.1f}%, "
                f"medias negativas: {np.sum(medias < 0)}", transform=ax.get_yaxis_transform(),
                fontsize=10.5, color=BODY)
    ax.axvline(0, color=LGRAY, lw=1)
    ax.set_ylim(-0.6, 1.5)
    ax.set_yticks([])
    _estilo(ax, "Media de la muestra")
    _titulo(ax, f"Una bolsa, muchas historias: con {N_PAPELITOS} papelitos la dispersión es "
                f"{disp[N_PAPELITOS] / disp[N_INICIO]:.2f} veces la de {N_INICIO}")
    _mostrar(fig)


def fig_intervalos_clase(tabla, grupo=None, v=None):
    """El intervalo al 95% de cada mesa, con sus primeros 4 papelitos (linea
    delgada) y con los 20 (linea gruesa). Con grupo, agrega al final el
    intervalo de todas las muestras juntas; con la verdad, la media de la bolsa
    y en rojo los intervalos que no la atrapan."""
    etiquetas = [str(m).replace("_", " ") for m in tabla["mesa"]]
    y = np.arange(len(tabla), dtype=float)
    if grupo is not None:
        etiquetas.append(f"el grupo ({grupo['n']})")
    fig, ax = plt.subplots(figsize=(9, 0.32 * len(etiquetas) + 1.8))
    atrapan = {}
    for n, dy, grosor, color in ((N_INICIO, -0.17, 1.2, LGRAY), (N_PAPELITOS, 0.17, 2.6, GRAY)):
        bajo, alto = tabla[f"bajo_{n}"].to_numpy(), tabla[f"alto_{n}"].to_numpy()
        atrapa = np.ones(len(tabla), bool) if v is None else (bajo <= v["media"]) & (v["media"] <= alto)
        atrapan[n] = atrapa.sum()
        ax.hlines(y + dy, bajo, alto, colors=[color if a else RED for a in atrapa], lw=grosor,
                  zorder=2)
        ax.scatter(tabla[f"media_{n}"], y + dy, s=10 if n == N_INICIO else 18, color=NAVY,
                   zorder=3)
    if grupo is not None:
        yg = len(tabla) + 0.5
        dentro = v is None or grupo["bajo"] <= v["media"] <= grupo["alto"]
        ax.hlines(yg, grupo["bajo"], grupo["alto"], colors=NAVY if dentro else RED, lw=4, zorder=2)
        ax.scatter([grupo["media"]], [yg], s=30, color=NAVY, zorder=3)
        y = np.append(y, yg)
    if v is None:
        titulo = f"El intervalo de cada quien, con {N_INICIO} y con {N_PAPELITOS} papelitos"
    else:
        ax.axvline(v["media"], color=GOLD, lw=2.2, zorder=1)
        titulo = (f"Atrapan la media de la bolsa, {v['media']:.2f}%: {atrapan[N_INICIO]} de "
                  f"{len(tabla)} con {N_INICIO} papelitos y {atrapan[N_PAPELITOS]} con {N_PAPELITOS}")
    ax.set_yticks(y, etiquetas, fontsize=8.5)
    ax.invert_yaxis()
    ax.legend(handles=[Line2D([], [], color=LGRAY, lw=1.2, label=f"con {N_INICIO} papelitos"),
                       Line2D([], [], color=GRAY, lw=2.6, label=f"con {N_PAPELITOS} papelitos")],
              loc="lower right", fontsize=9.5, frameon=False, labelcolor=BODY)
    _estilo(ax, "Rendimiento esperado")
    _titulo(ax, titulo)
    _mostrar(fig)


def fig_lgn(trayectorias, v):
    """Parte 2, ley de los grandes numeros: la media acumulada de varias
    secuencias de papelitos, con la banda de 1.96 sigma/raiz(n) alrededor de
    la media de la bolsa."""
    n = np.arange(1, trayectorias.shape[1] + 1)
    margen = 1.96 * v["sigma"] / np.sqrt(n)
    fig, ax = plt.subplots(figsize=(10, 4.4))
    ax.fill_between(n, v["media"] - margen, v["media"] + margen, color=GOLD, alpha=0.15, lw=0,
                    label=r"media de la bolsa $\pm\, 1.96\, \sigma/\sqrt{n}$")
    for t in trayectorias:
        ax.plot(n, t, color=NAVY, lw=1.2, alpha=0.8)
    ax.axhline(v["media"], color=GOLD, lw=2.2, label=f"media de la bolsa, {v['media']:.2f}%")
    ax.set_xscale("log")
    ax.set_ylim(-50, 50)
    ax.xaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(100, decimals=0))
    _estilo(ax, "Papelitos sacados, n (escala logarítmica)", porcentaje_x=False)
    ax.set_ylabel("Media de los primeros n", fontsize=11, color=GRAY)
    ax.legend(loc="upper right", fontsize=9.5, frameon=False, labelcolor=BODY)
    _titulo(ax, f"{len(trayectorias)} historias: cada media se acerca a la de la bolsa")
    _mostrar(fig)


def fig_glivenko(valores, f_bolsa, empiricas):
    """Parte 2, Glivenko-Cantelli: la distribucion empirica de una muestra de
    cada tamanio frente a la de la bolsa, con su distancia maxima."""
    fig, ejes = plt.subplots(1, len(empiricas), figsize=(12, 3.8), sharey=True)
    xs = np.concatenate([[-55], valores, [55]])
    for ax, (n, f_n) in zip(ejes, empiricas.items()):
        ax.step(xs, np.concatenate([[0], f_bolsa, [1]]), where="post", color=GOLD, lw=2.4,
                label="la bolsa")
        ax.step(xs, np.concatenate([[0], f_n, [1]]), where="post", color=NAVY, lw=1.6,
                label="la muestra")
        _estilo(ax, "Rendimiento anual")
        ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(25))
        _titulo(ax, f"n = {n:,}: distancia {np.max(np.abs(f_n - f_bolsa)):.2f}")
    ejes[0].set_ylabel("Proporción de papelitos hasta x", fontsize=11, color=GRAY)
    ejes[0].legend(loc="upper left", fontsize=9.5, frameon=False, labelcolor=BODY)
    _mostrar(fig)


def fig_tcl(medias, v):
    """Parte 2, teorema central del limite: las medias de SIMULACIONES
    muestras de cada tamanio, frente a la normal con media mu y desviacion
    sigma/raiz(n). Con un papelito es la bolsa misma."""
    fig, ejes = plt.subplots(len(medias), 1, figsize=(9, 7.6), sharex=True)
    x = np.linspace(-50, 50, 1000)
    for ax, (n, m) in zip(ejes, medias.items()):
        # Cada papelito termina en 5, asi que las medias caen en una reticula
        # de paso 10/n que empieza en (5n mod 10)/n; cada barra junta los
        # puntos de la reticula que caben en un cuarto de sigma/raiz(n).
        paso, origen = 10 / n, (5 * n) % 10 / n
        ancho = paso * max(1, round(v["sigma"] / np.sqrt(n) / 4 / paso))
        k = np.ceil(60 / ancho)
        bordes = origen - paso / 2 + ancho * np.arange(-k, k + 1)
        ax.hist(m, bins=bordes, density=True, color=NAVY, alpha=0.8, edgecolor="white",
                linewidth=0.5, zorder=2)
        if n > 1:
            ax.plot(x, norm.pdf(x, v["media"], v["sigma"] / np.sqrt(n)), color=GOLD, lw=2.2,
                    zorder=3)
        ax.axvline(v["media"], color=RED, lw=1.4, ls="--", zorder=4)
        etiqueta = "1 papelito: la bolsa" if n == 1 else f"n = {n}"
        ax.text(0.01, 0.92, etiqueta, transform=ax.transAxes, fontsize=11, color=NAVY,
                fontweight="bold", va="top")
        ax.text(0.99, 0.92, f"desviación de las medias: {m.std():.2f}%\n"
                rf"$\sigma/\sqrt{{n}}$ = {v['sigma'] / np.sqrt(n):.2f}%",
                transform=ax.transAxes, fontsize=10, color=BODY, va="top", ha="right")
        ax.set_yticks([])
        _estilo(ax)
        ax.spines["left"].set_visible(False)
    ejes[0].set_xlim(-50, 50)
    ejes[-1].set_xlabel("Rendimiento anual promedio de la muestra", fontsize=11, color=GRAY)
    _titulo(ejes[0], f"Medias de {SIMULACIONES:,} muestras sacadas de la bolsa")
    _mostrar(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="orden", required=True)
    p = sub.add_parser("papelitos", help="PDF con la hoja de los 50 papelitos")
    p.add_argument("salida", nargs="?", default=OUT_PAPELITOS)
    args = parser.parse_args()
    papelitos(args.salida)


if __name__ == "__main__":
    matplotlib.use("Agg")
    main()
