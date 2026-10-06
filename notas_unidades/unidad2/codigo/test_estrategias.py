"""Pruebas de las funciones y los ejemplos de 4_estrategias_renta_fija.md.

Uso (desde la raiz del repo):
    python -m pytest notas_unidades/unidad2/codigo -q
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from estrategias import (  # noqa: E402
    calce_flujos, cupon_anual_implicito, duracion_macaulay, ejemplos,
    rendimiento_horizonte, tasa_equilibrio,
)
from valuacion import flujos_bono, precio_bono  # noqa: E402

E = ejemplos()


def test_cupones_implicitos_de_la_nota_de_rendimiento():
    # cupon implicito con un pago anual (4_estrategias usa flujos anuales);
    # con pagos cada 182 dias, el apendice de 2_ da 8.61% a 10 anios
    assert round(E["c3"], 2) == 8.61
    assert round(E["c10"], 4) == 8.5951


@pytest.mark.parametrize("c,n,r", [(8, 3, 0.09), (5, 10, 0.07), (0, 4, 0.1)])
def test_cupon_implicito_recupera_el_cupon(c, n, r):
    assert cupon_anual_implicito(float(precio_bono(c, n, r)), r, n) == pytest.approx(c)


def test_calce_cubre_cada_pago_y_deja_el_cupon_del_anio_2():
    for t, oblig, flujo, sobrante in E["tabla"]:
        assert flujo >= oblig - 1e-6
    assert [round(f[3], 2) for f in E["tabla"]] == [0.0, 7924.34, 0.0]


def test_calce_ejemplo_de_la_nota():
    assert round(E["titulos"][3], 2) == 920.76
    assert round(E["titulos"][3] * 100.94, 2) == 92941.17
    assert round(E["titulos"][1] * E["precio_cete"], 2) == 85795.08
    assert round(E["costo"], 2) == 178736.26


def test_calce_con_obligaciones_distintas_cubre_exacto():
    oblig = {1: 50.0, 2: 80.0, 3: 120.0}
    bonos = {1: (95.0, 0.0), 2: (98.0, 6.0), 3: (101.0, 9.0)}
    _, _, tabla = calce_flujos(oblig, bonos)
    assert all(abs(s) < 1e-9 for *_, s in tabla)


def test_escenarios_a_un_anio():
    esc = {round(d * 1e4): round(r * 100, 2) for d, r in E["escenarios"].items()}
    assert esc == {-100: 15.45, 0: 9.16, 100: 3.36}
    assert round(E["r_cete"] * 100, 2) == 7.32


def test_sin_cambio_de_tasa_el_rendimiento_es_el_ytm():
    c = cupon_anual_implicito(96.40, 0.0916, 10)
    assert rendimiento_horizonte(96.40, c, 10, 0.0916) == pytest.approx(0.0916)


def test_tasa_de_equilibrio_iguala_al_cete():
    assert round(E["r_eq"] * 100, 2) == 9.47
    assert rendimiento_horizonte(96.40, E["c10"], 10, E["r_eq"]) == pytest.approx(E["r_cete"])


def test_duracion_de_un_cupon_cero_es_su_plazo():
    assert duracion_macaulay([0, 0, 0, 100], 0.08) == pytest.approx(4)


def test_duracion_con_cupones_es_menor_que_el_plazo():
    assert duracion_macaulay(flujos_bono(8, 10, 100), 0.09) < 10


def test_inmunizacion_ejemplo_de_la_nota():
    v0, d_obl, m_a, m_b = E["inm"]
    assert round(v0, 2) == 168961.47
    assert round(d_obl, 2) == 1.91
    assert round(E["d_b"], 2) == 7.05
    assert m_a + m_b == pytest.approx(v0)
    assert (round(m_a, 2), round(m_b, 2)) == (143451.07, 25510.39)


def test_inmunizacion_protege_ante_choques_de_100_pb():
    for vp, vo in E["choque"].values():
        assert vp >= vo
        assert (vp - vo) / vo < 0.001


def test_tasa_equilibrio_con_bono_a_la_par():
    r_eq = tasa_equilibrio(100.0, 9.0, 5, 0.09)
    assert r_eq == pytest.approx(0.09, abs=1e-8)
