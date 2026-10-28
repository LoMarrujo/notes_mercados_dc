# Unidad 3 · Valuación de Acciones

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante calcule el valor de una acción con el modelo de descuento de dividendos a partir de su información financiera, para decidir si su precio de mercado está caro o barato.

## Contenido

|      | Tema                                            | Qué cubre                                                                                                                                                                                                                                        |
| ---- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| I    | De un bono a una acción                         | Flujos inciertos y sin vencimiento: la acción preferente como perpetuidad y el valor como descuento de dividendos (Williams)                                                                                                                     |
| II   | Modelo de Gordon                                | Dividendos que crecen a tasa constante, con la tasa requerida igual al CETE más la prima de riesgo                                                                                                                                               |
| III  | Los datos del reporte financiero                | Dividendo a partir de la utilidad por acción (UPA) y la razón de pago; crecimiento igual a retención por ROE                                                                                                                                     |
| IV   | ¿Importan los dividendos?                       | Miller y Modigliani: la política de dividendos no cambia el valor; la utilidad lo crea y el dividendo lo reparte                                                                                                                                 |
| V    | Caro o barato                                   | Valor calculado frente a precio de mercado, o rendimiento implícito frente a tasa requerida                                                                                                                                                      |
| VI   | Límites del modelo                              | Cuando el crecimiento alcanza la tasa o no hay dividendos: flujo de caja descontado y múltiplo precio/utilidad                                                                                                                                   |
| VII  | Escuelas de valuación y gestión activa o pasiva | Fundamental (Graham y Dodd), técnica y pasiva (mercados eficientes, Fama), y por qué alguien sigue analizando (Grossman y Stiglitz); el fondo activo promedio no le gana a su índice (Jensen, SPIVA), las comisiones y el sesgo de supervivencia |
| VIII | Tecnología y mercados                           | Estrategias cuantitativas y operación de alta frecuencia: cómo cambia la tecnología la formación de precios; aplicaciones sin comisión y asesores automatizados (robo-advisors): quien más opera, menos gana (Barber y Odean)                    |
| IX   | Burbujas y finanzas conductuales                | Punto com, 2008 y acciones meme; los precios se mueven más de lo que justifican los dividendos (Shiller); sesgos del inversionista: exceso de confianza, efecto manada, aversión a las pérdidas (Kahneman y Tversky)                             |
| X    | Ética del asesor                                | Conflicto de interés, perfil del cliente y la diferencia entre asesorar y gestionar en las disposiciones de la CNBV                                                                                                                              |

> La práctica de este tema está en [`practica_5_valuacion_acciones.md`](../../practicas/unidad3/practica_5_valuacion_acciones.md).

> **Por redactar.** Esta nota solo tiene el objetivo y la estructura; falta la teoría. La sección II se deriva del descuento de flujos de [`1_valuacion_instrumentos_deuda.md`](../unidad2/1_valuacion_instrumentos_deuda.md), y la tasa requerida viene de la prima de riesgo de [`4_rendimiento_y_riesgo_acciones.md`](4_rendimiento_y_riesgo_acciones.md). El rendimiento implícito de la sección V es la versión accionaria del rendimiento al vencimiento de [`2_rendimiento_y_curva_de_rendimientos.md`](../unidad2/2_rendimiento_y_curva_de_rendimientos.md). Las secciones VII a X cierran la unidad y sirven de repaso antes del examen: la burbuja de 2008 retoma las colas pesadas de [`3_hechos_estilizados_y_regresion.md`](3_hechos_estilizados_y_regresion.md), y la ética del asesor se puede trabajar como caso (distinguir un sesgo de comportamiento del inversionista de un conflicto de interés del asesor). Al Apéndice: una línea de tiempo de Graham y Dodd (1934) a Bessembinder (2018), con los premios Nobel de 1990 y 2013. La última sesión de práctica de la unidad es el examen. Las cifras de SPIVA están por verificar.

## Fuentes y referencias recomendadas

- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press: modelo de descuento de dividendos y crecimiento constante.
- Mishkin, F. S., & Eakins, S. G. (2024). *Financial Markets and Institutions* (10ª ed.). Pearson: valuación de acciones con el modelo de Gordon y con el múltiplo precio/utilidad.
- Williams, J. B. (1938). *The Theory of Investment Value*. Harvard University Press: el valor de una acción como valor presente de sus dividendos.
- Gordon, M. J. (1959). *Dividends, Earnings, and Stock Prices*. Review of Economics and Statistics, 41(2), 99-105: el modelo de crecimiento constante.
- Miller, M. H., & Modigliani, F. (1961). *Dividend Policy, Growth, and the Valuation of Shares*. Journal of Business, 34(4), 411-433: irrelevancia de la política de dividendos.
- Graham, B., & Dodd, D. L. (1934). *Security Analysis*. McGraw-Hill: el análisis fundamental y la distinción entre precio y valor.
- Fama, E. F. (1970). *Efficient Capital Markets: A Review of Theory and Empirical Work*. Journal of Finance, 25(2), 383-417: la hipótesis de mercados eficientes.
- Grossman, S. J., & Stiglitz, J. E. (1980). *On the Impossibility of Informationally Efficient Markets*. American Economic Review, 70(3), 393-408: si los precios lo reflejaran todo, nadie pagaría por analizar.
- Jensen, M. C. (1968). *The Performance of Mutual Funds in the Period 1945-1964*. Journal of Finance, 23(2), 389-416: los fondos activos no superan al mercado después de comisiones.
- S&P Dow Jones Indices. (s. f.). *SPIVA Scorecard*: porcentaje de fondos activos que rinden menos que su índice de referencia, por mercado y plazo.
- Budish, E., Cramton, P., & Shim, J. (2015). *The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response*. Quarterly Journal of Economics, 130(4), 1547-1621: la carrera por la velocidad en la operación de alta frecuencia.
- Barber, B. M., & Odean, T. (2000). *Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors*. Journal of Finance, 55(2), 773-806: los inversionistas que más operan obtienen menos.
- Shiller, R. J. (1981). *Do Stock Prices Move Too Much to be Justified by Subsequent Changes in Dividends?* American Economic Review, 71(3), 421-436: volatilidad excesiva de los precios frente a los dividendos.
- Shiller, R. J. (2000). *Irrational Exuberance*. Princeton University Press: burbujas bursátiles y su explicación conductual.
- Kahneman, D., & Tversky, A. (1979). *Prospect Theory: An Analysis of Decision under Risk*. Econometrica, 47(2), 263-291: aversión a las pérdidas y decisiones bajo riesgo.
- De Bondt, W. F. M., & Thaler, R. (1985). *Does the Stock Market Overreact?* Journal of Finance, 40(3), 793-805: sobrerreacción de los precios.
- Comisión Nacional Bancaria y de Valores. (2015). *Disposiciones de carácter general aplicables a las entidades financieras y demás personas que proporcionen servicios de inversión*. Diario Oficial de la Federación: perfil del cliente, razonabilidad de la recomendación y conflictos de interés.
- Royal Swedish Academy of Sciences. (2013). *Understanding Asset Prices* [Antecedentes científicos del Premio en Ciencias Económicas]: los trabajos de Fama, Hansen y Shiller.
