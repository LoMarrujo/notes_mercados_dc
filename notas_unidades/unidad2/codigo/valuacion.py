"""Funciones de valuacion de 1_valuacion_instrumentos_deuda.md.

Cada funcion implementa una formula de la nota con los mismos simbolos:
a (capital), c (cupon o pago), r (tasa por periodo), N (periodos), v_N
(valor nominal), s_t (saldo insoluto), k_t (abono a capital). Las pruebas
de test_valuacion.py comprueban que las formulas cerradas coinciden con
la suma de flujos descontados uno por uno y reproducen el ejemplo oficial
de Banxico citado en la nota.
"""
import numpy as np
import pandas as pd

DIAS_CUPON = 182  # el Bono M paga cupon cada 182 dias
BASE = 360        # base del mercado de dinero mexicano


def precio_descuento(vn, r_nom, n, base=BASE):
    """Seccion 1: v_0 = v_N / (1 + r_nom n/base)."""
    return vn / (1 + r_nom * n / base)


def flujos_bono(c, n, vn):
    """Vector (c_1, ..., c_N) de un bono con cupon fijo: N-1 cupones y un
    ultimo pago de c + v_N. El flujo inicial -a no se incluye."""
    f = np.full(n, float(c))
    f[-1] += vn
    return f


def precio_flujos(flujos, r):
    """Valor presente de (c_1, ..., c_N) una a una: la definicion de la que
    sale la formula cerrada."""
    t = np.arange(1, len(flujos) + 1)
    return float(np.sum(np.asarray(flujos) * (1 + r) ** -t))


def precio_bono(c, n, r, vn=100.0):
    """Seccion 2, formula cerrada: anualidad de c mas flujo unico de v_N.
    Acepta r escalar o arreglo; la formula excluye r = 0."""
    r = np.asarray(r, dtype=float)
    if np.any(r == 0):
        raise ValueError("la formula cerrada excluye r = 0; usar n*c + vn")
    return c * (1 - (1 + r) ** -n) / r + vn * (1 + r) ** -n


def precio_bono_m(tasa_cupon, rend, cupones_por_cobrar, dias_devengados, vn=100.0):
    """Precio sucio y limpio de un Bono M con la descripcion tecnica de
    Banxico: cupon c = v_N tasa_cupon 182/360, factor por periodo
    R = 1 + rend 182/360, y descuento de los (182 - d)/182 de periodo que
    faltan para el proximo cupon. Devuelve (sucio, limpio)."""
    c = vn * tasa_cupon * DIAS_CUPON / BASE
    r_per = rend * DIAS_CUPON / BASE
    # valor en la proxima fecha de cupon: ese cupon, mas los siguientes
    # (anualidad) y el valor nominal a cupones_por_cobrar - 1 periodos
    v_prox = c + precio_bono(c, cupones_por_cobrar - 1, r_per, vn)
    sucio = v_prox * (1 + r_per) ** (-(DIAS_CUPON - dias_devengados) / DIAS_CUPON)
    devengado = vn * tasa_cupon * dias_devengados / BASE
    return float(sucio), float(sucio - devengado)


def cupon_implicito(precio, rend, n, vn=100.0):
    """Cupon anual (con la convencion 182/360) que hace que un bono de n
    periodos de 182 dias, liquidado en fecha de cupon, valga `precio` al
    rendimiento `rend`. El precio es lineal en c, asi que se despeja sin
    resolver ninguna ecuacion:
        precio = c a(n, r_per) + v_N (1+r_per)^-n."""
    r_per = rend * DIAS_CUPON / BASE
    anualidad = (1 - (1 + r_per) ** -n) / r_per
    c = (precio - vn * (1 + r_per) ** -n) / anualidad
    return float(c / vn * BASE / DIAS_CUPON)


def tabla_amortizacion(sistema, a, r, n, retiros=None):
    """Tabla de amortizacion de un capital `a` a `n` periodos con tasa `r`.

    sistema: "frances" (pago total constante), "aleman" (abono a capital
    constante) o "sinking" (abonos k_t segun el calendario `retiros`, una
    lista de n montos que suma a). Cada fila cumple pago = interes + abono
    y saldo_final = saldo_inicial - abono."""
    if sistema == "frances":
        c = a * r / (1 - (1 + r) ** -n)
        abonos = None
    elif sistema == "aleman":
        abonos = [a / n] * n
    elif sistema == "sinking":
        if retiros is None or len(retiros) != n or not np.isclose(sum(retiros), a):
            raise ValueError("retiros debe tener n montos que sumen a")
        abonos = list(retiros)
    else:
        raise ValueError(f"sistema desconocido: {sistema}")

    filas, saldo = [], a
    for t in range(1, n + 1):
        interes = r * saldo
        k = (c - interes) if abonos is None else abonos[t - 1]
        filas.append({"periodo": t, "saldo_inicial": saldo, "interes": interes,
                      "abono_capital": k, "pago": interes + k,
                      "saldo_final": saldo - k})
        saldo -= k
    return pd.DataFrame(filas)


def precio_amortizable(tabla, r):
    """Seccion 4: v_0 = suma de (k_t + r s_{t-1})(1+r)^-t, es decir, cada
    pago de la tabla descontado a su propio periodo."""
    return float((tabla["pago"] * (1 + r) ** -tabla["periodo"]).sum())
