"""Genera las figuras de 1_probabilidad_y_riesgo.md. Se versiona junto a las
imagenes que produce para que sean reproducibles: si el contenido cambia, se
corrige este script y se vuelve a correr, nunca se edita el .png a mano.

Uso:
    python notas_unidades/unidad3/img/generar_figuras.py
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import lognorm

NAVY = "#1E2761"
GOLD = "#C9A227"
GRAY = "#5B6482"
LGRAY = "#A6ADC7"
BODY = "#27314D"

plt.rcParams["font.family"] = "Calibri"
sns.set_theme(style="white", rc={"axes.edgecolor": LGRAY, "axes.linewidth": 0.8})

IMG_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_INCUMPLIMIENTO = os.path.join(IMG_DIR, "incumplimiento_masa_distribucion.png")

OUT_ACCION = os.path.join(IMG_DIR, "accion_lognormal_densidad_distribucion.png")

PROB_INCUMPLIR = 0.05  # ilustrativa, la misma del ejemplo de la nota
S0_ACCION, MU_ACCION, SIGMA_ACCION = 100, 0.05, 0.25  # ilustrativos
VALOR_NOMINAL, PERDIDA_MIN = 100, 20  # si incumple, la perdida es uniforme en [20, 100]
OUT_PERDIDA = os.path.join(IMG_DIR, "perdida_incumplimiento_mixta.png")


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
    ax_d.set_ylabel("F'(x)", fontsize=11, color=GRAY)
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
    ax_d.set_ylabel("F'(x) fuera del salto", fontsize=11, color=GRAY)
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


def main():
    fig_incumplimiento_masa_distribucion()
    fig_accion_lognormal()
    fig_perdida_mixta()


if __name__ == "__main__":
    main()
