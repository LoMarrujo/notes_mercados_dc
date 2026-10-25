# Unidad 3 · Estadística y Datos

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante construya un intervalo de confianza para el rendimiento esperado de un activo a partir de sus rendimientos históricos.

## Contenido

|     | Tema                             | Qué cubre                                                                                                                                                                                                                                                |
| --- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I   | Contexto                         | De los datos al modelo: población y muestra, el modelo desconocido y los datos como una realización suya; Graunt, Gauss y Laplace, Fisher                                                                                                                |
| II  | Muestra y estadísticos           | Muestra aleatoria (vector aleatorio con componentes independientes e idénticamente distribuidas), histograma, media, desviación estándar con $n-1$, mediana, cuantiles, covarianza y correlación muestrales, con los 98 rendimientos anuales del S&P 500 |
| III | Estimadores y error estándar     | El estimador como variable aleatoria; esperanza y varianza de la media muestral, error estándar $s/\sqrt{n}$ y la desviación estándar de una suma, $\sigma\sqrt{t}$                                                                                      |
| IV  | Ley de los grandes números y TCL | Por qué el promedio converge y por qué es aproximadamente normal; intervalo de confianza al 95% para el rendimiento esperado del S&P 500                                                                                                                 |
| V   | Hechos estilizados               | Colas pesadas, asimetría negativa, normalidad por agregación (anual frente a diario), rendimientos sin autocorrelación y agrupamiento de volatilidad; efecto apalancamiento, solo mención                                                                |
| VI  | Regresión                        | Mínimos cuadrados, pendiente como covarianza entre varianza y $R^2$; tendencia del logaritmo del S&P 500 y beta de FEMSA frente a NAFTRAC: riesgo sistemático frente al de la emisora                                                                    |

> La práctica de este tema está en [`practica_2_estadistica_y_datos.md`](../../practicas/unidad3/practica_2_estadistica_y_datos.md).

> **Por redactar.** Esta nota solo tiene el objetivo y la estructura; falta la teoría. Sigue el estilo de [`1_probabilidad_y_riesgo.md`](1_probabilidad_y_riesgo.md), que va del modelo a los datos; aquí se va de los datos al modelo. El hilo son los 98 rendimientos anuales del S&P 500 de la sección 4.3 de esa nota ($ar{r} = 11.86\%$, $s = 19.40\%$, mediana $15.22\%$, error estándar $1.96\%$, intervalo al 95% de $8.01\%$ a $15.70\%$), con la acción de los escenarios (5.5%, 15.40%) como modelo conocido del que se simulan muestras. La sección V usa los cierres diarios y de fin de mes del S&P 500, no la serie mensual de Shiller, porque esta promedia los cierres diarios y crea una autocorrelación que no existe. La sección VI usa la tendencia de $\ln p_t$ (pendiente $0.0668$, $6.91\%$ anual sin dividendos, $R^2 = 0.96$, con la serie de Shiller) y la beta de FEMSA frente a NAFTRAC con 80 rendimientos mensuales ajustados por dividendos ($b = 0.82$, $R^2 = 0.39$). Al Apéndice: el divisor $n-1$ (Bessel), la $t$ de Student, prueba de hipótesis y valor p, el error estándar de la pendiente y los supuestos de la regresión. La nota es la base de [`3_rendimiento_y_riesgo_acciones.md`](3_rendimiento_y_riesgo_acciones.md), que aplica estos estimadores al IPC, y de la prima de riesgo que usa [`4_valuacion_acciones.md`](4_valuacion_acciones.md).

## Fuentes y referencias recomendadas

- Cont, R. (2001). *Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues*. Quantitative Finance, 1(2), 223-236: los hechos estilizados de los rendimientos.
- Linton, O. (2019). *Financial Econometrics: Models and Methods*. Cambridge University Press: estimación de la media y la volatilidad, autocorrelación y regresión con rendimientos.
- Damodaran, A. (2026). *Historical Returns on Stocks, Bonds and Bills: 1928-2025*. NYU Stern School of Business. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html: rendimientos anuales del S&P 500 con dividendos.
- Yahoo Finance. (2026). *S&P 500 (^GSPC), FEMSA (FEMSAUBD.MX) y NAFTRAC (NAFTRAC.MX), historial de precios* [datos]. https://finance.yahoo.com: cierres diarios del S&P 500 desde 1927 y cierres mensuales de FEMSA y NAFTRAC desde 2020, consultados el 24 de octubre de 2026.
- Shiller, R. J. (2023). *U.S. Stock Markets 1871-Present and CAPE Ratio* [datos]. Yale University. http://www.econ.yale.edu/~shiller/data.htm: nivel mensual del S&P 500.
