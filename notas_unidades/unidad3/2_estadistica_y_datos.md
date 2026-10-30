# Unidad 3 · Estadística y Datos

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante construya un intervalo de confianza para el rendimiento esperado de un activo a partir de sus rendimientos históricos.

## Contenido

|     | Tema                                    | Qué cubre                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I   | Contexto                                | Los datos y el modelo: probabilidad deductiva y estadística inductiva, el ciclo de descubrimiento del conocimiento, datos observacionales, población, muestreo aleatorio simple y muestra aleatoria, la serie de tiempo, los datos como una realización suya y el ruido blanco; modelo paramétrico, de localización y escala, no paramétrico, semiparamétrico o bayesiano, su especificación e identificación, con modelos clásicos de finanzas; la inferencia y sus problemas: estimación, intervalo de confianza y prueba de hipótesis |
| II  | Describir los datos                     | Histograma, media, desviación estándar y media geométrica de los 98 rendimientos anuales del S&P 500; distribución empírica, cuantil empírico y VaR y CVaR históricos; covarianza y correlación muestrales de FEMSA frente al S&P 500 y frente a un ruido blanco                                                                                                                                                                                                                                                                         |
| III | Estimadores                             | El estimador como variable aleatoria y la media muestral como un portafolio de los años; principios de estimación: sustitución, verosimilitud de Fisher y Bayes; el VaR y un límite de pérdidas con la normal, la Cauchy y los datos; sesgo, media muestral y error estándar $s/\sqrt{n}$                                                                                                                                                                                                                                                |
| IV  | Del estimador al intervalo de confianza | Consistencia: convergencia en probabilidad, desigualdad de Chebyshev, ley de los grandes números y Glivenko-Cantelli; la forma de la distribución: convergencia en distribución, teoremas central del límite y de Slutsky; intervalo de confianza al 95% para el rendimiento esperado, de 8.01% a 15.70%, y por remuestreo para el CVaR; la dinámica de la bolsa del S&P 500 y su notebook                                                                                                                                               |

> La práctica de este tema es la dinámica de la sección 4.4, en el notebook [`bolsa_sp500.ipynb`](codigo/bolsa_sp500.ipynb).

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

**Definición (población).** La **población** es la distribución $F_X$ de la variable aleatoria $X$ que interesa, como el rendimiento anual del S&P 500: la que generó los datos y que no se conoce. Si hay una lista finita de unidades, como las emisoras de la BMV, la población es la propia lista, y $F_X$ es la distribución del rendimiento por dividendos de una emisora elegida al azar; con los rendimientos de un índice no hay una lista de la cual elegir, y la población es solo esa distribución.

Para aprender algo de ella se usa una **muestra**, $n$ variables aleatorias

$$X_1, X_2, \dots, X_n,$$

y los números que toman, $x_1, \dots, x_n$, son la **muestra observada**, los datos. En la práctica a las dos se les llama muestra.

Detrás de toda muestra hay dos procesos:

- El primero genera los datos. Son **experimentales** si quien investiga interviene, como al probar dos precios con clientes elegidos al azar, y **observacionales** si solo registra lo que ocurrió; en finanzas casi todo es observacional, porque nadie le asigna a una empresa su política de dividendos para ver qué pasa.
- El segundo proceso es el **muestreo**, la regla con que se eligen las observaciones. De esa regla depende lo que la muestra permite concluir: si favorece a ciertos datos, la estimación hereda ese sesgo, y más datos no lo corrigen.

Un modelo de los datos tiene que describir los dos procesos: lo que se sabe del mercado y la regla con que se eligieron las observaciones.

> **¿De dónde sale la fórmula?** Si las observaciones son independientes, la probabilidad de que todas caigan donde caen es el producto de las probabilidades de cada una, como $P(A \cap B) = P(A) P(B)$ en la sección 3.3 de la nota anterior.

**Definición (muestra aleatoria).** $X_1, \dots, X_n$ son una **muestra aleatoria** de $X$ si son independientes y cada una tiene la misma distribución que $X$ (independientes e idénticamente distribuidas, iid). Su distribución conjunta es entonces

$$F_{X_1, \dots, X_n}(x_1, \dots, x_n) = F_X(x_1) F_X(x_2) \cdots F_X(x_n).$$

Es el supuesto con el que la sección 3 calcula la media muestral y su error estándar. Los tipos de muestreo más simples son cuatro:

| Tipo                                | Cómo se eligen las observaciones                                                     | Ejemplo en finanzas                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Aleatorio simple                    | Al azar y sin reemplazo: cualquier grupo de $n$ unidades tiene la misma probabilidad | Sortear 30 emisoras de la BMV para estimar su rendimiento por dividendos promedio                       |
| Estratificado (stratified sampling) | Se divide la población en grupos, los estratos, y se sortea dentro de cada uno       | Un ETF de bonos que no compra todos los títulos de su índice, sino una muestra por plazo y calificación |
| Sistemático                         | Cada $k$-ésima unidad, o a intervalos fijos de tiempo                                | Los cierres diarios, de fin de mes o de fin de año del S&P 500                                          |
| Por conveniencia (no aleatorio)     | Las que están a la mano                                                              | Solo las emisoras que siguen cotizando hoy, con su sesgo de supervivencia (survivorship bias, nota 0_)  |

En el muestreo aleatorio simple, una emisora que ya salió no vuelve a salir, y cada sorteo cambia lo que queda: las observaciones tienen la misma distribución, pero no son independientes, así que no forman una muestra aleatoria. Si la muestra es menos del 5% de la lista, el efecto es pequeño y se puede tratar como una. Las 30 emisoras de la tabla no cumplen esa regla, porque la BMV tiene muchas menos de las 600 que harían falta.

Con los rendimientos de un índice no se sortea nada: el mercado produce una sola sucesión, y lo único que se elige es la frecuencia y el periodo, **un muestreo sistemático en el tiempo de datos observacionales**. Para tratar esa sucesión como una muestra aleatoria hace falta un supuesto más.

Los rendimientos se modelan como una **serie de tiempo**, una sucesión de variables aleatorias indexadas por el tiempo,

$$\{X_t\}_{t=1}^{T} = X_1, X_2, \dots, X_T,$$

donde $X_t$ es el rendimiento del índice en el año $t$.

> Ejemplo: Los rendimientos del S&P 500 son una serie de tiempo que va de 1928 ($t = 1$) a 2025 ($t = T = 98$). Como en la nota anterior, la mayúscula $X_t$ es la variable aleatoria antes de observarla y la minúscula $x_t$ el número observado, como $x_4 = -43.84\%$ en 1931. La historia ocurrió una sola vez: $x_1, \dots, x_{98}$ son una realización de la serie, una de las muchas trayectorias que el mercado pudo haber seguido. Tratarlos como 98 observaciones del mismo fenómeno exige suponer que la distribución de $X_t$ no cambia con $t$ (estacionariedad, stationarity), un supuesto que la nota 3_ revisa.

Si además los rendimientos de años distintos son independientes, la serie es una muestra aleatoria. La independencia también se lee como condicional: como $P(A \mid B) = P(A)$ para eventos independientes (sección 3.3 de la nota anterior), saber dónde cayó un año no cambia la distribución de otro, $P(X_{t+1} \leq x \mid X_t = x_t) = F_X(x)$. Que 1931 perdiera $43.84\%$ no dice nada de 1932; la nota 3_ lo revisa con la autocorrelación.

**Definición (ruido blanco).** Un **ruido blanco** es una sucesión $\varepsilon_1, \varepsilon_2, \dots$ de variables aleatorias independientes con la misma distribución, media 0 y varianza constante: ningún valor dice nada de los demás.

> **¿De dónde sale la fórmula?** Si $X_t$ tiene media $\mu$ y desviación estándar $\sigma$, al restarle $\mu$ queda con media 0, y al dividirla entre $\sigma$ su desviación estándar también se divide entre $\sigma$ y queda en 1. Esa variable estandarizada es $\varepsilon_t = (X_t - \mu) / \sigma$; al despejar $X_t$ sale la fórmula, y si las $X_t$ son iid, las $\varepsilon_t$ también.

Una serie iid con media $\mu$ y desviación estándar $\sigma$ es entonces una constante más un ruido blanco de varianza 1,

$$X_t = \mu + \sigma \varepsilon_t:$$

$\mu$ es lo que se espera cada año y $\sigma \varepsilon_t$, la sorpresa. En el S&P 500, la media de $11.86\%$ estima $\mu$, y $s = 19.40\%$ estima $\sigma$, el tamaño típico de la sorpresa. Con esta forma se simula el ruido de la sección 2.3 y se escribe la regresión de la nota 3_.

Obtener buenos datos en finanzas es difícil por los dos procesos.

- Del lado del **proceso generador**, no se puede experimentar ni repetir la historia, y el mecanismo cambia mientras se observa: cambian la regulación, la tecnología, las empresas que forman el índice y hasta los inversionistas, que reaccionan a lo que publican otros, de modo que un patrón que se vuelve conocido tiende a desaparecer cuando se aprovecha. Además, la señal es débil frente al ruido: el rendimiento promedio del S&P 500, $11.86\%$, es pequeño frente a la dispersión de un solo año, $19.40\%$, así que hacen falta muchos años para estimarlo, y los eventos extremos, los que más importan para el riesgo, son los que menos se observan.
- Del lado del **muestreo y el registro**, las bases suelen guardar solo a las empresas que sobrevivieron; el precio de una acción poco operada puede ser el de una operación de hace días; hay que ajustar por dividendos y por divisiones de acciones para no confundir un reparto con una pérdida; un promedio mensual de cierres diarios, como el de la serie de Shiller, crea una autocorrelación que no existe, y hasta las fechas pueden venir mal: en los precios mensuales de FEMSA que usa la sección 2.3, el cambio de horario corrió las etiquetas de algunos meses entre 2020 y 2022.

Por último, como solo hay una historia, quien prueba muchas estrategias con los mismos datos termina encontrando alguna que funcionó por suerte, el riesgo del trabajo de exploración que se presenta como confirmación. Oliver Linton (2019) bromea que los datos son el plural de las anécdotas: el $-43.84\%$ de 1931 es una anécdota y 98 años juntos son datos. Advierte que una sola observación extrema, como el desplome de octubre de 1987, puede pesar demasiado en una estimación, y que la crisis de 2008 dejó escepticismo sobre lo que la econometría puede predecir "y, ojalá, algo de humildad".

<!-- diapositivas: conservar -->
- **Probabilidad (nota 1_):** con el modelo conocido se calculan $E[R]$, $\sigma$, el VaR y el CVaR.
- **Estadística:** con los datos se estiman $E[R]$, $\sigma$, el VaR y el CVaR (estos dos, con el IPC en la nota 4_), y se mide qué tan lejos pueden estar de los parámetros del modelo.
- **Los datos como realización:** 98 rendimientos son una de muchas trayectorias posibles; suponer que la distribución no cambia en el tiempo y que los años son independientes permite tratarlos como una muestra aleatoria, $X_t = \mu + \sigma \varepsilon_t$.
- **Reconocer lo que no sabemos:** el promedio de 98 años, $11.86\%$, es solo una estimación de $E[R]$; con otra historia del mercado habría salido otro número. Por eso la respuesta es un intervalo, de $8.01\%$ a $15.70\%$ al 95% de confianza, que dice cuánto puede alejarse la estimación del rendimiento esperado. Suele ser más angosto cuanto más datos hay y cuanto menos dispersos son los rendimientos.

#### 1.3 Los modelos

Suponiendo que tenemos los datos, ¿qué hacemos con ellos?

**Definición (modelo).** Un **modelo** es la colección $\mathcal{M}$ de distribuciones que se consideran posibles para los datos $X_1, X_2, \dots$: las candidatas a ser la población.

Un modelo puede ser muy general, como "cualquier distribución con varianza finita", o simplificarse con más supuestos, y cada supuesto deja fuera distribuciones.

> Ejemplo: Los rendimientos de activos de participación de capital en sociedades de responsabilidad limitada están limitados a $-100\%$. Esto elimina muchos modelos que asignan probabilidades positivas a valores más chicos que $-100\%$. Entonces, se dice que esos modelos no son razonables.

Un concepto que ayuda a restringir considerablemente el espacio de modelos en cuestión es el de parámetro.

**Definición (parámetro).** Un **parámetro** es una característica numérica de la distribución, $\theta = T(F_X)$: la esperanza $\mu$, la desviación estándar $\sigma$, un cuantil $q_p$ como el VaR o la probabilidad de perder, $P(X < 0)$. Existe en cualquier modelo, general o no, y es lo que la estadística trata de estimar.

**Definición (modelo paramétrico).** Un modelo es **paramétrico** si un número fijo de parámetros $\theta = (\theta_1, \dots, \theta_k)$ basta para determinar la distribución completa:

$$\mathcal{M} = \{ F(x; \theta) : \theta \in \Theta \},$$

donde $\Theta$, el **espacio paramétrico**, es el conjunto de valores posibles de los parámetros. Se escribe $X \sim F(x; \theta)$, que se lee "$X$ se distribuye como $F(x; \theta)$": quien conoce $\theta$ conoce la distribución completa. El rendimiento normal es el ejemplo más usado: $\theta = (\mu, \sigma)$, con $\Theta = \mathbb{R} \times (0, \infty)$. El modelo de escenarios de la nota anterior también lo es, con las tres probabilidades como parámetros.

Muchos modelos paramétricos de rendimientos tienen la forma $X = \mu + \sigma \varepsilon$ de la sección 1.2 con la distribución de $\varepsilon$ fija, y se llaman de **localización y escala**: $\mu$ mueve la distribución y $\sigma$ la estira. Sus cuantiles se mueven igual: si $z_p$ es el cuantil de $\varepsilon$, el de $X$ es $q_p = \mu + \sigma z_p$, como en la sección 6.1 de la nota anterior con la normal. Así sale el VaR al 99% de la sección 1.1: con $\mu = 0$ y $z_{0.01} = -2.326$, $q_{0.01} = -2.326 \times 1.2\% = -2.79\%$.

> Ejemplo: El modelo paramétrico más simple es el de Bernoulli. Si $D = 1$ cuando el S&P 500 pierde en el año y $D = 0$ cuando no, **la distribución de $D$ queda determinada por un solo parámetro, la probabilidad de perder $p = P(D = 1) = P(X < 0)$**, con $\Theta = (0, 1)$. Con $D = 1$ si el deudor no paga, es el modelo del incumplimiento de la sección 3.1 de la nota anterior y de la tabla de modelos clásicos, al final de esta sección.

**Definición (modelo no paramétrico).** Un modelo es **no paramétrico** si ningún número fijo de parámetros determina la distribución, como cuando $\mathcal{M}$ contiene todas las distribuciones, o casi todas. Los parámetros siguen existiendo, la esperanza o el VaR, pero cada uno se estima por separado, a partir de la distribución empírica.

El VaR histórico es el ejemplo: no supone ninguna forma y lee el cuantil de los datos ordenados. Su costo es que necesita muchos datos donde hay pocos. **Con los 98 rendimientos anuales del S&P 500, el VaR al 99% está en la posición $\lceil 98 \times 0.01 \rceil = 1$: descansa en un solo dato, el peor año, 1931, con $-43.84\%$.** Con los 24,803 rendimientos diarios está en la posición 249, y quedan 248 días más allá del cuantil para describir la cola.

Entre los dos están los modelos **semiparamétricos**, que fijan la forma de una parte del modelo y dejan libre el resto. En la regresión del CAPM, $R_i = \alpha + \beta R_m + \varepsilon$, la relación con el mercado es paramétrica, con $\alpha$ y $\beta$, pero la distribución del error $\varepsilon$, un ruido como el de la sección 1.2, queda libre (nota 3_). En la teoría de valores extremos (extreme value theory), el VaR de una cola muy lejana se calcula suponiendo una forma solo para la cola, la de Pareto, justo donde faltan datos, y se deja libre el centro de la distribución.

Todos estos modelos tratan al parámetro como un número fijo que no conocemos. El enfoque **bayesiano** agrega una pieza: lo que se cree sobre el parámetro antes de ver los datos, expresado como una distribución. En vez de decir "no sé cuánto vale el rendimiento esperado $\mu$ del S&P 500", un analista dice "probablemente está cerca de $8\%$, y rara vez fuera del rango de $4\%$ a $12\%$".

**Definición (modelo bayesiano).** Un **modelo bayesiano** tiene dos piezas, un modelo paramétrico para los datos y una **distribución a priori** $g(\theta)$ sobre los valores posibles $\Theta$ del parámetro:

$$X_1, \dots, X_n \mid \theta \sim F(x; \theta), \qquad \theta \sim g(\theta),$$

donde $\mid$ se lee "dado". Es decir: si el parámetro valiera $\theta$, los datos tendrían la distribución $F(x; \theta)$; antes de verlos, $\theta$ es incierto, con distribución $g$.

Con los datos, la a priori se actualiza a una **a posteriori**. La sección 3.1 lo hace con el analista: **su opinión de $8\% \pm 2\%$ y los 98 años del S&P 500 dan $9.97\%$.** Es la manera formal de meter al modelo el conocimiento del mercado, con el costo de que la a priori es un supuesto más que hay que justificar.

La elección es un intercambio. Si la forma supuesta es razonable, el modelo paramétrico aprovecha mejor pocos datos; si no lo es, carga con su error. El no paramétrico supone menos, pero pide muchos más datos, sobre todo en las colas de la distribución.

Los dos extremos de esa elección son $\mathcal{M} = \{G\}$, una sola distribución conocida, que es la probabilidad de la nota anterior, y $\mathcal{M}$ con todas las distribuciones, el VaR histórico. En medio, cada familia paramétrica es un hilo de distribuciones, recorrido por $\theta$, dentro de todas las posibles: la normal es uno, la Cauchy de la sección 3.2 es otro, y la población de los rendimientos diarios del S&P 500 no está en ninguno de los dos.

Elegir la familia $\mathcal{M}$ y los supuestos que la acompañan es **especificar** el modelo. Los supuestos son de dos tipos: **estructurales**, cómo se relacionan las observaciones entre sí, como que los rendimientos de años distintos sean independientes y con la misma distribución, o solo que no estén correlacionados; y **distribucionales**, cuál es la distribución de cada una, como la normal. La diferencia entre independientes y no correlacionados importa: los rendimientos diarios casi no están correlacionados, pero no son independientes, porque los días de mucha volatilidad se agrupan (nota 3_). Los datos solos no deciden la especificación; la mayor parte viene del conocimiento del mercado. Un modelo no es correcto ni equivocado: es una simplificación, más o menos razonable para el uso que se le da. Uno bueno es consistente con lo que se sabe del fenómeno, se comporta bien en los casos extremos y tiene parámetros con una interpretación clara. Hay un **error de especificación** cuando la población no está en el modelo, $F_X \notin \mathcal{M}$, porque sus supuestos se alejan de los datos o de lo que se sabe del mercado. Más datos no lo corrigen: el estimador sigue respondiendo la pregunta del modelo, no la del mercado. Pesa sobre todo en los modelos paramétricos, pero el no paramétrico también supone algo: que los datos son independientes y que su distribución no cambia en el tiempo (sección 1.2). En sentido estricto casi ningún modelo contiene a la población: la normal admite pérdidas de más de $100\%$, aunque con los datos anuales del S&P 500 les da una probabilidad de cuatro en mil millones. Lo que importa es qué tan lejos queda la población del modelo.

Los modelos clásicos de las finanzas muestran el mismo patrón: el conocimiento del mercado fija la forma del modelo, y la estadística estima los parámetros que quedan.

| Modelo                               | Lo que aporta el contexto                                                      | Qué se estima con datos                    |
| ------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------ |
| Caminata aleatoria, Bachelier (1900) | Si los cambios de precio fueran predecibles, alguien ya los habría aprovechado | Media y desviación estándar de los cambios |
| Media y varianza, Markowitz (1952)   | Al inversionista le importan la ganancia esperada y su dispersión              | $E[R]$, $\sigma$ y covarianzas             |
| CAPM, Sharpe (1964)                  | Solo se paga el riesgo que no se elimina diversificando                        | La beta, pendiente de una regresión        |
| Dividendos crecientes, Gordon (1959) | El dividendo crece a una tasa $g$ menor que el rendimiento requerido $r$       | La prima de riesgo dentro de $r$, y $g$    |
| VaR normal, Basilea (1996)           | Los bancos deben reservar capital contra la pérdida de un día malo             | $\sigma$ y el cuantil al 99%               |
| Incumplimientos independientes       | Cada deudor paga o no paga por su cuenta                                       | La probabilidad de incumplimiento          |

No todo parámetro de un modelo se puede estimar con datos. Un modelo es **identificable** si parámetros distintos dan distribuciones distintas para los datos; si dos valores de $\theta$ producen los mismos datos, ninguna cantidad de datos los distingue.

> **¿De dónde sale la fórmula?** En el modelo de Gordon, el precio de una acción es el valor presente de sus dividendos: $d_1$ el próximo año, cada uno $g$ más grande que el anterior, descontados a la tasa requerida $r$. La suma $\sum_{t=1}^{\infty} d_1 (1 + g)^{t-1} / (1 + r)^t$ es una serie geométrica de razón $(1 + g) / (1 + r)$, que si $g < r$ suma $d_1 / (r - g)$ (nota 5_).

**Ejemplo (Gordon no separa $r$ de $g$).** En el modelo de Gordon, el precio de una acción es $v_0 = d_1 / (r - g)$, con $g < r$, y solo depende de la diferencia $r - g$. Con precios y dividendos se estima el rendimiento por dividendos, $d_1 / v_0 = r - g$, pero no $r$ y $g$ por separado: **$r = 10\%$ con $g = 6\%$ y $r = 8\%$ con $g = 4\%$ dan el mismo precio.** Por eso la tabla separa los dos: para estimar la prima de riesgo dentro de $r$ hace falta estimar $g$ con otra fuente, como el crecimiento de las utilidades.

<!-- diapositivas: conservar -->
- **Tipos de modelo:** una familia $\{F(x; \theta)\}$ fijada por unos cuantos parámetros, como la normal; casi todas las distribuciones, como en el VaR histórico; o forma solo en una parte, como la beta del CAPM; el bayesiano agrega una distribución a priori sobre los parámetros. El primero rinde más con pocos datos si es razonable, el segundo supone menos pero pide más datos.
- **Especificar:** elegir la familia de distribuciones y sus supuestos; lo decide sobre todo el conocimiento del problema. Un modelo no es correcto ni equivocado, sino más o menos razonable.
- **Buen modelo:** consistente con el contexto, bien comportado en los extremos y con parámetros interpretables.
- **Error de especificación:** la población no está en el modelo, $F_X \notin \mathcal{M}$; más datos no lo corrigen.

#### 1.4 Los problemas de la inferencia

Con los datos y un modelo, el trabajo que sigue es la inferencia.

**Definición (inferencia).** La **inferencia** es el proceso de obtener conclusiones sobre la población a partir de la muestra observada.

Rara vez interesa la población completa: interesa una propiedad suya, casi siempre un parámetro, como el rendimiento esperado o la probabilidad de perder. Las conclusiones son inciertas porque poblaciones distintas pudieron generar los mismos datos, y la pregunta se puede plantear de varias formas, cada una con su manera de medir esa incertidumbre:

| Problema                  | Qué busca                                                         | Ejemplo en finanzas                                            |
| ------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------- |
| Estimación puntual        | Un número para el parámetro                                       | El rendimiento esperado del S&P 500, $11.86\%$ (sección 3)     |
| Intervalo de confianza    | Un rango que atrapa al parámetro con una probabilidad fijada      | De $8.01\%$ a $15.70\%$ al 95% (sección 4)                     |
| Prueba de hipótesis       | Qué tan fuerte es la evidencia de los datos contra una hipótesis  | ¿Pierde el mercado la mitad de los años?                       |
| Regresión                 | Cómo cambia, en promedio, una variable con otra                   | La beta del CAPM (nota 3_)                                     |
| Clasificación             | A cuál de varios grupos conocidos pertenece una observación nueva | Si una emisora incumplirá, a partir de sus razones financieras |
| Agrupamiento (clustering) | Qué grupos hay, sin conocerlos de antemano                        | Acciones que se mueven juntas, más allá de su sector           |
| Selección y ordenamiento  | Cuál de varias poblaciones tiene el mejor parámetro               | Cuál de 20 fondos tiene el mayor rendimiento esperado          |

Esta nota resuelve los dos primeros, y la nota 3_, la regresión.

La **estimación puntual** da una buena propuesta para la cantidad de interés con base en la muestra. Esa cantidad suele ser un parámetro, pero también puede ser la distribución completa, un cuantil como el VaR o el valor futuro de una variable, como el rendimiento del próximo año. Toda estimación tiene un **error de estimación**, $\hat{\theta} - \theta$, que no se conoce porque el parámetro tampoco; la sección 3 mide su tamaño típico.

Un **intervalo de confianza** dice lo que la estimación puntual no dice: qué tan precisa es. Es un intervalo calculado con la muestra que contiene al parámetro con una probabilidad fijada de antemano, su **nivel de confianza**, como 95%. Lo aleatorio es el intervalo, que cambia de una historia a otra, y el parámetro es fijo: "de $8.01\%$ a $15.70\%$ al 95%" quiere decir que el método que lo produjo atrapa al rendimiento esperado en 95 de cada 100 historias posibles, no que $\mu$ tenga 95% de probabilidad de estar ahí.

Una **prueba de hipótesis** mide qué tan fuerte es la evidencia de los datos contra una hipótesis $H$ sobre el parámetro.

> Ejemplo: Si el mercado fuera una moneda, un año de pérdida sería tan probable como uno de ganancia: en el modelo de Bernoulli de la sección 1.3, $H: p = 1/2$. Con esa hipótesis se esperarían unos 49 de los 98 años con pérdida, y hubo 26. **Si $p = 1/2$, ver 26 pérdidas o menos en 98 años independientes ocurriría en unas 2 de cada millón de historias** (Apéndice): los datos contradicen la hipótesis.

Ninguna hipótesis es literalmente cierta: es una aproximación a la realidad, útil si predice bien. Con suficientes datos, la evidencia contra cualquier hipótesis termina por acumularse, como contra cualquier modelo (sección 1.3), así que la pregunta no es si es verdadera, sino si los datos la contradicen lo suficiente para dejar de usarla.

Cada problema mide la incertidumbre a su manera, y confundirlos hace perder ese control. Si se elige el mejor de 20 fondos por su promedio histórico y después se reporta su intervalo al 95% como si fuera el único fondo analizado, el intervalo promete más de lo que da: el fondo ganador es, en parte, el que tuvo más suerte, el mismo riesgo de quien prueba muchas estrategias con una sola historia (sección 1.2).

Antes de estimar conviene ver los datos. La sección 2 los describe con el histograma, la media y la desviación estándar, que en un trabajo de exploración sugieren el modelo (sección 1.1) y son el punto de partida de los estimadores de la sección 3.

### 2. Describir los datos

Los datos $x_1, \dots, x_n$ son una realización de la muestra $X_1, \dots, X_n$ (sección 1.2). Un **estadístico** es una función de la muestra, $g(X_1, \dots, X_n)$, que no depende de ningún parámetro desconocido; con los datos da un número, $g(x_1, \dots, x_n)$, como el promedio. Describir no necesita un modelo: los estadísticos de esta sección dicen qué pasó, y leerlos como estimaciones de los parámetros es el trabajo de la sección 3. Cada uno es la versión con datos de algo que en la nota anterior se calculaba con el modelo:

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

La media es el promedio de los datos y $s$ mide qué tan lejos de la media caen típicamente. Las desviaciones se miden respecto a $\bar{x}$ porque $\mu$ no se conoce, y una fórmula con $\mu$ no sería un estadístico; se divide entre $n - 1$ y no entre $n$ porque $\bar{x}$ queda más cerca de los datos que $\mu$, una razón de estimación que retoma la sección 3.3 (Apéndice); con 98 datos, la diferencia es de medio por ciento.

**Ejemplo (los 98 rendimientos del S&P 500).** Con intervalos de 10 puntos, 81 de los 98 años quedan entre $-10\%$ y $40\%$, y el intervalo más poblado es el de $10\%$ a $20\%$, con 21 años. La cola izquierda está más poblada que la derecha: 12 años perdieron más de $10\%$ y solo 5 ganaron $40\%$ o más. La media y la desviación estándar son

$$\bar{x} = 11.86\%, \qquad s = 19.40\%.$$

En la figura, 65 de los 98 años (66%) caen a una desviación estándar de la media, entre $-7.55\%$ y $31.26\%$, y 94 (96%) a dos. Una normal tendría 68% y 95%, así que con datos anuales el histograma se parece bastante a una normal; la nota 3_ muestra que con datos diarios no.

La línea roja es la **media geométrica**,

$$\left( \prod_{t=1}^{n} (1 + x_t) \right)^{1/n} - 1 = 10.02\%,$$

el rendimiento constante que habría dejado la misma riqueza final que la historia real (sección 4.3 de la nota anterior). Queda 1.84 puntos por debajo de la media porque una pérdida pesa más que una ganancia del mismo tamaño: perder 20% y luego ganar 20% deja 96 de cada 100 pesos. Cuanto más dispersos son los rendimientos, mayor es la brecha; aproximadamente, la media geométrica es $\bar{x} - s^2/2 = 9.98\%$ (Apéndice). La media dice cuánto se espera ganar en un año; la media geométrica, cuánto creció el dinero que se quedó invertido los 98 años.

<!-- diapositivas: figura sola -->
![Histograma de los 98 rendimientos anuales del S&P 500 con dividendos entre 1928 y 2025, en barras de 10 puntos de ancho desde -50% hasta 60%; una línea dorada marca la media de 11.86%, una línea roja de rayas y puntos marca la media geométrica de 10.02%, un poco a su izquierda, y una franja dorada clara, entre líneas punteadas en -7.55% y 31.26%, marca una desviación estándar de 19.40% a cada lado, con la leyenda 65 de 98 años dentro de la franja](img/sp500_histograma_media_desviacion.png)

#### 2.2 Distribución empírica y cuantiles

El VaR de la nota anterior es un cuantil del modelo. Con datos, el cuantil se lee de los datos ordenados.

**Definición (distribución empírica y cuantil empírico).** La **distribución empírica** $\hat{F}_n$ asigna probabilidad $1/n$ a cada dato observado. Su función de distribución es la proporción de datos que no pasan de $x$,

$$\hat{F}_n(x) = \frac{\text{número de datos } x_t \leq x}{n},$$

y el **cuantil empírico** es su cuantil, con la misma definición de la sección 6.1 de la nota anterior: $\hat{q}_p = \min\{x : \hat{F}_n(x) \geq p\}$. Con los datos ordenados del menor al mayor, es el dato en la posición $\lceil np \rceil$, el primer entero mayor o igual que $np$. El **VaR histórico** es la pérdida que marca ese cuantil, y el **CVaR histórico**, el promedio de los datos que quedan en él o por debajo.

**Ejemplo (VaR histórico del S&P 500).** Con $n = 98$ y $p = 0.05$, $np = 4.9$, así que $\hat{q}_{0.05}$ es el quinto peor año: 1930, con $-25.12\%$. **El VaR histórico anual al 95% es una pérdida de $25.12\%$**; con 10,000 pesos, 2,512 pesos. El CVaR histórico es el promedio de los cinco peores años,

$$\frac{-43.84\% - 36.55\% - 35.34\% - 25.90\% - 25.12\%}{5} = -33.35\%:$$

en el peor año de cada veinte se perdió, en promedio, $33.35\%$. La misma $\hat{F}_n$ dice cuántos años perdieron: $\hat{F}_n(0) = 26/98 = 26.5\%$, uno de cada cuatro.

#### 2.3 Covarianza y correlación

**Definición (covarianza y correlación muestrales).** Con dos series observadas en los mismos periodos, $x_t$ y $y_t$, la **covarianza muestral** y la **correlación muestral** son

$$s_{xy} = \frac{1}{n-1} \sum_{t=1}^{n} (x_t - \bar{x})(y_t - \bar{y}), \qquad \hat{\rho}_{x,y} = \frac{s_{xy}}{s_x s_y}.$$

Se leen igual que en la sección 5.2 de la nota anterior: cada producto es positivo cuando las dos series quedan del mismo lado de su media, y negativo cuando quedan de lados opuestos.

**Ejemplo (FEMSA frente al S&P 500).** FEMSA es una de las empresas más grandes de la bolsa mexicana, y el S&P 500 resume el mercado accionario de Estados Unidos. Con los 80 rendimientos mensuales de febrero de 2020 a septiembre de 2026, $x_t$ para el S&P 500, con sus cierres de fin de mes en dólares y sin dividendos, y $y_t$ para FEMSA, con precios ajustados por dividendos:

$$s_x = 4.89\%, \qquad s_y = 6.35\%, \qquad s_{xy} = 0.000981, \qquad \hat{\rho}_{x,y} = \frac{0.000981}{0.0489 \times 0.0635} = 0.32.$$

En el panel izquierdo de la figura, la nube se inclina hacia arriba a la derecha, pero poco: FEMSA tiende a subir cuando sube el mercado estadounidense, lejos de una línea recta. Una parte de su riesgo la comparte con los mercados de todo el mundo, como la caída de marzo de 2020, el punto de abajo a la izquierda; otra es propia de México y de la emisora.

Para saber cuánto es 0.32 conviene ver cómo luce la falta de relación: un ruido blanco (sección 1.2), en el que ningún valor dice nada de los demás. El panel derecho simula dos ruidos blancos independientes y normales, con las desviaciones estándar del S&P 500 y de FEMSA, 80 pares en la misma escala; su correlación muestral es 0.03. Contar puntos no los distingue: 40 de los 80 meses reales quedan del mismo lado de las medias, y 48 de los 80 pares simulados. Lo que los distingue es el tamaño de los productos $(x_t - ar{x})(y_t - ar{y})$: en los datos, los meses de movimientos grandes, como marzo y noviembre de 2020, caen del mismo lado y pesan mucho en la covarianza; en el ruido blanco, los productos grandes se reparten entre positivos y negativos y se cancelan.

<!-- diapositivas: figura sola -->
![Dos diagramas de dispersión lado a lado, en la misma escala, cada uno con una línea vertical y una horizontal en las medias que dividen el plano en cuatro cuadrantes, puntos dorados del mismo lado de las dos medias y grises en lados opuestos. A la izquierda, 80 rendimientos mensuales de febrero de 2020 a septiembre de 2026, con el S&P 500 en el eje horizontal y FEMSA en el vertical: 40 puntos dorados y 40 grises en una nube poco inclinada, con un punto aislado abajo a la izquierda, marzo de 2020, y otro arriba a la derecha; el título indica una correlación de 0.32. A la derecha, 80 pares simulados de dos ruidos blancos normales e independientes, con media 0 y las desviaciones estándar del S&P 500 y de FEMSA: 48 puntos dorados y 32 grises en una nube redonda sin inclinación; el título indica una correlación de 0.03](img/femsa_sp500_ruido_blanco_dispersion.png)

### 3. Estimadores

Los estadísticos de la sección 2 describen la única historia que ocurrió; usados para aproximar los parámetros del modelo, son estimadores. Esta sección dice de dónde salen (3.1), cuándo conviene estimar con un modelo o con los datos (3.2) y qué tan lejos pueden quedar del parámetro (3.3), la distancia que la sección 4 convierte en un intervalo.

**Definición (estimador y estimación).** Un **estimador** es un estadístico que se usa para aproximar un parámetro. Como depende de las variables aleatorias $X_1, \dots, X_n$, el estimador también es una variable aleatoria. Una **estimación** es el número que da con los datos observados: mayúscula antes de observar, minúscula después.

**Ejemplo (la media y la varianza muestrales como un portafolio).** Supongamos que $X_t$ es el rendimiento de un activo de capital, como el S&P 500, en el año $t$. Los estimadores más usados son los de su esperanza $\mu$ y su varianza $\sigma^2$: las fórmulas de la sección 2.1, escritas con las variables aleatorias,

$$\bar{X} = \frac{1}{n} \sum_{t=1}^{n} X_t, \qquad S^2 = \frac{1}{n-1} \sum_{t=1}^{n} (X_t - \bar{X})^2.$$

Con los 98 años del S&P 500 dan las estimaciones $\bar{x} = 11.86\%$ y $s = 19.40\%$. Luenberger (2013) calcula el rendimiento esperado y el riesgo de un portafolio a partir de los de sus activos, y $\bar{X}$ se lee igual: es el rendimiento de un portafolio que pone el mismo peso, $1/n$, en $n$ activos, uno por año de la historia, y $S^2$ estima el riesgo de cada uno. **Como portafolio, $\bar{X}$ tiene el rendimiento esperado de sus activos, $\mu$, y menos riesgo que cada uno, porque diversifica entre los años.** La sección 3.3 hace las cuentas.

#### 3.1 Principios de estimación

Dos principios generales construyen estimadores: la **verosimilitud**, que usa solo los datos, y el enfoque **bayesiano**, que además usa lo que se sabía antes de verlos. El más sencillo de todos, la sustitución, resulta ser un caso particular del primero.

**Definición (estimador por sustitución).** Si el parámetro es $\theta = T(F_X)$, como en la sección 1.3, el **estimador por sustitución** (plug-in) es esa misma característica calculada en la **distribución empírica** $\hat{F}_n$, la que asigna probabilidad $1/n$ a cada dato observado (sección 2.2): $\hat{\theta} = T(\hat{F}_n)$.

La media muestral es de este tipo, porque la esperanza de $\hat{F}_n$ es $\bar{x}$, y también lo son la proporción de años con pérdida, el cuantil empírico y la correlación muestral de la sección 2. La varianza muestral, con su divisor $n - 1$, es una corrección de la sustitución (Apéndice).

**Principio de verosimilitud.** Fisher (1922) lo enunció así: "la verosimilitud de que un parámetro tenga un valor dado es proporcional a la probabilidad de que, si así fuera, el total de las observaciones fuera el que se observó". Un valor del parámetro es más verosímil que otro si con él los datos que ocurrieron eran más probables.

> **¿De dónde sale la fórmula?** Del principio y de la muestra aleatoria de la sección 1.2. La verosimilitud de $\theta$ es proporcional a la probabilidad de los datos observados si el parámetro valiera $\theta$, y si los rendimientos son independientes, esa probabilidad, o su densidad, es el producto de las densidades de cada uno, igual que la distribución conjunta. Ese producto se lee al revés: los datos quedan fijos y lo que varía es el parámetro.

**Definición (función de verosimilitud y máxima verosimilitud).** Si $X_1, \dots, X_n$ son independientes, con una densidad $f(x; \theta)$ que depende de un parámetro $\theta$, la **función de verosimilitud** (likelihood) de los datos es

$$L(\theta) = \prod_{t=1}^{n} f(x_t; \theta),$$

definida salvo una constante que no depende de $\theta$, y el **estimador de máxima verosimilitud** $\hat{\theta}$ es el valor del parámetro que la hace más grande: el modelo de la familia que hace más probables los datos observados. En la práctica se maximiza su logaritmo, $\ln L(\theta) = \sum_{t=1}^{n} \ln f(x_t; \theta)$, que convierte el producto en una suma y tiene el mismo máximo.

La verosimilitud no es la probabilidad de que el parámetro valga $\theta$: como función de $\theta$ no suma 1, y solo importan sus cocientes, como $L(\theta_1) / L(\theta_2)$.

**Ejemplo (el S&P 500 con un modelo normal).** Si los 98 rendimientos anuales vienen de una normal, la verosimilitud es máxima en $\hat{\mu} = \bar{x}$ y en $\hat{\sigma} = 19.30\%$, la desviación estándar con divisor $n$ (Apéndice). **Con la normal, la máxima verosimilitud da $\hat{\mu} = 11.86\%$, la misma media que la sustitución.** No es casualidad:

**Proposición (distribución empírica).** Entre todas las distribuciones posibles, la que hace más probables los datos observados es la distribución empírica $\hat{F}_n$: es el estimador no paramétrico de máxima verosimilitud de $F_X$ (Apéndice).

Así, la sustitución es la máxima verosimilitud sin suponer ninguna familia: el modelo no paramétrico de la sección 1.3 llevado a la estimación.

La verosimilitud usa solo los datos, pero la sección 1.3 insistió en que el conocimiento del mercado también informa al modelo. El enfoque **bayesiano** lo incorpora como una distribución: trata al parámetro como incierto, con una **distribución a priori** $g(\theta)$ que resume lo que se cree antes de ver los datos, y estima con el valor que maximiza la verosimilitud por la a priori, $L(\theta) g(\theta)$. Ese producto, escalado para que sume 1, es la distribución **a posteriori**. Por ejemplo, si un analista cree que el rendimiento esperado del S&P 500 está alrededor de $8\%$, con una duda de $2\%$ (ilustrativa), su opinión y los 98 años, que dan $11.86\%$ con un error típico de $1.96\%$ (sección 3.3), pesan casi lo mismo, y **la estimación bayesiana queda entre los dos, en $9.97\%$** (Apéndice). Con pocos datos manda la a priori, y con muchos, los datos; así combinan Black y Litterman (1992) el equilibrio del mercado con las opiniones de los analistas.

Para la verosimilitud, $\mu$ es un número fijo y lo aleatorio es el estimador, que cambia de una historia a otra; para el enfoque bayesiano, lo incierto es $\mu$. Con muchos datos llegan casi al mismo número.

<!-- diapositivas: conservar -->
- **Sustitución:** calcular el parámetro en la distribución empírica; da la media, el cuantil empírico y la correlación muestrales.
- **Máxima verosimilitud:** por el principio de Fisher, el valor del parámetro que hace más probables los datos; con la normal da $\bar{x} = 11.86\%$, y sin suponer familia es la sustitución.
- **Bayes:** el valor que maximiza la verosimilitud por la a priori; un promedio de la opinión previa y de los datos, ponderado por su precisión: $9.97\%$ para el S&P 500.

#### 3.2 Estimar con un modelo o con los datos

El VaR histórico y la proporción de años con pérdida de la sección 2.2 describen la historia, pero también son estimaciones por sustitución: del VaR del rendimiento y de la probabilidad de perder $p$ del modelo de Bernoulli (sección 1.3). Los mismos parámetros se pueden estimar con un modelo paramétrico, calculándolos en la normal con $\bar{x}$ y $s$, como en la sección 6.1 de la nota anterior.

**Ejemplo (el S&P 500 con la normal y con los datos).** Con la normal, el VaR anual al 95% es una pérdida de $20.1\%$, 2,006 pesos de cada 10,000; con los datos, $25.12\%$, 2,512 pesos: **en la cola, la normal subestima la pérdida de un año malo.** En el centro de la distribución, en cambio, coinciden: la normal da una probabilidad de perder $P(X < 0) = 27.1\%$, y los datos, $26.5\%$.

La forma supuesta importa poco donde hay muchos datos y mucho en la cola, donde hay pocos. El VaR histórico no supone ninguna distribución, pero descansa en cinco años: un sexto año malo lo movería bastante. Es el intercambio de la sección 1.3: si su forma es razonable, el modelo paramétrico aprovecha mejor pocos datos; el no paramétrico supone menos, pero pide más.

**Ejemplo (un límite de pérdidas con tres modelos).** En la cola, la forma del modelo puede pesar más que su desviación estándar. El área de riesgos de la sección 1.1 supone rendimientos diarios normales, con media 0 y desviación estándar $1.2\%$, y fija su límite de pérdidas en el VaR al 99% a un día: una pérdida de $2.79\%$, que según su modelo se rebasa unas 2.5 veces al año. Pero los rendimientos diarios del S&P 500 tienen un pico más alto y extremos más poblados que la normal. La **Cauchy** (Apéndice de la nota anterior) tiene esa forma: es de localización y escala, como la normal (sección 1.3), pero sus extremos son tan pesados que no tiene media ni varianza, así que su centro y su escala se estiman por máxima verosimilitud: con los 24,803 rendimientos diarios, $0.06\%$ y $0.47\%$. Supongamos, para ilustrar, que esa Cauchy es la distribución "real". Con cada distribución se simulan 10,000 años de 252 días, y se comparan con los datos diarios del S&P 500 de 1928 a 2026:

|                                               | Normal (supuesta)        | Cauchy (simulada)                    | S&P 500 (datos)       |
| --------------------------------------------- | ------------------------ | ------------------------------------ | --------------------- |
| Días al año en que se rebasa el límite        | 2.5                      | 13.1                                 | 4.5                   |
| Pérdida promedio en esos días (CVaR)          | $3.20\%$                 | no existe; $31.8\%$ en la simulación | $4.19\%$              |
| Días al año con una pérdida de más de $5\%$   | 0.004, uno cada 240 años | 7.4                                  | 0.88, casi uno al año |
| Días al año con una pérdida de más de $100\%$ | 0                        | 0.38, uno cada tres años             | 0                     |

La normal subestima: en los datos el límite se rebasa 4.5 días al año, no 2.5. La Cauchy sobrestima: lo rebasa 13 días al año, su CVaR no existe y produce pérdidas de más de $100\%$ en un día, imposibles por la responsabilidad limitada (sección 1.3). **Es el error de especificación en sus dos versiones, un modelo demasiado tranquilo y uno demasiado nervioso; los datos quedan entre los dos**, y por eso conviene medir las pérdidas grandes directamente con ellos.

<!-- diapositivas: figura sola -->
![Dos paneles del ejemplo del límite de pérdidas: a la izquierda, sobre el histograma gris de los rendimientos diarios del S&P 500 de 1928 a 2026, la densidad normal supuesta, con media 0 y desviación 1.2%, en dorado, y la Cauchy ajustada a los datos, la "real", en azul marino, con un pico más alto que el histograma; una línea roja punteada marca el límite de -2.79%, y un acercamiento entre -7% y -2.5% muestra el histograma entre las dos curvas, con la normal cayendo a cero antes de -4% y la Cauchy muy por encima de los datos; a la derecha, histogramas de cuántos días al año se rebasa el límite en 10,000 años simulados, 2.5 días en promedio con la normal, en contorno dorado, y 13.1 con la Cauchy, en barras azul marino, con una línea roja punteada en los 4.5 días al año del S&P 500 real, entre los dos](img/limite_perdidas_normal_cauchy.png)

#### 3.3 Sesgo y error estándar

Toda estimación cambia de una historia a otra: los dos ruidos blancos de la sección 2.3 son independientes, así que su correlación es 0, y aun así su correlación muestral dio 0.03. Un estimador tiene, entonces, una distribución, la de sus valores en todas las historias posibles: su centro dice si acierta en promedio, y su dispersión, cuánto se equivoca típicamente.

**Definición (sesgo y error estándar).** El **sesgo** de un estimador $\hat{\theta}$ es $E[\hat{\theta}] - \theta$, y el estimador es **insesgado** si su sesgo es 0: en promedio, sobre todas las historias posibles, acierta. Su **error estándar** es su desviación estándar, estimada con los datos.

**Proposición (varianza de una suma).** Para variables aleatorias $X$ y $Y$ y una constante $a$,

$$\operatorname{Var}(aX) = a^2 \operatorname{Var}(X), \qquad \operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2 \operatorname{Cov}(X, Y).$$

Si $X$ y $Y$ son independientes, su covarianza es 0 (sección 5.2 de la nota anterior) y las varianzas simplemente se suman; lo mismo vale para $n$ variables independientes.

**Proposición (media muestral).** Si $X_1, \dots, X_n$ son independientes, cada una con media $\mu$ y varianza $\sigma^2$, entonces

$$E[\bar{X}] = \mu, \qquad \operatorname{Var}(\bar{X}) = \frac{\sigma^2}{n}, \qquad \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}.$$

**Justificación matemática.** Son las cuentas del portafolio del inicio de la sección. Por la linealidad de la esperanza (sección 4.2 de la nota anterior), $E[\bar{X}] = \frac{1}{n}(\mu + \cdots + \mu) = \mu$. Por la proposición anterior, con $a = 1/n$ y las varianzas de variables independientes sumadas, $\operatorname{Var}(\bar{X}) = \frac{1}{n^2}(\sigma^2 + \cdots + \sigma^2) = \frac{\sigma^2}{n}$. Si los años estuvieran correlacionados, las covarianzas no desaparecerían: con una correlación de $0.3$ entre cada par de años (ilustrativa), la desviación estándar del promedio no bajaría de $\sqrt{0.3} \times 19.40\% = 10.63\%$, por más años que se juntaran, como un portafolio de activos que se mueven juntos. Por eso importa el supuesto de independencia de la sección 1.2.

Así, $\bar{X}$ es insesgado, y la varianza muestral también lo es, $E[S^2] = \sigma^2$, gracias al divisor $n - 1$ (Apéndice). Como no se conoce $\sigma$, se sustituye por $s$, y el error estándar de la media es

$$\operatorname{ee}(\bar{x}) = \frac{s}{\sqrt{n}}.$$

**Ejemplo (S&P 500).** Con los 98 rendimientos anuales, $s = 19.40\%$ y

$$\operatorname{ee}(\bar{x}) = \frac{19.40\%}{\sqrt{98}} = 1.96\%.$$

Promediar 98 años divide el riesgo de un solo año entre $\sqrt{98} \approx 10$: **el promedio de $11.86\%$ puede alejarse típicamente unos 2 puntos del rendimiento esperado.**

La fórmula supone que $\sigma$ existe. Con la Cauchy de la sección 3.2 no existe, y el promedio no se vuelve más preciso: con la normal, la mitad central de los promedios anuales cabe en un rango de $0.10\%$; con la Cauchy, en uno de $0.94\%$, el mismo que el de un solo día.

<!-- diapositivas: conservar -->
- **Estimador:** se calcula con la muestra y es una variable aleatoria; cada historia da una estimación distinta.
- **Sesgo:** $E[\hat{\theta}] - \theta$; la media y la varianza muestrales son insesgadas, y la media varía $\sigma / \sqrt{n}$, como un portafolio que diversifica entre los años.
- **Error estándar:** $s / \sqrt{n}$, la desviación estándar estimada de la media; para el S&P 500, $1.96\%$.

Del estimador $\bar{X}$ ya se conocen el centro y la dispersión; la sección 4 da su forma, y con ella el intervalo.

### 4. Del estimador al intervalo de confianza

La sección 3 dio una estimación, $\bar{x} = 11.86\%$, y su error estándar, $1.96\%$; para convertirlos en un intervalo falta la distribución de $\bar{X}$, que con $n$ fijo depende de una población desconocida. Cuando $n$ crece, los teoremas de convergencia dicen dónde se concentra (4.1) y qué forma toma (4.2); con ellos se construye el intervalo (4.3), y la bolsa del S&P 500 los pone a prueba en clase (4.4).

#### 4.1 Consistencia

**Definición (convergencia en probabilidad y estimador consistente).** Una sucesión de variables aleatorias $Y_n$ **converge en probabilidad** a una constante $c$ si, para cualquier margen $\varepsilon > 0$, $P(|Y_n - c| \geq \varepsilon) \to 0$ cuando $n \to \infty$. Un estimador calculado con $n$ datos, $\hat{\theta}_n$, forma una sucesión así, y es **consistente** si converge en probabilidad al parámetro: con datos sin fin, no falla.

> **¿De dónde sale la fórmula?** La varianza (sección 5.1 de la nota anterior) promedia los cuadrados de las distancias a la media. Donde $|Y - \mu_Y| \geq \varepsilon$, cada cuadrado vale al menos $\varepsilon^2$, y en el resto, al menos 0; por eso la varianza es al menos $\varepsilon^2$ por la probabilidad de quedar a $\varepsilon$ o más de la media.

**Proposición (desigualdad de Chebyshev).** Si $Y$ tiene media $\mu_Y$ y varianza finita, para cualquier $\varepsilon > 0$,

$$P(|Y - \mu_Y| \geq \varepsilon) \leq \frac{\operatorname{Var}(Y)}{\varepsilon^2}.$$

**Proposición (ley de los grandes números).** Si $X_1, X_2, \dots$ son independientes, con la misma distribución y esperanza $\mu$, la media muestral $\bar{X}$ es un estimador consistente de $\mu$.

Con varianza finita sale de Chebyshev con $Y = \bar{X}$, de media $\mu$ y varianza $\sigma^2/n$ (sección 3.3): $P(|\bar{X} - \mu| \geq \varepsilon) \leq \sigma^2/(n \varepsilon^2)$, que se va a 0; el mismo argumento vale para cualquier estimador cuyo sesgo y error estándar se van a 0 (Apéndice). La ley necesita que la esperanza exista: el promedio de variables Cauchy de la sección 3.2 tiene la misma distribución que un solo dato, y no se acerca a nada.

**Proposición (distribución empírica).** Si $X_1, X_2, \dots$ son independientes, con distribución $F_X$, $\hat{F}_n(x)$ converge en probabilidad a $F_X(x)$ en cada $x$, y la mayor distancia entre las dos curvas también se va a 0 (teorema de Glivenko-Cantelli).

En cada $x$, $\hat{F}_n(x)$ es la proporción de datos que no pasan de $x$, un promedio de indicadores de Bernoulli, como la proporción de años con pérdida, $26.5\%$; su convergencia es la ley de los grandes números. Por eso la sustitución de la sección 3.1 se acerca a lo que daría la población.

#### 4.2 La forma de la distribución

**Definición (convergencia en distribución).** Una sucesión de variables aleatorias $Y_n$ **converge en distribución** a una variable $Y$ si su función de distribución se acerca a la de $Y$, $F_{Y_n}(y) \to F_Y(y)$ cuando $n \to \infty$, en cada $y$ donde $F_Y$ es continua. Para $n$ grande, las probabilidades de $Y_n$ se calculan, aproximadamente, con la distribución de $Y$.

> **¿De dónde sale la fórmula?** La sección 1.2 estandarizó un rendimiento: restarle su media y dividirlo entre su desviación estándar deja una variable con media 0 y desviación 1. Lo mismo con $\bar{X}$, que tiene media $\mu$ y desviación estándar $\sigma/\sqrt{n}$ (sección 3.3). El teorema dice, además, qué forma tiene esa variable.

**Proposición (teorema central del límite).** Si $X_1, X_2, \dots$ son independientes, con la misma distribución, media $\mu$ y varianza $\sigma^2$ finita, la media estandarizada converge en distribución a la normal estándar, sea cual sea la distribución de cada $X_t$: para $n$ grande,

$$\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \approx N(0, 1).$$

Es mucho más preciso que Chebyshev, que vale con cualquier distribución: a 1.96 errores estándar de $\mu$, Chebyshev solo garantiza que la probabilidad de quedar más lejos no pasa de $1/1.96^2 = 26\%$, y el teorema dice $5\%$. Pero el cociente usa $\sigma$, que no se conoce. Por la ley de los grandes números, $S$ es un estimador consistente de $\sigma$ (Apéndice), y el último teorema permite sustituirla.

**Proposición (teorema de Slutsky).** Si $Y_n$ converge en distribución a $Y$ y $W_n$ converge en probabilidad a una constante $c$, entonces $Y_n W_n$ converge en distribución a $cY$, y $Y_n + W_n$, a $Y + c$.

Con $Y_n$ la media estandarizada y $W_n = \sigma/S$, que converge en probabilidad a 1, el cociente con $S$, con el que se construye el intervalo, también converge en distribución a la normal estándar:

$$\frac{\bar{X} - \mu}{S / \sqrt{n}} = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \frac{\sigma}{S}.$$

#### 4.3 Intervalos de confianza

**Definición (intervalo de confianza).** Sean $T_1$ y $T_2$ dos estadísticos, funciones de la muestra que no dependen del parámetro. El intervalo aleatorio $[T_1, T_2]$ es un **intervalo de confianza** para $\theta$ con **cobertura** $1 - \alpha$ si atrapa al parámetro con al menos esa probabilidad, sea cual sea su valor:

$$P(T_1 \leq \theta \leq T_2) \geq 1 - \alpha.$$

Con $\alpha = 0.05$ es el intervalo al 95% de la sección 1.4: lo aleatorio es el intervalo y el parámetro es fijo.

Para construirlo hace falta una cantidad **pivotal**, una función de la muestra y del parámetro cuya distribución se conoce, al menos de forma aproximada: se buscan los cuantiles de esa distribución que encierran una probabilidad $1 - \alpha$ y se despeja el parámetro. Para la esperanza, la pivotal es el cociente de la sección 4.2: con muchos datos,

$$Z = \frac{\bar{X} - \mu}{S / \sqrt{n}} \approx N(0, 1).$$

> **¿De dónde sale la fórmula?** Con la lectura de cuantiles de la sección 6.1 de la nota anterior, la normal estándar deja $2.5\%$ de probabilidad por debajo de $-1.96$ y $2.5\%$ por encima de $1.96$, así que $P(-1.96 \leq Z \leq 1.96) \approx 0.95$. Al multiplicar las desigualdades por $S/\sqrt{n}$ queda $-1.96\, S/\sqrt{n} \leq \bar{X} - \mu \leq 1.96\, S/\sqrt{n}$, y al despejar $\mu$, $\bar{X} - 1.96\, S/\sqrt{n} \leq \mu \leq \bar{X} + 1.96\, S/\sqrt{n}$.

**Definición (intervalo de Wald).** El intervalo de confianza aproximado al 95% para la esperanza, o intervalo por aproximación normal, es

$$\bar{x} \pm 1.96 \frac{s}{\sqrt{n}} = \bar{x} \pm 1.96 \operatorname{ee}(\bar{x}).$$

**Ejemplo (rendimiento esperado del S&P 500).** Con los 98 rendimientos anuales, $\bar{x} = 11.86\%$ y $\operatorname{ee}(\bar{x}) = 1.96\%$ (sección 3.3), así que

$$11.86\% \pm 1.96 \times 1.96\% = 11.86\% \pm 3.84\%.$$

**El intervalo al 95% para el rendimiento esperado del S&P 500 va de $8.01\%$ a $15.70\%$**, y se lee como en la sección 1.4: el método atrapa a $\mu$ en 95 de cada 100 historias posibles.

El margen, $1.96 \times 19.40\% / \sqrt{n}$, baja con $\sqrt{n}$ y llega a un punto porcentual solo con $n = 1{,}446$ años: la señal débil frente al ruido de la sección 1.2. Con pocos datos, $S$ todavía queda lejos de $\sigma$ y el intervalo atrapa menos de lo que promete; la dinámica de la sección 4.4 lo pone a prueba, y la $t$ de Student lo corrige (Apéndice).

**Definición (remuestreo e intervalo por remuestreo).** El **remuestreo** (bootstrap), que propuso Efron (1979), saca muchas muestras con reemplazo de los propios datos, es decir, de $\hat{F}_n$, cada una con tantos valores como datos hay, y calcula el estimador en cada una: como $\hat{F}_n$ se acerca a $F_X$ (sección 4.1), esas muestras imitan otras historias posibles. El **intervalo por remuestreo** al 95% va del cuantil empírico $2.5\%$ al $97.5\%$ de esos valores (sección 2.2). No necesita una fórmula para el error estándar, y por eso sirve para el CVaR, que no tiene una tan sencilla como $s/\sqrt{n}$.

**Ejemplo (CVaR del S&P 500).** Con 10,000 muestras de 98 años sacadas de los datos se calcula el CVaR histórico al 95% de cada una, el promedio de sus 5 peores años; con los datos es $-33.35\%$ (sección 2.2). **El intervalo al 95% para el CVaR anual va de $-40.92\%$ a $-19.54\%$**, 21 puntos de ancho, frente a 7.7 del intervalo para el rendimiento esperado. Para la media, el mismo método da de $8.12\%$ a $15.67\%$, casi el intervalo de Wald.

La cola descansa en 5 años (sección 3.2), así que la pérdida promedio de un año malo, la que usa quien reserva capital con el CVaR histórico, puede estar en cualquier punto entre 20% y 41%.

#### 4.4 Dinámica: la bolsa del S&P 500

<!-- diapositivas: conservar -->
La teoría se pone a prueba con una población que sí se conoce: una bolsa con 50 papelitos que imita los 98 rendimientos anuales del S&P 500. Cada pareja saca 20 papelitos con reemplazo, y el notebook [`bolsa_sp500.ipynb`](codigo/bolsa_sp500.ipynb), que trae las instrucciones, estima la media y el intervalo con los primeros 4, con los 20 y con las muestras de todo el grupo juntas (parte 1); después, con miles de muestras simuladas, ilustra la convergencia de las secciones 4.1 y 4.2 (parte 2).

<!-- diapositivas: conservar -->
- **Consistencia:** la media muestral se acerca a $\mu$ (ley de los grandes números) y la distribución empírica, a $F_X$ (Glivenko-Cantelli).
- **Forma:** para $n$ grande, $(\bar{X} - \mu)/(S/\sqrt{n})$ es aproximadamente normal estándar (teoremas central del límite y de Slutsky).
- **Intervalo:** $\bar{x} \pm 1.96\, s/\sqrt{n}$, de $8.01\%$ a $15.70\%$ para el S&P 500; por remuestreo, el del CVaR va de $-40.92\%$ a $-19.54\%$.
- **La bolsa:** 50 papelitos que imitan los 98 años; cada pareja saca 20 con reemplazo, y el notebook estima con 4, con 20 y con todo el grupo.

## Apéndice: Complementos de estadística

Esta sección amplía el núcleo; no forma parte del objetivo ni se evalúa. Reúne la formulación general de la población y el modelo, la probabilidad de la prueba de hipótesis de la sección 1.4 y el valor p, las justificaciones de la media geométrica, de la máxima verosimilitud con la normal, del divisor $n - 1$, de la desviación estándar de una suma, $\sigma \sqrt{t}$, de la distribución empírica como estimador de máxima verosimilitud y de la a posteriori normal, la densidad de la Cauchy y la eficiencia de la máxima verosimilitud en ella, la hipótesis conjunta de Fama, el error cuadrático medio y la consistencia de $S$, y la $t$ de Student.

**Población y modelo en la formulación general.** Los datos no siempre son números: pueden ser una trayectoria de precios, una tabla o una curva. En general son la realización de un elemento aleatorio definido en un espacio de probabilidad $(\Omega, \mathcal{F}, P)$, como el de la sección 2.3 de la nota anterior, y la población es la medida $P$ misma. Un modelo paramétrico es entonces una familia de medidas $\{P_\theta : \theta \in \Theta\}$ indexada por el espacio paramétrico $\Theta$; la sección 1.3 es el caso en que los datos son $n$ números y cada $P_\theta$ queda descrita por su función de distribución $F(x; \theta)$.

**26 pérdidas en 98 años si el mercado fuera una moneda.** Si cada año pierde con probabilidad $1/2$, independiente de los demás, las $2^{98}$ secuencias posibles de años con pérdida y con ganancia son igual de probables, y las que tienen exactamente $k$ pérdidas son $\binom{98}{k}$, las maneras de elegir cuáles $k$ años pierden. La probabilidad de 26 pérdidas o menos es entonces

$$\sum_{k=0}^{26} \binom{98}{k} \frac{1}{2^{98}} = 1.84 \times 10^{-6},$$

unas 2 de cada millón. Es la distribución binomial, la del número de éxitos en $n$ ensayos de Bernoulli independientes.

**Prueba de hipótesis y valor p.** La probabilidad anterior es un **valor p**: la probabilidad, si la hipótesis fuera cierta, de un resultado al menos tan alejado de ella como el observado. Un valor p pequeño es evidencia contra la hipótesis. Para el rendimiento esperado, la pivotal de la sección 4.3 sirve igual. Si $H: \mu = 0$, el S&P 500 no rendiría nada en promedio, y $Z = \bar{X} / (S/\sqrt{n})$ sería aproximadamente normal estándar. Con los datos, $z = 11.86\% / 1.96\% = 6.05$, y $P(|Z| \geq 6.05) = 1.5 \times 10^{-9}$. La prueba y el intervalo son dos caras de lo mismo: la hipótesis $\mu = \mu_0$ tiene un valor p menor que $5\%$ justo cuando $\mu_0$ queda fuera del intervalo al 95%, y 0 queda fuera del intervalo de $8.01\%$ a $15.70\%$.

**La media geométrica, aproximadamente $\bar{x} - s^2/2$.** Si $g$ es la media geométrica, $\ln(1 + g) = \frac{1}{n} \sum_{t=1}^{n} \ln(1 + x_t)$. Para rendimientos pequeños, $\ln(1 + x) \approx x - x^2/2$, así que el lado derecho es aproximadamente $\bar{x} - \frac{1}{2n} \sum_{t=1}^{n} x_t^2 \approx \bar{x} - (s^2 + \bar{x}^2)/2$, y el izquierdo, $g - g^2/2$. Como $g$ y $\bar{x}$ son parecidos, sus cuadrados casi se cancelan y queda $g \approx \bar{x} - s^2/2$. Con el S&P 500 da $9.98\%$, frente a los $10.02\%$ exactos.

**La máxima verosimilitud con la normal.** Con la densidad normal de la nota anterior, la log-verosimilitud de $n$ rendimientos es

$$\ln L(\mu, \sigma) = -n \ln \sigma - \frac{1}{2 \sigma^2} \sum_{t=1}^{n} (x_t - \mu)^2 - \frac{n}{2} \ln (2\pi).$$

Para cualquier $\sigma$, la mejor $\mu$ es la que hace más pequeña la suma de cuadrados, y como

$$\sum_{t=1}^{n} (x_t - \mu)^2 = \sum_{t=1}^{n} (x_t - \bar{x})^2 + n (\bar{x} - \mu)^2,$$

esa es la media, $\hat{\mu} = \bar{x}$. Con $\mu = \bar{x}$, la mejor $\sigma$ es $\hat{\sigma} = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (x_t - \bar{x})^2}$, que divide entre $n$, igual que la sustitución; con el S&P 500, $19.30\%$.

**El divisor $n - 1$.** La descomposición del párrafo anterior, con las variables aleatorias, da $\sum_{t=1}^{n} (X_t - \bar{X})^2 = \sum_{t=1}^{n} (X_t - \mu)^2 - n (\bar{X} - \mu)^2$. Su esperanza es $n \sigma^2 - n \operatorname{Var}(\bar{X}) = n \sigma^2 - \sigma^2 = (n - 1) \sigma^2$ (sección 3.3), así que dividir entre $n - 1$ da $E[S^2] = \sigma^2$: la varianza muestral es insesgada, y la de la distribución empírica, que divide entre $n$, la subestima un poco.

**La suma crece con $\sqrt{t}$.** La proposición de la varianza de una suma de la sección 3.3 da la desviación estándar de una suma de $t$ rendimientos independientes: $\sqrt{t \sigma^2} = \sigma \sqrt{t}$. Así se pasa, aproximadamente, de una frecuencia a otra: la desviación estándar diaria del S&P 500, $1.19\%$ (el $1.2\%$ de la sección 1.1), con unos 252 días de operación al año, da $1.19\% \times \sqrt{252} = 18.9\%$ al año, cerca del $19.40\%$ medido con los rendimientos anuales. En 10 años, la suma de los rendimientos varía $19.40\% \times \sqrt{10} = 61.3\%$, mientras que su promedio varía solo $19.40\% / \sqrt{10} = 6.1\%$: el promedio se vuelve más preciso con más años, pero lo acumulado se vuelve más incierto.

**La distribución empírica como estimador de máxima verosimilitud.** Sin una familia no hay densidad que usar, así que la verosimilitud se toma con la probabilidad $p_t$ que la distribución asigna a cada dato observado: $L = p_1 p_2 \cdots p_n$, con $p_1 + \cdots + p_n \leq 1$. (Con densidades arbitrarias no habría máximo: una densidad cada vez más concentrada sobre los datos haría crecer $L$ sin límite.) Poner probabilidad fuera de los datos solo resta, así que la suma es 1, y un producto de números positivos con suma fija es máximo cuando son iguales, porque la media geométrica nunca supera a la aritmética. Por eso $p_t = 1/n$; con datos repetidos, cada valor recibe su frecuencia relativa.

**La a posteriori normal.** Con $\sigma$ igual a $s$, en la descomposición de la máxima verosimilitud con la normal, arriba, solo $n (\bar{x} - \mu)^2$ depende de $\mu$, así que la verosimilitud es $L(\mu) \propto \exp\left( -n (\bar{x} - \mu)^2 / (2 s^2) \right)$: una normal en $\mu$ centrada en $\bar{x}$, con desviación $s / \sqrt{n}$. Con una a priori normal con media $\mu_0$ y desviación estándar $\sigma_0$, $g(\mu) \propto \exp\left( -(\mu - \mu_0)^2 / (2 \sigma_0^2) \right)$, el producto es la exponencial de

$$-\frac{1}{2} \left[ \frac{n}{s^2} (\mu - \bar{x})^2 + \frac{1}{\sigma_0^2} (\mu - \mu_0)^2 \right] = -\frac{1}{2} \left( \frac{n}{s^2} + \frac{1}{\sigma_0^2} \right) (\mu - \hat{\mu}_{post})^2 + \text{constante},$$

al completar el cuadrado, con $\hat{\mu}_{post} = w \bar{x} + (1 - w) \mu_0$ y $w = \frac{n / s^2}{n / s^2 + 1 / \sigma_0^2}$, el peso de los datos. Es una densidad normal con máximo en $\hat{\mu}_{post}$, un promedio de los dos centros ponderado por su **precisión**, uno entre la varianza; su precisión, $n / s^2 + 1 / \sigma_0^2$, es la suma de las dos. Con el analista de la sección 3.1, $\mu_0 = 8\%$ y $\sigma_0 = 2\%$, y como el error estándar de los datos, $1.96\%$, es casi igual a su duda, los dos pesan casi lo mismo, $w = 0.51$: el máximo queda en $0.51 \times 11.86\% + 0.49 \times 8\% = 9.97\%$, con desviación $1 / \sqrt{n / s^2 + 1 / \sigma_0^2} = 1.40\%$, menor que la de la a priori y que la de la verosimilitud. Si el mismo promedio viniera de solo 10 años, con $s / \sqrt{10} = 6.14\%$, el peso de los datos bajaría a $w = 0.10$ y la estimación quedaría en $8.37\%$, cerca del analista.

**Eficiencia en la Cauchy.** La densidad de la Cauchy de la sección 3.2, con centro $x_0$, su mediana, y escala $\gamma$, la mitad de su rango intercuartil, es

$$f(x) = \frac{1}{\pi \gamma \left[ 1 + \left( \frac{x - x_0}{\gamma} \right)^2 \right]}.$$

La sustitución da valores parecidos a los de la máxima verosimilitud: con los rendimientos diarios del S&P 500, la mediana muestral es $0.05\%$ y la mitad del rango intercuartil, $0.50\%$. Para muestras grandes, la varianza de la mediana muestral es aproximadamente $1 / (4 n f(x_0)^2)$, que en la Cauchy, con $f(x_0) = 1 / (\pi \gamma)$, es $\pi^2 \gamma^2 / (4n) \approx 2.47 \gamma^2 / n$; la del estimador de máxima verosimilitud del centro es $2 \gamma^2 / n$, alrededor de 20% menor. La sustitución sirve con cualquier distribución; la máxima verosimilitud paramétrica aprovecha la forma supuesta, y si la forma no es razonable, esa ventaja se convierte en error de especificación. Ninguna de las dos estima lo que la distribución no tiene: con datos Cauchy, la media muestral se puede calcular, pero no estima nada, porque la esperanza no existe.

**La hipótesis conjunta.** Para probar si un mercado es eficiente en el sentido de Fama (1970) hace falta un modelo del rendimiento que se esperaría sin información nueva; si la prueba rechaza, no se sabe si el mercado no es eficiente o si ese modelo no era razonable. El error de especificación no se puede separar de la pregunta.

**El error cuadrático medio y la consistencia de $S$.** La desigualdad de Chebyshev de la sección 4.1, con $E[(\hat{\theta}_n - \theta)^2]$ en lugar de la varianza, da $P(|\hat{\theta}_n - \theta| \geq \varepsilon) \leq E[(\hat{\theta}_n - \theta)^2] / \varepsilon^2$ para cualquier estimador. Esa esperanza es el **error cuadrático medio**, que es igual al sesgo al cuadrado, $(E[\hat{\theta}_n] - \theta)^2$, más la varianza; si los dos se van a 0, el estimador es consistente. La varianza muestral se escribe con dos promedios, $S^2 = \frac{n}{n - 1} \left( \frac{1}{n} \sum_{t=1}^{n} X_t^2 - \bar{X}^2 \right)$, y por la ley de los grandes números el primero se acerca a $E[X^2] = \sigma^2 + \mu^2$ y $\bar{X}$, a $\mu$. Una función continua de variables que convergen en probabilidad converge a la función de sus límites (teorema de la función continua), así que $S^2$ se acerca a $\sigma^2 + \mu^2 - \mu^2 = \sigma^2$, y $S = \sqrt{S^2}$, a $\sigma$.

**La $t$ de Student.** Si los datos fueran normales, $(\bar{X} - \mu)/(S/\sqrt{n})$ tendría exactamente la distribución **$t$ de Student** con $n - 1$ grados de libertad, que William Gosset publicó con el seudónimo de Student (1908). Tiene colas más pesadas que la normal, porque $S$ también cambia de una muestra a otra, y se acerca a la normal conforme crece $n$. Su cuantil $0.975$ es $3.182$ con 3 grados de libertad, $2.131$ con 15 y $1.985$ con 97, en lugar de $1.96$. Para el S&P 500 da $11.86\% \pm 1.985 \times 1.96\%$, de $7.97\%$ a $15.75\%$, casi el intervalo de Wald.

## Fuentes y referencias recomendadas

- Linton, O. (2019). *Financial Econometrics: Models and Methods*. Cambridge University Press: estimación de la media y la volatilidad, autocorrelación y regresión con rendimientos.
- Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer: estimación, convergencia de variables aleatorias, consistencia, intervalos de confianza y remuestreo.
- Kroese, D. P., y Chan, J. C. C. (2014). *Statistical Modeling and Computation*. Springer: población, muestra, modelos y pivotales.
- Shao, J. (2003). *Mathematical Statistics* (2.ª ed.). Springer: muestras aleatorias, familias paramétricas y análisis asintótico.
- Chihara, L. M., y Hesterberg, T. C. (2018). *Mathematical Statistics with Resampling and R* (2.ª ed.). Wiley: consistencia y remuestreo.
- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press: rendimiento esperado y varianza de un portafolio, y diversificación.
- Damodaran, A. (2026). *Historical Returns on Stocks, Bonds and Bills: 1928-2025*. NYU Stern School of Business. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html: rendimientos anuales del S&P 500 con dividendos.
- Yahoo Finance. (2026). *S&P 500 (^GSPC), FEMSA (FEMSAUBD.MX) y NAFTRAC (NAFTRAC.MX), historial de precios* [datos]. https://finance.yahoo.com: cierres diarios del S&P 500 desde 1927 y cierres mensuales de FEMSA y NAFTRAC desde 2020, consultados el 24 de octubre de 2026.
- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 17, 21-86: primer modelo probabilístico de los precios de mercado.
- Student. (1908). The probable error of a mean. *Biometrika*, 6(1), 1-25: la distribución $t$.
- Fisher, R. A. (1922). On the mathematical foundations of theoretical statistics. *Philosophical Transactions of the Royal Society of London, Series A*, 222, 309-368: el principio de verosimilitud y el método de máxima verosimilitud.
- Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, 7(1), 77-91: el modelo de media y varianza.
- Gordon, M. J. (1959). Dividends, earnings, and stock prices. *The Review of Economics and Statistics*, 41(2), 99-105: el modelo de dividendos crecientes.
- Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. *The Journal of Finance*, 19(3), 425-442: el CAPM.
- Fama, E. F. (1970). Efficient capital markets: A review of theory and empirical work. *The Journal of Finance*, 25(2), 383-417: la eficiencia del mercado y la hipótesis conjunta.
- Efron, B. (1979). Bootstrap methods: Another look at the jackknife. *The Annals of Statistics*, 7(1), 1-26: el remuestreo.
- Black, F., y Litterman, R. (1992). Global portfolio optimization. *Financial Analysts Journal*, 48(5), 28-43: la combinación bayesiana del equilibrio del mercado con las opiniones de los analistas.
- Basel Committee on Banking Supervision. (1996). *Amendment to the Capital Accord to incorporate market risks*. Bank for International Settlements: el VaR como base del capital por riesgo de mercado.
