"""Tablas numericas del apendice de 1_valuacion_instrumentos_deuda.md:
conciliacion con el precio publicado, costo de las simplificaciones y
comparacion de sistemas de amortizacion. Cada cifra que el apendice cita
sale de aqui.

Uso (desde la raiz del repo):
    python notas_unidades/unidad2/codigo/analisis_valuacion.py
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulacion import simular_precios  # noqa: E402
from valuacion import (  # noqa: E402
    BASE, DIAS_CUPON, cupon_implicito, precio_bono, precio_descuento,
    tabla_amortizacion,
)

RUTA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "..", "datos", "cetesdirecto_2026-09-21.csv")
DT = DIAS_CUPON / BASE


def cargar_datos():
    return pd.read_csv(RUTA_DATOS)


def _plazo_anios(txt):
    return int(txt.split()[0])


def conciliacion():
    """Precio calculado contra precio publicado, y cupon que haria falta
    para que la formula reproduzca el publicado.

    CETES: la formula de la seccion 1 con n = 28 o 91 dias.
    BONOS y UDIBONOS: se supone plazo remanente igual al plazo nominal
    (2N periodos de 182 dias) y liquidacion en fecha de cupon, de modo
    que precio limpio = sucio; el cupon implicito absorbe todo lo demas
    (cupon real de la serie, plazo remanente exacto, dias devengados)."""
    d = cargar_datos()
    udi = float(d.loc[d.instrumento == "UDI", "precio"].iloc[0])
    filas = []
    for _, f in d[d.instrumento != "UDI"].iterrows():
        r = f.tasa_pct / 100
        if f.instrumento == "CETES":
            dias = {"1 mes": 28, "3 meses": 91}[f.plazo]
            calc = precio_descuento(10, r, dias)
            filas.append({"instrumento": f"CETES {f.plazo}", "tasa_pct": f.tasa_pct,
                          "calculado": calc, "publicado": f.precio, "diferencia": calc - f.precio,
                          "cupon_implicito_pct": np.nan})
            continue
        n = 2 * _plazo_anios(f.plazo)
        precio = f.precio / udi if f.instrumento == "UDIBONOS" else f.precio
        cup = cupon_implicito(precio, r, n)
        filas.append({"instrumento": f"{f.instrumento} {f.plazo}",
                      "tasa_pct": f.tasa_pct,
                      "calculado": np.nan, "publicado": precio, "diferencia": np.nan,
                      "cupon_implicito_pct": cup * 100})
    return pd.DataFrame(filas)


def descomposicion_bono_m_10a():
    """De 93.58 (ejemplo de la seccion 2) a 96.40 (publicado), un cambio a
    la vez y en este orden: (1) tasa 9% a 9.16%, (2) pagos cada 182 dias en
    vez de uno al anio, (3) el cupon que cierra la brecha. El orden importa
    para cuanto se atribuye a cada paso; el total no."""
    publicado = 96.40
    p0 = precio_bono(8, 10, 0.09)
    p1 = precio_bono(8, 10, 0.0916)
    c_per, r_per = 100 * 0.08 * DT, 0.0916 * DT
    p2 = precio_bono(c_per, 20, r_per)
    cup = cupon_implicito(publicado, 0.0916, 20)
    return pd.DataFrame([
        {"paso": "Ejemplo de la nota: cupon 8% anual, tasa 9%, pago anual", "precio": p0},
        {"paso": "Tasa publicada 9.16% (aun pago anual)", "precio": p1},
        {"paso": "Pagos cada 182 dias con base 360 (cupon 8%)", "precio": p2},
        {"paso": f"Cupon implicito de {cup * 100:.2f}% que reproduce el publicado", "precio": publicado},
    ])


def simplificaciones():
    """Diferencia de precio entre la simplificacion y la convencion real."""
    filas = []
    for dias, r in ((28, 0.0625), (91, 0.0666)):
        p360, p365 = precio_descuento(10, r, dias, 360), precio_descuento(10, r, dias, 365)
        filas.append({"caso": f"CETE {dias} dias al {r * 100:.2f}%: base 360 contra 365",
                      "simplificado": p365, "convencion": p360, "diferencia": p365 - p360})
    p_anual = precio_bono(8, 10, 0.09)
    p_182 = precio_bono(100 * 0.08 * DT, 20, 0.09 * DT)
    filas.append({"caso": "Bono M 10 anios, cupon 8%, tasa 9%: pago anual contra 182 dias",
                  "simplificado": p_anual, "convencion": p_182, "diferencia": p_anual - p_182})
    return pd.DataFrame(filas)


def comparacion_amortizacion(a=500_000, r=0.10, n=20):
    retiros = [0.10 * a] * 5 + [0] * 14 + [0.50 * a]
    filas = []
    for nombre, sistema, ret in (("Frances", "frances", None), ("Aleman", "aleman", None),
                                 ("Sinking fund", "sinking", retiros)):
        t = tabla_amortizacion(sistema, a, r, n, ret)
        filas.append({"sistema": nombre, "primer_pago": t.pago.iloc[0], "ultimo_pago": t.pago.iloc[-1],
                      "interes_total": t.interes.sum(), "pago_total": t.pago.sum()})
    return pd.DataFrame(filas)


def resumen_simulacion():
    fijo, variable = simular_precios()
    filas = []
    for k, etiqueta in ((2, "1 anio"), (6, "3 anios"), (10, "5 anios")):
        filas.append({"horizonte": etiqueta,
                      "fijo_media": fijo[:, k].mean(), "fijo_desv": fijo[:, k].std(),
                      "fijo_p5": np.percentile(fijo[:, k], 5), "fijo_p95": np.percentile(fijo[:, k], 95),
                      "var_media": variable[:, k].mean(), "var_desv": variable[:, k].std(),
                      "var_p5": np.percentile(variable[:, k], 5), "var_p95": np.percentile(variable[:, k], 95)})
    return pd.DataFrame(filas)


if __name__ == "__main__":
    pd.set_option("display.width", 200)
    pd.set_option("display.float_format", lambda v: f"{v:,.4f}")
    for titulo, df in (("Conciliacion", conciliacion()),
                       ("Descomposicion Bono M 10a", descomposicion_bono_m_10a()),
                       ("Simplificaciones", simplificaciones()),
                       ("Amortizacion", comparacion_amortizacion()),
                       ("Simulacion", resumen_simulacion())):
        print(f"\n== {titulo} ==")
        print(df.to_string(index=False))
