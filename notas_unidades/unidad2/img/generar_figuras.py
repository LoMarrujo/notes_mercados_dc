"""Genera los diagramas de flujo de efectivo de las mecanicas de pago
usados en 0_mercado_e_instrumentos_deuda.md, seccion "Como paga un
instrumento: mecanicas y vector de flujos". Se versiona junto a las imagenes que produce
para que sean reproducibles: si el contenido cambia, se corrige este
script y se vuelve a correr, nunca se edita el .png a mano.

Uso:
    python notas_unidades/unidad2/img/generar_figuras.py
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "codigo"))
from calibracion import calibrar_vasicek, evaluar_oos  # noqa: E402
from datos_fred import cargar  # noqa: E402
from simulacion import DT, simular_precios  # noqa: E402
from valuacion import tabla_amortizacion  # noqa: E402

NAVY = "#1E2761"
GOLD = "#C9A227"
GRAY = "#5B6482"
LGRAY = "#A6ADC7"
BODY = "#27314D"

plt.rcParams["font.family"] = "Calibri"
sns.set_theme(style="white", rc={"axes.edgecolor": LGRAY, "axes.linewidth": 0.8})

IMG_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DESCUENTO = os.path.join(IMG_DIR, "flujo_descuento.png")
OUT_CUPON_FIJO = os.path.join(IMG_DIR, "flujo_cupon_fijo.png")
OUT_CUPON_VARIABLE = os.path.join(IMG_DIR, "flujo_cupon_variable.png")
OUT_AMORTIZACION = os.path.join(IMG_DIR, "flujo_amortizacion.png")
OUT_PRECIO_REND = os.path.join(IMG_DIR, "precio_rendimiento.png")
OUT_CURVA_BONO = os.path.join(IMG_DIR, "curva_ubicar_bono.png")
OUT_HACIA_LA_PAR = os.path.join(IMG_DIR, "precio_hacia_la_par.png")
OUT_AMORT_TABLA = os.path.join(IMG_DIR, "amortizacion_interes_capital.png")
OUT_FIJO_VARIABLE = os.path.join(IMG_DIR, "fijo_vs_variable_simulacion.png")
OUT_CALIBRACION = os.path.join(IMG_DIR, "calibracion_tasas.png")


def _scale(f):
    return np.sign(f) * np.sqrt(abs(f))


def _panel_flujo(ax, periods, flows, titulo, y_max=None):
    """Dibuja, sobre un eje ya existente, una linea de tiempo con una
    flecha vertical por flujo: hacia arriba (azul) si es entrada, hacia
    abajo (dorado) si es salida. Reutilizable en figuras de un solo panel
    o de varios paneles apilados."""
    ax.axhline(0, color=LGRAY, lw=1.4, zorder=1)
    t_min, t_max = min(periods), max(periods)
    ax.annotate("", xy=(t_max + 0.55, 0), xytext=(t_min - 0.35, 0),
                arrowprops={"arrowstyle": "-|>", "color": LGRAY, "lw": 1.4})
    ax.text(t_max + 0.6, 0, "tiempo", va="center", fontsize=10, color=GRAY)

    for t, f in zip(periods, flows):
        y = _scale(f)
        color = NAVY if f > 0 else GOLD
        ax.annotate("", xy=(t, y), xytext=(t, 0),
                    arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.6, "mutation_scale": 16})
        label = f"${f:,.2f}" if f > 0 else f"-${abs(f):,.2f}"
        va, dy = ("bottom", 10) if f > 0 else ("top", -10)
        ax.annotate(label, xy=(t, y), xytext=(0, dy), textcoords="offset points",
                    ha="center", va=va, fontsize=11, color=BODY, fontweight="bold")
        ax.annotate(str(t), xy=(t, 0), xytext=(0, 10 if f < 0 else -18),
                    textcoords="offset points", ha="center",
                    va="bottom" if f < 0 else "top", fontsize=10, color=GRAY)

    if y_max is None:
        y_max = max(abs(_scale(f)) for f in flows) * 1.335
    ax.set_xlim(t_min - 0.6, t_max + 1.3)
    ax.set_ylim(-y_max, y_max)
    ax.axis("off")
    if titulo:
        ax.set_title(titulo, fontsize=12.5, color=NAVY, fontweight="bold", loc="left", pad=10)


def fig_flujo_efectivo(periods, flows, out_path, titulo):
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    _panel_flujo(ax, periods, flows, titulo)
    fig.tight_layout()
    fig.savefig(out_path, dpi=200, facecolor="white")
    print(f"figura generada: {out_path}")


def fig_flujo_cupon_variable():
    """Flujo de un certificado bursatil a tasa variable, nominal 100 y
    tasa de referencia 10%: el cupon mas proximo (t=1) ya quedo fijo en
    el ultimo reseteo (a la par con la tasa vigente), los siguientes
    (t=2, t=3) dependen de una tasa de referencia que todavia no se
    conoce. Los flujos conocidos se dibujan solidos con su monto en
    pesos; los inciertos, punteados y etiquetados con el simbolo C_t."""
    periods = [0, 1, 2, 3]
    flows = [-100, 10, 11, 111]
    known = [True, True, False, False]
    labels = [None, "$10", "$C_2$", "$C_3+100$"]

    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.axhline(0, color=LGRAY, lw=1.4, zorder=1)
    t_min, t_max = min(periods), max(periods)
    ax.annotate("", xy=(t_max + 0.55, 0), xytext=(t_min - 0.35, 0),
                arrowprops={"arrowstyle": "-|>", "color": LGRAY, "lw": 1.4})
    ax.text(t_max + 0.6, 0, "tiempo", va="center", fontsize=10, color=GRAY)

    for t, f, k, lab in zip(periods, flows, known, labels):
        y = _scale(f)
        if f < 0:
            color, style = GOLD, "-"
        else:
            color, style = (NAVY, "-") if k else (LGRAY, "--")
        ax.annotate("", xy=(t, y), xytext=(t, 0),
                    arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.6,
                                "mutation_scale": 16, "linestyle": style})
        label = lab if lab else f"-${abs(f):,.2f}"
        va, dy = ("bottom", 10) if f > 0 else ("top", -10)
        text_color = BODY if (f < 0 or k) else GRAY
        ax.annotate(label, xy=(t, y), xytext=(0, dy), textcoords="offset points",
                    ha="center", va=va, fontsize=11, color=text_color, fontweight="bold")
        ax.annotate(str(t), xy=(t, 0), xytext=(0, 10 if f < 0 else -18),
                    textcoords="offset points", ha="center",
                    va="bottom" if f < 0 else "top", fontsize=10, color=GRAY)

    y_max = max(abs(_scale(f)) for f in flows) * 1.335
    ax.set_xlim(t_min - 0.6, t_max + 1.3)
    ax.set_ylim(-y_max, y_max)
    ax.axis("off")
    ax.set_title("Flujo de efectivo con cupón variable (certificado bursátil)",
                  fontsize=12.5, color=NAVY, fontweight="bold", loc="left", pad=10)
    fig.tight_layout()
    fig.savefig(OUT_CUPON_VARIABLE, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_CUPON_VARIABLE}")


def fig_flujo_amortizacion():
    """Bullet (todo el capital al vencimiento) vs. amortizacion con
    capital constante (sistema aleman) vs. amortizacion con pago total
    constante (sistema frances): mismo capital prestado ($100), misma
    tasa (10%) y mismo plazo (3 periodos), tres formas de repartir el
    pago. El pago frances sale de despejar c en la formula de anualidad:
    c = a r / (1 - (1+r)^-N)."""
    a, r, n = 100, 0.10, 3
    periods = [0, 1, 2, 3]
    bullet = [-a, a * r, a * r, a * r + a]
    aleman = [-a] + [round(a / n + r * (a - a / n * t), 2) for t in range(n)]
    c_frances = round(a * r / (1 - (1 + r) ** -n), 2)
    frances = [-a] + [c_frances] * n

    y_max = max(abs(_scale(f)) for f in bullet + aleman + frances) * 1.335

    fig, axes = plt.subplots(3, 1, figsize=(7.5, 8.0))
    _panel_flujo(axes[0], periods, bullet, "Bullet: todo el capital al vencimiento", y_max=y_max)
    _panel_flujo(axes[1], periods, aleman, "Amortizado: capital constante cada periodo (sistema alemán)", y_max=y_max)
    _panel_flujo(axes[2], periods, frances, "Amortizado: pago total constante cada periodo (sistema francés)", y_max=y_max)
    fig.tight_layout()
    fig.savefig(OUT_AMORTIZACION, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_AMORTIZACION}")


def _precio_bono(c, n, r, vn=100):
    """Valor presente de un bono con cupon anual c, n periodos y valor
    nominal vn a la tasa r (r distinta de 0): formula de 1_valuacion."""
    return c * (1 - (1 + r) ** -n) / r + vn * (1 + r) ** -n


def fig_precio_rendimiento():
    """Curva precio-rendimiento de un bono con cupon de 8% y valor nominal
    100 para tres plazos (3, 10 y 30 anios): pendiente negativa, convexa,
    a la par cuando el rendimiento es igual al cupon, y mas empinada
    mientras mas largo el plazo (todas pivotan sobre el punto de la par)."""
    r = np.linspace(0.04, 0.16, 300)
    series = ((3, GRAY, "3 años"), (10, GOLD, "10 años"), (30, NAVY, "30 años"))

    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    ax.axhline(100, color=LGRAY, lw=1, ls="--", zorder=1)
    ax.axvline(0.08, color=LGRAY, lw=1, ls="--", zorder=1)
    for n, color, label in series:
        p = _precio_bono(8, n, r)
        ax.plot(r, p, color=color, lw=2.8, zorder=3)
        ax.text(0.163, p[-1], label, color=color, fontsize=11, fontweight="bold", va="center")
    ax.plot([0.08], [100], "o", color=BODY, ms=8, zorder=4)
    ax.annotate("a la par: rendimiento = cupón (8%)", xy=(0.08, 100), xytext=(0.092, 138),
                fontsize=10.5, color=BODY,
                arrowprops={"arrowstyle": "-", "color": GRAY, "lw": 1})

    ax.set_xlim(0.04, 0.19)
    ax.set_ylim(40, 180)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v * 100:.0f}%"))
    ax.set_xlabel("Rendimiento al vencimiento (YTM)", fontsize=11, color=GRAY)
    ax.set_ylabel("Precio (% del valor nominal)", fontsize=11, color=GRAY)
    ax.tick_params(colors=GRAY, labelsize=10)
    ax.set_title("Precio y rendimiento de un bono con cupón de 8%",
                 fontsize=12.5, color=NAVY, fontweight="bold", loc="left", pad=10)
    sns.despine(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_PRECIO_REND, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_PRECIO_REND}")


def fig_curva_ubicar_bono():
    """Curva de rendimientos del 21 de septiembre de 2026 (Cetes y Bonos M
    segun las tablas de cetesdirecto, la misma de
    2_rendimiento_y_curva_de_rendimientos.md; ver datos/cetesdirecto_2026-09-21.csv
    para los Bonos M y la tabla de CETES de esa fecha para los plazos de 6
    meses y 1 anio) y dos bonos a 10 anios ubicados en ella: el Bono M
    publicado (precio 96.40, YTM 9.16%, sobre la curva) y un bono corporativo
    ilustrativo (precio 88, cupon 8%, YTM 9.95%), cuya diferencia es la
    sobretasa (9.95 - 9.16 = 0.79 pp)."""
    dias = [28, 91, 182, 364]
    anios = [d / 360 for d in dias] + [3, 5, 10, 20, 30]
    ytm = [6.25, 6.66, 6.90, 7.24, 8.24, 9.00, 9.16, 9.64, 9.87]
    etiquetas = ["28 d", "91 d", "182 d", "1 a", "3 a", "5 a", "10 a", "20 a", "30 a"]

    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    ax.plot(anios, ytm, "-o", color=NAVY, lw=2.6, ms=6, zorder=3)
    ax.set_xscale("log")
    ax.set_xticks(anios)
    ax.set_xticklabels(etiquetas)
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    ax.xaxis.set_minor_locator(plt.NullLocator())

    ax.plot([10], [9.95], "o", color=GOLD, ms=11, zorder=4)
    ax.annotate("Bono corporativo a 10 años\nprecio \\$88, YTM 9.95%", xy=(10, 9.95),
                xytext=(0.3, 10.2), fontsize=10.5, color=BODY, fontweight="bold", va="center",
                arrowprops={"arrowstyle": "-", "color": GOLD, "lw": 1.2,
                            "shrinkA": 4, "shrinkB": 8})
    ax.annotate("Bono M a 10 años\nprecio \\$96.40, YTM 9.16%", xy=(10, 9.16),
                xytext=(0.3, 9.5), fontsize=10.5, color=BODY, fontweight="bold", va="center",
                arrowprops={"arrowstyle": "-", "color": NAVY, "lw": 1.2,
                            "shrinkA": 4, "shrinkB": 6})
    ax.annotate("", xy=(10, 9.26), xytext=(10, 9.86),
                arrowprops={"arrowstyle": "<->", "color": GRAY, "lw": 1.2,
                            "shrinkA": 0, "shrinkB": 0})
    ax.text(12, 10.02, "sobretasa\n≈ 0.79 pp", fontsize=10, color=GRAY, va="center")

    ax.set_xlim(0.06, 45)
    ax.set_ylim(6.0, 10.6)
    ax.set_yticks([6, 7, 8, 9, 10])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.set_xlabel("Plazo (escala logarítmica)", fontsize=11, color=GRAY)
    ax.set_ylabel("Rendimiento al vencimiento (YTM)", fontsize=11, color=GRAY)
    ax.tick_params(colors=GRAY, labelsize=10)
    ax.set_title("Curva de rendimientos del 21 de septiembre de 2026 y dos bonos a 10 años",
                 fontsize=12.5, color=NAVY, fontweight="bold", loc="left", pad=10)
    sns.despine(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_CURVA_BONO, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_CURVA_BONO}")


def fig_precio_hacia_la_par():
    """Tres bonos a 10 anios con cupon de 12%, 9% y 6% y una tasa de mercado
    que se queda en 9%: el que paga premio pierde valor, el que se vende a
    descuento lo gana, y los tres llegan a 100 al vencimiento. Ilustra los
    tres casos de 1_valuacion (seccion 3, c contra r) y la convergencia a
    la par (pull to par). Pagos anuales, como en el ejemplo de la nota."""
    anios = np.arange(0, 11)
    r, n = 0.09, 10
    series = ((12, NAVY, "Cupón 12% > tasa 9%: con premio", (0.2, 3.0), "bottom"),
              (9, GRAY, "Cupón 9% = tasa 9%: a la par", (0.2, 3.0), "bottom"),
              (6, GOLD, "Cupón 6% < tasa 9%: a descuento", (0.2, -3.0), "top"))

    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    ax.axhline(100, color=LGRAY, lw=1, ls="--", zorder=1)
    for c, color, label, (dx, dy), va in series:
        p = _precio_bono(c, n - anios, r)  # con 0 periodos por vencer vale 100
        ax.plot(anios, p, "-o", color=color, lw=2.4, ms=5, zorder=3)
        ax.text(dx, p[0] + dy, label, color=color if color != GRAY else BODY,
                fontsize=10.5, fontweight="bold", va=va)

    ax.set_xlim(-0.3, 10.4)
    ax.set_ylim(70, 130)
    ax.set_xticks(anios)
    ax.set_xlabel("Años transcurridos (la tasa de mercado se queda en 9%)", fontsize=11, color=GRAY)
    ax.set_ylabel("Precio (% del valor nominal)", fontsize=11, color=GRAY)
    ax.tick_params(colors=GRAY, labelsize=10)
    ax.set_title("Un bono a 10 años converge a su valor nominal, sin importar su cupón",
                 fontsize=12.5, color=NAVY, fontweight="bold", loc="left", pad=10)
    sns.despine(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_HACIA_LA_PAR, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_HACIA_LA_PAR}")


def fig_amortizacion_interes_capital():
    """Interes y abono a capital de cada pago de un credito de $500,000 a 20
    anios y 10% anual, en sistema frances y aleman (el ejemplo de la
    seccion 5 de 1_valuacion). Las barras apiladas suman el pago total."""
    a, r, n = 500_000, 0.10, 20
    fig, axes = plt.subplots(2, 1, figsize=(7.5, 6.4), sharex=True, sharey=True)
    paneles = (("frances", "Sistema francés: pago total constante", "pago de \\$58,730 cada año"),
               ("aleman", "Sistema alemán: abono a capital constante", "pago de \\$75,000 el año 1, \\$27,500 el año 20"))
    for ax, (sistema, titulo, nota) in zip(axes, paneles):
        t = tabla_amortizacion(sistema, a, r, n)
        ax.bar(t.periodo, t.abono_capital, color=NAVY, width=0.82, edgecolor="white", linewidth=1,
               label="Abono a capital")
        ax.bar(t.periodo, t.interes, bottom=t.abono_capital, color=GOLD, width=0.82, edgecolor="white",
               linewidth=1, label="Interés")
        ax.text(20.6, 96_000, nota, ha="right", va="top", fontsize=10.5, color=BODY, fontweight="bold")
        ax.set_title(titulo, fontsize=12, color=NAVY, fontweight="bold", loc="left", pad=8)
        ax.set_ylim(0, 100_000)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"\\${v / 1000:,.0f} mil"))
        ax.set_ylabel("Pago del año", fontsize=11, color=GRAY)
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)
    axes[0].legend(loc="upper right", bbox_to_anchor=(1.0, 0.80), frameon=False, fontsize=10.5)
    axes[1].set_xticks(range(1, n + 1))
    axes[1].set_xlabel("Año", fontsize=11, color=GRAY)
    fig.tight_layout()
    fig.savefig(OUT_AMORT_TABLA, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_AMORT_TABLA}")


def fig_calibracion_tasas():
    """Dos paneles del laboratorio (practicas/unidad2/laboratorio_calibracion.md).

    Izquierda: la tasa corta observada contra el nivel de largo plazo
    estimado, que es hacia donde el modelo la hace revertir.
    Derecha: U de Theil, el cociente del RMSE de cada modelo contra el de
    la caminata aleatoria. Se usa el cociente y no el RMSE crudo porque el
    error crece con el horizonte y eso haria incomparables las barras. Por
    debajo de 1 el modelo le gana a la caminata aleatoria; por arriba,
    pierde."""
    datos = cargar()
    corta = datos["r_corta"].dropna()
    par = calibrar_vasicek(corta)
    oos = evaluar_oos(datos)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))

    ax1.plot(corta.index, corta.values, color=NAVY, lw=1.6, zorder=3)
    ax1.axhline(par["r_lp"], color=GOLD, lw=2, ls="--", zorder=2)
    ax1.text(corta.index[2], par["r_lp"] + 0.55,
             f"nivel de largo plazo estimado: {par['r_lp']:.2f}%",
             color=GOLD, fontsize=10.5, fontweight="bold")
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax1.set_ylabel("Tasa interbancaria a 3 meses", fontsize=11, color=GRAY)
    ax1.set_title(f"Reversión a la media: κ = {par['kappa']:.2f}, "
                  f"vida media {par['vida_media']:.1f} años",
                  fontsize=11.5, color=NAVY, fontweight="bold", loc="left", pad=8)
    ax1.tick_params(colors=GRAY, labelsize=10)
    sns.despine(ax=ax1)

    # las barras se dibujan como desviacion desde 1, que es la caminata
    # aleatoria: la linea base de este grafico no es el cero, y arrancarlas
    # en cero (o truncarlas en un valor arbitrario) exageraria diferencias
    x = np.arange(len(oos))
    ancho = 0.34
    for valores, dx, color, etiqueta in ((oos.theil_ar1, -ancho / 2, NAVY, "AR(1) / Vasicek"),
                                         (oos.theil_ardl, ancho / 2, GOLD, "ARDL con macro")):
        ax2.bar(x + dx, valores - 1, ancho, bottom=1, color=color, label=etiqueta,
                edgecolor="white", linewidth=1, zorder=3)
        for xi, v in zip(x + dx, valores):
            arriba = v >= 1
            ax2.text(xi, v + (0.006 if arriba else -0.006), f"{v:.2f}", ha="center",
                     va="bottom" if arriba else "top", fontsize=9.5, color=BODY,
                     fontweight="bold", zorder=4)
    ax2.axhline(1, color=GRAY, lw=1.4, zorder=2)
    ax2.text(len(oos) - 0.4, 1.004, "caminata aleatoria", ha="right", va="bottom",
             fontsize=10, color=GRAY, fontweight="bold")
    ax2.set_xticks(x)
    ax2.set_xticklabels([f"{h} {'mes' if h == 1 else 'meses'}" for h in oos.h_meses])
    ax2.set_xlabel("Horizonte del pronóstico", fontsize=11, color=GRAY)
    ax2.set_ylabel("RMSE relativo (U de Theil)", fontsize=11, color=GRAY)
    ax2.set_ylim(0.76, 1.14)
    ax2.set_title("Solo le ganan a plazo largo",
                  fontsize=11.5, color=NAVY, fontweight="bold", loc="left", pad=26)
    ax2.legend(frameon=False, fontsize=10, ncol=2, loc="lower left",
               bbox_to_anchor=(0, 1.0))
    ax2.tick_params(colors=GRAY, labelsize=10)
    sns.despine(ax=ax2)

    fig.tight_layout()
    fig.savefig(OUT_CALIBRACION, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_CALIBRACION}")


def fig_fijo_vs_variable():
    """Monte Carlo del apendice de 1_valuacion: precio de un bono a tasa fija
    y de un certificado a tasa variable ante 10,000 trayectorias de tasas
    generadas con el modelo de Vasicek calibrado (ver codigo/simulacion.py).
    Mismo eje vertical en ambos paneles para poder comparar la dispersion."""
    fijo, variable = simular_precios()
    anios = np.arange(fijo.shape[1]) * DT
    paneles = ((fijo, NAVY, "Bono M a 10 años (cupón fijo)"),
               (variable, GOLD, "Certificado a tasa variable"))

    fig, axes = plt.subplots(1, 2, figsize=(7.5, 4.4), sharey=True)
    for ax, (precios, color, titulo) in zip(axes, paneles):
        ax.axhline(100, color=LGRAY, lw=1, ls="--", zorder=1)
        ax.plot(anios, precios[:40].T, color=color, lw=0.8, alpha=0.18, zorder=2)
        p5, p50, p95 = np.percentile(precios, [5, 50, 95], axis=0)
        ax.fill_between(anios, p5, p95, color=color, alpha=0.22, lw=0, zorder=3)
        ax.plot(anios, p50, color=color, lw=2.6, zorder=4)
        ax.set_title(titulo, fontsize=11.5, color=NAVY, fontweight="bold", loc="left", pad=8)
        ax.set_xlabel("Años", fontsize=11, color=GRAY)
        ax.set_xlim(0, anios[-1])
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)
    axes[0].set_ylim(80, 125)
    axes[0].set_ylabel("Precio (% del valor nominal)", fontsize=11, color=GRAY)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.24)
    fig.text(0.01, 0.015,
             "10,000 trayectorias (40 dibujadas). Línea gruesa: mediana; banda: 5% a 95% de los escenarios.\n"
             "Modelo de Vasicek calibrado: κ = 0.217, σ = 1.24 pp anual. Margen de crédito: 0.3 pp, supuesto.",
             fontsize=9, color=GRAY, va="bottom")
    fig.savefig(OUT_FIJO_VARIABLE, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_FIJO_VARIABLE}")


def main():
    fig_flujo_efectivo([0, 1], [-90.91, 100], OUT_DESCUENTO,
                        "Flujo de efectivo a descuento (CETE)")
    fig_flujo_efectivo([0, 1, 2, 3], [-100, 10, 10, 110], OUT_CUPON_FIJO,
                        "Flujo de efectivo con cupón fijo (Bono M)")
    fig_flujo_cupon_variable()
    fig_flujo_amortizacion()
    fig_precio_rendimiento()
    fig_curva_ubicar_bono()
    fig_precio_hacia_la_par()
    fig_amortizacion_interes_capital()
    fig_fijo_vs_variable()
    fig_calibracion_tasas()


if __name__ == "__main__":
    main()
