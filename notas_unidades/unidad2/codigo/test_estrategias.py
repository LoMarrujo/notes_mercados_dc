"""Pruebas de las funciones y los ejemplos de 4_estrategias_renta_fija.md.

Uso (desde la raiz del repo):
    python -m pytest notas_unidades/unidad2/codigo -q
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from estrategias import (  # noqa: E402
    CETES, calce_flujos, cupon_anual_implicito, depreciacion_equilibrio, precio_cete,
    ejemplos, rendimiento_bonde_f, rendimiento_en_dolares, rendimiento_horizonte, rendimiento_real,
    tasa_equilibrio, tasa_fondeo_equilibrio, ytm_curva,
)
from valuacion import precio_bono  # noqa: E402

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


def test_tasa_equilibrio_con_bono_a_la_par():
    r_eq = tasa_equilibrio(100.0, 9.0, 5, 0.09)
    assert r_eq == pytest.approx(0.09, abs=1e-8)


def test_calce_valuado_con_la_curva():
    assert round(E["v_oblig_curva"], 2) == 172035.24
    assert round(E["v_sobrante"], 2) == 6826.67
    assert round(E["costo"] - E["v_oblig_curva"], 2) == 6701.02


def test_ytm_interpolado_en_la_curva():
    assert round(ytm_curva(2) * 100, 2) == 7.74
    assert round(ytm_curva(9) * 100, 3) == 9.128
    assert ytm_curva(10) == pytest.approx(0.0916)


def test_recorrer_la_curva_sin_cambio():
    assert round(E["rodada"][3] * 100, 2) == 9.13
    assert round(E["rodada"][10] * 100, 2) == 9.35
    # precio de venta del Bono M a 10 anios como bono a 9, al 9.128% de la curva
    assert round(precio_bono(E["c10"], 9, ytm_curva(9)), 2) == 96.82


def test_bonde_f_contra_cete():
    bf = {round(d * 1e4): round(r * 100, 2) for d, r in E["bonde_f"].items()}
    assert bf == {0: 6.79, 50: 7.33, 100: 7.88}
    assert round(E["fondeo_eq"] * 100, 2) == 6.99
    assert rendimiento_bonde_f(tasa_fondeo_equilibrio(0.05)) == pytest.approx(0.05)


def test_udibono_contra_bono_m():
    assert round(E["infl_aprox"] * 100, 2) == 4.41
    assert round(E["infl_exacta"] * 100, 2) == 4.21
    real = {k: round(v * 100, 2) for k, v in E["real_bono_m"].items()}
    assert real == {0.03: 5.98, 0.06: 2.98}
    # con la inflacion implicita exacta, el Bono M rinde lo mismo que el UDIBONO
    assert rendimiento_real(0.0916, E["infl_exacta"]) == pytest.approx(0.0475)


def test_comprar_y_conservar_bono_m_3_anios():
    (n, flujos, vf, rend), (_, _, vf_baja, rend_baja) = E["conservar"].values()
    assert round(n, 2) == 990.69
    assert [round(float(f), 2) for f in flujos] == [8526.19, 8526.19, 107594.94]
    # reinvirtiendo al YTM de la compra se gana exactamente ese YTM
    assert rend == pytest.approx(0.0824)
    assert round(vf, 2) == 126812.88
    assert round(vf_baja, 2) == 126345.94
    assert round(rend_baja * 100, 2) == 8.11


def test_escalera_de_cetes():
    parte, tasa = E["escalera"]
    assert parte == 25000.0
    assert round(tasa * 100, 2) == 6.76


def test_calce_no_cuesta_mas_que_lo_que_compra():
    # el costo coincide con el valor de la obligacion mas el del sobrante
    assert round(E["costo"] - E["v_oblig_curva"] - E["v_sobrante"], 2) == -125.65


def test_cete_comprado_a_364_y_vendido_a_182():
    assert round(E["cete_rodado"] * 100, 2) == 7.32
    assert round((E["cete_rodado"] - 0.069) * 1e4) == 42


def test_corporativo_contra_bono_m():
    assert round(E["sobretasa"] * 100, 2) == 0.79
    cr = {round(d * 1e4): round(r * 100, 2) for d, r in E["credito"].items()}
    assert cr == {-25: 11.47, 0: 9.94, 50: 6.98}
    assert round(E["sobretasa_eq"] * 100, 2) == 0.92
    assert round((E["sobretasa_eq"] - E["sobretasa"]) * 1e4) == 13


def test_carry_en_dolares():
    assert round(E["deprec_eq"] * 100, 2) == 2.75
    ca = {m: round(r * 100, 2) for m, r in E["carry"].items()}
    assert ca == {-0.03: 10.64, 0.0: 7.32, 0.05: 2.21}
    # con la depreciacion de equilibrio, el CETE rinde lo mismo que el Treasury
    s1 = 17.2252 * (1 + depreciacion_equilibrio(E["r_cete"], 0.0445))
    assert rendimiento_en_dolares(E["r_cete"], 17.2252, s1) == pytest.approx(0.0445)
    assert round(s1, 2) == 17.70


def test_escalera_lo_que_vence_cada_tramo():
    vence = {d: round(v, 2) for d, v in E["escalera_vence"].items()}
    assert vence == {28: 25121.53, 91: 25420.88, 182: 25872.08, 364: 26830.11}


def test_fondo_contra_directo():
    directo, medio, uno = (E["fondo"][k] for k in (0.0, 0.005, 0.01))
    assert round(directo[1], 2) == 107320.44
    assert round(medio[1], 2) == 106820.44
    assert round(directo[10] - medio[10], 2) == 9247.51
    assert round(directo[10] - uno[10], 2) == 18113.55


def test_bala_y_barra_mismo_plazo_promedio():
    cete, largo = E["barra_montos"]
    assert cete + largo == pytest.approx(1_000_000)
    assert (cete * 1 + largo * 20) / 1_000_000 == pytest.approx(10)
    assert round(largo, 2) == 473684.21


def test_bala_y_barra_escenarios_y_equilibrio():
    tabla = {d: (round(b1 * 100, 2), round(b2 * 100, 2)) for d, (b1, b2) in E["bala_barra"].items()}
    assert tabla == {-0.005: (9.35, 10.81), 0.0: (9.35, 8.62), 0.005: (9.35, 6.58)}
    assert round(E["barra_eq"] * 1e4) == -17


def test_escalera_precio_y_titulos_por_tramo():
    # CETE de $10 de valor nominal: precio y titulos que compran $25,000
    tabla = {d: (round(precio_cete(r, d, vn=10), 4), round(25_000 / precio_cete(r, d, vn=10), 2))
             for d, r in CETES.items()}
    assert tabla == {28: (9.9516, 2512.15), 91: (9.8344, 2542.09),
                     182: (9.6629, 2587.21), 364: (9.3179, 2683.01)}
