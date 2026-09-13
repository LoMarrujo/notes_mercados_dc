"""Genera los diagramas de flujo de efectivo de las mecanicas de pago
usados en 0_caracteristicas_mercado_deuda.md, seccion "Las mecanicas de
pago como vector de flujos". Se versiona junto a las imagenes que produce
para que sean reproducibles: si el contenido cambia, se corrige este
script y se vuelve a correr, nunca se edita el .png a mano.

Uso:
    python notas_unidades/unidad2/img/generar_figuras.py
"""
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

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
    capital constante (sistema aleman): mismo capital prestado ($100) y
    misma tasa (10%), dos formas muy distintas de repartir el pago."""
    periods = [0, 1, 2, 3]
    bullet = [-100, 10, 10, 110]
    amortizado = [-100, 43.33, 40.00, 36.67]

    y_max = max(abs(_scale(f)) for f in bullet + amortizado) * 1.335

    fig, axes = plt.subplots(2, 1, figsize=(7.5, 6.2))
    _panel_flujo(axes[0], periods, bullet, "Bullet: todo el capital al vencimiento", y_max=y_max)
    _panel_flujo(axes[1], periods, amortizado, "Amortizado: capital constante cada periodo (sistema alemán)", y_max=y_max)
    fig.tight_layout()
    fig.savefig(OUT_AMORTIZACION, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_AMORTIZACION}")


def main():
    fig_flujo_efectivo([0, 1], [-90.91, 100], OUT_DESCUENTO,
                        "Flujo de efectivo a descuento (CETE)")
    fig_flujo_efectivo([0, 1, 2, 3], [-100, 10, 10, 110], OUT_CUPON_FIJO,
                        "Flujo de efectivo con cupón fijo (Bono M)")
    fig_flujo_cupon_variable()
    fig_flujo_amortizacion()


if __name__ == "__main__":
    main()
