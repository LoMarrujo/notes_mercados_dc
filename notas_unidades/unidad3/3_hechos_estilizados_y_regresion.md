# Unidad 3 · Hechos Estilizados y Regresión

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante identifique, en los rendimientos históricos de una acción o un índice, en qué se alejan del modelo normal y cuánto se mueven con el mercado.

## Contenido

|     | Tema               | Qué cubre                                                                                                                                                                                 |
| --- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I   | Hechos estilizados | Colas pesadas, asimetría negativa, normalidad por agregación (anual frente a diario), rendimientos sin autocorrelación y agrupamiento de volatilidad; efecto apalancamiento, solo mención |
| II  | Regresión          | Mínimos cuadrados, pendiente como covarianza entre varianza y $R^2$; tendencia del logaritmo del S&P 500 y beta de FEMSA frente a NAFTRAC: riesgo sistemático frente al de la emisora     |

> La práctica de este tema está en [`practica_3_hechos_estilizados_y_regresion.md`](../../practicas/unidad3/practica_3_hechos_estilizados_y_regresion.md).

> **Por redactar.** Esta nota solo tiene el objetivo y la estructura; falta la teoría. Es el paso "Evaluar" del ciclo de la sección 1.1 de [`2_estadistica_y_datos.md`](2_estadistica_y_datos.md): revisa los supuestos de esa nota (rendimientos independientes, con la misma distribución en el tiempo y aproximadamente normales) y usa sus estadísticos sin definirlos de nuevo. La sección I usa los cierres diarios y de fin de mes del S&P 500, no la serie mensual de Shiller, porque esta promedia los cierres diarios y crea una autocorrelación que no existe; retoma el límite de pérdidas de la sección 3.2 de 2_ y los 87 días con caídas de más de $5\%$ de su sección 1.3. La sección II usa la tendencia de $\ln p_t$ (pendiente $0.0668$, $6.91\%$ anual sin dividendos, $R^2 = 0.96$, con la serie de Shiller) y la beta de FEMSA frente a NAFTRAC con 80 rendimientos mensuales ajustados por dividendos ($b = 0.82$, $R^2 = 0.39$), con la covarianza y la correlación de la sección 2.3 de 2_. Al Apéndice: el error estándar de la pendiente y los supuestos de la regresión. La beta se usa como mención en la prima de riesgo de [`4_rendimiento_y_riesgo_acciones.md`](4_rendimiento_y_riesgo_acciones.md).

## Fuentes y referencias recomendadas

- Cont, R. (2001). *Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues*. Quantitative Finance, 1(2), 223-236: los hechos estilizados de los rendimientos.
- Linton, O. (2019). *Financial Econometrics: Models and Methods*. Cambridge University Press: autocorrelación, volatilidad y regresión con rendimientos.
- Mandelbrot, B. (1963). The variation of certain speculative prices. *The Journal of Business*, 36(4), 394-419: las colas pesadas de los cambios de precio.
- Shiller, R. J. (2023). *U.S. Stock Markets 1871-Present and CAPE Ratio* [datos]. Yale University. http://www.econ.yale.edu/~shiller/data.htm: nivel mensual del S&P 500.
- Yahoo Finance. (2026). *S&P 500 (^GSPC), FEMSA (FEMSAUBD.MX) y NAFTRAC (NAFTRAC.MX), historial de precios* [datos]. https://finance.yahoo.com: cierres diarios del S&P 500 y cierres mensuales de FEMSA y NAFTRAC, consultados el 24 de octubre de 2026.
