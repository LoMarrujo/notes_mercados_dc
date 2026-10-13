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

from valuacion import flujos_bono, precio_bono

VN = 100.0
# CETE a 364 dias: tasa simple 7.24% con base 360, se toma como el plazo de un anio
TASA_CETE_364 = 0.0724
FACTOR_CETE_364 = 1 + TASA_CETE_364 * 364 / 360
# Bonos M del 21 de septiembre de 2026: plazo -> (precio, YTM)
BONOS_M = {3: (100.94, 0.0824), 5: (98.90, 0.0900), 10: (96.40, 0.0916), 20: (86.34, 0.0964)}
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


def comprar_y_conservar(monto, precio, c, n, r_reinv, vn=VN):
    """Invierte `monto` en un bono de n anios con cupon anual c, comprado a
    `precio`, y lo conserva al vencimiento reinvirtiendo cada cupon a r_reinv
    hasta el anio n. Devuelve (titulos, flujos de los anios 1..n, valor
    acumulado en n, rendimiento anual del monto)."""
    titulos = monto / precio
    flujos = titulos * flujos_bono(c, n, vn)
    t = np.arange(1, n + 1)
    valor_final = float(np.sum(flujos * (1 + r_reinv) ** (n - t)))
    return titulos, flujos, valor_final, (valor_final / monto) ** (1 / n) - 1


def escalera_flujos(monto, tasas_por_plazo, base=360):
    """Lo que devuelve cada tramo de una escalera de CETES al vencer:
    {dias: monto por parte (1 + r dias / base)}."""
    parte = monto / len(tasas_por_plazo)
    return {d: parte * (1 + r * d / base) for d, r in sorted(tasas_por_plazo.items())}


def directo_vs_fondo(monto, r, comisiones, anios):
    """Valor de `monto` tras cada anio si rinde r directo, o r menos la
    comision anual en un fondo que replica el mismo indice.
    Devuelve {comision: [valor en t = 0, 1, ..., anios]} (comision 0 = directo)."""
    return {k: [monto * (1 + r - k) ** t for t in range(anios + 1)] for k in (0.0, *comisiones)}


def bala_y_barra(monto, r_cete, plazo_bala, plazo_largo, cambios_largo, curva=CURVA, vn=VN):
    """Bala: todo en el Bono M a `plazo_bala`. Barra: CETE a un anio y Bono M
    a `plazo_largo`, con pesos que dan el mismo plazo promedio que la bala.
    El rendimiento a un anio se calcula si el tramo largo cambia `d` sobre la
    curva y el resto de la curva no cambia (el tramo medio queda igual).
    Devuelve (monto en CETE, monto en el largo, {d: (bala, barra)}, d de equilibrio)."""
    p_b, r_b = BONOS_M[plazo_bala]
    p_l, r_l = BONOS_M[plazo_largo]
    c_b = cupon_anual_implicito(p_b, r_b, plazo_bala)
    c_l = cupon_anual_implicito(p_l, r_l, plazo_largo)
    w = (plazo_bala - 1) / (plazo_largo - 1)
    bala = rendimiento_horizonte(p_b, c_b, plazo_bala, ytm_curva(plazo_bala - 1, curva), vn)

    def barra(d):
        largo = rendimiento_horizonte(p_l, c_l, plazo_largo, ytm_curva(plazo_largo - 1, curva) + d, vn)
        return (1 - w) * r_cete + w * largo

    lo, hi = -0.05, 0.05  # la barra gana mas mientras mas baje el tramo largo
    for _ in range(200):
        mid = (lo + hi) / 2
        if barra(mid) > bala:
            lo = mid
        else:
            hi = mid
    return (1 - w) * monto, w * monto, {d: (bala, barra(d)) for d in cambios_largo}, (lo + hi) / 2


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
    escalera_vence = escalera_flujos(100_000.0, CETES)

    # indexacion: CETE a un anio directo contra un fondo con comision
    # (ilustrativo: se supone que el indice rinde lo mismo que el CETE)
    fondo = directo_vs_fondo(100_000.0, r_cete, (0.005, 0.01), 10)

    # bala (Bono M a 10 anios) contra barra (CETE y Bono M a 20 anios)
    barra_cete, barra_largo, bala_barra, barra_eq = bala_y_barra(
        1_000_000.0, r_cete, 10, 20, (-0.005, 0.0, 0.005))

    # comprar y conservar el Bono M a 3 anios, con los cupones reinvertidos
    # al YTM de la compra o a la tasa objetivo de Banxico
    conservar = {r: comprar_y_conservar(100_000.0, BONOS_M[3][0], c3, 3, r)
                 for r in (BONOS_M[3][1], TASA_OBJETIVO)}

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

    return {
        "c3": c3, "c10": c10, "precio_cete": precio_cete, "r_cete": r_cete,
        "titulos": titulos, "costo": costo, "tabla": tabla,
        "escenarios": escenarios, "r_eq": r_eq,
        "v_oblig_curva": float(v_oblig_curva), "v_sobrante": float(v_sobrante),
        "rodada": rodada, "bonde_f": bonde_f, "fondeo_eq": fondeo_eq,
        "infl_aprox": infl_aprox, "infl_exacta": infl_exacta, "real_bono_m": real_bono_m,
        "escalera": escalera, "escalera_vence": escalera_vence, "fondo": fondo,
        "barra_montos": (barra_cete, barra_largo), "bala_barra": bala_barra, "barra_eq": barra_eq,
        "conservar": conservar, "cete_rodado": cete_rodado,
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
    for r, (n, fl, vf, rend) in e["conservar"].items():
        print(f"comprar y conservar Bono M 3a, reinversion {r:.2%}: titulos {n:,.2f} "
              f"flujos {[round(float(x), 2) for x in fl]} valor final {vf:,.2f} rendimiento {rend:.4%}")
    print("escalera, recibe al vencer:", {d: round(v, 2) for d, v in e["escalera_vence"].items()})
    for k, v in e["fondo"].items():
        print(f"comision {k:.2%}: 1 anio {v[1]:,.2f}, 10 anios {v[10]:,.2f}")
    print(f"barra: CETE {e['barra_montos'][0]:,.2f} Bono M 20a {e['barra_montos'][1]:,.2f}")
    for d, (b1, b2) in e["bala_barra"].items():
        print(f"  tramo largo {d * 1e4:+.0f} pb: bala {b1:.4%} barra {b2:.4%}")
    print(f"  equilibrio: tramo largo {e['barra_eq'] * 1e4:+.1f} pb, YTM a 19a {ytm_curva(19) + e['barra_eq']:.4%}")
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
