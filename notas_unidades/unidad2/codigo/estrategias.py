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
# CETES del 21 de septiembre de 2026: plazo en dias -> tasa (cetesdirecto)
CETES = {28: 0.0625, 91: 0.0666, 182: 0.0690, 364: 0.0724}
# Curva de rendimientos de esa fecha, plazo en anios -> YTM. El CETE a 364
# dias se toma como el punto de un anio, como en el resto de la nota.
CURVA = {1: 0.0724, 3: 0.0824, 5: 0.0900, 10: 0.0916, 20: 0.0964, 30: 0.0987}
# UDIBONOS de esa fecha: plazo en anios -> tasa real
UDIBONOS = {3: 0.0399, 10: 0.0475, 30: 0.0490}
# Tasa objetivo de Banxico, vigente del 6 de agosto de 2026 (se mantuvo el
# 24 de septiembre); la TIIE de Fondeo la sigue de cerca
TASA_OBJETIVO = 0.0650
# Bono corporativo a 10 anios de la seccion 4 de 2_ (ilustrativo):
# cupon 8, precio 88, YTM 9.95%, sobretasa 0.79 pp sobre el Bono M
CORPORATIVO = (88.0, 8.0, 0.0995)
# FRED del 21 de septiembre de 2026 (datos/fred_carry_2026-09-21.csv):
# Treasury a 1 anio (DGS1) y pesos por dolar (DEXMXUS)
TREASURY_1A = 0.0445
TIPO_CAMBIO = 17.2252


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


def ytm_curva(plazo, curva=CURVA):
    """YTM de la curva a `plazo` anios, interpolando en linea recta entre
    los dos puntos cotizados mas cercanos."""
    plazos = sorted(curva)
    return float(np.interp(plazo, plazos, [curva[p] for p in plazos]))


def rendimiento_curva_sin_cambio(precio, c, n, curva=CURVA, vn=VN):
    """Rendimiento a un anio si la curva completa no cambia: el bono se vende
    como bono de n-1 anios al YTM que la curva tiene en ese plazo."""
    return rendimiento_horizonte(precio, c, n, ytm_curva(n - 1, curva), vn)


def rendimiento_bonde_f(r, dias=364, base=360):
    """Rendimiento en `dias` de un Bonde F comprado a la par en fecha de
    cupon, con sobretasa 0: la TIIE de Fondeo `r` se capitaliza cada dia."""
    return float((1 + r / base) ** dias - 1)


def tasa_fondeo_equilibrio(r_alternativa, dias=364, base=360):
    """TIIE de Fondeo promedio con la que el Bonde F rinde lo mismo que una
    alternativa a tasa fija que gana r_alternativa en esos dias."""
    return float(((1 + r_alternativa) ** (1 / dias) - 1) * base)


def inflacion_implicita(r_nom, r_real):
    """Inflacion implicita aproximada, r_nom - r_real (apendice de 2_)."""
    return r_nom - r_real


def inflacion_implicita_exacta(r_nom, r_real):
    """Inflacion que iguala el rendimiento real de los dos bonos:
    (1+r_nom)/(1+r_inf) - 1 = r_real (ecuacion de Fisher)."""
    return (1 + r_nom) / (1 + r_real) - 1


def rendimiento_real(r_nom, r_inf):
    """Tasa real que gana un bono nominal al YTM r_nom si la inflacion
    promedio resulta r_inf (ecuacion de Fisher)."""
    return (1 + r_nom) / (1 + r_inf) - 1


def escalera_cetes(monto, tasas_por_plazo):
    """Reparte `monto` en partes iguales entre los plazos de CETES. Devuelve
    (monto por parte, tasa promedio de hoy)."""
    parte = monto / len(tasas_por_plazo)
    return parte, float(np.mean(list(tasas_por_plazo.values())))


def precio_cete(r, dias, vn=VN, base=360):
    """Precio de un CETE a `dias` con tasa de rendimiento simple r."""
    return vn / (1 + r * dias / base)


def rendimiento_cete_rodado(tasa_compra, dias_compra, tasa_venta, dias_venta, base=360):
    """Rendimiento anualizado (simple, base 360) de comprar un CETE a
    `dias_compra` y venderlo cuando le quedan `dias_venta`, a la tasa
    `tasa_venta` que tenga entonces ese plazo."""
    p0 = precio_cete(tasa_compra, dias_compra)
    p1 = precio_cete(tasa_venta, dias_venta)
    dias = dias_compra - dias_venta
    return float((p1 / p0 - 1) * base / dias)


def sobretasa_equilibrio(precio, c, n, r_gob1, r_alternativa, vn=VN):
    """Sobretasa al cierre del anio (sobre el YTM gubernamental r_gob1 del
    plazo n-1) con la que el bono corporativo rinde r_alternativa."""
    return tasa_equilibrio(precio, c, n, r_alternativa, vn) - r_gob1


def rendimiento_en_dolares(r_mxn, s0, s1):
    """Rendimiento en dolares de invertir en pesos a r_mxn: se compran
    pesos a s0 y se regresan a s1 (pesos por dolar)."""
    return (1 + r_mxn) * s0 / s1 - 1


def depreciacion_equilibrio(r_mxn, r_usd):
    """Depreciacion del peso, s1/s0 - 1, con la que invertir en pesos rinde
    en dolares lo mismo que r_usd."""
    return (1 + r_mxn) / (1 + r_usd) - 1


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

    # calce valuado con la curva: obligacion y sobrante del anio 2
    v_oblig_curva = (100_000.0 / FACTOR_CETE_364
                     + 100_000.0 * (1 + BONOS_M[3][1]) ** -3)
    v_sobrante = tabla[1][3] * (1 + ytm_curva(2)) ** -2

    # recorrer la curva: el bono baja de plazo y de YTM si la curva no cambia
    rodada = {3: rendimiento_curva_sin_cambio(BONOS_M[3][0], c3, 3),
              10: rendimiento_curva_sin_cambio(BONOS_M[10][0], c10, 10)}

    # Bonde F a la par contra el CETE a 364 dias, si la TIIE de Fondeo
    # promedio del anio queda en 6.50% o sube 50 o 100 pb
    bonde_f = {d: rendimiento_bonde_f(TASA_OBJETIVO + d) for d in (0.0, 0.005, 0.01)}
    fondeo_eq = tasa_fondeo_equilibrio(r_cete)

    # UDIBONO contra Bono M a 10 anios conservados al vencimiento
    infl_aprox = inflacion_implicita(BONOS_M[10][1], UDIBONOS[10])
    infl_exacta = inflacion_implicita_exacta(BONOS_M[10][1], UDIBONOS[10])
    real_bono_m = {r_inf: rendimiento_real(BONOS_M[10][1], r_inf) for r_inf in (0.03, 0.06)}

    escalera = escalera_cetes(100_000.0, CETES)

    # recorrer la curva con CETES: comprar a 364 y vender a los 182 dias
    cete_rodado = rendimiento_cete_rodado(CETES[364], 364, CETES[182], 182)

    # corporativo contra Bono M a 10 anios (YTM sin cambio), un anio
    p_corp, c_corp, ytm_corp = CORPORATIVO
    sobretasa = ytm_corp - BONOS_M[10][1]
    r_gob9 = BONOS_M[10][1]
    credito = {d: rendimiento_horizonte(p_corp, c_corp, 10, r_gob9 + sobretasa + d)
               for d in (-0.0025, 0.0, 0.005)}
    sobretasa_eq = sobretasa_equilibrio(p_corp, c_corp, 10, r_gob9, escenarios[0.0])

    # carry: CETE a 364 dias contra Treasury a 1 anio, en dolares
    deprec_eq = depreciacion_equilibrio(r_cete, TREASURY_1A)
    carry = {m: rendimiento_en_dolares(r_cete, TIPO_CAMBIO, TIPO_CAMBIO * (1 + m))
             for m in (-0.03, 0.0, 0.05)}

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
        "v_oblig_curva": float(v_oblig_curva), "v_sobrante": float(v_sobrante),
        "rodada": rodada, "bonde_f": bonde_f, "fondeo_eq": fondeo_eq,
        "infl_aprox": infl_aprox, "infl_exacta": infl_exacta, "real_bono_m": real_bono_m,
        "escalera": escalera, "cete_rodado": cete_rodado,
        "sobretasa": sobretasa, "credito": credito, "sobretasa_eq": sobretasa_eq,
        "deprec_eq": deprec_eq, "carry": carry,
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
    print(f"calce a la curva: obligacion {e['v_oblig_curva']:,.2f} sobrante {e['v_sobrante']:,.2f}")
    print(f"YTM interpolado a 2a {ytm_curva(2):.4%}, a 9a {ytm_curva(9):.4%}")
    for n, r in e["rodada"].items():
        print(f"curva sin cambio, Bono M {n}a: {r:.4%}")
    for d, r in e["bonde_f"].items():
        print(f"Bonde F, fondeo {(TASA_OBJETIVO + d):.2%}: {r:.4%}")
    print(f"fondeo de equilibrio contra el CETE 364: {e['fondeo_eq']:.4%}")
    print(f"inflacion implicita 10a: aprox {e['infl_aprox']:.4%}, exacta {e['infl_exacta']:.4%}")
    for r_inf, r in e["real_bono_m"].items():
        print(f"  Bono M real con inflacion {r_inf:.0%}: {r:.4%} (UDIBONO {UDIBONOS[10]:.2%})")
    print(f"escalera: {e['escalera'][0]:,.2f} por parte, tasa promedio {e['escalera'][1]:.4%}")
    print(f"CETE 364 vendido a los 182 dias: {e['cete_rodado']:.4%} (CETE 182: {CETES[182]:.2%})")
    print(f"calce: costo - (obligacion + sobrante) = "
          f"{e['costo'] - e['v_oblig_curva'] - e['v_sobrante']:,.2f}")
    print(f"corporativo: sobretasa {e['sobretasa']:.4%}")
    for d, r in e["credito"].items():
        print(f"  sobretasa {d * 1e4:+.0f} pb: {r:.4%}")
    print(f"  sobretasa de equilibrio {e['sobretasa_eq']:.4%} "
          f"({(e['sobretasa_eq'] - e['sobretasa']) * 1e4:+.1f} pb)")
    print(f"carry: depreciacion de equilibrio {e['deprec_eq']:.4%}, "
          f"tipo de cambio {TIPO_CAMBIO * (1 + e['deprec_eq']):.4f}")
    for m, r in e["carry"].items():
        print(f"  peso {m:+.0%} (s1 {TIPO_CAMBIO * (1 + m):.4f}): {r:.4%} en dolares")
    v0, d_obl, m_a, m_b = e["inm"]
    print(f"inmunizacion: v0 {v0:,.2f} D {d_obl:.4f} D_B {e['d_b']:.4f} CETE {m_a:,.2f} BonoM {m_b:,.2f}")
    for d, (vp, vo) in e["choque"].items():
        print(f"  {d * 1e4:+.0f} pb: portafolio {vp:,.2f} obligacion {vo:,.2f} diferencia {vp - vo:,.2f}")
