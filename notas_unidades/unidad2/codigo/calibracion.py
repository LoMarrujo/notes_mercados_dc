"""Calibracion del modelo de tasas de Vasicek por minimos cuadrados, y su
extension con variables explicativas. Sostiene el laboratorio
practicas/unidad2/laboratorio_calibracion.md.

La idea que une todo: la discretizacion exacta de Vasicek es un AR(1), asi
que calibrar el modelo es correr una regresion.

    dr = kappa (r_lp - r) dt + sigma dW
    r_{t+1} = a + b r_t + e,  con b = e^{-kappa dt},  a = r_lp (1-b)

De ahi, meter variables explicativas es extender esa misma regresion: el
nivel de largo plazo deja de ser una constante y pasa a depender de la
inflacion, de la tasa de EE.UU. o del tipo de cambio.

Unidades: todas las funciones de estimacion trabajan con las series como
vienen de FRED, en por ciento (6.79 es 6.79%), asi que r_lp sale en por
ciento y sigma en puntos porcentuales. La simulacion trabaja en decimales,
y la conversion se hace al pasar de un modulo al otro.

Estilo de estimacion tomado de data/enoe/mincer_enoe.py (especificacion
principal mas robustez, errores estandar robustos, coeficiente de interes
impreso con su intervalo), con una diferencia: aqui los errores van HAC
(Newey-West) en vez de HC1, porque esto es serie de tiempo.

Uso (desde la raiz del repo):
    python notas_unidades/unidad2/codigo/calibracion.py
"""
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datos_fred import cargar  # noqa: E402

DT = 1 / 12  # paso mensual, en anios
HAC_LAGS = 6

# Cuanto carga cada regresor sobre la tasa corta. La pendiente se construye
# como r_larga - r_corta, asi que lleva la tasa corta dentro con signo
# negativo: ignorarlo hace que el coeficiente de r_corta se lea como si el
# proceso fuera explosivo. Ver kappa_efectiva().
CARGA_R_CORTA = {"r_corta": 1.0, "pendiente": -1.0}


def ar1_a_vasicek(a, b, sigma_resid, dt=DT):
    """Traduce los coeficientes de un AR(1) a los parametros de Vasicek.

    b = e^{-kappa dt}          -> kappa = -ln(b)/dt
    a = r_lp (1-b)             -> r_lp  = a/(1-b)
    var(e) = sigma^2 (1-b^2)/(2 kappa) -> sigma = sd(e) sqrt(2 kappa/(1-b^2))

    Requiere 0 < b < 1: con b >= 1 el proceso no revierte y kappa no existe."""
    if not 0 < b < 1:
        raise ValueError(f"b={b:.4f} fuera de (0,1): el proceso no revierte a la media")
    kappa = -np.log(b) / dt
    r_lp = a / (1 - b)
    sigma = sigma_resid * np.sqrt(2 * kappa / (1 - b ** 2))
    return {"kappa": kappa, "r_lp": r_lp, "sigma": sigma,
            "vida_media": np.log(2) / kappa}


def calibrar_vasicek(serie, dt=DT):
    """Estima el AR(1) de `serie` por MCO y devuelve los parametros de
    Vasicek junto con el resultado de statsmodels."""
    s = pd.Series(serie).dropna()
    y = s.iloc[1:].values
    x = sm.add_constant(s.iloc[:-1].values)
    res = sm.OLS(y, x).fit(cov_type="HAC", cov_kwds={"maxlags": HAC_LAGS})
    a, b = res.params
    par = ar1_a_vasicek(a, b, np.std(res.resid, ddof=2), dt)
    par.update({"a": a, "b": b, "n": int(res.nobs), "r2": res.rsquared, "res": res})
    return par


def prueba_raiz_unitaria(serie):
    """ADF con constante. Un valor p alto significa que no se puede
    rechazar la raiz unitaria, es decir, que los datos no distinguen la
    reversion a la media de una caminata aleatoria."""
    s = pd.Series(serie).dropna().values
    est, pvalor, _, nobs, criticos, _ = adfuller(s, regression="c")
    return {"estadistico": est, "p": pvalor, "n": nobs, "criticos": criticos}


def kappa_efectiva(params):
    """Velocidad de reversion implicita en una regresion con explicativas.

    Suma el coeficiente de cada regresor por lo que ese regresor carga
    sobre la tasa corta. Leer solo el coeficiente de r_corta cuando la
    pendiente esta en la especificacion da un valor mayor que 1, es decir,
    un proceso explosivo que es un artefacto de como se construyo la
    pendiente, no un hallazgo sobre las tasas."""
    b = sum(params.get(k, 0.0) * carga for k, carga in CARGA_R_CORTA.items())
    if not 0 < b < 1:
        return {"b_efectiva": b, "kappa": np.nan, "vida_media": np.nan}
    kappa = -np.log(b) / DT
    return {"b_efectiva": b, "kappa": kappa, "vida_media": np.log(2) / kappa}


def ardl(datos, cols, h=1, etiqueta="", verbose=True):
    """Regresa la tasa corta h meses adelante contra `cols`, con errores HAC.

    Con cols=["r_corta"] es el Vasicek puro; agregar columnas es abrirlo a
    variables explicativas."""
    d = datos.copy()
    d["y"] = d["r_corta"].shift(-h)
    m = d.dropna(subset=["y"] + cols)
    res = sm.OLS(m["y"], sm.add_constant(m[cols])).fit(
        cov_type="HAC", cov_kwds={"maxlags": HAC_LAGS})
    ef = kappa_efectiva(res.params)
    if verbose:
        print(f"\n=== {etiqueta} (n={int(res.nobs)}, R2={res.rsquared:.4f}) ===")
        for k in res.params.index:
            ic = res.conf_int().loc[k]
            print(f"   {k:14s} {res.params[k]:+9.4f}  (t={res.tvalues[k]:+6.2f}, "
                  f"IC95% [{ic[0]:+.4f}, {ic[1]:+.4f}])")
        if np.isfinite(ef["kappa"]):
            print(f"   -> b efectiva {ef['b_efectiva']:.4f}, kappa {ef['kappa']:.3f}, "
                  f"vida media {ef['vida_media']:.2f} anios")
    return res, ef


def r2_en_cambios(datos, specs):
    """R2 de la misma regresion escrita en cambios en vez de en niveles.

    Una serie muy persistente da un R2 altisimo en niveles aunque el modelo
    no aporte casi nada: el regresor ya es practicamente la variable
    dependiente. En cambios se ve cuanto explica de verdad.

    Las tres especificaciones se estiman sobre la misma muestra, la que
    sobrevive a pedir todas las columnas de todas ellas. Comparar R2 entre
    regresiones estimadas sobre muestras distintas no dice nada."""
    d = datos.copy()
    d["dr"] = d["r_corta"].shift(-1) - d["r_corta"]
    usadas = sorted({c for cols, _ in specs for c in cols})
    comun = d.dropna(subset=["dr"] + usadas)
    filas = []
    for cols, etiqueta in specs:
        niv = sm.OLS(comun["r_corta"].shift(-1).dropna(),
                     sm.add_constant(comun[cols].iloc[:-1])).fit()
        cam = sm.OLS(comun["dr"], sm.add_constant(comun[cols])).fit()
        filas.append({"especificacion": etiqueta, "n": int(cam.nobs),
                      "r2_niveles": niv.rsquared, "r2_cambios": cam.rsquared})
    return pd.DataFrame(filas)


def evaluar_oos(datos, cols_ardl=("r_corta", "pendiente", "depreciacion"),
                horizontes=(1, 6, 12, 24), minimo=120):
    """Comparacion fuera de muestra con ventana expansiva.

    En cada mes se reestima con la informacion disponible hasta ese momento
    y se pronostica h meses adelante. La caminata aleatoria pronostica la
    tasa de hoy, y es el punto de comparacion: la U de Theil es el cociente
    de su RMSE, asi que un valor menor que 1 significa ganarle."""
    d = datos.dropna(subset=["r_corta", "pendiente", "depreciacion"]).copy()
    cols_ardl = list(cols_ardl)
    filas = []
    for h in horizontes:
        e_rw, e_ar, e_ardl = [], [], []
        for i in range(minimo, len(d) - h):
            tr, real, hoy = d.iloc[:i], d["r_corta"].iloc[i + h], d["r_corta"].iloc[i]
            obj = tr["r_corta"].shift(-h).dropna()
            e_rw.append(real - hoy)
            m_ar = sm.OLS(obj, sm.add_constant(tr[["r_corta"]].iloc[:-h])).fit()
            e_ar.append(real - m_ar.predict([[1, hoy]])[0])
            m_ardl = sm.OLS(obj, sm.add_constant(tr[cols_ardl].iloc[:-h])).fit()
            e_ardl.append(real - m_ardl.predict(
                [[1] + [d[c].iloc[i] for c in cols_ardl]])[0])
        rmse = lambda e: float(np.sqrt(np.mean(np.square(e))))
        filas.append({"h_meses": h, "n": len(e_rw),
                      "rmse_caminata": rmse(e_rw), "rmse_ar1": rmse(e_ar),
                      "rmse_ardl": rmse(e_ardl),
                      "theil_ar1": rmse(e_ar) / rmse(e_rw),
                      "theil_ardl": rmse(e_ardl) / rmse(e_rw)})
    return pd.DataFrame(filas)


def vasicek_afin(tau, kappa, r_lp, sigma, r0):
    """Rendimiento del cupon cero a plazo tau bajo Vasicek.

    El precio es afin en la tasa corta, P(tau) = A(tau) e^{-B(tau) r0}, con
    B(tau) = (1-e^{-kappa tau})/kappa. Lo que importa aqui es que
    B(tau)/tau < 1 y decrece con tau: la tasa larga se mueve menos que la
    corta, que es justo lo que un modelo de un solo factor sin esta
    estructura no captura."""
    tau = np.asarray(tau, dtype=float)
    b = (1 - np.exp(-kappa * tau)) / kappa
    ln_a = (r_lp - sigma ** 2 / (2 * kappa ** 2)) * (b - tau) - sigma ** 2 * b ** 2 / (4 * kappa)
    return {"B": b, "sensibilidad": b / tau, "rendimiento": (b * r0 - ln_a) / tau}


def nivel_que_ancla(objetivo, tau, kappa, sigma, r0):
    """Nivel de largo plazo que hace que el modelo reproduzca un rendimiento
    observado a plazo tau.

    kappa y sigma salen de la serie historica, pero el nivel de largo plazo
    del descuento se elige para que la curva del modelo pase por el dato de
    mercado de hoy, en vez de partir de una curva inventada. El rendimiento
    es lineal en r_lp, asi que se despeja sin resolver numericamente."""
    b = (1 - np.exp(-kappa * tau)) / kappa
    resto = b * r0 + sigma ** 2 * b ** 2 / (4 * kappa) - objetivo * tau
    return sigma ** 2 / (2 * kappa ** 2) + resto / (b - tau)


def main():
    pd.set_option("display.width", 200)
    datos = cargar()
    corta = datos["r_corta"].dropna()

    print("=" * 72)
    print(f"Muestra: {corta.index.min():%Y-%m} a {corta.index.max():%Y-%m}  (n={len(corta)})")
    print("=" * 72)

    par = calibrar_vasicek(corta)
    print(f"\n== Vasicek puro, calibrado por MCO ==")
    print(f"   a={par['a']:.4f}  b={par['b']:.4f}  (R2 en niveles {par['r2']:.4f})")
    print(f"   kappa = {par['kappa']:.3f}  (vida media {par['vida_media']:.1f} anios)")
    print(f"   nivel de largo plazo = {par['r_lp']:.2f}%")
    print(f"   sigma = {par['sigma']:.2f} pp anual")

    adf = prueba_raiz_unitaria(corta)
    print(f"\n== Raiz unitaria (ADF) ==")
    print(f"   estadistico {adf['estadistico']:.3f}, valor p {adf['p']:.3f}")
    print("   " + ("NO se rechaza la raiz unitaria: los datos no distinguen la"
                   " reversion de una caminata aleatoria."
                   if adf["p"] > 0.05 else "Se rechaza la raiz unitaria."))

    print(f"\n== El R2 en niveles enganya ==")
    print(r2_en_cambios(datos, [
        (["r_corta"], "solo nivel"),
        (["r_corta", "pendiente"], "+ pendiente"),
        (["r_corta", "pendiente", "depreciacion", "us_10a"], "completo"),
    ]).to_string(index=False, float_format=lambda v: f"{v:.4f}"))

    ardl(datos, ["r_corta"], etiqueta="Vasicek puro")
    ardl(datos, ["r_corta", "pendiente", "depreciacion", "us_10a"],
         etiqueta="ARDL: pendiente, depreciacion y tasa de EE.UU.")
    ardl(datos.dropna(subset=["inflacion"]), ["r_corta", "inflacion", "pendiente"],
         etiqueta="Regla de Taylor: con inflacion (muestra hasta julio 2024)")

    print(f"\n== Fuera de muestra, ventana expansiva ==")
    print(evaluar_oos(datos).to_string(index=False, float_format=lambda v: f"{v:.3f}"))

    r0 = corta.iloc[-1] / 100
    anclado = nivel_que_ancla(0.0916, 10, par["kappa"], par["sigma"] / 100, r0)
    afin = vasicek_afin([1, 5, 10, 30], par["kappa"], anclado, par["sigma"] / 100, r0)
    print(f"\n== Curva afin de Vasicek ==")
    print(f"   tasa corta observada {r0 * 100:.2f}%, nivel anclado al 9.16% a 10 anios: "
          f"{anclado * 100:.2f}%")
    for tau, sens, rend in zip([1, 5, 10, 30], afin["sensibilidad"], afin["rendimiento"]):
        print(f"   {tau:2d} anios: rendimiento {rend * 100:5.2f}%, "
              f"un movimiento de 100 pb en la corta mueve {sens * 100:5.1f} pb")


if __name__ == "__main__":
    main()
