"""Genera las figuras de 1_probabilidad_y_riesgo.md. Se versiona junto a las
imagenes que produce para que sean reproducibles: si el contenido cambia, se
corrige este script y se vuelve a correr, nunca se edita el .png a mano.

Uso:
    python notas_unidades/unidad3/img/generar_figuras.py
"""
import os

import matplotlib
import matplotlib.ticker
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import lognorm, multivariate_normal, norm

NAVY = "#1E2761"
GOLD = "#C9A227"
GRAY = "#5B6482"
LGRAY = "#A6ADC7"
BODY = "#27314D"
RED = "#C0392B"

plt.rcParams["font.family"] = "Calibri"
sns.set_theme(style="white", rc={"axes.edgecolor": LGRAY, "axes.linewidth": 0.8})

IMG_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_INCUMPLIMIENTO = os.path.join(IMG_DIR, "incumplimiento_masa_distribucion.png")

OUT_ACCION = os.path.join(IMG_DIR, "accion_lognormal_densidad_distribucion.png")

PROB_INCUMPLIR = 0.05  # ilustrativa, la misma del ejemplo de la nota
S0_ACCION, MU_ACCION, SIGMA_ACCION = 100, 0.05, 0.25  # ilustrativos
VALOR_NOMINAL, PERDIDA_MIN = 100, 20  # si incumple, la perdida es uniforme en [20, 100]
OUT_PERDIDA = os.path.join(IMG_DIR, "perdida_incumplimiento_mixta.png")
OUT_VECTOR = os.path.join(IMG_DIR, "vector_rendimientos_conjunta.png")
OUT_VECTOR_ESPERANZA = os.path.join(IMG_DIR, "vector_rendimientos_esperanza.png")
OUT_SP500 = os.path.join(IMG_DIR, "sp500_rendimientos_anuales.png")
OUT_SP500_SERIE = os.path.join(IMG_DIR, "sp500_precio_y_rendimientos.png")
OUT_NORMAL = os.path.join(IMG_DIR, "normal_dos_rendimientos.png")
OUT_CUANTIL = os.path.join(IMG_DIR, "normal_cuantil_var.png")
OUT_CVAR = os.path.join(IMG_DIR, "normal_cvar.png")
MU_NORMAL, SIGMA_NORMAL = 0.08, (0.15, 0.25)  # ilustrativos
DATOS_SP500_PRECIO = os.path.join(IMG_DIR, "..", "datos", "sp500_precio_mensual.csv")
DATOS_SP500 = os.path.join(IMG_DIR, "..", "datos", "sp500_rendimientos_anuales.csv")
MU_VECTOR, SIGMA_VECTOR, RHO_VECTOR = (0.05, 0.08), (0.25, 0.30), 0.6  # ilustrativos


def fig_incumplimiento_masa_distribucion():
    """Densidad y funcion de distribucion de la variable de
    incumplimiento D (0 si la emisora paga, 1 si incumple), del ejemplo de
    la seccion 1.5, "Distribucion". En la de distribucion, el punto relleno
    marca el valor que F si toma en cada salto y el hueco el que no."""
    q = PROB_INCUMPLIR
    valores = [0, 1]
    masa = [1 - q, q]
    etiquetas = ["Paga", "Incumple"]

    fig, (ax_m, ax_f) = plt.subplots(1, 2, figsize=(10, 4.2))

    # Densidad: una barra delgada por valor posible
    ax_m.vlines(valores, 0, masa, color=NAVY, lw=3, zorder=3)
    ax_m.plot(valores, masa, "o", color=NAVY, ms=9, zorder=4)
    for x, p, et in zip(valores, masa, etiquetas):
        ax_m.text(x, p + 0.04, f"{p:.2f}", ha="center", va="bottom",
                  fontsize=11, color=BODY, fontweight="bold")
        ax_m.text(x, -0.12, et, ha="center", va="top", fontsize=10, color=GRAY)
    ax_m.set_xlim(-0.6, 1.6)
    ax_m.set_ylim(0, 1.1)
    ax_m.set_xticks(valores)
    ax_m.set_xlabel("x", fontsize=11, color=GRAY, labelpad=18)
    ax_m.set_ylabel("dF(x) = P(D = x)", fontsize=11, color=GRAY)
    ax_m.set_title("Densidad", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    # Funcion de distribucion: escalera con saltos en 0 y en 1
    tramos = [(-0.6, 0, 0.0), (0, 1, 1 - q), (1, 1.6, 1.0)]
    for x0, x1, y in tramos:
        ax_f.hlines(y, x0, x1, color=NAVY, lw=2.4, zorder=3)
    for x, y_antes, y_despues in [(0, 0.0, 1 - q), (1, 1 - q, 1.0)]:
        ax_f.vlines(x, y_antes, y_despues, color=LGRAY, lw=1, ls="--", zorder=2)
        ax_f.plot(x, y_antes, "o", ms=8, mfc="white", mec=NAVY, mew=2, zorder=4)
        ax_f.plot(x, y_despues, "o", ms=8, color=NAVY, zorder=5)
    ax_f.text(0.5, 1 - q - 0.06, f"F(0) = {1 - q:.2f}: paga", ha="center", va="top",
              fontsize=10.5, color=BODY)
    ax_f.annotate(f"salto de {q:.2f}: incumple", xy=(1.03, 1 - q / 2), xytext=(1.12, 0.72),
                  fontsize=10.5, color=BODY,
                  arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})
    ax_f.set_xlim(-0.6, 1.6)
    ax_f.set_ylim(0, 1.1)
    ax_f.set_xticks(valores)
    ax_f.set_xlabel("x", fontsize=11, color=GRAY)
    ax_f.set_ylabel("F(x) = P(D ≤ x)", fontsize=11, color=GRAY)
    ax_f.set_title("Función de distribución", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    for ax in (ax_m, ax_f):
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)

    fig.suptitle("Incumplimiento de un bono con probabilidad 0.05 (ilustrativa)",
                 fontsize=13, color=NAVY, fontweight="bold", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(OUT_INCUMPLIMIENTO, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_INCUMPLIMIENTO}")


def fig_accion_lognormal():
    """Densidad y funcion de distribucion del precio en un anio de una accion
    lognormal (seccion 1.5, ejemplo "precio de la accion"): s0 = 100 y el
    rendimiento continuo ln(S1/s0) normal con media 5% y desviacion 25%,
    ilustrativos. Sombrea P(90 < S1 <= 110) = F(110) - F(90) en los dos
    paneles: como area en la densidad y como subida en la distribucion."""
    s0, mu, sigma = S0_ACCION, MU_ACCION, SIGMA_ACCION
    dist = lognorm(s=sigma, scale=s0 * np.exp(mu))
    a, b = 90, 110
    x = np.linspace(0.5, 220, 600)
    fa, fb = dist.cdf(a), dist.cdf(b)

    fig, (ax_d, ax_f) = plt.subplots(1, 2, figsize=(10, 4.2))

    # Densidad, con el area entre a y b sombreada
    ax_d.plot(x, dist.pdf(x), color=NAVY, lw=2.4, zorder=3)
    xs = np.linspace(a, b, 200)
    ax_d.fill_between(xs, 0, dist.pdf(xs), color=GOLD, alpha=0.45, lw=0, zorder=2)
    ax_d.text((a + b) / 2, dist.pdf(100) * 0.45, f"{fb - fa:.3f}", ha="center",
              fontsize=11, color=BODY, fontweight="bold", zorder=4)
    ax_d.set_xlim(0, 220)
    ax_d.set_ylim(0, dist.pdf(x).max() * 1.15)
    ax_d.set_xlabel("x (pesos)", fontsize=11, color=GRAY)
    ax_d.set_ylabel("f(x)", fontsize=11, color=GRAY)
    ax_d.set_title("Densidad", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    # Funcion de distribucion, con la subida entre a y b marcada
    ax_f.plot(x, dist.cdf(x), color=NAVY, lw=2.4, zorder=3)
    for v, f in ((a, fa), (b, fb)):
        ax_f.vlines(v, 0, f, color=LGRAY, lw=1, ls="--", zorder=2)
        ax_f.hlines(f, 0, v, color=LGRAY, lw=1, ls="--", zorder=2)
        ax_f.plot(v, f, "o", ms=8, color=NAVY, zorder=4)
        ax_f.text(3, f + 0.015, f"F({v}) = {f:.3f}", fontsize=10.5, color=BODY, va="bottom")
    ax_f.annotate("", xy=(b + 6, fb), xytext=(b + 6, fa),
                  arrowprops={"arrowstyle": "<->", "color": GOLD, "lw": 2})
    ax_f.text(b + 11, (fa + fb) / 2, f"{fb - fa:.3f}", va="center",
              fontsize=11, color=BODY, fontweight="bold")
    ax_f.set_xlim(0, 220)
    ax_f.set_ylim(0, 1.05)
    ax_f.set_xlabel("x (pesos)", fontsize=11, color=GRAY)
    ax_f.set_ylabel("F(x) = P($S_1$ ≤ x)", fontsize=11, color=GRAY)
    ax_f.set_title("Función de distribución", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    for ax in (ax_d, ax_f):
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)

    fig.suptitle(f"Precio de la acción en un año, lognormal con $s_0$ = {s0}, "
                 f"$\\mu$ = {mu * 100:.0f}% y $\\sigma$ = {sigma * 100:.0f}% (ilustrativa)",
                 fontsize=13, color=NAVY, fontweight="bold", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(OUT_ACCION, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_ACCION}")


def fig_perdida_mixta():
    """Densidad y funcion de distribucion de la perdida L de un bono con valor
    nominal 100 (seccion 1.5, ejemplo "perdida con incumplimiento"). Con
    probabilidad 0.95 la emisora paga y L = 0 (un salto); con 0.05 incumple
    y la perdida es uniforme entre 20 y 100 (parte continua). El salto se
    dibuja como flecha, fuera de escala, porque su tamano (0.95) no cabe en
    el mismo eje que la parte continua (0.05/80 por peso)."""
    q, lo, hi, vn = PROB_INCUMPLIR, PERDIDA_MIN, VALOR_NOMINAL, VALOR_NOMINAL
    altura = q / (hi - lo)

    def distribucion(x):
        x = np.asarray(x, dtype=float)
        return np.where(x < 0, 0.0,
                        np.where(x < lo, 1 - q,
                                 np.where(x < hi, 1 - q + altura * (x - lo), 1.0)))

    fig, (ax_d, ax_f) = plt.subplots(1, 2, figsize=(10, 4.2))

    # Densidad: flecha para el salto en 0 y un tramo plano para la parte continua
    tope = altura * 1.6
    ax_d.annotate("", xy=(0, tope), xytext=(0, 0),
                  arrowprops={"arrowstyle": "-|>", "color": NAVY, "lw": 2.4})
    ax_d.text(3, tope * 0.93, f"salto: P(L = 0) = {1 - q:.2f}", fontsize=10.5,
              color=BODY, va="top")
    ax_d.hlines(0, -10, lo, color=NAVY, lw=2.4, zorder=3)
    ax_d.hlines(altura, lo, hi, color=NAVY, lw=2.4, zorder=3)
    ax_d.hlines(0, hi, vn + 10, color=NAVY, lw=2.4, zorder=3)
    ax_d.fill_between([lo, hi], 0, altura, color=GOLD, alpha=0.45, lw=0, zorder=2)
    ax_d.text((lo + hi) / 2, altura * 0.5, f"área {q:.2f}", ha="center", va="center",
              fontsize=11, color=BODY, fontweight="bold")
    ax_d.set_xlim(-10, vn + 10)
    ax_d.set_ylim(0, tope * 1.05)
    ax_d.set_xlabel("pérdida x (pesos)", fontsize=11, color=GRAY)
    ax_d.set_ylabel("f(x) fuera del salto", fontsize=11, color=GRAY)
    ax_d.set_title("Densidad", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    # Funcion de distribucion: salto en 0, plana hasta 20 y sube hasta 100
    x = np.linspace(0, vn + 10, 400)
    ax_f.hlines(0, -10, 0, color=NAVY, lw=2.4, zorder=3)
    ax_f.plot(x, distribucion(x), color=NAVY, lw=2.4, zorder=3)
    ax_f.vlines(0, 0, 1 - q, color=LGRAY, lw=1, ls="--", zorder=2)
    ax_f.plot(0, 0, "o", ms=8, mfc="white", mec=NAVY, mew=2, zorder=4)
    ax_f.plot(0, 1 - q, "o", ms=8, color=NAVY, zorder=5)
    ax_f.text(4, 1 - q - 0.06, f"salto de {1 - q:.2f} en 0: paga", fontsize=10.5,
              color=BODY, va="top")
    ax_f.annotate(f"sube {q:.2f} entre {lo} y {hi}: incumple", xy=(60, distribucion(60)),
                  xytext=(28, 0.72), fontsize=10.5, color=BODY,
                  arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})
    ax_f.set_xlim(-10, vn + 10)
    ax_f.set_ylim(0, 1.05)
    ax_f.set_xlabel("pérdida x (pesos)", fontsize=11, color=GRAY)
    ax_f.set_ylabel("F(x) = P(L ≤ x)", fontsize=11, color=GRAY)
    ax_f.set_title("Función de distribución", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    for ax in (ax_d, ax_f):
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)

    fig.suptitle(f"Pérdida de un bono de {vn} pesos que incumple con probabilidad {q} (ilustrativa)",
                 fontsize=13, color=NAVY, fontweight="bold", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(OUT_PERDIDA, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_PERDIDA}")


def fig_vector_rendimientos(con_esperanza=False):
    """Densidad conjunta de los rendimientos en un anio de dos acciones,
    (R_A, R_B), con sus marginales en los margenes (seccion 1.6). Modelo
    ilustrativo: normal bivariada con medias 5% y 8%, desviaciones 25% y
    30% y correlacion 0.6. La region B sombreada es el cuadrante en que las
    dos acciones pierden; su probabilidad es el volumen de la densidad
    conjunta sobre B. Con con_esperanza=True (seccion 1.8) marca ademas
    E[R_A] y E[R_B] y el punto donde se cruzan."""
    mu = np.array(MU_VECTOR)
    sa, sb = SIGMA_VECTOR
    rho = RHO_VECTOR
    cov = np.array([[sa ** 2, rho * sa * sb], [rho * sa * sb, sb ** 2]])
    conjunta = multivariate_normal(mean=mu, cov=cov)
    p_ambas = conjunta.cdf([0, 0])

    g = np.linspace(-0.8, 0.9, 300)
    xx, yy = np.meshgrid(g, g)
    zz = conjunta.pdf(np.dstack([xx, yy]))

    fig = plt.figure(figsize=(7.2, 6.4))
    gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4),
                          wspace=0.05, hspace=0.05)
    ax = fig.add_subplot(gs[1, 0])
    ax_x = fig.add_subplot(gs[0, 0], sharex=ax)
    ax_y = fig.add_subplot(gs[1, 1], sharey=ax)

    niveles = np.linspace(zz.max() * 0.08, zz.max(), 6)
    ax.contourf(xx, yy, zz, levels=np.append(niveles, zz.max() * 1.01),
                cmap=sns.light_palette(NAVY, as_cmap=True), alpha=0.9, zorder=1)
    ax.contour(xx, yy, zz, levels=niveles, colors=NAVY, linewidths=0.8, zorder=2)
    ax.fill_between([-0.8, 0], -0.8, 0, color=GOLD, alpha=0.25, lw=0, zorder=0)
    ax.axhline(0, color=LGRAY, lw=0.8, zorder=0)
    ax.axvline(0, color=LGRAY, lw=0.8, zorder=0)
    # Esperanza del vector: una linea por componente y el punto (E[R_A], E[R_B])
    if con_esperanza:
        ax.axvline(mu[0], color=GOLD, lw=1.6, ls="--", zorder=4)
        ax.axhline(mu[1], color=GOLD, lw=1.6, ls="--", zorder=4)
        ax.plot(mu[0], mu[1], "o", ms=9, color=GOLD, mec="white", mew=1.5, zorder=5)
        ax.text(mu[0] + 0.03, 0.84, f"$E[R_A] = {mu[0] * 100:.0f}\\%$", fontsize=10.5,
                color=BODY, va="top")
        ax.text(0.86, mu[1] + 0.03, f"$E[R_B] = {mu[1] * 100:.0f}\\%$", fontsize=10.5,
                color=BODY, ha="right")
    ax.text(-0.76, -0.74, "B: las dos pierden\n" + r"$P((R_A, R_B) \in B)$" + f" = {p_ambas:.2f}",
            fontsize=10.5, color=BODY, va="bottom")
    ax.set_xlim(-0.8, 0.9)
    ax.set_ylim(-0.8, 0.9)
    pct = matplotlib.ticker.PercentFormatter(1.0, decimals=0)
    ax.xaxis.set_major_formatter(pct)
    ax.yaxis.set_major_formatter(pct)
    ax.set_xlabel("Rendimiento de la acción A, $R_A$", fontsize=11, color=GRAY)
    ax.set_ylabel("Rendimiento de la acción B, $R_B$", fontsize=11, color=GRAY)

    ax_x.plot(g, norm.pdf(g, mu[0], sa), color=NAVY, lw=2)
    ax_x.fill_between(g, 0, norm.pdf(g, mu[0], sa), color=NAVY, alpha=0.12, lw=0)
    ax_x.text(0.88, norm.pdf(mu[0], mu[0], sa) * 0.6, "marginal\nde $R_A$", ha="right",
              fontsize=10, color=BODY)
    ax_y.plot(norm.pdf(g, mu[1], sb), g, color=NAVY, lw=2)
    ax_y.fill_betweenx(g, 0, norm.pdf(g, mu[1], sb), color=NAVY, alpha=0.12, lw=0)
    ax_y.text(norm.pdf(mu[1], mu[1], sb) * 0.45, -0.55, "marginal\nde $R_B$",
              fontsize=10, color=BODY, va="top")
    for a in (ax_x, ax_y):
        a.axis("off")

    ax.tick_params(colors=GRAY, labelsize=10)
    sns.despine(ax=ax)
    titulo = "Esperanza de dos rendimientos (ilustrativa)" if con_esperanza else "Densidad conjunta de dos rendimientos (ilustrativa)"
    out = OUT_VECTOR_ESPERANZA if con_esperanza else OUT_VECTOR
    fig.suptitle(titulo, fontsize=13,
                 color=NAVY, fontweight="bold", x=0.02, ha="left", y=0.98)
    fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight")
    print(f"figura generada: {out}  P(ambas pierden) = {p_ambas:.4f}")


def fig_sp500_serie():
    """Serie de tiempo del S&P 500, 1928-2025 (seccion 1.8): arriba, el nivel
    mensual del indice en escala logaritmica (Shiller hasta 2023-09, promedio
    mensual; Yahoo despues, cierre mensual; ver ../datos/); abajo, los
    rendimientos anuales con dividendos de Damodaran, con su promedio."""
    precio = pd.read_csv(DATOS_SP500_PRECIO)
    t = pd.to_datetime(precio["fecha"]).dt.year + (pd.to_datetime(precio["fecha"]).dt.month - 0.5) / 12
    rend = pd.read_csv(DATOS_SP500)
    promedio = rend["rendimiento"].mean()

    fig, (ax_p, ax_r) = plt.subplots(2, 1, figsize=(9, 6.2), sharex=True,
                                     gridspec_kw={"height_ratios": (1.1, 1)})

    ax_p.plot(t, precio["precio"], color=NAVY, lw=1.6)
    ax_p.set_yscale("log")
    ax_p.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax_p.set_ylabel("Nivel del índice\n(escala logarítmica)", fontsize=11, color=GRAY)
    ax_p.set_title("Precio: el nivel del S&P 500 cada mes", fontsize=12, color=NAVY,
                   fontweight="bold", loc="left", pad=8)
    p0, p1 = precio["precio"].iloc[0], precio["precio"].iloc[-1]
    ax_p.annotate(f"{p0:,.0f} en 1928", xy=(1928.0, p0), xytext=(1940, 40), fontsize=10, color=BODY,
                  arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})
    ax_p.annotate(f"{p1:,.0f} en 2025", xy=(2025.9, p1), xytext=(2003, 4500), fontsize=10, color=BODY,
                  ha="right", arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})

    colores = [GOLD if v >= 0 else RED for v in rend["rendimiento"]]
    ax_r.bar(rend["anio"], rend["rendimiento"], color=colores, width=0.8, zorder=2)
    ax_r.axhline(0, color=LGRAY, lw=1, zorder=1)
    ax_r.axhline(promedio, color=GRAY, lw=1.4, ls="--", zorder=3)
    ax_r.text(2026.5, promedio, f"promedio\n{promedio:.2%}", fontsize=10, color=BODY, va="center")
    ax_r.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax_r.set_ylabel("Rendimiento anual\ncon dividendos", fontsize=11, color=GRAY)
    ax_r.set_title("Rendimientos: dorado si el año ganó, rojo si perdió", fontsize=12, color=NAVY,
                   fontweight="bold", loc="left", pad=8)
    ax_r.set_xlim(1926, 2026)

    for ax in (ax_p, ax_r):
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)
    fig.suptitle("S&P 500, 1928-2025", fontsize=13, color=NAVY, fontweight="bold", x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(OUT_SP500_SERIE, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_SP500_SERIE}")


def fig_sp500_rendimientos():
    """Histograma de los 98 rendimientos anuales del S&P 500 con dividendos,
    1928-2025 (datos de Damodaran, NYU Stern, en ../datos/), con el promedio
    aritmetico y el rendimiento geometrico marcados (seccion 1.8, ejemplo
    "rendimiento anual esperado del S&P 500")."""
    r = pd.read_csv(DATOS_SP500)["rendimiento"].to_numpy()
    aritmetico = r.mean()
    geometrico = np.prod(1 + r) ** (1 / len(r)) - 1

    fig, ax = plt.subplots(figsize=(8, 4.4))
    bordes = np.round(np.arange(-0.5, 0.61, 0.1), 2) + 0.0
    ax.hist(r, bins=bordes, color=NAVY, alpha=0.85, edgecolor="white", linewidth=2, zorder=2)
    ax.axvline(aritmetico, color=GOLD, lw=2.4, zorder=3)
    ax.axvline(geometrico, color=GRAY, lw=1.8, ls="--", zorder=3)
    tope = ax.get_ylim()[1] * 1.3
    ax.set_ylim(0, tope)
    ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
    ax.text(aritmetico + 0.012, tope * 0.98, f"promedio aritmético\n{aritmetico:.2%}",
            fontsize=10.5, color=BODY, va="top")
    ax.text(geometrico - 0.012, tope * 0.98, f"rendimiento geométrico\n{geometrico:.2%}",
            fontsize=10.5, color=BODY, va="top", ha="right")
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_xticks(bordes)
    ax.set_xlabel("Rendimiento anual con dividendos", fontsize=11, color=GRAY)
    ax.set_ylabel("Número de años", fontsize=11, color=GRAY)
    ax.tick_params(colors=GRAY, labelsize=10)
    ax.set_title("S&P 500, 1928-2025: 98 rendimientos anuales", fontsize=12.5, color=NAVY,
                 fontweight="bold", loc="left", pad=10)
    sns.despine(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_SP500, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_SP500}")


def fig_normal_dos_rendimientos():
    """Dos rendimientos normales con la misma esperanza y distinta varianza
    (seccion 1.9): una accion A N(8%, 15%^2) y una accion B N(8%, 25%^2),
    ilustrativas. Sombrea en cada densidad el area bajo cero, la
    probabilidad de perder en el anio."""
    mu = MU_NORMAL
    (sa, sb) = SIGMA_NORMAL
    x = np.linspace(-0.7, 0.85, 800)
    pa, pb = norm.cdf(0, mu, sa), norm.cdf(0, mu, sb)

    fig, ax = plt.subplots(figsize=(8, 4.4))
    for s, color in ((sa, NAVY), (sb, GOLD)):
        ax.plot(x, norm.pdf(x, mu, s), color=color, lw=2.4, zorder=3)
        xs = x[x <= 0]
        ax.fill_between(xs, 0, norm.pdf(xs, mu, s), color=color, alpha=0.25, lw=0, zorder=2)
    ax.axvline(mu, color=GRAY, lw=1.2, ls="--", zorder=1)
    ax.axvline(0, color=LGRAY, lw=1, zorder=1)
    tope = norm.pdf(mu, mu, sa)
    ax.text(mu + 0.012, tope * 1.08, f"$E[R_A] = E[R_B] = {mu * 100:.0f}\\%$", fontsize=10.5,
            color=BODY, va="top")
    ax.text(0.27, norm.pdf(0.27, mu, sa) + tope * 0.08,
            f"Acción A\n$\\sigma_A = {sa * 100:.0f}\\%$", fontsize=10.5, color=NAVY,
            fontweight="bold")
    ax.text(0.5, norm.pdf(0.5, mu, sb) + tope * 0.06,
            f"Acción B\n$\\sigma_B = {sb * 100:.0f}\\%$", fontsize=10.5, color=GOLD,
            fontweight="bold")
    ax.annotate(f"$P(R_B < 0) = {pb:.3f}$", xy=(-0.32, norm.pdf(-0.32, mu, sb) * 0.5),
                xytext=(-0.69, tope * 0.33), fontsize=10.5, color=BODY,
                arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})
    ax.annotate(f"$P(R_A < 0) = {pa:.3f}$", xy=(-0.1, norm.pdf(-0.1, mu, sa) * 0.5),
                xytext=(-0.55, tope * 0.68), fontsize=10.5, color=BODY,
                arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})
    ax.set_xlim(-0.7, 0.85)
    ax.set_ylim(0, tope * 1.17)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("Rendimiento anual", fontsize=11, color=GRAY)
    ax.set_ylabel("Densidad f(x)", fontsize=11, color=GRAY)
    ax.tick_params(colors=GRAY, labelsize=10)
    ax.set_title("Misma esperanza, distinta varianza (modelo normal, ilustrativo)", fontsize=12.5,
                 color=NAVY, fontweight="bold", loc="left", pad=10)
    sns.despine(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_NORMAL, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_NORMAL}  P(A<0) = {pa:.4f}, P(B<0) = {pb:.4f}")


def _sp500_cola(p=0.05):
    """Rendimientos ordenados del S&P 500 y sus medidas de cola al nivel p:
    cuantil y CVaR empiricos (con q_p = min{x : F(x) >= p}) y los de una
    normal con el mismo promedio y desviacion estandar."""
    r = np.sort(pd.read_csv(DATOS_SP500)["rendimiento"].to_numpy())
    n = len(r)
    k = int(np.ceil(p * n))
    q_emp, cvar_emp = r[k - 1], r[:k].mean()
    mu, s = r.mean(), r.std(ddof=1)
    q_norm = norm.ppf(p, mu, s)
    cvar_norm = mu - s * norm.pdf(norm.ppf(p)) / p
    return r, mu, s, q_emp, cvar_emp, q_norm, cvar_norm


def fig_normal_cuantil_var():
    """Cuantil 5% del rendimiento anual del S&P 500 (seccion 1.10), con los
    datos de 1928-2025 y con una normal del mismo promedio y desviacion.
    Izquierda: histograma de los datos y densidad normal, con la cola de 5%
    del modelo sombreada. Derecha: parte baja de la funcion de distribucion
    empirica (escalones) y de la normal, con la lectura inversa en p = 0.05."""
    p = 0.05
    r, mu, s, _, _, q_norm, _ = _sp500_cola(p)
    x = np.linspace(-0.6, 0.7, 800)

    fig, (ax_d, ax_f) = plt.subplots(1, 2, figsize=(10, 4.4))

    ax_d.hist(r, bins=np.round(np.arange(-0.5, 0.61, 0.1), 2) + 0.0, density=True, color=NAVY,
              alpha=0.25, edgecolor="white", linewidth=2, zorder=1, label="datos")
    ax_d.plot(x, norm.pdf(x, mu, s), color=GOLD, lw=2.4, zorder=3, label="normal")
    xs = x[x <= q_norm]
    ax_d.fill_between(xs, 0, norm.pdf(xs, mu, s), color=RED, alpha=0.45, lw=0, zorder=2)
    ax_d.axvline(q_norm, color=RED, lw=1.4, ls="--", zorder=4)
    tope = norm.pdf(mu, mu, s)
    ax_d.annotate(f"$q_{{0.05}} = {q_norm * 100:.1f}\\%$", xy=(q_norm, tope * 0.75),
                  xytext=(-0.58, tope * 1.05), fontsize=10.5, color=BODY, va="top",
                  arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})
    ax_d.set_xlim(-0.6, 0.7)
    ax_d.set_ylim(0, tope * 1.15)
    ax_d.set_ylabel("Densidad", fontsize=11, color=GRAY)
    ax_d.set_title("Densidad: la cola de 5%", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    xf = np.linspace(-0.5, 0.05, 400)
    escalones = np.arange(1, len(r) + 1) / len(r)
    ax_f.step(r, escalones, where="post", color=NAVY, lw=1.4, alpha=0.35, zorder=2)
    ax_f.plot(xf, norm.cdf(xf, mu, s), color=GOLD, lw=2.4, zorder=3, label="normal")
    ax_f.annotate("", xy=(q_norm, p), xytext=(-0.5, p),
                  arrowprops={"arrowstyle": "-|>", "color": RED, "lw": 1.6})
    ax_f.annotate("", xy=(q_norm, 0), xytext=(q_norm, p),
                  arrowprops={"arrowstyle": "-|>", "color": RED, "lw": 1.6})
    ax_f.plot(q_norm, p, "o", ms=7, color=RED, zorder=4)
    ax_f.text(-0.49, p + 0.008, f"p = {p:.2f}", fontsize=10.5, color=BODY)
    ax_f.text(q_norm + 0.01, 0.008, f"$q_{{0.05}} = {q_norm * 100:.1f}\\%$", fontsize=10.5, color=BODY)
    ax_f.set_xlim(-0.5, 0.05)
    ax_f.set_ylim(0, 0.3)
    ax_f.set_ylabel("F(x) = P(R ≤ x)", fontsize=11, color=GRAY)
    ax_f.set_title("Distribución (parte baja): de p al cuantil", fontsize=12.5, color=NAVY,
                   fontweight="bold", loc="left", pad=10)

    for ax in (ax_d, ax_f):
        ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
        ax.set_xlabel("Rendimiento anual", fontsize=11, color=GRAY)
        ax.tick_params(colors=GRAY, labelsize=10)
        sns.despine(ax=ax)
    fig.suptitle(f"Cuantil 5% del S&P 500 con una normal de media {mu * 100:.2f}% "
                 f"y desviación {s * 100:.2f}%", fontsize=13, color=NAVY, fontweight="bold",
                 x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(OUT_CUANTIL, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_CUANTIL}  q normal = {q_norm:.4f}")


def fig_normal_cvar():
    """VaR y CVaR al 5% del modelo normal del S&P 500 (seccion 1.11): la
    densidad normal sobre el histograma de los rendimientos de 1928-2025 (de
    fondo, sin anotar), la cola de 5% sombreada, una linea en el cuantil (VaR)
    y otra en el promedio de la cola (CVaR, su centro de masa)."""
    p = 0.05
    r, mu, s, _, _, q, cvar = _sp500_cola(p)
    x = np.linspace(-0.6, 0.7, 800)
    tope = norm.pdf(mu, mu, s)

    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.hist(r, bins=np.round(np.arange(-0.5, 0.61, 0.1), 2) + 0.0, density=True, color=NAVY,
            alpha=0.15, edgecolor="white", linewidth=2, zorder=1)
    ax.plot(x, norm.pdf(x, mu, s), color=GOLD, lw=2.4, zorder=3)
    xs = x[x <= q]
    ax.fill_between(xs, 0, norm.pdf(xs, mu, s), color=RED, alpha=0.4, lw=0, zorder=2)
    ax.axvline(q, color=RED, lw=1.4, ls="--", zorder=4)
    ax.axvline(cvar, color=NAVY, lw=1.8, zorder=4)
    ax.annotate(f"VaR: $q_{{0.05}} = {q * 100:.1f}\\%$\n(donde empieza la cola)", xy=(q, tope * 0.9),
                xytext=(0.32, tope * 1.08), fontsize=10.5, color=BODY, va="top",
                arrowprops={"arrowstyle": "-", "color": LGRAY, "lw": 1})
    ax.text(cvar - 0.015, tope * 0.6, f"CVaR $= {cvar * 100:.1f}\\%$\n(promedio de la cola)",
            fontsize=10.5, color=BODY, va="top", ha="right")
    ax.set_xlim(-0.6, 0.7)
    ax.set_ylim(0, tope * 1.12)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("Rendimiento anual", fontsize=11, color=GRAY)
    ax.set_ylabel("Densidad", fontsize=11, color=GRAY)
    ax.tick_params(colors=GRAY, labelsize=10)
    ax.set_title(f"VaR y CVaR al 5% del S&P 500 con una normal de media {mu * 100:.2f}% "
                 f"y desviación {s * 100:.2f}%", fontsize=12.5, color=NAVY, fontweight="bold",
                 loc="left", pad=10)
    sns.despine(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT_CVAR, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_CVAR}  VaR = {q:.4f}, CVaR = {cvar:.4f}")


def main():
    fig_incumplimiento_masa_distribucion()
    fig_accion_lognormal()
    fig_perdida_mixta()
    fig_vector_rendimientos()
    fig_vector_rendimientos(con_esperanza=True)
    fig_sp500_serie()
    fig_sp500_rendimientos()
    fig_normal_dos_rendimientos()
    fig_normal_cuantil_var()
    fig_normal_cvar()


if __name__ == "__main__":
    main()
