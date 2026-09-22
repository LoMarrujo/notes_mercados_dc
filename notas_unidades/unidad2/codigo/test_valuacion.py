"""Pruebas de las formulas de 1_valuacion_instrumentos_deuda.md.

Uso (desde la raiz del repo):
    python -m pytest notas_unidades/unidad2/codigo -q
"""
import os
import sys

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calibracion import (  # noqa: E402
    ar1_a_vasicek, kappa_efectiva, nivel_que_ancla, vasicek_afin,
)
from simulacion import (  # noqa: E402
    DT, KAPPA, R0, R_LP_DESC, SIGMA, cupon_a_la_par, simular_precios, simular_tasas,
)
from valuacion import (  # noqa: E402
    cupon_implicito, flujos_bono, precio_amortizable, precio_bono,
    precio_bono_m, precio_descuento, precio_flujos, tabla_amortizacion,
)


def test_cete_ejemplo_de_la_nota():
    # CETE a 28 dias, subasta del 15 de septiembre de 2026 al 6.25%
    assert precio_descuento(10, 0.0625, 28) == pytest.approx(9.9516, abs=5e-5)
    # CETE a 91 dias al 6.66% (cetesdirecto, 21 de septiembre de 2026)
    assert precio_descuento(10, 0.0666, 91) == pytest.approx(9.8344, abs=5e-5)


@pytest.mark.parametrize("c, n, r", [(8, 10, 0.09), (4.5, 20, 0.0455), (0, 5, 0.07), (12, 3, 0.02)])
def test_formula_cerrada_igual_suma_de_flujos(c, n, r):
    assert precio_bono(c, n, r, 100) == pytest.approx(precio_flujos(flujos_bono(c, n, 100), r))


def test_bono_m_ejemplo_de_la_nota():
    assert precio_bono(8, 10, 0.09, 100) == pytest.approx(93.58, abs=5e-3)


@pytest.mark.parametrize("n", [1, 5, 10, 30])
def test_a_la_par_cuando_cupon_igual_tasa(n):
    assert precio_bono(9, n, 0.09, 100) == pytest.approx(100)


def test_descuento_y_premio_segun_cupon_contra_tasa():
    assert precio_bono(6, 10, 0.09, 100) < 100 < precio_bono(12, 10, 0.09, 100)


def test_limite_cuando_r_tiende_a_cero():
    # la formula excluye r = 0: en el limite, el bono devuelve todos sus flujos sin descontar
    assert precio_bono(8, 10, 1e-7, 100) == pytest.approx(10 * 8 + 100, rel=1e-5)
    with pytest.raises(ValueError):
        precio_bono(8, 10, 0.0, 100)


def test_bono_m_ejemplo_oficial_de_banxico():
    # 18% de cupon, 6 cupones por cobrar, 21 dias devengados, rendimiento 19%
    sucio, limpio = precio_bono_m(0.18, 0.19, 6, 21)
    assert sucio == pytest.approx(98.81269, abs=5e-6)
    assert limpio == pytest.approx(97.76269, abs=5e-6)


def test_cupon_implicito_recupera_el_cupon():
    # con un cupon de 8.5% y rendimiento de 9%, el precio implica ese mismo cupon
    c_per = 100 * 0.085 * 182 / 360
    precio = precio_bono(c_per, 20, 0.09 * 182 / 360, 100)
    assert cupon_implicito(precio, 0.09, 20) == pytest.approx(0.085)


@pytest.mark.parametrize("sistema, retiros", [
    ("frances", None), ("aleman", None),
    ("sinking", [50_000] * 5 + [0] * 14 + [250_000]),
])
def test_amortizacion_cierra_el_saldo_y_paga_el_capital(sistema, retiros):
    a, r, n = 500_000, 0.10, 20
    t = tabla_amortizacion(sistema, a, r, n, retiros)
    assert t["abono_capital"].sum() == pytest.approx(a)
    assert t["saldo_final"].iloc[-1] == pytest.approx(0, abs=1e-6)
    assert np.allclose(t["pago"], t["interes"] + t["abono_capital"])
    # descontado a la tasa del credito, el valor presente de los pagos es el capital prestado
    assert precio_amortizable(t, r) == pytest.approx(a)


def test_frances_pago_constante_y_aleman_pago_decreciente():
    a, r, n = 500_000, 0.10, 20
    fr = tabla_amortizacion("frances", a, r, n)
    al = tabla_amortizacion("aleman", a, r, n)
    assert fr["pago"].iloc[0] == pytest.approx(58_729.6, abs=0.5)
    assert np.allclose(fr["pago"], fr["pago"].iloc[0])
    assert np.allclose(np.diff(al["pago"]), -r * a / n)  # baja $2,500 cada anio
    assert al["pago"].iloc[0] == pytest.approx(75_000)


def test_ambos_instrumentos_arrancan_a_la_par():
    fijo, variable = simular_precios(trayectorias=500)
    assert fijo[:, 0] == pytest.approx(100)
    assert variable[:, 0] == pytest.approx(100)


def test_variable_menos_dispersion_que_fijo():
    fijo, variable = simular_precios(trayectorias=2_000)
    assert variable[:, 2].std() < fijo[:, 2].std()


def test_vasicek_dispersa_menos_que_la_caminata_aleatoria():
    # es la razon de haber cambiado de modelo: la caminata aleatoria no
    # revierte a la media y mueve la tasa larga igual que la corta
    fijo_v, _ = simular_precios(trayectorias=2_000, modelo="vasicek")
    fijo_c, _ = simular_precios(trayectorias=2_000, modelo="caminata")
    assert fijo_v[:, -1].std() < fijo_c[:, -1].std()


def test_tasas_revierten_hacia_el_nivel_de_largo_plazo():
    # arrancando por encima del nivel, la media de los escenarios baja hacia el
    r = simular_tasas(pasos=60, trayectorias=5_000, r_lp=0.05, r0=0.10)
    assert r[:, 0] == pytest.approx(0.10)
    assert r[:, -1].mean() < r[:, 10].mean() < 0.10
    assert r[:, -1].mean() == pytest.approx(0.05, abs=0.01)


def test_varianza_estacionaria_converge():
    # a horizonte largo la varianza tiende a sigma^2/(2 kappa), no crece sin limite
    r = simular_tasas(pasos=400, trayectorias=8_000, kappa=KAPPA, sigma=SIGMA)
    assert r[:, -1].std() == pytest.approx(SIGMA / np.sqrt(2 * KAPPA), rel=0.05)


def test_ar1_a_vasicek_recupera_los_parametros():
    # ida y vuelta: simular con kappa y sigma conocidos, estimarlos por MCO
    kappa, sigma, r_lp = 0.30, 0.015, 0.07
    r = simular_tasas(pasos=40_000, trayectorias=1, kappa=kappa, r_lp=r_lp,
                      sigma=sigma, r0=r_lp, semilla=7)[0]
    y, x = r[1:], np.column_stack([np.ones(len(r) - 1), r[:-1]])
    a, b = np.linalg.lstsq(x, y, rcond=None)[0]
    resid = y - x @ np.array([a, b])
    par = ar1_a_vasicek(a, b, resid.std(ddof=2), DT)
    assert par["kappa"] == pytest.approx(kappa, rel=0.10)
    assert par["sigma"] == pytest.approx(sigma, rel=0.05)
    assert par["r_lp"] == pytest.approx(r_lp, abs=0.005)


def test_ar1_a_vasicek_rechaza_proceso_explosivo():
    with pytest.raises(ValueError):
        ar1_a_vasicek(0.1, 1.02, 0.01, DT)


def test_kappa_efectiva_corrige_la_pendiente():
    # con la pendiente en la especificacion, el coeficiente crudo de la tasa
    # corta pasa de 1 y sugeriria un proceso explosivo; el total si revierte
    params = pd.Series({"const": -0.18, "r_corta": 1.0375, "pendiente": 0.0877})
    ef = kappa_efectiva(params)
    assert params["r_corta"] > 1
    assert ef["b_efectiva"] == pytest.approx(1.0375 - 0.0877)
    assert 0 < ef["b_efectiva"] < 1
    assert ef["kappa"] > 0


def test_tasa_larga_se_mueve_menos_que_la_corta():
    afin = vasicek_afin([1, 5, 10, 30], KAPPA, R_LP_DESC, SIGMA, R0)
    sens = afin["sensibilidad"]
    assert np.all(sens < 1)
    assert np.all(np.diff(sens) < 0)  # decrece con el plazo
    assert sens[2] == pytest.approx(0.41, abs=0.01)  # 10 anios: 41 pb por cada 100


def test_nivel_que_ancla_reproduce_el_rendimiento_observado():
    # el 9.16% del Bono M a 10 anios del 21 de septiembre de 2026
    nivel = nivel_que_ancla(0.0916, 10, KAPPA, SIGMA, R0)
    assert vasicek_afin(10, KAPPA, nivel, SIGMA, R0)["rendimiento"] == pytest.approx(0.0916)


def test_cupon_a_la_par_deja_el_bono_en_su_valor_nominal():
    c = cupon_a_la_par(20)
    fijo, _ = simular_precios(cupon=c, trayectorias=100)
    assert fijo[0, 0] == pytest.approx(100)
