# Unidad 3 · Estadística y Datos

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante construya un intervalo de confianza para el rendimiento esperado de un activo a partir de sus rendimientos históricos.

## Contenido

|     | Tema                             | Qué cubre                                                                                                                                                                                                                                                                                                          |
| --- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| I   | Contexto                         | Los datos y el modelo: probabilidad deductiva y estadística inductiva, el ciclo de la estadística, datos observacionales, muestreo y muestra aleatoria simple, la serie de tiempo y los datos como una realización suya; especificación del modelo, paramétrico o no paramétrico, con modelos clásicos de finanzas |
| II  | Describir los datos              | Histograma, media, desviación estándar y media geométrica; distribución empírica, cuantil empírico y VaR y CVaR históricos; covarianza y correlación muestrales frente a un ruido blanco; con los 98 rendimientos anuales del S&P 500 y los mensuales de FEMSA y del S&P 500                                       |
| III | Estimadores                      | El estimador como variable aleatoria; principios de estimación: sustitución, máxima verosimilitud y Bayes; media muestral, error estándar $s/\sqrt{n}$ y $\sigma\sqrt{t}$; un límite de pérdidas con la normal, la Cauchy y los datos                                                                              |
| IV  | Ley de los grandes números y TCL | Por qué el promedio converge y por qué es aproximadamente normal; intervalo de confianza al 95% para el rendimiento esperado del S&P 500                                                                                                                                                                           |

> La práctica de este tema está en [`practica_2_estadistica_y_datos.md`](../../practicas/unidad3/practica_2_estadistica_y_datos.md).

> **Por redactar.** Las secciones 1 a 3 están escritas; falta la teoría de la sección 4, que además del intervalo para el rendimiento esperado debe dar uno para el CVaR, el que promete la caja "Predecir" del ciclo de la sección 1.1. Sigue el estilo de [`1_probabilidad_y_riesgo.md`](1_probabilidad_y_riesgo.md), que va del modelo a los datos; aquí se va de los datos al modelo. El hilo son los 98 rendimientos anuales del S&P 500 de la sección 4.3 de esa nota ($\bar{r} = 11.86\%$, $s = 19.40\%$, mediana $15.22\%$, error estándar $1.96\%$, intervalo al 95% de $8.01\%$ a $15.70\%$), con la acción de los escenarios (5.5%, 15.40%) como modelo conocido del que se simulan muestras. Pendiente para el Apéndice: la $t$ de Student, prueba de hipótesis y valor p. Los hechos estilizados y la regresión siguen en [`3_hechos_estilizados_y_regresion.md`](3_hechos_estilizados_y_regresion.md). La nota es la base de [`4_rendimiento_y_riesgo_acciones.md`](4_rendimiento_y_riesgo_acciones.md), que aplica estos estimadores al IPC, y de la prima de riesgo que usa [`5_valuacion_acciones.md`](5_valuacion_acciones.md).

### 1. Contexto

#### 1.1 El ciclo de descubrimiento del conocimiento

La probabilidad es deductiva: se toma un modelo dado y se deducen sus implicaciones.

> Ejemplo: Si el rendimiento diario del S&P 500 fuera normal, con media 0 y la desviación estándar de $1.2\%$, una caída de $1.2\%$ o más debería ocurrir uno de cada seis días, y una caída de más de $5\%$, una vez cada 300 años. Así trabaja el área de riesgos de un banco con un portafolio de acciones de 100 millones de pesos: con el mismo modelo deduce, sin observar un solo precio, el valor en riesgo al 99% a un día, $2.326 \times 1.2\% \times 100 = 2.79$ millones de pesos, la pérdida que solo se supera uno de cada 100 días, unas dos o tres veces al año. La conclusión se sigue de los supuestos con certeza; qué tan útil es depende de qué tan razonables sean.

La estadística es inductiva: recorre el camino partiendo de los datos y alimenta la modelación.

> Ejemplo: En la práctica nadie le da al banco ese $1.2\%$, ni le asegura que el rendimiento sea normal; tiene precios pasados, y con ellos infiere el modelo que pudo haberlos generado. El problema de esta nota es de ese tipo: cuánto rinde en promedio el S&P 500, a partir de sus 98 rendimientos anuales de 1928 a 2025. Las conclusiones de la estadística nunca son seguras, porque otros datos habrían dado otra estimación; parte de su trabajo es medir qué tan lejos puede estar la estimación del parámetro del modelo.

El trabajo de descubrimiento del conocimiento sigue un ciclo iterativo:

1. Se parte de una **pregunta**: cuánto rinde en promedio el S&P 500, que interesa a quien invierte a largo plazo, o cuánto pierde en sus peores años, que interesa a quien debe reservar capital para soportarlos y se mide con el CVaR.
2. Después vienen los **datos** y el **modelo** que pudo haberlos generado. El orden depende del tipo de trabajo.
    - En un trabajo de **exploración**, se describen primero los datos y estos sugieren el modelo, como cuando el histograma de los rendimientos diarios sugiere colas más pesadas que las de la normal.
    - En uno de **confirmación**, el modelo y la hipótesis se fijan antes de ver los datos, que solo sirven para ponerlos a prueba; si los mismos datos sugirieran el modelo y lo confirmaran, la prueba se aprobaría casi siempre.
3. Luego se **estiman** los parámetros, y con ellos su propia incertidumbre, porque otra historia habría dado otra estimación.
4. Con lo estimado se **predice** lo que pide la pregunta, el rendimiento esperado y la pérdida en los peores años, cada uno con un intervalo.
5. Al final se **evalúa** en dos sentidos. Si no es lo suficientemente bueno, se vuelve a especificar.
    - Primero, si el modelo predice bien con datos que no usó para estimarse, por ejemplo contando cuántos días se rebasa un límite de pérdidas.
    - Segundo, si la respuesta sirve al problema de negocio: si el capital reservado alcanza para un año malo, o si el rendimiento esperado compensa el riesgo para el inversionista.

<!-- diapositivas: figura sola -->
![Diagrama del ciclo del descubrimiento de conocimiento en cinco cajas unidas por flechas de izquierda a derecha, cada una con la sección de la nota que la cubre: Pregunta, cuánto rinde en promedio el S&P 500 y cuánto pierde en sus peores años (CVaR) (sección 1.1); Datos y modelo, en dorado, donde al explorar los datos sugieren el modelo y al confirmar el modelo se fija antes de verlos (secciones 1.2, 1.3 y 2); Estimar, estimadores y su propia incertidumbre (sección 3); Predecir, rendimiento esperado y pérdida en los peores años (CVaR), con su intervalo (sección 4); y Evaluar, si predice bien con datos que no usó y si sirve para la decisión de negocio (nota 3_); una flecha roja punteada regresa de Evaluar a Datos y modelo con la leyenda si no es lo suficientemente bueno, se vuelve a especificar](img/proceso_estadistico.png)

#### 1.2 Los datos

Inicialmente se supone una variable aleatoria $X$ y queremos aprender algo sobre este proceso con base en una muestra, es decir, en un número $n$ de observaciones
$$X_1, X_2, \dots, X_n.$$

Detrás de toda muestra hay dos procesos:

- El primero genera los datos. Son **experimentales** si quien investiga interviene, como al probar dos precios con clientes elegidos al azar, y **observacionales** si solo registra lo que ocurrió; en finanzas casi todo es observacional, porque nadie le asigna a una empresa su política de dividendos para ver qué pasa.
- El segundo proceso es el **muestreo**, la regla con que se eligen las observaciones. De esa regla depende lo que la muestra permite concluir: si favorece a ciertos datos, la estimación hereda ese sesgo, y más datos no lo corrigen.

> **¿De dónde sale la fórmula?** Si las observaciones son independientes, la probabilidad de que todas caigan donde caen es el producto de las probabilidades de cada una, como $P(A \cap B) = P(A) P(B)$ en la sección 3.3 de la nota anterior.

**Definición (muestra aleatoria simple).** $X_1, \dots, X_n$ son una **muestra aleatoria simple** de $X$ si son independientes y cada una tiene la misma distribución que $X$ (independientes e idénticamente distribuidas, iid). Su distribución conjunta es entonces

$$F_{X_1, \dots, X_n}(x_1, \dots, x_n) = F_X(x_1) F_X(x_2) \cdots F_X(x_n).$$

Es el supuesto con el que la sección 3 calcula la media muestral y su error estándar. Los tipos de muestreo más simples son cuatro:

| Tipo                                | Cómo se eligen las observaciones                                               | Ejemplo en finanzas                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Aleatorio simple                    | Al azar, cada una con la misma probabilidad y de forma independiente           | Sortear 30 emisoras de la BMV para estimar su rendimiento por dividendos promedio                       |
| Estratificado (stratified sampling) | Se divide la población en grupos, los estratos, y se sortea dentro de cada uno | Un ETF de bonos que no compra todos los títulos de su índice, sino una muestra por plazo y calificación |
| Sistemático                         | Cada $k$-ésima unidad, o a intervalos fijos de tiempo                          | Los cierres diarios, de fin de mes o de fin de año del S&P 500                                          |
| Por conveniencia (no aleatorio)     | Las que están a la mano                                                        | Solo las emisoras que siguen cotizando hoy, con su sesgo de supervivencia (survivorship bias, nota 0_)  |

Con los rendimientos de un índice no se sortea nada: el mercado produce una sola sucesión, y lo único que se elige es la frecuencia y el periodo, **un muestreo sistemático en el tiempo de datos observacionales**. Para tratar esa sucesión como una muestra aleatoria simple hace falta un supuesto más.

Los rendimientos se modelan como una **serie de tiempo**, una sucesión de variables aleatorias indexadas por el tiempo,

$$\{X_t\}_{t=1}^{T} = X_1, X_2, \dots, X_T,$$

donde $X_t$ es el rendimiento del índice en el año $t$.

> Ejemplo: Los rendimientos del S&P 500 son una serie de tiempo que va de 1928 ($t = 1$) a 2025 ($t = T = 98$). Como en la nota anterior, la mayúscula $X_t$ es la variable aleatoria antes de observarla y la minúscula $x_t$ el número observado, como $x_4 = -43.84\%$ en 1931. La historia ocurrió una sola vez: $x_1, \dots, x_{98}$ son una realización de la serie, una de las muchas trayectorias que el mercado pudo haber seguido. Tratarlos como 98 observaciones del mismo fenómeno exige suponer que la distribución de $X_t$ no cambia con $t$ (estacionariedad, stationarity), un supuesto que la nota 3_ revisa.

Obtener buenos datos en finanzas es difícil por los dos procesos.

- Del lado del **proceso generador**, no se puede experimentar ni repetir la historia, y el mecanismo cambia mientras se observa: cambian la regulación, la tecnología, las empresas que forman el índice y hasta los inversionistas, que reaccionan a lo que publican otros, de modo que un patrón que se vuelve conocido tiende a desaparecer cuando se aprovecha. Además, la señal es débil frente al ruido: el rendimiento promedio del S&P 500, $11.86\%$, es pequeño frente a la dispersión de un solo año, $19.40\%$, así que hacen falta muchos años para estimarlo, y los eventos extremos, los que más importan para el riesgo, son los que menos se observan.
- Del lado del **muestreo y el registro**, las bases suelen guardar solo a las empresas que sobrevivieron; el precio de una acción poco operada puede ser el de una operación de hace días; hay que ajustar por dividendos y por divisiones de acciones para no confundir un reparto con una pérdida; un promedio mensual de cierres diarios, como el de la serie de Shiller, crea una autocorrelación que no existe, y hasta las fechas pueden venir mal: en los precios mensuales de FEMSA que usa la sección 2.3, el cambio de horario corrió las etiquetas de algunos meses entre 2020 y 2022.

Por último, como solo hay una historia, quien prueba muchas estrategias con los mismos datos termina encontrando alguna que funcionó por suerte, el riesgo del trabajo de exploración que se presenta como confirmación. Oliver Linton (2019) bromea que los datos son el plural de las anécdotas: el $-43.84\%$ de 1931 es una anécdota y 98 años juntos son datos. Advierte que una sola observación extrema, como el desplome de octubre de 1987, puede pesar demasiado en una estimación, y que la crisis de 2008 dejó escepticismo sobre lo que la econometría puede predecir "y, ojalá, algo de humildad".

<!-- diapositivas: conservar -->
- **Probabilidad (nota 1_):** con el modelo conocido se calculan $E[R]$, $\sigma$, el VaR y el CVaR.
- **Estadística:** con los datos se estiman $E[R]$, $\sigma$, el VaR y el CVaR (estos dos, con el IPC en la nota 4_), y se mide qué tan lejos pueden estar de los parámetros del modelo.
- **Los datos como realización:** 98 rendimientos son una de muchas trayectorias posibles; suponer que la distribución no cambia en el tiempo permite tratarlos como una muestra.
- **Reconocer lo que no sabemos:** el promedio de 98 años, $11.86\%$, es solo una estimación de $E[R]$; con otra historia del mercado habría salido otro número. Por eso la respuesta es un intervalo, de $8.01\%$ a $15.70\%$ al 95% de confianza, que dice cuánto puede alejarse la estimación del rendimiento esperado. Suele ser más angosto cuanto más datos hay y cuanto menos dispersos son los rendimientos.

#### 1.3 Los modelos

Especificar un modelo es elegir la familia de distribuciones que pudo haber generado los datos y sus supuestos: si los rendimientos de años distintos son independientes, si su distribución cambia con el tiempo, si es normal. Los datos solos no lo deciden; la mayor parte viene del conocimiento del mercado. Un modelo no es correcto ni equivocado: es una simplificación, más o menos razonable para el uso que se le da. Uno bueno es consistente con lo que se sabe del fenómeno, se comporta bien en los casos extremos y tiene parámetros con una interpretación clara. Cuando sus supuestos se alejan de los datos o de lo que se sabe del mercado hay un **error de especificación**, y más datos no lo corrigen: el estimador sigue respondiendo la pregunta del modelo, no la del mercado.

Una primera decisión es cuánta forma suponer. Un modelo **paramétrico** supone una familia que queda determinada por unos cuantos números, sus **parámetros**, como la normal con $\mu$ y $\sigma$ o el modelo de escenarios de la nota anterior. Un modelo **no paramétrico** no supone una forma y deja que los datos la describan, con el histograma y la distribución empírica de la sección 2. El VaR muestra la diferencia: el área de riesgos de la sección 1.1 lo deduce de la normal, y la sección 2.2 lo lee de los años ordenados. Si la forma es razonable, el paramétrico aprovecha mejor pocos datos; si no lo es, carga con su error de especificación. El no paramétrico supone menos, pero pide muchos más datos, sobre todo en las colas. Entre los dos están los **semiparamétricos**, que fijan la forma solo de una parte de la distribución, por ejemplo de la cola.

Los modelos clásicos de las finanzas muestran el mismo patrón: el conocimiento del mercado fija la forma del modelo, y la estadística estima los parámetros que quedan.

| Modelo                               | Lo que aporta el contexto                                                      | Qué se estima con datos                    |
| ------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------ |
| Caminata aleatoria, Bachelier (1900) | Si los cambios de precio fueran predecibles, alguien ya los habría aprovechado | Media y desviación estándar de los cambios |
| Media y varianza, Markowitz (1952)   | Al inversionista le importan la ganancia esperada y su dispersión              | $E[R]$, $\sigma$ y covarianzas             |
| CAPM, Sharpe (1964)                  | Solo se paga el riesgo que no se elimina diversificando                        | La beta, pendiente de una regresión        |
| Dividendos crecientes, Gordon (1959) | El dividendo crece a una tasa $g$ menor que el rendimiento requerido $r$       | La prima de riesgo dentro de $r$, y $g$    |
| VaR normal, Basilea (1996)           | Los bancos deben reservar capital contra la pérdida de un día malo             | $\sigma$ y el cuantil al 99%               |
| Incumplimientos independientes       | Cada deudor paga o no paga por su cuenta                                       | La probabilidad de incumplimiento          |

Cada uno enseña algo sobre la especificación:

- **Los casos extremos.** Bachelier supuso cambios de precio normales, y una normal permite precios negativos; una acción no puede valer menos de cero porque la responsabilidad del accionista es limitada (nota 0_). Por eso hoy se modela el logaritmo del precio, la lognormal del Apéndice de 1_.
- **El límite de Gordon.** Si $g \geq r$, la fórmula da un precio infinito; el conocimiento de que ninguna empresa crece para siempre más rápido que la economía descarta esos valores.
- **Parámetros con interpretación.** La beta del CAPM dice cuánto se mueve la acción cuando se mueve el mercado, y por eso se puede discutir si $b = 0.82$ es razonable para FEMSA.
- **El error de especificación.** El modelo normal de 1.1 predice una caída de más de $5\%$ en un día del S&P 500 una vez cada 300 años; de 1928 a 2026 hubo 87. Mandelbrot (1963) ya había advertido que las colas son más pesadas, y 1987 y 2008 lo confirmaron. Por eso el VaR normal subestima la pérdida de un día malo, y el CVaR, que promedia las pérdidas más allá del VaR, depende todavía más de la cola que se suponga. Los incumplimientos independientes fallaron por lo mismo: en una crisis los deudores quiebran juntos.

El modelo de esta nota también es una especificación: rendimientos anuales del S&P 500 independientes, con la misma $E[R]$ y la misma $\sigma$ de 1928 a 2025, aunque en esos años hubo una guerra mundial, la inflación de los setenta y un índice que pasó de 90 a 500 empresas. La nota 3_ revisa qué tanto se sostiene. El Apéndice muestra un caso, la eficiencia del mercado, en que el error de especificación no se puede separar de lo que se quiere probar.

<!-- diapositivas: conservar -->
- **Especificar:** elegir la familia de distribuciones y sus supuestos; lo decide sobre todo el conocimiento del problema. Un modelo no es correcto ni equivocado, sino más o menos razonable.
- **Paramétrico o no paramétrico:** una familia fijada por unos cuantos parámetros, como la normal, o ninguna forma supuesta, como el histograma y el VaR histórico; el primero rinde más con pocos datos si es razonable, el segundo supone menos pero pide más datos.
- **Buen modelo:** consistente con el contexto, bien comportado en los extremos y con parámetros interpretables.
- **Error de especificación:** los supuestos se alejan de lo que muestran los datos o de lo que se sabe del mercado; más datos no lo corrigen.

### 2. Describir los datos

Los datos $x_1, \dots, x_n$ son una realización de las variables aleatorias $X_1, \dots, X_n$, la **muestra**. Un **estadístico** es cualquier número que se calcula con los datos, como su promedio. Cada estadístico de esta sección es la versión con datos de algo que en la nota anterior se calculaba con el modelo:

| Con el modelo (nota 1_)      | Con los datos (estadístico)                  |
| ---------------------------- | -------------------------------------------- |
| Densidad $f_X$               | Histograma                                   |
| Esperanza $\mu = E[X]$       | Media muestral $\bar{x}$                     |
| Desviación estándar $\sigma$ | Desviación estándar muestral $s$             |
| Distribución $F_X$           | Distribución empírica $\hat{F}_n$            |
| Cuantil $q_p$ y VaR          | Cuantil empírico $\hat{q}_p$ y VaR histórico |
| Correlación $\rho_{X,Y}$     | Correlación muestral $\hat{\rho}_{x,y}$      |

#### 2.1 Histograma, media y desviación estándar

**Definición (histograma).** Se divide el rango de los datos en intervalos del mismo ancho y se cuenta cuántas observaciones caen en cada uno. El **histograma** dibuja una barra por intervalo, con altura igual a esa cuenta. Es la versión con datos de la densidad: donde la densidad es alta caen muchas observaciones.

**Definición (media y desviación estándar muestrales).** La **media muestral** y la **desviación estándar muestral** son

$$\bar{x} = \frac{1}{n} \sum_{t=1}^{n} x_t, \qquad s = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} (x_t - \bar{x})^2}.$$

La media es el promedio de los datos y $s$ mide qué tan lejos de la media caen típicamente. Se divide entre $n - 1$ y no entre $n$ porque las desviaciones se miden respecto a $\bar{x}$, que queda más cerca de los datos que $\mu$ (Apéndice); con 98 datos, la diferencia es de medio por ciento.

**Ejemplo (los 98 rendimientos del S&P 500).** Con intervalos de 10 puntos, 81 de los 98 años quedan entre $-10\%$ y $40\%$, y el intervalo más poblado es el de $10\%$ a $20\%$, con 21 años. La cola izquierda está más poblada que la derecha: 12 años perdieron más de $10\%$ y solo 5 ganaron $40\%$ o más. La media y la desviación estándar son

$$\bar{x} = 11.86\%, \qquad s = 19.40\%.$$

En la figura, 65 de los 98 años (66%) caen a una desviación estándar de la media, entre $-7.55\%$ y $31.26\%$, y 94 (96%) a dos. Una normal tendría 68% y 95%, así que con datos anuales el histograma se parece bastante a una normal; la nota 3_ muestra que con datos diarios no.

La línea roja es la **media geométrica**,

$$\left( \prod_{t=1}^{n} (1 + x_t) \right)^{1/n} - 1 = 10.02\%,$$

el rendimiento constante que habría dejado la misma riqueza final que la historia real (sección 4.3 de la nota anterior). Queda 1.84 puntos por debajo de la media porque una pérdida pesa más que una ganancia del mismo tamaño: perder 20% y luego ganar 20% deja 96 de cada 100 pesos. Cuanto más dispersos son los rendimientos, mayor es la brecha; aproximadamente, la media geométrica es $\bar{x} - s^2/2 = 9.98\%$ (Apéndice). La media dice cuánto se espera ganar en un año; la media geométrica, cuánto creció el dinero que se quedó invertido los 98 años.

<!-- diapositivas: figura sola -->
![Histograma de los 98 rendimientos anuales del S&P 500 con dividendos entre 1928 y 2025, en barras de 10 puntos de ancho desde -50% hasta 60%; una línea dorada marca la media de 11.86%, una línea roja de rayas y puntos marca la media geométrica de 10.02%, un poco a su izquierda, y una franja dorada clara, entre líneas punteadas en -7.55% y 31.26%, marca una desviación estándar de 19.40% a cada lado, con la leyenda 65 de 98 años dentro de la franja](img/sp500_histograma_media_desviacion.png)

#### 2.2 Distribución empírica y VaR histórico

El VaR de la nota anterior es un cuantil del modelo. Con datos, el cuantil se lee de los datos ordenados.

**Definición (distribución empírica y cuantil empírico).** La **distribución empírica** $\hat{F}_n$ asigna probabilidad $1/n$ a cada dato observado. Su función de distribución es la proporción de datos que no pasan de $x$,

$$\hat{F}_n(x) = \frac{\text{número de datos } x_t \leq x}{n},$$

y el **cuantil empírico** es su cuantil, con la misma definición de la sección 6.1 de la nota anterior: $\hat{q}_p = \min\{x : \hat{F}_n(x) \geq p\}$. Con los datos ordenados del menor al mayor, es el dato en la posición $\lceil np \rceil$, el primer entero mayor o igual que $np$. El **VaR histórico** es la pérdida que marca ese cuantil, y el **CVaR histórico**, el promedio de los datos que quedan en él o por debajo.

**Ejemplo (VaR histórico del S&P 500).** Con $n = 98$ y $p = 0.05$, $np = 4.9$, así que $\hat{q}_{0.05}$ es el quinto peor año: 1930, con $-25.12\%$. **El VaR histórico anual al 95% es una pérdida de $25.12\%$**; con 10,000 pesos, 2,512 pesos. El modelo normal de la nota anterior daba $20.1\%$, 2,006 pesos, así que en estos datos la normal subestima la pérdida de un año malo. El CVaR histórico es el promedio de los cinco peores años,

$$\frac{-43.84\% - 36.55\% - 35.34\% - 25.90\% - 25.12\%}{5} = -33.35\%:$$

en el peor año de cada veinte se pierde, en promedio, $33.35\%$. El VaR histórico no supone ninguna distribución, pero descansa en cinco años: un sexto año malo lo movería bastante.

#### 2.3 Covarianza y correlación

**Definición (covarianza y correlación muestrales).** Con dos series observadas en los mismos periodos, $x_t$ y $y_t$, la **covarianza muestral** y la **correlación muestral** son

$$s_{xy} = \frac{1}{n-1} \sum_{t=1}^{n} (x_t - \bar{x})(y_t - \bar{y}), \qquad \hat{\rho}_{x,y} = \frac{s_{xy}}{s_x s_y}.$$

Se leen igual que en la sección 5.2 de la nota anterior: cada producto es positivo cuando las dos series quedan del mismo lado de su media, y negativo cuando quedan de lados opuestos.

**Ejemplo (FEMSA frente al S&P 500).** FEMSA es una de las empresas más grandes de la bolsa mexicana, y el S&P 500 resume el mercado accionario de Estados Unidos. Con los 80 rendimientos mensuales de febrero de 2020 a septiembre de 2026, $x_t$ para el S&P 500, con sus cierres de fin de mes en dólares y sin dividendos, y $y_t$ para FEMSA, con precios ajustados por dividendos:

$$s_x = 4.89\%, \qquad s_y = 6.35\%, \qquad s_{xy} = 0.000981, \qquad \hat{\rho}_{x,y} = \frac{0.000981}{0.0489 \times 0.0635} = 0.32.$$

La nube se inclina hacia arriba a la derecha, pero poco: FEMSA tiende a subir cuando sube el mercado estadounidense, lejos de una línea recta. Una parte de su riesgo la comparte con los mercados de todo el mundo, como la caída de marzo de 2020, el punto de abajo a la izquierda; otra es propia de México y de la emisora.

<!-- diapositivas: figura sola -->
![Diagrama de dispersión de 80 rendimientos mensuales, de febrero de 2020 a septiembre de 2026, con el S&P 500 en el eje horizontal y FEMSA en el vertical; una línea vertical y una horizontal en las medias dividen el plano en cuatro cuadrantes; 40 puntos dorados caen del mismo lado de las dos medias y 40 grises en lados opuestos, en una nube poco inclinada con un punto aislado abajo a la izquierda, marzo de 2020, y otro arriba a la derecha; el título indica una correlación de 0.32](img/femsa_sp500_dispersion.png)

Para saber cuánto es 0.32 conviene ver cómo luce la falta de relación. Un **ruido blanco** es una sucesión de variables aleatorias independientes con la misma distribución, media 0 y varianza constante: ningún valor dice nada de los demás. La siguiente figura simula dos ruidos blancos independientes y normales, con las desviaciones estándar del S&P 500 y de FEMSA, 80 pares en la misma escala que la anterior; su correlación muestral es 0.03. Contar puntos no las distingue: 40 de los 80 meses reales quedan del mismo lado de las medias, y 48 de los 80 pares simulados. Lo que las distingue es el tamaño de los productos $(x_t - \bar{x})(y_t - \bar{y})$: en los datos, los meses de movimientos grandes, como marzo y noviembre de 2020, caen del mismo lado y pesan mucho en la covarianza; en el ruido blanco, los productos grandes se reparten entre positivos y negativos y se cancelan.

<!-- diapositivas: figura sola -->
![Diagrama de dispersión de 80 pares simulados de dos ruidos blancos normales e independientes, con media 0 y las desviaciones estándar del S&P 500 y de FEMSA, en la misma escala que la figura de FEMSA frente al S&P 500; las líneas en las medias dividen el plano en cuatro cuadrantes; 48 puntos dorados caen del mismo lado de las dos medias y 32 grises en lados opuestos, en una nube redonda sin inclinación; el título indica una correlación de 0.03](img/ruido_blanco_dispersion.png)

### 3. Estimadores

Los estadísticos de la sección 2 describen la única historia que ocurrió. Para usarlos como estimaciones del modelo hay que responder dos preguntas: de dónde sale un estadístico para un parámetro (3.1) y cuánto cambiaría con otra historia (3.2).

**Definición (estimador y estimación).** Un **estimador** es un estadístico calculado con la muestra aleatoria, antes de observar los datos; por ejemplo, la media muestral

$$\bar{X} = \frac{1}{n} \sum_{t=1}^{n} X_t.$$

Como depende de las variables aleatorias $X_1, \dots, X_n$, el estimador también es una variable aleatoria. Una **estimación** es el número que da con los datos observados, $\bar{x}$: mayúscula antes de observar, minúscula después.

#### 3.1 Principios de estimación

Dos principios generales construyen estimadores: la **verosimilitud**, que usa solo los datos, y el enfoque **bayesiano**, que además usa lo que se sabía antes de verlos. Antes conviene nombrar el más sencillo, que resultará ser un caso particular del primero.

**Definición (estimador por sustitución).** Si el parámetro es una característica de la distribución, $\theta = T(F_X)$, como su esperanza o un cuantil, el **estimador por sustitución** (plug-in) es esa misma característica calculada en la distribución empírica de la sección 2.2, $\hat{\theta} = T(\hat{F}_n)$.

Los estadísticos de la sección 2 son de este tipo: la esperanza de $\hat{F}_n$ es $\sum_{t=1}^{n} x_t / n = \bar{x}$, su cuantil es el cuantil empírico y su correlación es $\hat{\rho}_{x,y}$ (los divisores se cancelan en el cociente). La excepción es la varianza: la de $\hat{F}_n$ divide entre $n$, y el $n - 1$ de $s$ es una corrección para que no tenga sesgo (Apéndice).

> **¿De dónde sale la fórmula?** Si los rendimientos son independientes, su densidad conjunta es el producto de las densidades de cada uno, como $P(A \cap B) = P(A) P(B)$ en la sección 3.3 de la nota anterior. Con los datos ya observados, ese producto se lee al revés: como función del parámetro, qué tan probables hace cada valor del parámetro a los datos que ocurrieron.

**Definición (verosimilitud y máxima verosimilitud).** Si $X_1, \dots, X_n$ son independientes, con una densidad $f(x; \theta)$ que depende de un parámetro $\theta$, la **verosimilitud** (likelihood) de los datos es

$$L(\theta) = \prod_{t=1}^{n} f(x_t; \theta),$$

y el **estimador de máxima verosimilitud** $\hat{\theta}$ es el valor del parámetro que la hace más grande: el modelo de la familia que hace más probables los datos observados. En la práctica se maximiza su logaritmo, $\ln L(\theta) = \sum_{t=1}^{n} \ln f(x_t; \theta)$, que convierte el producto en una suma y tiene el mismo máximo.

**Ejemplo (el S&P 500 con un modelo normal).** Con la densidad normal de la nota anterior, la log-verosimilitud de los 98 rendimientos anuales es

$$\ln L(\mu, \sigma) = -n \ln \sigma - \frac{1}{2 \sigma^2} \sum_{t=1}^{n} (x_t - \mu)^2 - \frac{n}{2} \ln (2\pi).$$

Para cualquier $\sigma$, la mejor $\mu$ es la que hace más pequeña la suma de cuadrados, y como

$$\sum_{t=1}^{n} (x_t - \mu)^2 = \sum_{t=1}^{n} (x_t - \bar{x})^2 + n (\bar{x} - \mu)^2,$$

esa es la media: $\hat{\mu} = \bar{x} = 11.86\%$. Con $\mu = \bar{x}$, la mejor $\sigma$ es $\hat{\sigma} = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (x_t - \bar{x})^2} = 19.30\%$, que divide entre $n$, igual que la sustitución. **Con la normal, la máxima verosimilitud da $\hat{\mu} = 11.86\%$, la misma media que la sustitución.** No es casualidad:

**Proposición (distribución empírica).** Entre todas las distribuciones posibles, la que hace más probables los datos observados es la distribución empírica $\hat{F}_n$: es el estimador no paramétrico de máxima verosimilitud de $F_X$ (Apéndice).

Si no se supone ninguna familia, el modelo que mejor explica lo que ocurrió reparte la probabilidad por igual entre lo que ocurrió. Así, la sustitución es la máxima verosimilitud sin familia, el modelo no paramétrico de la sección 1.3 llevado a la estimación, y la máxima verosimilitud con una familia es su versión paramétrica.

La verosimilitud usa solo los datos, pero la sección 1.3 insistió en que el conocimiento del mercado también informa al modelo. El enfoque **bayesiano** lo incorpora como una distribución: trata al parámetro como incierto, con una **distribución a priori** que resume lo que se cree antes de ver los datos, y la actualiza con ellos.

> **¿De dónde sale la fórmula?** De la probabilidad condicional de la sección 3.3 de la nota anterior: $P(A \cap B) = P(A \mid B) P(B) = P(B \mid A) P(A)$, y al despejar, $P(A \mid B) = P(B \mid A) P(A) / P(B)$, la **regla de Bayes**. Si $A$ es un valor del parámetro y $B$ son los datos observados, $P(B \mid A)$ es la verosimilitud, y $P(B)$ no depende del parámetro.

**Definición (distribución a posteriori).** Si $g(\theta)$ es la densidad a priori del parámetro, su **densidad a posteriori**, la que tiene después de ver los datos, es

$$g(\theta \mid x_1, \dots, x_n) = \frac{L(\theta) g(\theta)}{\int L(u) g(u) \, du}:$$

la verosimilitud por la a priori, dividida entre una constante que hace que el total sea 1.

**Ejemplo (un analista y 98 años del S&P 500).** Un analista cree, por la prima de riesgo que se observa en otros mercados, que el rendimiento esperado del S&P 500 está alrededor de $8\%$, y expresa su duda con una a priori normal con media $\mu_0 = 8\%$ y desviación estándar $\sigma_0 = 2\%$ (ilustrativas). Con $\sigma$ igual a $s$, en la descomposición del ejemplo anterior solo $n(\bar{x} - \mu)^2$ depende de $\mu$, así que

$$L(\mu) \propto \exp\left( -\frac{n (\bar{x} - \mu)^2}{2 s^2} \right),$$

una normal en $\mu$ centrada en $\bar{x} = 11.86\%$, con desviación $s / \sqrt{n} = 1.96\%$ (el error estándar de la sección 3.2). El producto de dos densidades normales en $\mu$ es otra normal (Apéndice), cuya media es el promedio de las dos medias ponderado por su **precisión**, uno entre la varianza:

$$\hat{\mu}_{post} = w \bar{x} + (1 - w) \mu_0, \qquad w = \frac{n / s^2}{n / s^2 + 1 / \sigma_0^2}, \qquad \sigma_{post} = \frac{1}{\sqrt{n / s^2 + 1 / \sigma_0^2}}.$$

Como $s / \sqrt{n} = 1.96\%$ es casi igual a la duda del analista, $2\%$, los dos pesan casi lo mismo, $w = 0.51$:

$$\hat{\mu}_{post} = 0.51 \times 11.86\% + 0.49 \times 8\% = 9.97\%, \qquad \sigma_{post} = 1.40\%.$$

**La a posteriori queda en $9.97\%$, entre la opinión del analista y los datos, y es más precisa que cualquiera de los dos.** Si el mismo promedio viniera de solo 10 años, con $s / \sqrt{10} = 6.14\%$, el peso de los datos bajaría a $w = 0.10$ y la a posteriori quedaría en $8.37\%$, cerca del analista: con pocos datos manda la a priori, y con muchos, los datos. Así combinan Black y Litterman (1992) los rendimientos que implica el equilibrio del mercado con las opiniones de los analistas para armar un portafolio.

<!-- diapositivas: figura sola -->
![Tres densidades normales del rendimiento esperado del S&P 500, mu, en el eje horizontal entre 0% y 20%: la a priori del analista, centrada en 8% con desviación 2%, en dorado de rayas; la verosimilitud de los 98 años, centrada en 11.86% con desviación 1.96%, en gris; y la a posteriori, centrada en 9.97% con desviación 1.40%, en azul marino, más alta y angosta que las otras dos y entre ellas](img/sp500_bayes_priori_posteriori.png)

Las dos maneras de razonar difieren en qué es incierto: para la verosimilitud, $\mu$ es un número fijo y lo aleatorio es el estimador, que cambia de una historia a otra; para el enfoque bayesiano, los datos ya ocurrieron y lo incierto es $\mu$. Con muchos datos llegan casi al mismo número, y la a priori es un supuesto más de la especificación, que hay que justificar.

<!-- diapositivas: conservar -->
- **Sustitución:** calcular el parámetro en la distribución empírica; da los estadísticos de la sección 2.
- **Máxima verosimilitud:** el valor del parámetro que hace más probables los datos; con la normal da $\bar{x} = 11.86\%$, y sin suponer familia es la sustitución.
- **Bayes:** a posteriori proporcional a verosimilitud por a priori; un promedio de la opinión previa y de los datos, ponderado por su precisión: $9.97\%$ para el S&P 500.

#### 3.2 Media muestral y error estándar

El promedio de $11.86\%$ depende de qué años tocaron; con otra historia del mercado habría salido otro número. Esta subsección mide cuánto puede cambiar.

**Proposición (varianza de una suma).** Para variables aleatorias $X$ y $Y$ y una constante $a$,

$$\operatorname{Var}(aX) = a^2 \operatorname{Var}(X), \qquad \operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2 \operatorname{Cov}(X, Y).$$

Si $X$ y $Y$ son independientes, su covarianza es 0 (sección 5.2 de la nota anterior) y las varianzas simplemente se suman; lo mismo vale para $n$ variables independientes.

**Proposición (media muestral).** Si $X_1, \dots, X_n$ son independientes, cada una con media $\mu$ y varianza $\sigma^2$, entonces

$$E[\bar{X}] = \mu, \qquad \operatorname{Var}(\bar{X}) = \frac{\sigma^2}{n}, \qquad \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}.$$

**Justificación matemática.** Por la linealidad de la esperanza (sección 4.2 de la nota anterior), $E[\bar{X}] = \frac{1}{n}(\mu + \cdots + \mu) = \mu$. Por la proposición anterior, con $a = 1/n$ y las varianzas de variables independientes sumadas, $\operatorname{Var}(\bar{X}) = \frac{1}{n^2}(\sigma^2 + \cdots + \sigma^2) = \frac{\sigma^2}{n}$.

Un estimador cuya esperanza es el parámetro que estima se llama **insesgado**: en promedio, sobre todas las historias posibles, $\bar{X}$ acierta. La varianza muestral también lo es, $E[S^2] = \sigma^2$, gracias al divisor $n - 1$ (Apéndice).

**Definición (error estándar).** En la práctica no se conoce $\sigma$ y se sustituye por $s$. El **error estándar** de la media es la desviación estándar estimada del estimador,

$$\operatorname{ee}(\bar{x}) = \frac{s}{\sqrt{n}}.$$

**Ejemplo (S&P 500).** Con los 98 rendimientos anuales, $s = 19.40\%$ y

$$\operatorname{ee}(\bar{x}) = \frac{19.40\%}{\sqrt{98}} = 1.96\%.$$

Promediar 98 años reduce la dispersión de un solo año unas diez veces, porque $\sqrt{98} \approx 10$: **el promedio de $11.86\%$ puede alejarse típicamente unos 2 puntos del rendimiento esperado $E[R]$**, y la sección 4 convierte ese error en un intervalo.

**Ejemplo (la suma crece con $\sqrt{t}$).** La misma proposición da la desviación estándar de una suma de $t$ rendimientos independientes: $\sqrt{t \sigma^2} = \sigma \sqrt{t}$. Así se pasa, aproximadamente, de una frecuencia a otra. La desviación estándar diaria del S&P 500, $1.19\%$ (el $1.2\%$ de la sección 1.1), con unos 252 días de operación al año, da

$$1.19\% \times \sqrt{252} = 18.9\%$$

al año, cerca del $19.40\%$ medido con los rendimientos anuales. En 10 años, la suma de los rendimientos varía $19.40\% \times \sqrt{10} = 61.3\%$, mientras que su promedio varía solo $19.40\% / \sqrt{10} = 6.1\%$: el promedio se vuelve más preciso con más años, pero lo acumulado se vuelve más incierto.

<!-- diapositivas: conservar -->
- **Estimador:** se calcula con la muestra y es una variable aleatoria; cada historia da una estimación distinta.
- **Media muestral:** $E[\bar{X}] = \mu$ y $\sigma_{\bar{X}} = \sigma / \sqrt{n}$; el promedio se vuelve más preciso con más datos, mientras que una suma de $t$ periodos varía $\sigma \sqrt{t}$.
- **Error estándar:** $s / \sqrt{n}$, la desviación estándar estimada de la media; para el S&P 500, $1.96\%$.

#### 3.3 Un límite de pérdidas con tres modelos

**Ejemplo (un límite de pérdidas con otra densidad).** Un límite de pérdidas depende de la forma de la densidad, no solo de la desviación estándar. El área de riesgos de la sección 1.1 supone rendimientos diarios normales, con media 0 y desviación estándar $1.2\%$, y fija su límite de pérdidas en el VaR al 99% a un día: una pérdida de $2.79\%$ del portafolio, que según su modelo se rebasa uno de cada 100 días, unas 2.5 veces al año. Pero el histograma de los rendimientos diarios del S&P 500 tiene un pico más alto y extremos más poblados que la normal. Una distribución con nombre que tiene esa forma es la **Cauchy**, con densidad

$$f(x) = \frac{1}{\pi \gamma \left[ 1 + \left( \frac{x - x_0}{\gamma} \right)^2 \right]},$$

donde $x_0$ es su centro, la mediana, y $\gamma$ su escala, la mitad de su rango intercuartil. Sus extremos son tan pesados que no tiene media ni varianza (Apéndice de la nota anterior), así que se ajusta por máxima verosimilitud (sección 3.1): con los 24,803 rendimientos diarios, $x_0 = 0.06\%$ y $\gamma = 0.47\%$. La sustitución da valores parecidos, la mediana muestral, $0.05\%$, y la mitad del rango intercuartil, $0.50\%$ (Apéndice). Supongamos, para ilustrar, que esa Cauchy es la distribución "real". Con cada distribución se simulan 10,000 años de 252 días, y se comparan con los datos diarios del S&P 500 de 1928 a 2026, leídos directamente como en la sección 2.2:

|                                               | Normal (supuesta)        | Cauchy (simulada)                    | S&P 500 (datos)       |
| --------------------------------------------- | ------------------------ | ------------------------------------ | --------------------- |
| Días al año en que se rebasa el límite        | 2.5                      | 13.1                                 | 4.5                   |
| Pérdida promedio en esos días (CVaR)          | $3.20\%$                 | no existe; $31.8\%$ en la simulación | $4.19\%$              |
| Días al año con una pérdida de más de $5\%$   | 0.004, uno cada 240 años | 7.4                                  | 0.88, casi uno al año |
| Días al año con una pérdida de más de $100\%$ | 0                        | 0.38, uno cada tres años             | 0                     |

La normal y la Cauchy fallan en sentidos opuestos. La normal subestima: en los datos el límite se rebasa 4.5 días al año, no 2.5. La Cauchy sobrestima: lo rebasa 13 días al año, su CVaR no existe y produce pérdidas de más de $100\%$ en un día, imposibles por la responsabilidad limitada (los casos extremos de la sección 1.3). Tampoco cumple lo que promete el error estándar de la sección 3.2: con la normal, la mitad central de los promedios anuales cabe en un rango de $0.10\%$; con la Cauchy, en uno de $0.94\%$, el mismo que el de un solo día, porque el promedio de variables Cauchy independientes es otra Cauchy con la misma escala. La fórmula $\sigma / \sqrt{n}$ supone que $\sigma$ existe. **Es el error de especificación en sus dos versiones, un modelo demasiado tranquilo y uno demasiado nervioso; los datos quedan entre los dos**, y por eso conviene medir las pérdidas grandes directamente con ellos.

<!-- diapositivas: figura sola -->
![Dos paneles del ejemplo del límite de pérdidas: a la izquierda, sobre el histograma gris de los rendimientos diarios del S&P 500 de 1928 a 2026, la densidad normal supuesta, con media 0 y desviación 1.2%, en dorado, y la Cauchy ajustada a los datos, la "real", en azul marino, con un pico más alto que el histograma; una línea roja punteada marca el límite de -2.79%, y un acercamiento entre -7% y -2.5% muestra el histograma entre las dos curvas, con la normal cayendo a cero antes de -4% y la Cauchy muy por encima de los datos; a la derecha, histogramas de cuántos días al año se rebasa el límite en 10,000 años simulados, 2.5 días en promedio con la normal, en contorno dorado, y 13.1 con la Cauchy, en barras azul marino, con una línea roja punteada en los 4.5 días al año del S&P 500 real, entre los dos](img/limite_perdidas_normal_cauchy.png)

## Apéndice: Complementos de estadística

Esta sección amplía el núcleo; no forma parte del objetivo ni se evalúa. Reúne las justificaciones de la media geométrica, del divisor $n - 1$, de la distribución empírica como estimador de máxima verosimilitud y de la a posteriori normal, la eficiencia de la máxima verosimilitud en la Cauchy y la hipótesis conjunta de Fama.

**La media geométrica, aproximadamente $\bar{x} - s^2/2$.** Si $g$ es la media geométrica, $\ln(1 + g) = \frac{1}{n} \sum_{t=1}^{n} \ln(1 + x_t)$. Para rendimientos pequeños, $\ln(1 + x) \approx x - x^2/2$, así que el lado derecho es aproximadamente $\bar{x} - \frac{1}{2n} \sum_{t=1}^{n} x_t^2 \approx \bar{x} - (s^2 + \bar{x}^2)/2$, y el izquierdo, $g - g^2/2$. Como $g$ y $\bar{x}$ son parecidos, sus cuadrados casi se cancelan y queda $g \approx \bar{x} - s^2/2$. Con el S&P 500 da $9.98\%$, frente a los $10.02\%$ exactos.

**El divisor $n - 1$.** La descomposición de la sección 3.1, con las variables aleatorias, da $\sum_{t=1}^{n} (X_t - \bar{X})^2 = \sum_{t=1}^{n} (X_t - \mu)^2 - n (\bar{X} - \mu)^2$. Su esperanza es $n \sigma^2 - n \operatorname{Var}(\bar{X}) = n \sigma^2 - \sigma^2 = (n - 1) \sigma^2$ (sección 3.2), así que dividir entre $n - 1$ da $E[S^2] = \sigma^2$: la varianza muestral es insesgada, y la de la distribución empírica, que divide entre $n$, la subestima un poco.

**La distribución empírica como estimador de máxima verosimilitud.** Sin una familia no hay densidad que usar, así que la verosimilitud se toma con la probabilidad $p_t$ que la distribución asigna a cada dato observado: $L = p_1 p_2 \cdots p_n$, con $p_1 + \cdots + p_n \leq 1$. (Con densidades arbitrarias no habría máximo: una densidad cada vez más concentrada sobre los datos haría crecer $L$ sin límite.) Poner probabilidad fuera de los datos solo resta, así que la suma es 1, y un producto de números positivos con suma fija es máximo cuando son iguales, porque la media geométrica nunca supera a la aritmética. Por eso $p_t = 1/n$; con datos repetidos, cada valor recibe su frecuencia relativa.

**La a posteriori normal.** Con la a priori $g(\mu) \propto \exp\left( -(\mu - \mu_0)^2 / (2 \sigma_0^2) \right)$ y la verosimilitud $L(\mu) \propto \exp\left( -n (\bar{x} - \mu)^2 / (2 s^2) \right)$ de la sección 3.1, el producto es la exponencial de

$$-\frac{1}{2} \left[ \frac{n}{s^2} (\mu - \bar{x})^2 + \frac{1}{\sigma_0^2} (\mu - \mu_0)^2 \right] = -\frac{1}{2} \left( \frac{n}{s^2} + \frac{1}{\sigma_0^2} \right) (\mu - \hat{\mu}_{post})^2 + \text{constante},$$

al completar el cuadrado, con $\hat{\mu}_{post} = w \bar{x} + (1 - w) \mu_0$ y $w$ como en la sección 3.1. Es una densidad normal cuya precisión, $n / s^2 + 1 / \sigma_0^2$, es la suma de las dos precisiones, y cuya desviación es $\sigma_{post}$.

**Eficiencia en la Cauchy.** Para muestras grandes, la varianza de la mediana muestral es aproximadamente $1 / (4 n f(x_0)^2)$, que en la Cauchy, con $f(x_0) = 1 / (\pi \gamma)$, es $\pi^2 \gamma^2 / (4n) \approx 2.47 \gamma^2 / n$; la del estimador de máxima verosimilitud del centro es $2 \gamma^2 / n$, alrededor de 20% menor. La sustitución sirve con cualquier distribución; la máxima verosimilitud paramétrica aprovecha la forma supuesta, y si la forma no es razonable, esa ventaja se convierte en error de especificación. Ninguna de las dos estima lo que la distribución no tiene: con datos Cauchy, la media muestral se puede calcular, pero no estima nada, porque la esperanza no existe.

**La hipótesis conjunta.** Para probar si un mercado es eficiente en el sentido de Fama (1970) hace falta un modelo del rendimiento que se esperaría sin información nueva; si la prueba rechaza, no se sabe si el mercado no es eficiente o si ese modelo no era razonable. El error de especificación no se puede separar de la pregunta.

## Fuentes y referencias recomendadas

- Linton, O. (2019). *Financial Econometrics: Models and Methods*. Cambridge University Press: estimación de la media y la volatilidad, autocorrelación y regresión con rendimientos.
- Damodaran, A. (2026). *Historical Returns on Stocks, Bonds and Bills: 1928-2025*. NYU Stern School of Business. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html: rendimientos anuales del S&P 500 con dividendos.
- Yahoo Finance. (2026). *S&P 500 (^GSPC), FEMSA (FEMSAUBD.MX) y NAFTRAC (NAFTRAC.MX), historial de precios* [datos]. https://finance.yahoo.com: cierres diarios del S&P 500 desde 1927 y cierres mensuales de FEMSA y NAFTRAC desde 2020, consultados el 24 de octubre de 2026.
- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 17, 21-86: primer modelo probabilístico de los precios de mercado.
- Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, 7(1), 77-91: el modelo de media y varianza.
- Gordon, M. J. (1959). Dividends, earnings, and stock prices. *The Review of Economics and Statistics*, 41(2), 99-105: el modelo de dividendos crecientes.
- Mandelbrot, B. (1963). The variation of certain speculative prices. *The Journal of Business*, 36(4), 394-419: las colas pesadas de los cambios de precio.
- Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. *The Journal of Finance*, 19(3), 425-442: el CAPM.
- Fama, E. F. (1970). Efficient capital markets: A review of theory and empirical work. *The Journal of Finance*, 25(2), 383-417: la eficiencia del mercado y la hipótesis conjunta.
- Black, F., y Litterman, R. (1992). Global portfolio optimization. *Financial Analysts Journal*, 48(5), 28-43: la combinación bayesiana del equilibrio del mercado con las opiniones de los analistas.
- Basel Committee on Banking Supervision. (1996). *Amendment to the Capital Accord to incorporate market risks*. Bank for International Settlements: el VaR como base del capital por riesgo de mercado.
