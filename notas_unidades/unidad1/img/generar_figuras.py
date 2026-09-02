"""Genera las figuras de representaciones graficas de flujos estocasticos
usadas en 4_ciencia_inversion.md, seccion "Que es invertir?". Se versiona
junto a las imagenes que produce para que sean reproducibles: si el
contenido cambia, se corrige este script y se vuelve a correr, nunca se
edita el .png a mano.

Uso:
    python notas_unidades/unidad1/img/generar_figuras.py
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
OUT_INTERES = os.path.join(IMG_DIR, "interes_simple_vs_compuesto.png")
OUT_TNA_TEA = os.path.join(IMG_DIR, "tna_vs_tea_continua.png")
OUT_DETERMINISTICO = os.path.join(IMG_DIR, "flujo_deterministico.png")
OUT_BINOMIAL = os.path.join(IMG_DIR, "arbol_binomial.png")
OUT_LATTICE = os.path.join(IMG_DIR, "red_binomial.png")
OUT_TRINOMIAL = os.path.join(IMG_DIR, "arbol_multinomial.png")
OUT_PATHS = os.path.join(IMG_DIR, "trayectorias_simuladas.png")
OUT_FAN = os.path.join(IMG_DIR, "fan_chart.png")


def _strip_spines(ax, keep=()):
    for spine in ("top", "right", "left", "bottom"):
        if spine in keep:
            ax.spines[spine].set_color(LGRAY)
        else:
            ax.spines[spine].set_visible(False)
    ax.tick_params(colors=GRAY, labelsize=9)


def panel_lattice(ax):
    """Red binomial recombinante: dos caminos distintos llegan al mismo nodo."""
    T = 3
    for t in range(T + 1):
        for j in range(t + 1):
            x, y = t, t / 2 - j
            if t < T:
                ax.plot([x, t + 1], [y, (t + 1) / 2 - j], color=LGRAY, lw=1.5, zorder=1)
                ax.plot([x, t + 1], [y, (t + 1) / 2 - (j + 1)], color=LGRAY, lw=1.5, zorder=1)
    for t in range(T + 1):
        for j in range(t + 1):
            x, y = t, t / 2 - j
            ax.scatter([x], [y], s=110, color=NAVY, zorder=3, edgecolor="white", linewidth=1)
    ax.set_xlabel("tiempo", fontsize=10, color=GRAY)
    ax.set_xticks(range(T + 1))
    ax.set_yticks([])
    ax.set_title("Red binomial recombinante", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    _strip_spines(ax, keep=("bottom",))


def panel_trinomial(ax):
    """Arbol multinomial: mas de dos resultados posibles por periodo."""
    ax.scatter([0], [0], s=120, color=NAVY, zorder=3, edgecolor="white", linewidth=1)
    ramas = [("sube", 1, GOLD), ("igual", 0, GRAY), ("baja", -1, NAVY)]
    for label, y, color in ramas:
        ax.plot([0, 1], [0, y], color=LGRAY, lw=1.5, zorder=1)
        ax.scatter([1], [y], s=100, color=color, zorder=3, edgecolor="white", linewidth=1)
        ax.text(1.12, y, f"{label}  (p = 1/3)", va="center", fontsize=11, color=BODY, fontweight="bold")
    ax.set_xlim(-0.3, 2.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["t = 0", "t = 1"])
    ax.set_yticks([])
    ax.set_title("Árbol multinomial", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    _strip_spines(ax, keep=("bottom",))


def panel_paths(ax):
    """Trayectorias simuladas (random walk / Monte Carlo)."""
    rng = np.random.default_rng(6)
    n_paths, n_steps = 9, 40
    steps = rng.normal(0, 0.028, size=(n_paths, n_steps))
    paths = 100 * np.cumprod(1 + steps, axis=1)
    paths = np.hstack([100 * np.ones((n_paths, 1)), paths])
    t = np.arange(paths.shape[1])
    for p in paths:
        ax.plot(t, p, color=LGRAY, lw=1.2, alpha=0.85, zorder=1)
    ax.plot(t, paths.mean(axis=0), color=NAVY, lw=2.6, zorder=3, label="promedio")
    ax.set_xlabel("tiempo", fontsize=10, color=GRAY)
    ax.set_ylabel("valor", fontsize=10, color=GRAY)
    ax.legend(frameon=False, fontsize=10, labelcolor=BODY, loc="upper left")
    ax.set_title("Trayectorias simuladas", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    _strip_spines(ax, keep=("bottom", "left"))


def panel_fan(ax):
    """Fan chart: banda de confianza que se abre conforme pasa el tiempo."""
    t = np.arange(0, 41)
    mean = np.full_like(t, 100, dtype=float)
    spread = 4.2 * np.sqrt(t)
    for mult, alpha in ((1.0, 0.3), (2.0, 0.16)):
        ax.fill_between(t, mean - mult * spread, mean + mult * spread,
                         color=NAVY, alpha=alpha, linewidth=0)
    ax.plot(t, mean, color=GOLD, lw=2.4, zorder=3)
    ax.set_xlabel("tiempo", fontsize=10, color=GRAY)
    ax.set_ylabel("valor", fontsize=10, color=GRAY)
    ax.set_title("Distribución de valores futuros", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    _strip_spines(ax, keep=("bottom", "left"))


def fig_interes_simple_vs_compuesto():
    """Crecimiento lineal (interés simple) vs. geométrico (interés
    compuesto) de $100 al 10% anual, siguiendo la Figura 2.1 de
    Luenberger."""
    t = np.arange(0, 26)
    simple = 100 * (1 + 0.10 * t)
    compound = 100 * (1.10 ** t)

    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.fill_between(t, simple, compound, color=NAVY, alpha=0.07, zorder=1)
    ax.plot(t, simple, color=GOLD, lw=2.6, zorder=3)
    ax.plot(t, compound, color=NAVY, lw=2.8, zorder=3)

    ax.text(t[-1] + 0.6, simple[-1], f"Interés simple\n\${simple[-1]:,.0f}",
            color=GOLD, fontsize=11, fontweight="bold", va="center")
    ax.text(t[-1] + 0.6, compound[-1], f"Interés compuesto\n\${compound[-1]:,.0f}",
            color=NAVY, fontsize=11, fontweight="bold", va="center")

    ax.set_xlabel("años", fontsize=10.5, color=GRAY)
    ax.set_ylabel("valor de \\$100 invertidos al 10%", fontsize=10.5, color=GRAY)
    ax.set_xlim(0, 33)
    ax.set_ylim(0, compound[-1] * 1.12)
    ax.set_title("Interés simple vs. compuesto", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    _strip_spines(ax, keep=("bottom", "left"))
    fig.tight_layout()
    fig.savefig(OUT_INTERES, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_INTERES}")


def fig_tna_vs_tea_continua():
    """TNA vs. TEA bajo capitalización continua (TEA = e^TNA - 1): el
    efecto se acelera mientras más alta es la tasa nominal."""
    tna = np.linspace(0, 100, 200)
    tea = (np.exp(tna / 100) - 1) * 100

    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.fill_between(tna, tna, tea, color=NAVY, alpha=0.07, zorder=1)
    ax.plot(tna, tna, color=GOLD, lw=2.6, zorder=3)
    ax.plot(tna, tea, color=NAVY, lw=2.8, zorder=3)

    for x in (10, 20, 50, 100):
        y = (np.exp(x / 100) - 1) * 100
        ax.scatter([x], [y], s=45, color=NAVY, zorder=4, edgecolor="white", linewidth=1)

    ax.text(tna[-1] + 2, tna[-1], "TNA\n(sin efecto)", color=GOLD, fontsize=11,
            fontweight="bold", va="center")
    ax.text(tna[-1] + 2, tea[-1], f"TEA continua\n{tea[-1]:,.0f}%", color=NAVY, fontsize=11,
            fontweight="bold", va="center")

    ax.set_xlabel("TNA (%)", fontsize=10.5, color=GRAY)
    ax.set_ylabel("TEA continua (%)", fontsize=10.5, color=GRAY)
    ax.set_xlim(0, 122)
    ax.set_ylim(0, tea[-1] * 1.1)
    ax.set_title("TNA vs. TEA bajo capitalización continua", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    _strip_spines(ax, keep=("bottom", "left"))
    fig.tight_layout()
    fig.savefig(OUT_TNA_TEA, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_TNA_TEA}")


def fig_flujo_deterministico():
    """Diagrama de flujo de efectivo determinístico: linea de tiempo con
    una barra vertical por flujo, hacia arriba si es entrada y hacia abajo
    si es salida. La altura usa una escala de raiz cuadrada (monotónica,
    preserva el orden) en vez de lineal: con -1,000/+100/+100/+1,100
    lineales, los flujos de $100 quedan casi invisibles junto a los de
    ~$1,000; la raiz cuadrada los mantiene legibles sin dejar de mostrar
    que los flujos grandes son mayores."""
    periods = [0, 1, 2, 3]
    flows = [-1000, 100, 100, 1100]

    def scale(f):
        return np.sign(f) * np.sqrt(abs(f))

    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.axhline(0, color=LGRAY, lw=1.4, zorder=1)
    ax.annotate("", xy=(3.55, 0), xytext=(-0.35, 0),
                arrowprops={"arrowstyle": "-|>", "color": LGRAY, "lw": 1.4})
    ax.text(3.6, 0, "tiempo", va="center", fontsize=10, color=GRAY)

    for t, f in zip(periods, flows):
        y = scale(f)
        color = NAVY if f > 0 else GOLD
        ax.annotate("", xy=(t, y), xytext=(t, 0),
                    arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.6, "mutation_scale": 16})
        label = f"${f:,}" if f > 0 else f"-${abs(f):,}"
        va, dy = ("bottom", 10) if f > 0 else ("top", -10)
        ax.annotate(label, xy=(t, y), xytext=(0, dy), textcoords="offset points",
                    ha="center", va=va, fontsize=11, color=BODY, fontweight="bold")
        ax.annotate(str(t), xy=(t, 0), xytext=(0, 10 if f < 0 else -18),
                    textcoords="offset points", ha="center",
                    va="bottom" if f < 0 else "top", fontsize=10, color=GRAY)

    ax.set_xlim(-0.6, 4.3)
    ax.set_ylim(-40, 44)
    ax.axis("off")
    ax.set_title("Flujo de efectivo determinístico", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    fig.tight_layout()
    fig.savefig(OUT_DETERMINISTICO, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_DETERMINISTICO}")


def fig_arbol_binomial():
    """Arbol binomial de un periodo: comprar hoy en $100, subir a $130 o
    bajar a $80 en un año, cada rama con probabilidad 0.5."""
    fig, ax = plt.subplots(figsize=(6, 3.2))

    ax.annotate("", xy=(0, 0), xytext=(0, -1),
                arrowprops={"arrowstyle": "-|>", "color": GOLD, "lw": 2.6, "mutation_scale": 16})
    ax.text(0, -1.18, "$100", ha="center", va="top", fontsize=11, color=BODY, fontweight="bold")

    ramas = [("$130", 1, "p = 0.5", NAVY), ("$80", -1, "p = 0.5", NAVY)]
    for label, y, prob, color in ramas:
        ax.plot([0, 1], [0, y], color=LGRAY, lw=1.6, zorder=1)
        ax.scatter([1], [y], s=100, color=color, zorder=3, edgecolor="white", linewidth=1)
        ax.text(1.12, y, f"{label}   ({prob})", va="center", fontsize=11.5, color=BODY, fontweight="bold")

    ax.scatter([0], [0], s=120, color=NAVY, zorder=3, edgecolor="white", linewidth=1)
    ax.text(-0.08, 0, "t = 0", ha="right", va="center", fontsize=10, color=GRAY)
    ax.text(1, 1.35, "t = 1", ha="center", va="center", fontsize=10, color=GRAY)

    ax.set_xlim(-0.6, 2.3)
    ax.set_ylim(-1.6, 1.7)
    ax.axis("off")
    ax.set_title("Árbol binomial de un periodo", fontsize=12.5, color=NAVY,
                  fontweight="bold", loc="left", pad=10)
    fig.tight_layout()
    fig.savefig(OUT_BINOMIAL, dpi=200, facecolor="white")
    print(f"figura generada: {OUT_BINOMIAL}")


def _standalone(panel_fn, out_path, figsize=(6.5, 3.2)):
    fig, ax = plt.subplots(figsize=figsize)
    panel_fn(ax)
    fig.tight_layout()
    fig.savefig(out_path, dpi=200, facecolor="white")
    print(f"figura generada: {out_path}")


def main():
    fig_interes_simple_vs_compuesto()
    fig_tna_vs_tea_continua()
    fig_flujo_deterministico()
    fig_arbol_binomial()
    _standalone(panel_lattice, OUT_LATTICE)
    _standalone(panel_trinomial, OUT_TRINOMIAL)
    _standalone(panel_paths, OUT_PATHS, figsize=(7, 3.2))
    _standalone(panel_fan, OUT_FAN, figsize=(7, 3.2))


if __name__ == "__main__":
    main()
