"""Descarga las series mensuales que calibran el modelo de tasas del
laboratorio (practicas/unidad2/laboratorio_calibracion.md).

FRED sirve cada serie como CSV sin llave de API, asi que el ejercicio corre
sin registrarse en ningun lado. Las series mexicanas son el espejo que la
OCDE publica en FRED, no la fuente primaria: Banxico es la autoridad, y
comprobar estos numeros contra el SIE es uno de los ejercicios del
laboratorio. La comprobacion mas rapida ya esta hecha: el ultimo dato de
IRLTLT01MXM156N es 9.16%, identico al rendimiento del Bono M a 10 anios que
cetesdirecto publico el 21 de septiembre de 2026 y que ya esta guardado en
datos/cetesdirecto_2026-09-21.csv.

El CSV descargado se versiona junto al codigo, con la fecha de descarga en
el nombre, para que las cifras del laboratorio no dependan de una consulta
que cambia cada mes. Si ya existe, se lee en vez de volver a descargar.

Uso (desde la raiz del repo):
    python notas_unidades/unidad2/codigo/datos_fred.py
"""
import io
import os

import numpy as np
import pandas as pd
import requests

DIR_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "datos")
RUTA = os.path.join(DIR_DATOS, "fred_tasas_mensual.csv")
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"

# Julio de 2001: Banxico adopta formalmente objetivos de inflacion, y es
# tambien donde arranca la serie del bono a 10 anios. Empezar en 1997
# metria el periodo posterior a la crisis del Tequila, con tasas de 25%,
# que triplica la volatilidad estimada y describe un regimen que ya no existe.
INICIO = "2001-07"

SERIES = {
    "r_corta": ("IR3TIB01MXM156N", "Tasa interbancaria MX a 3 meses, % anual"),
    "r_larga": ("IRLTLT01MXM156N", "Bono del gobierno MX a 10 anios, % anual"),
    "us_10a": ("DGS10", "Tesoro de EE.UU. a 10 anios, % anual"),
    "us_ff": ("FEDFUNDS", "Tasa de fondos federales de EE.UU., % anual"),
    "tc": ("EXMXUS", "Tipo de cambio pesos por dolar"),
    "inflacion": ("CPALTT01MXM659N", "Inflacion anual MX, % (se corta en julio 2024)"),
}


def _descargar(serie_id):
    r = requests.get(URL.format(serie_id), timeout=30)
    r.raise_for_status()
    d = pd.read_csv(io.StringIO(r.text), parse_dates=[0])
    d.columns = ["fecha", serie_id]
    d[serie_id] = pd.to_numeric(d[serie_id], errors="coerce")
    # varias series son diarias; el ultimo dato de cada mes es el que entra
    return d.set_index("fecha")[serie_id].dropna().resample("MS").last()


def descargar():
    """Arma el panel mensual desde FRED y lo guarda en datos/."""
    panel = pd.DataFrame({k: _descargar(sid) for k, (sid, _) in SERIES.items()})
    panel = panel.loc[INICIO:]
    os.makedirs(DIR_DATOS, exist_ok=True)
    panel.to_csv(RUTA, float_format="%.6f")
    print(f"datos guardados: {RUTA}  ({len(panel)} meses, "
          f"{panel.index.min():%Y-%m} a {panel.index.max():%Y-%m})")
    return panel


def cargar(forzar=False):
    """Lee el CSV versionado; lo descarga solo si falta o si forzar=True.

    Agrega las dos variables derivadas que usa el laboratorio: la pendiente
    de la curva (larga menos corta) y la depreciacion anual del peso."""
    panel = descargar() if (forzar or not os.path.exists(RUTA)) else pd.read_csv(
        RUTA, parse_dates=["fecha"], index_col="fecha")
    panel["pendiente"] = panel["r_larga"] - panel["r_corta"]
    panel["depreciacion"] = 100 * np.log(panel["tc"]).diff(12)
    return panel


if __name__ == "__main__":
    p = cargar(forzar=True)
    print()
    for col, (sid, desc) in SERIES.items():
        s = p[col].dropna()
        print(f"{col:12s} {sid:18s} n={len(s):4d}  hasta {s.index.max():%Y-%m}  "
              f"ultimo={s.iloc[-1]:8.3f}   {desc}")
