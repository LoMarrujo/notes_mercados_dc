"""Simulacion del apendice de 1_valuacion_instrumentos_deuda.md: precio de
un bono con cupon fijo contra uno con cupon variable cuando cambian las
tasas de mercado.

El modelo es Vasicek, un proceso con reversion a la media, calibrado con
datos mensuales de 2001 en adelante (ver calibracion.py y el laboratorio en
practicas/unidad2/laboratorio_calibracion.md). Sustituye a la caminata
aleatoria que tenia antes esta simulacion, que fallaba en dos cosas: su
varianza crecia sin limite, y movia la tasa a 10 anios lo mismo que la
tasa corta.

Dos niveles de largo plazo, que hacen cosas distintas:

- `r_lp_real` (6.11%) sale de la serie historica y gobierna hacia donde
  revierten las tasas en los escenarios simulados.
- `r_lp_desc` (10.91%) se elige para que la curva del modelo reproduzca el
  9.16% que el Bono M a 10 anios rendia el 21 de septiembre de 2026, y solo
  se usa para descontar. Sin el, el modelo descontaria con una curva
  inventada en vez de con la del mercado de ese dia.

Confundirlos tiene consecuencias: simular con el nivel de descuento haria
que las tasas derivaran hacia 10.91%, que no es un escenario razonable.
"""
import numpy as np

from valuacion import BASE, DIAS_CUPON

DT = DIAS_CUPON / BASE  # fraccion de anio entre cupones

# Parametros calibrados por MCO sobre la tasa interbancaria mexicana a 3
# meses, mensual, julio 2001 a agosto 2026. Reproducibles con
# `python notas_unidades/unidad2/codigo/calibracion.py`.
KAPPA = 0.217        # vida media de 3.2 anios
SIGMA = 0.0124       # 1.24 pp anual
R_LP_REAL = 0.0611   # nivel de largo plazo estimado
R0 = 0.0679          # ultima tasa corta observada (agosto de 2026)
R_LP_DESC = 0.1091   # nivel que ancla la curva al 9.16% a 10 anios
SIGMA_M = 0.003      # volatilidad del margen de credito, supuesta


def _afin(tau, kappa, r_lp, sigma):
    """Coeficientes del precio del cupon cero bajo Vasicek:
    P(tau) = exp(ln_A(tau) - B(tau) r).

    B(tau)/tau decrece con tau, y esa es la razon de usar esto en vez de
    aplicar la tasa corta a todos los plazos: la tasa larga se mueve menos
    que la corta."""
    tau = np.asarray(tau, dtype=float)
    b = (1 - np.exp(-kappa * tau)) / kappa
    ln_a = (r_lp - sigma ** 2 / (2 * kappa ** 2)) * (b - tau) - sigma ** 2 * b ** 2 / (4 * kappa)
    return b, ln_a


def _precios_cupon_cero(tau, r, kappa, r_lp, sigma):
    """P(tau) para cada plazo de `tau` y cada tasa corta de `r`.
    Devuelve forma (len(r), len(tau))."""
    b, ln_a = _afin(tau, kappa, r_lp, sigma)
    return np.exp(ln_a[None, :] - b[None, :] * np.asarray(r)[:, None])


def cupon_a_la_par(n, kappa=KAPPA, r_lp=R_LP_DESC, sigma=SIGMA, r0=R0, vn=100.0):
    """Cupon por periodo que hace que un bono de `n` periodos valga
    exactamente su valor nominal con la curva del modelo. Arrancar a la par
    es lo que permite comparar la dispersion de los dos instrumentos sin
    que uno empiece con ventaja."""
    tau = np.arange(1, n + 1) * DT
    p = _precios_cupon_cero(tau, [r0], kappa, r_lp, sigma)[0]
    return float(vn * (1 - p[-1]) / p.sum())


def simular_tasas(pasos, trayectorias, kappa=KAPPA, r_lp=R_LP_REAL, sigma=SIGMA,
                  r0=R0, semilla=2026, modelo="vasicek"):
    """Trayectorias de la tasa corta, una observacion por fecha de cupon.

    Vasicek se simula con su discretizacion exacta, que no necesita esquema
    de Euler ni pasos finos:

        R_{k+1} = r_lp + (R_k - r_lp)e^{-kappa dt}
                  + sigma sqrt((1-e^{-2 kappa dt})/(2 kappa)) Z

    `modelo="caminata"` conserva la caminata aleatoria anterior, que sigue
    siendo el punto de comparacion contra el que se mide cualquier modelo
    de tasas fuera de muestra."""
    rng = np.random.default_rng(semilla)
    z = rng.standard_normal((trayectorias, pasos))
    r = np.empty((trayectorias, pasos + 1))
    r[:, 0] = r0
    if modelo == "vasicek":
        phi = np.exp(-kappa * DT)
        desv = sigma * np.sqrt((1 - np.exp(-2 * kappa * DT)) / (2 * kappa))
        for k in range(pasos):
            r[:, k + 1] = r_lp + (r[:, k] - r_lp) * phi + desv * z[:, k]
    elif modelo == "caminata":
        r[:, 1:] = r0 + (sigma * np.sqrt(DT) * z).cumsum(axis=1)
    else:
        raise ValueError(f"modelo desconocido: {modelo}")
    return r


def simular_precios(cupon=None, n=20, pasos=10, trayectorias=10_000,
                    kappa=KAPPA, sigma=SIGMA, r_lp_real=R_LP_REAL,
                    r_lp_desc=R_LP_DESC, r0=R0, sigma_m=SIGMA_M, vn=100.0,
                    semilla=2026, modelo="vasicek"):
    """Precio de un bono con cupon fijo y de uno con cupon variable en cada
    fecha de cupon, para `trayectorias` escenarios de tasas.

    Fijo: se valua descontando los `n-k` flujos que le quedan con la curva
    del modelo evaluada en la tasa corta de ese escenario. Como el factor
    de descuento de cada plazo responde menos que la tasa corta, el precio
    se mueve menos que si se aplicara la tasa corta a todos los plazos.

    Variable: su cupon se reajusta a la tasa vigente en cada reseteo, asi
    que lo unico que lo separa de la par es el margen acumulado M_k, un
    flujo de M_k dt v_N por periodo que se descuenta con la misma curva.

    Devuelve (fijo, variable), de forma (trayectorias, pasos+1)."""
    if cupon is None:
        cupon = cupon_a_la_par(n, kappa, r_lp_desc, sigma, r0, vn)
    rng = np.random.default_rng(semilla + 1)
    margen = np.concatenate([
        np.zeros((trayectorias, 1)),
        (sigma_m * np.sqrt(DT) * rng.standard_normal((trayectorias, pasos))).cumsum(axis=1),
    ], axis=1)
    r = simular_tasas(pasos, trayectorias, kappa, r_lp_real, sigma, r0, semilla, modelo)

    fijo = np.empty_like(r)
    variable = np.empty_like(r)
    for k in range(pasos + 1):
        tau = np.arange(1, n - k + 1) * DT
        p = _precios_cupon_cero(tau, r[:, k], kappa, r_lp_desc, sigma)
        flujos = np.full(n - k, cupon)
        flujos[-1] += vn
        fijo[:, k] = p @ flujos
        variable[:, k] = vn - margen[:, k] * DT * vn * p.sum(axis=1)
    return fijo, variable
