"""Funciones de 4_estrategias_renta_fija.md.

Misma convencion simplificada de 2_rendimiento_y_curva_de_rendimientos.md:
un cupon anual c por cada 100 de valor nominal, descontado con la formula
cerrada de precio_bono. Los datos son los de cetesdirecto del 21 de
septiembre de 2026 (datos/cetesdirecto_2026-09-21.csv y la tabla de CETES
de esa fecha para el plazo de 364 dias). Las pruebas de
test_estrategias.py reproducen cada numero que cita la nota.

Uso (desde la raiz del repo):
    python notas_unidades/unidad2/codigo/estrategias.py
"""
import numpy as np

from valuacion import flujos_bono, precio_bono, precio_flujos

VN = 100.0
# CETE a 364 dias: tasa simple 7.24% con base 360, se toma como el plazo de un anio
TASA_CETE_364 = 0.0724
FACTOR_CETE_364 = 1 + TASA_CETE_364 * 364 / 360
# Bonos M del 21 de septiembre de 2026: plazo -> (precio, YTM)
BONOS_M = {3: (100.94, 0.0824), 10: (96.40, 0.0916)}


def cupon_anual_implicito(precio, r, n, vn=VN):
    """Cupon anual que hace que un bono de n anios valga `precio` al YTM r:
    se despeja c de a = c[1-(1+r)^-n]/r + v_N(1+r)^-n, como en 2_ seccion 1."""
    anualidad = (1 - (1 + r) ** -n) / r
    return float((precio - vn * (1 + r) ** -n) / anualidad)


def calce_flujos(obligaciones, bonos, vn=VN):
    """Calce de flujos hacia atras.

    obligaciones: {anio: monto a pagar}.
    bonos: {anio de vencimiento: (precio, cupon anual)}; un cupon cero
    tiene cupon 0. Debe haber un bono por cada anio con obligacion.

    Empieza por el ultimo pago: compra los titulos del bono de ese plazo
    que lo cubren exactamente con su ultimo flujo (c + v_N); los cupones de
    esos titulos reducen lo que falta en las fechas anteriores, y se repite.
    Devuelve (titulos por plazo, costo total, tabla), con tabla una lista de
    (anio, obligacion, flujo del portafolio, sobrante)."""
    horizonte = max(obligaciones)
    flujo = np.zeros(horizonte + 1)
    titulos = {}
    for t in sorted(obligaciones, reverse=True):
        falta = obligaciones[t] - flujo[t]
        precio, c = bonos[t]
        n = max(falta, 0.0) / (c + vn)
        titulos[t] = n
        flujo[1:t + 1] += n * flujos_bono(c, t, vn)
    costo = sum(n * bonos[t][0] for t, n in titulos.items())
    tabla = [(t, obligaciones.get(t, 0.0), flujo[t], flujo[t] - obligaciones.get(t, 0.0))
             for t in range(1, horizonte + 1)]
    return titulos, float(costo), tabla


def rendimiento_horizonte(precio, c, n, r1, vn=VN):
    """Rendimiento a un anio de comprar hoy en `precio` un bono de n anios,
    cobrar un cupon y venderlo como bono de n-1 anios al YTM r1."""
    return float((c + precio_bono(c, n - 1, r1, vn) - precio) / precio)


def tasa_equilibrio(precio, c, n, r_alternativa, vn=VN, lo=0.0001, hi=0.5):
    """YTM al cierre del anio con el que el bono rinde lo mismo que la
    alternativa segura: rendimiento_horizonte(...) = r_alternativa. Se
    resuelve por biseccion, porque el rendimiento baja al subir r1."""
    for _ in range(200):
        mid = (lo + hi) / 2
        if rendimiento_horizonte(precio, c, n, mid, vn) > r_alternativa:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def duracion_macaulay(flujos, r):
    """D = sum t c_t (1+r)^-t / v_0, flujos (c_1, ..., c_N); 4_ seccion 2."""
    flujos = np.asarray(flujos, dtype=float)
    t = np.arange(1, len(flujos) + 1)
    return float(np.sum(t * flujos * (1 + r) ** -t) / precio_flujos(flujos, r))


def inmunizar(obligacion, d_a, flujos_b, r):
    """Pesos que igualan valor presente y duracion del portafolio con los de
    la obligacion, con un cupon cero de duracion d_a y un bono B con flujos
    flujos_b, todo a la tasa plana r. Devuelve (v_0 obligacion,
    D obligacion, monto en A, monto en B)."""
    v0 = precio_flujos(obligacion, r)
    d_obl = duracion_macaulay(obligacion, r)
    d_b = duracion_macaulay(flujos_b, r)
    w_b = (d_obl - d_a) / (d_b - d_a)
    return v0, d_obl, (1 - w_b) * v0, w_b * v0


def valor_portafolio(monto_a, d_a, r0, monto_b, flujos_b, r1):
    """Valor a la tasa r1 de un portafolio armado a la tasa r0."""
    va = monto_a * (1 + r0) ** d_a * (1 + r1) ** -d_a
    vb = monto_b * precio_flujos(flujos_b, r1) / precio_flujos(flujos_b, r0)
    return float(va + vb)


def ejemplos():
    """Numeros que cita 4_estrategias_renta_fija.md."""
    c3 = cupon_anual_implicito(*BONOS_M[3], 3)
    c10 = cupon_anual_implicito(*BONOS_M[10], 10)
    precio_cete = VN / FACTOR_CETE_364
    oblig = {1: 100_000.0, 3: 100_000.0}
    titulos, costo, tabla = calce_flujos(oblig, {1: (precio_cete, 0.0), 3: (BONOS_M[3][0], c3)})

    r_cete = FACTOR_CETE_364 - 1
    escenarios = {d: rendimiento_horizonte(BONOS_M[10][0], c10, 10, BONOS_M[10][1] + d)
                  for d in (-0.01, 0.0, 0.01)}
    r_eq = tasa_equilibrio(BONOS_M[10][0], c10, 10, r_cete)

    r_plana = 0.09
    flujos_obl = [100_000.0, 0.0, 100_000.0]
    flujos_b = flujos_bono(c10, 10, VN)
    v0, d_obl, m_a, m_b = inmunizar(flujos_obl, 1.0, flujos_b, r_plana)
    choque = {d: (valor_portafolio(m_a, 1.0, r_plana, m_b, flujos_b, r_plana + d),
                  precio_flujos(flujos_obl, r_plana + d)) for d in (-0.01, 0.01)}
    return {
        "c3": c3, "c10": c10, "precio_cete": precio_cete, "r_cete": r_cete,
        "titulos": titulos, "costo": costo, "tabla": tabla,
        "escenarios": escenarios, "r_eq": r_eq,
        "d_b": duracion_macaulay(flujos_b, r_plana),
        "inm": (v0, d_obl, m_a, m_b), "choque": choque,
    }


if __name__ == "__main__":
    e = ejemplos()
    print(f"cupon implicito 3a {e['c3']:.4f}, 10a {e['c10']:.4f}")
    print(f"CETE 364: precio {e['precio_cete']:.4f}, rendimiento anual {e['r_cete']:.4%}")
    print("calce:", {t: round(n, 2) for t, n in e["titulos"].items()}, f"costo {e['costo']:,.2f}")
    for fila in e["tabla"]:
        print("  anio %d oblig %10.2f flujo %10.2f sobrante %9.2f" % fila)
    for d, r in e["escenarios"].items():
        print(f"Bono M 10a, {d * 1e4:+.0f} pb: {r:.4%}")
    print(f"tasa de equilibrio {e['r_eq']:.4%} ({(e['r_eq'] - 0.0916) * 1e4:+.1f} pb)")
    v0, d_obl, m_a, m_b = e["inm"]
    print(f"inmunizacion: v0 {v0:,.2f} D {d_obl:.4f} D_B {e['d_b']:.4f} CETE {m_a:,.2f} BonoM {m_b:,.2f}")
    for d, (vp, vo) in e["choque"].items():
        print(f"  {d * 1e4:+.0f} pb: portafolio {vp:,.2f} obligacion {vo:,.2f} diferencia {vp - vo:,.2f}")
