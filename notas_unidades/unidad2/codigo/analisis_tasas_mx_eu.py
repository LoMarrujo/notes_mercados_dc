"""Analisis exploratorio (no evaluado, no parte de ninguna nota): como se han
movido las tasas de interes de Mexico y Estados Unidos, 2001-07 a 2026-09.

Tres preguntas, con los datos que ya descarga datos_fred.cargar():
    1. Nivel y ciclos de alza/baja de cada tasa por separado.
    2. El diferencial (spread) entre la tasa mexicana y la estadounidense.
    3. Si una tasa se adelanta a la otra (correlacion cruzada de sus
       cambios mensuales, nunca de sus niveles: ver la nota de mas abajo).

Por que cambios y no niveles. La tasa de un mes se parece muchisimo a la
del mes anterior (persistencia), asi que casi cualquier par de series de
tasas sale correlacionado en niveles sin que exista una relacion real
entre ellas; es la misma trampa que ya identifico
practicas/unidad2/laboratorio_calibracion.md (seccion "La trampa del R2").
La correlacion cruzada de este script se calcula sobre el cambio mes a
mes de cada serie, no sobre su nivel.

Uso (desde la raiz del repo):
    python notas_unidades/unidad2/codigo/analisis_tasas_mx_eu.py
"""
import os
import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datos_fred import cargar  # noqa: E402

NAVY = "#1E2761"   # Mexico
GOLD = "#C9A227"   # Estados Unidos
GRAY = "#5B6482"
LGRAY = "#A6ADC7"
BODY = "#27314D"

plt.rcParams["font.family"] = "Calibri"
sns.set_theme(style="white", rc={"axes.edgecolor": LGRAY, "axes.linewidth": 0.8})

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")
OUT_NIVELES = os.path.join(IMG_DIR, "tasas_mx_eu_niveles.png")
OUT_SPREAD = os.path.join(IMG_DIR, "tasas_mx_eu_spread.png")
OUT_CORRELACION = os.path.join(IMG_DIR, "tasas_mx_eu_correlacion.png")


def detectar_episodios(serie, ventana=3, minimo_meses=3, minimo_cambio_pp=0.15):
    """Episodios de alza y de baja de una serie mensual de tasas.

    Suaviza con una media movil de `ventana` meses (para no reaccionar a
    ruido de un solo mes), toma el signo del cambio mes a mes, agrupa
    tramos consecutivos del mismo signo y descarta los de menos de
    `minimo_meses`. Un mes en el que el suavizado no cambia (cambio
    exactamente 0) se pega al tramo anterior, no abre uno nuevo.

    El filtro de duracion no basta: en los anios en que la tasa se quedo
    practicamente plana (2010-2015 en ambos paises), el suavizado sigue
    oscilando de signo por decimas de punto base durante varios meses
    seguidos, y eso pasaria el filtro de duracion como si fuera un ciclo
    real. `minimo_cambio_pp` descarta ademas los episodios cuyo cambio
    total, de inicio a fin, es menor a ese umbral en valor absoluto.

    Devuelve un DataFrame con inicio, fin, duracion en meses, tipo
    ("alza"/"baja") y cambio total en puntos porcentuales de la serie
    original (sin suavizar) entre el inicio y el fin del episodio."""
    s = serie.dropna()
    suave = s.rolling(ventana, min_periods=ventana).mean().dropna()
    cambio = suave.diff().dropna()
    signo = cambio.apply(lambda v: 1 if v > 0 else (-1 if v < 0 else 0))
    signo = signo.replace(0, np.nan).ffill().fillna(0)

    filas = []
    grupo_id = (signo != signo.shift()).cumsum()
    for _, idx in signo.groupby(grupo_id).groups.items():
        tipo_signo = signo.loc[idx].iloc[0]
        if tipo_signo == 0 or len(idx) < minimo_meses:
            continue
        ini, fin = idx[0], idx[-1]
        cambio = float(s.loc[fin] - s.loc[ini])
        if abs(cambio) < minimo_cambio_pp:
            continue
        filas.append({
            "tipo": "alza" if tipo_signo > 0 else "baja",
            "inicio": ini, "fin": fin,
            "duracion_meses": len(idx),
            "cambio_pp": cambio,
        })
    return pd.DataFrame(filas)


def spreads(datos):
    """Diferencial MX menos EE.UU., corto y largo plazo.

    No confundir con la columna `pendiente` de datos_fred.cargar(), que es
    la pendiente de la curva mexicana (r_larga - r_corta, un solo pais);
    esto es un spread entre paises al mismo plazo."""
    d = datos.copy()
    d["spread_corto"] = d["r_corta"] - d["us_ff"]
    d["spread_largo"] = d["r_larga"] - d["us_10a"]
    return d


def resumen_spread(serie, etiqueta):
    s = serie.dropna()
    return {"spread": etiqueta, "promedio_pp": s.mean(), "minimo_pp": s.min(),
            "fecha_minimo": s.idxmin(), "maximo_pp": s.max(), "fecha_maximo": s.idxmax()}


def correlacion_cruzada(x, y, max_rezago=24):
    """Correlacion de x contra y desplazada `rezago` meses, para cada
    rezago de -max_rezago a +max_rezago.

    Convencion de signo: rezago > 0 compara x_t contra y_{t-rezago}, es
    decir, y de `rezago` meses atras. Si el pico de correlacion cae en un
    rezago positivo, es x la que se parece a y con retraso: dicho con las
    series de este modulo, si se llama correlacion_cruzada(mx, us) y el
    pico esta en un rezago positivo, Mexico sigue a Estados Unidos ese
    numero de meses. Fijar bien el signo es facil de errar, por eso
    test_correlacion_cruzada_recupera_el_rezago_sintetico en la funcion
    main() lo comprueba con una serie sintetica antes de leer el resultado
    real.

    Devuelve un DataFrame con columnas rezago y correlacion."""
    x, y = x.dropna(), y.dropna()
    filas = []
    for rezago in range(-max_rezago, max_rezago + 1):
        xa, ya = x.align(y.shift(rezago), join="inner")
        if len(xa) < 12:
            continue
        filas.append({"rezago": rezago, "correlacion": xa.corr(ya)})
    return pd.DataFrame(filas)


def _prueba_signo_rezago():
    """Caso sintetico: x sigue a `lider` con k meses de atraso, es decir
    x repite hoy lo que `lider` ya hizo hace k meses (x_t = lider_{t-k}).
    correlacion_cruzada(x, lider) debe dar el pico en rezago = +k,
    confirmando que un rezago positivo significa 'la primera serie (x)
    sigue a la segunda (lider)'. Se corre siempre en main(), antes de leer
    los resultados reales, precisamente porque el signo es facil de errar:
    la primera version de esta prueba tenia los papeles invertidos (lider
    y seguidora al reves) y el assert fallaba con el signo contrario."""
    rng = np.random.default_rng(0)
    idx = pd.date_range("2000-01-01", periods=120, freq="MS")
    lider = pd.Series(rng.standard_normal(120).cumsum(), index=idx)
    k = 5
    x = lider.shift(k)  # x repite hoy lo que lider hizo hace k meses: x sigue a lider
    cc = correlacion_cruzada(x, lider, max_rezago=12)
    pico = cc.loc[cc["correlacion"].idxmax(), "rezago"]
    assert pico == k, f"signo del rezago mal calibrado: se esperaba {k}, salio {pico}"
    print(f"[verificacion] correlacion_cruzada recupera el rezago sintetico "
          f"(k={k}) correctamente: pico en rezago={pico}")


def fig_niveles(datos):
    """Dos paneles apilados, un eje cada uno: tasa corta MX vs. EE.UU.
    arriba, tasa larga MX vs. EE.UU. abajo. Nunca dos ejes en el mismo
    panel: son la misma unidad (tasa anual, %), comparables en un eje.

    r_larga (bono MX a 10 años) tiene 67 meses sin dato de 303, 58 de ellos
    huecos aislados de un solo mes: dibujados tal cual, matplotlib corta la
    linea en cada hueco y se ve como una serie punteada que no lo es. Para
    que se lea bien, la version que se dibuja interpola linealmente huecos
    de hasta 2 meses (`limit=2`); los huecos mas largos (2 casos) siguen
    apareciendo como corte real. Esto es solo para el trazo: los calculos
    de episodios, spread y correlacion siguen usando la serie sin
    interpolar (cada funcion hace su propio `.dropna()`)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 7.2), sharex=True)
    for ax, (mx, us, titulo) in zip(
        (ax1, ax2),
        (("r_corta", "us_ff", "Tasa corta: interbancaria MX (3 meses) vs. fed funds"),
         ("r_larga", "us_10a", "Tasa larga: bono MX a 10 años vs. Tesoro EE.UU. a 10 años")),
    ):
        serie_mx = datos[mx].interpolate(limit=2) if mx == "r_larga" else datos[mx]
        ax.plot(datos.index, serie_mx, color=NAVY, lw=1.8, label="México", zorder=3)
        ax.plot(datos.index, datos[us], color=GOLD, lw=1.8, label="Estados Unidos", zorder=3)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))
        ax.set_title(titulo, fontsize=12, color=NAVY, fontweight="bold", loc="left", pad=8)
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)
    # zona sin datos en el panel superior (2010-2015, parte alta): ahi la
    # leyenda no tapa ninguna linea
    ax1.legend(frameon=False, fontsize=10, loc="upper center", bbox_to_anchor=(0.46, 0.97))
    fig.text(0.01, 0.005, "Bono MX a 10 años: huecos de hasta 2 meses interpolados solo para el trazo.",
             fontsize=8.5, color=GRAY, va="bottom")
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(OUT_NIVELES, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_NIVELES}")


def fig_spread(datos):
    """Un panel: los dos spreads (corto y largo) en el tiempo, con una
    linea de referencia en 0."""
    fig, ax = plt.subplots(figsize=(9.5, 4.4))
    ax.axhline(0, color=LGRAY, lw=1.2, zorder=1)
    ax.plot(datos.index, datos["spread_corto"], color=NAVY, lw=1.8, label="Corto plazo (interbancaria - fed funds)")
    ax.plot(datos.index, datos["spread_largo"], color=GOLD, lw=1.8, label="Largo plazo (bono 10a MX - Tesoro 10a)")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f} pp"))
    ax.set_title("Diferencial de tasas, México menos Estados Unidos", fontsize=12.5,
                 color=NAVY, fontweight="bold", loc="left", pad=8)
    ax.legend(frameon=False, fontsize=10, loc="upper right")
    ax.tick_params(colors=GRAY, labelsize=10)
    sns.despine(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_SPREAD, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_SPREAD}")


def fig_correlacion(cc_corto, cc_largo):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))
    for ax, cc, titulo in ((ax1, cc_corto, "Corto plazo: Δinterbancaria vs. Δfed funds"),
                           (ax2, cc_largo, "Largo plazo: Δbono MX 10a vs. Δbono EE.UU. 10a")):
        pico = cc.loc[cc["correlacion"].idxmax()]
        colores = [GOLD if r == pico["rezago"] else NAVY for r in cc["rezago"]]
        ax.bar(cc["rezago"], cc["correlacion"], color=colores, width=0.8, zorder=3)
        ax.axvline(0, color=LGRAY, lw=1, zorder=2)
        ax.axhline(0, color=LGRAY, lw=1, zorder=2)
        ax.set_title(titulo, fontsize=11, color=NAVY, fontweight="bold", loc="left", pad=8)
        ax.set_xlabel("Rezago (meses); positivo = México sigue a EE.UU.", fontsize=9.5, color=GRAY)
        ax.tick_params(colors=GRAY, labelsize=9.5)
        sns.despine(ax=ax)
    ax1.set_ylabel("Correlación", fontsize=10.5, color=GRAY)
    fig.tight_layout()
    fig.savefig(OUT_CORRELACION, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_CORRELACION}")


def main():
    pd.set_option("display.width", 200)
    _prueba_signo_rezago()

    datos = cargar()
    datos = spreads(datos)

    print("\n=== 1. Episodios de alza y baja ===")
    for col, etiqueta in (("r_corta", "México, interbancaria 3m"), ("us_ff", "Estados Unidos, fed funds")):
        ep = detectar_episodios(datos[col])
        print(f"\n-- {etiqueta} --")
        print(ep.to_string(index=False, float_format=lambda v: f"{v:+.2f}"))

    print("\n=== 2. Diferencial de tasas (spread) ===")
    resumen = pd.DataFrame([resumen_spread(datos["spread_corto"], "corto plazo"),
                            resumen_spread(datos["spread_largo"], "largo plazo")])
    print(resumen.to_string(index=False, float_format=lambda v: f"{v:.2f}" if isinstance(v, float) else str(v)))

    print("\n=== 3. Correlación cruzada de los cambios mensuales ===")
    dmx_corta, dus_ff = datos["r_corta"].diff(), datos["us_ff"].diff()
    dmx_larga, dus_10a = datos["r_larga"].diff(), datos["us_10a"].diff()
    cc_corto = correlacion_cruzada(dmx_corta, dus_ff)
    cc_largo = correlacion_cruzada(dmx_larga, dus_10a)
    for etiqueta, cc in (("corto plazo", cc_corto), ("largo plazo", cc_largo)):
        pico = cc.loc[cc["correlacion"].idxmax()]
        print(f"  {etiqueta}: pico de correlacion {pico['correlacion']:.3f} en rezago "
              f"{int(pico['rezago']):+d} meses")

    fig_niveles(datos)
    fig_spread(datos)
    fig_correlacion(cc_corto, cc_largo)


if __name__ == "__main__":
    main()
