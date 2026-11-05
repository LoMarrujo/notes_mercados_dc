# Unidad 3 · Estadística, Rendimiento y Riesgo

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

> **Prototipo.** Une [`2_estadistica_y_datos.md`](2_estadistica_y_datos.md) y [`4_rendimiento_y_riesgo_acciones.md`](4_rendimiento_y_riesgo_acciones.md) para revisar la estructura antes de migrar. Las marcas "(se migra de 2_ §x.y)" indican texto que ya existe y no se copia aquí; solo la sección 1.1 está redactada. La sección 1 está redactada; las secciones 2 a 6 son un esquema con la teoría de portafolios como eje y la estadística como herramienta que entra donde se necesita. El semi-rigor va en bloques `> **Nota técnica (...).**`: enunciados precisos con una línea de intuición o un esbozo de prueba, que se quedan solo en el `.md` (el generador no pasa los blockquotes al deck conciso) y no se evalúan.

## Objetivo de la unidad

Que el estudiante elija la proporción entre acciones y un instrumento libre de riesgo en una cartera a partir de sus rendimientos históricos, estimando con un intervalo de confianza el rendimiento esperado y comparándolo con la volatilidad, el VaR y el CVaR.

## Contenido

|   | Tema                                   | Qué cubre                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Contexto                               | Qué mueve el precio de una acción (flujos esperados, tasa de descuento y demanda) y por qué su cambio no se puede predecir; la caminata aleatoria, el ciclo de descubrimiento del conocimiento, los datos, los modelos y los problemas de la inferencia                                                                                                                      |
| 2 | Rendimiento y riesgo de cada activo    | Media, desviación estándar y media geométrica de los 98 años del S&P 500 y de los T-bills; anualizar con la raíz del tiempo                                                                                                                                                                                                                                                  |
| 3 | La cartera de media-varianza           | Rendimiento y varianza de una cartera con la covarianza muestral; diversificación y frontera eficiente con el S&P 500 y FEMSA (Markowitz); el activo libre de riesgo, la separación (Tobin) y la razón de Sharpe; elegir la proporción con un límite de volatilidad                                                                                                          |
| 4 | Las carteras de media-VaR y media-CVaR | Elegir con un límite de pérdida: el VaR (Roy; Campbell, Huisman y Koedijk; Alexander y Baptista), que no es subaditivo; el CVaR, medida coherente (Artzner et al.), estándar de Basilea y programa lineal (Krokhmal, Palmquist y Uryasev; Rockafellar y Uryasev)                                                                                                             |
| 5 | Estimar y comparar con datos           | Estimadores y error estándar, ley de los grandes números y teorema central del límite; intervalo de confianza para el rendimiento esperado, de 8.01% a 15.70%; el error de estimación en la optimización (Michaud; Chopra y Ziemba; DeMiguel, Garlappi y Uppal); la dinámica de la bolsa del S&P 500; VaR y CVaR históricos con remuestreo; comparación de las tres carteras |

> La práctica de este tema es la dinámica de la sección 5.4, en el notebook [`bolsa_sp500.ipynb`](codigo/bolsa_sp500.ipynb), y la elección de cartera de [`practica_4_rendimiento_riesgo_acciones.md`](../../practicas/unidad3/practica_4_rendimiento_riesgo_acciones.md).

### 1. Contexto

#### 1.1 Qué mueve el precio y por qué no se puede predecir

Según el modelo de dividendos descontados, el precio de una acción debería igualar el valor presente de los dividendos que se espera que pague, descontados a una tasa que compensa su riesgo (Williams, 1938); la nota de valuación lo desarrolla. Si fuera así, el precio solo cambiaría con noticias sobre esos dividendos o sobre la tasa de descuento (Campbell y Shiller, 1988). Cutler, Poterba y Summers (1989) pusieron a prueba esta idea con el mercado estadounidense: las noticias macroeconómicas explican menos de **un tercio** de la varianza de los rendimientos, y muchos de los movimientos más grandes ocurren en días sin una noticia identificable. La investigación posterior encontró parte de lo que faltaba. Cochrane (2011) muestra que la variación de la razón precio-dividendo se debe sobre todo a cambios en la tasa de descuento, no en los dividendos esperados. Bernanke y Kuttner (2005) estiman que un recorte sorpresivo de 25 puntos base en la tasa de la Reserva Federal sube el índice alrededor de **1%**, principalmente porque reduce la prima de riesgo exigida, un canal que en México corresponde a las decisiones de Banxico. Con análisis de texto, Boudoukh, Feldman, Kogan y Richardson (2019) atribuyen a noticias de la propia emisora cerca de **la mitad** de la volatilidad específica de una acción fuera del horario de negociación, y Baker, Bloom, Davis y Sammon (2021), que leen la prensa del día siguiente a cada salto del mercado en varios países, encuentran que los periódicos atribuyen el **38%** de los saltos de su mercado a noticias económicas y de política de Estados Unidos.

El precio también se mueve sin información nueva. Cuando una acción entra al S&P 500 nada cambia en la empresa, pero los fondos indexados deben comprarla. Shleifer (1986) encuentra que su precio sube y lo interpreta como evidencia de que la demanda por una acción tiene pendiente negativa; Harris y Gurel (1986) documentan, en cambio, que la subida se revierte en pocas semanas, y la discusión sobre si el efecto es permanente sigue abierta. Gabaix y Koijen (2021) llevan el argumento al mercado completo: como buena parte del ahorro está en instituciones cuyos mandatos limitan cuánto pueden moverse entre acciones y bonos, la demanda agregada es poco sensible al precio, y estiman que cada dólar que entra al mercado accionario eleva su valor en unos **cinco dólares**, resultado que los propios autores presentan como hipótesis. El precio responde así a tres fuerzas: lo que se espera que pague la empresa, la tasa con que se descuenta y la demanda de quienes compran.

La incertidumbre es la condición general de cualquier decisión sobre el futuro. La probabilidad es el lenguaje para describirla y la estadística, la herramienta para responder preguntas con datos y reducirla dentro de lo posible, sin llegar a eliminarla. El mercado accionario es un caso extremo de esa incertidumbre, porque el precio no depende solo de la naturaleza, sino de las decisiones de millones de personas que reaccionan a la información y a lo que creen que harán las demás. Keynes (1936) lo comparó con un concurso de belleza en el que no gana quien elige la cara más bonita, sino quien acierta la que elegirán los demás. Hayek (1974) advirtió que, ante fenómenos sociales de esta complejidad, la ciencia puede anticipar patrones, no resultados exactos. Las finanzas adoptaron esa postura desde Bachelier (1900), que modeló el cambio de precio como una variable aleatoria. Samuelson (1965) mostró por qué es el modelo natural: si el precio ya incorpora lo que se espera, solo se mueve con lo nuevo, y lo nuevo no se puede anticipar. Los datos lo respaldan: ni los pronosticadores profesionales (Cowles, 1933) ni la historia de los precios (Kendall, 1953) anticipan el siguiente cambio. Por eso, en lugar de predecir el rendimiento del próximo año, se describe su distribución con la probabilidad, y como esa distribución no se conoce, se estima con la estadística. La decisión que sí está en manos del inversionista no es qué acción subirá, sino cuánto poner en cada activo con lo que se sabe de esa distribución.

#### 1.2 El ciclo de descubrimiento del conocimiento

La probabilidad es deductiva: se toma un modelo dado y se deducen sus implicaciones. El primer modelo probabilístico del precio de una acción es la **caminata aleatoria** de Bachelier: el precio de mañana es el de hoy más un choque que no se puede anticipar. Si $X_t$ es ese choque, el cambio del precio en el periodo $t$, el modelo dice que

$$X_1, X_2, \dots \text{ son independientes, con } E[X_t] = 0 \text{ y } \operatorname{Var}(X_t) = \sigma^2,$$

y el precio después de $t$ periodos es el inicial más la suma de los choques. Es la forma matemática del párrafo anterior: si el precio ya incorpora lo que se espera, su cambio solo responde a lo nuevo. En su versión moderna, Osborne (1959) aplicó la caminata al logaritmo del precio, de modo que $X_t$ es el rendimiento y el precio nunca es negativo; así se lee $X_t$ en el resto de la nota.

**¿De dónde sale la raíz del tiempo?** Después de $t$ días, el rendimiento acumulado es la suma de $t$ choques, $X_1 + \dots + X_t$. Como los choques son independientes, la varianza de la suma es la suma de las varianzas (nota de probabilidad, sección 5.2), $t\sigma^2$, y la desviación estándar del cambio acumulado es

$$\sigma_t = \sigma\sqrt{t}.$$

La incertidumbre crece con el horizonte, pero más despacio que el horizonte mismo.

> Ejemplo: Si el rendimiento diario del S&P 500 siguiera una caminata aleatoria con choques normales de media 0 y desviación estándar de $1.2\%$, una caída de $1.2\%$ o más ocurriría uno de cada seis días, y la volatilidad de un año de 252 días de negociación sería $1.2\% \times \sqrt{252} = $ **19.05%**. Así trabaja el área de riesgos de un banco con un portafolio de acciones de 100 millones de pesos: con el mismo modelo deduce, sin observar un solo precio, el valor en riesgo al 99% a un día, $2.326 \times 1.2\% \times 100 = 2.79$ millones de pesos, la pérdida que solo se supera uno de cada 100 días. La conclusión se sigue de los supuestos con certeza; qué tan útil es depende de qué tan razonables sean.

La estadística es inductiva: recorre el camino partiendo de los datos y alimenta la modelación.

> Ejemplo: En la práctica nadie le da al banco ese $1.2\%$, ni le asegura que los choques sean independientes o normales; tiene precios pasados, y con ellos infiere el modelo que pudo haberlos generado. La caminata aleatoria es entonces una **hipótesis** que los datos pueden respaldar o no: Kendall encontró que los cambios de precio casi no se correlacionan con los anteriores, como predice el modelo, y la nota de hechos estilizados muestra en qué falla, con colas más pesadas que las de la normal y periodos de volatilidad alta y baja. Las conclusiones de la estadística nunca son seguras, porque otros datos habrían dado otra estimación; parte de su trabajo es medir qué tan lejos puede estar la estimación del parámetro del modelo.

El trabajo de descubrimiento del conocimiento sigue un ciclo iterativo:

1. Se parte de una **pregunta**: qué proporción del ahorro poner en el S&P 500 y qué proporción en T-bills. Responderla requiere saber cuánto rinde en promedio cada uno, que interesa a quien invierte a largo plazo, y cuánto se pierde en los peores años, que interesa a quien debe soportarlos y se mide con el CVaR.
2. Después vienen los **datos** y el **modelo** que pudo haberlos generado. El orden depende del tipo de trabajo.
    - En un trabajo de **exploración**, se describen primero los datos y estos sugieren el modelo, como cuando el histograma de los rendimientos diarios sugiere colas más pesadas que las de la normal.
    - En uno de **confirmación**, el modelo y la hipótesis se fijan antes de ver los datos, que solo sirven para ponerlos a prueba, como la caminata aleatoria frente a la correlación de los cambios de precio; si los mismos datos sugirieran el modelo y lo confirmaran, la prueba se aprobaría casi siempre.
3. Luego se **estiman** los parámetros, la media, la volatilidad y la correlación de cada activo, y con ellos su propia incertidumbre, porque otra historia habría dado otra estimación.
4. Con lo estimado se **predice** lo que pide la pregunta: el rendimiento esperado y la pérdida en los peores años de cada cartera posible, cada uno con un intervalo.
5. Al final se **evalúa** en dos sentidos. Si no es lo suficientemente bueno, se vuelve a especificar.
    - Primero, si el modelo predice bien con datos que no usó para estimarse, por ejemplo contando cuántos días se rebasa un límite de pérdidas.
    - Segundo, si la respuesta sirve a la decisión: si la proporción elegida deja una pérdida en los peores años que el inversionista puede soportar, y si el rendimiento esperado compensa ese riesgo.

> **Figura.** Se reusa `img/proceso_estadistico.png` de 2_ §1.1, pero hay que regenerarla con `img/generar_figuras.py`: la caja Pregunta pasa a ser la proporción entre S&P 500 y T-bills, la caja Predecir pasa a "cada cartera posible" y la caja Evaluar apunta a las secciones 3, 5 y 6. Además se renumeran las secciones del texto alternativo.

#### 1.3 Los datos

Antes de estimar hay que responder tres preguntas sobre los datos: qué representan, cómo se obtuvieron y qué hay que suponer para usarlos.

**Qué representan.** La **población** es la distribución que generó los datos y que no se conoce. Para elegir una cartera interesan dos rendimientos a la vez, el $X$ del S&P 500 y el $Y$ de los T-bills, así que la población es su distribución conjunta $F_{X,Y}$ (nota de probabilidad, sección 3.3), que incluye cómo se mueven juntos. Para aprender algo de ella se usa una **muestra**, $n$ pares de variables aleatorias $(X_1, Y_1), \dots, (X_n, Y_n)$. Los números que toman, $(x_1, y_1), \dots, (x_n, y_n)$, son la **muestra observada**, los datos. Cada par es un mismo año: separar las dos columnas perdería la covarianza que necesita la sección 3.

**Cómo se obtuvieron.** Detrás de toda muestra hay dos procesos.

- El **proceso generador** produce los datos. Son **experimentales** si quien investiga interviene, como al probar dos precios con clientes elegidos al azar, y **observacionales** si solo registra lo que ocurrió. En finanzas casi todo es observacional: nadie le asigna a una empresa su política de dividendos para ver qué pasa.
- El **muestreo** es la regla con que se eligen las observaciones. Si favorece a ciertos datos, la estimación hereda ese sesgo, y más datos no lo corrigen.

| Tipo de muestreo                    | Cómo se eligen las observaciones                                                     | Ejemplo en finanzas                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Aleatorio simple                    | Al azar y sin reemplazo: cualquier grupo de $n$ unidades tiene la misma probabilidad | Sortear 30 emisoras de la BMV para estimar su rendimiento por dividendos promedio                       |
| Estratificado (stratified sampling) | Se divide la población en grupos, los estratos, y se sortea dentro de cada uno       | Un ETF de bonos que no compra todos los títulos de su índice, sino una muestra por plazo y calificación |
| Sistemático                         | Cada $k$-ésima unidad, o a intervalos fijos de tiempo                                | Los cierres diarios, de fin de mes o de fin de año del S&P 500                                          |
| Por conveniencia (no aleatorio)     | Las que están a la mano                                                              | Solo las emisoras que siguen cotizando hoy, con su sesgo de supervivencia (survivorship bias, nota 0_)  |

Con los rendimientos de un índice no se sortea nada: el mercado produce una sola sucesión, y lo único que se elige es la frecuencia y el periodo. Es **un muestreo sistemático en el tiempo de datos observacionales**.

**Qué hay que suponer.** Esa sucesión se modela como una **serie de tiempo**, variables aleatorias indexadas por el tiempo, $\{X_t\}_{t=1}^{T} = X_1, X_2, \dots, X_T$, con $X_t$ el rendimiento del índice en el año $t$; la de los T-bills, $\{Y_t\}$, corre en paralelo.

> Ejemplo: Los rendimientos del S&P 500 van de 1928 ($t = 1$) a 2025 ($t = T = 98$). La mayúscula $X_t$ es la variable aleatoria antes de observarla y la minúscula $x_t$ el número observado, como $x_4 = -43.84\%$ en 1931. La historia ocurrió una sola vez: $x_1, \dots, x_{98}$ son **una realización** de la serie, una de las muchas trayectorias que el mercado pudo haber seguido.

Tratar esa única trayectoria como 98 observaciones del mismo fenómeno exige dos supuestos, que la nota 3_ pone a prueba:

1. **Estacionariedad** (stationarity): la distribución de $X_t$ no cambia con $t$.
2. **Independencia**: saber dónde cayó un año no cambia la distribución de otro; que 1931 perdiera $43.84\%$ no dice nada de 1932.

> **¿De dónde sale la fórmula?** Si las observaciones son independientes, la probabilidad de que todas caigan donde caen es el producto de las probabilidades de cada una, como $P(A \cap B) = P(A) P(B)$ en la sección 3.3 de la nota de probabilidad.

**Definición (muestra aleatoria).** $X_1, \dots, X_n$ son una **muestra aleatoria** de $X$ si son independientes y cada una tiene la misma distribución que $X$ (independientes e idénticamente distribuidas, iid). Su distribución conjunta es entonces

$$F_{X_1, \dots, X_n}(x_1, \dots, x_n) = F_X(x_1) F_X(x_2) \cdots F_X(x_n).$$

Es el supuesto con el que la sección 5 calcula la media muestral y su error estándar.

**Definición (ruido blanco).** Un **ruido blanco** es una sucesión $\varepsilon_1, \varepsilon_2, \dots$ de variables aleatorias iid con media 0 y varianza constante: ningún valor dice nada de los demás. Es la caminata aleatoria de la sección 1.2 con los choques estandarizados.

> **¿De dónde sale la fórmula?** Si $X_t$ tiene media $\mu$ y desviación estándar $\sigma$, la variable estandarizada $\varepsilon_t = (X_t - \mu) / \sigma$ tiene media 0 y desviación estándar 1; al despejar $X_t$ sale la fórmula, y si las $X_t$ son iid, las $\varepsilon_t$ también.

Una muestra aleatoria con media $\mu$ y desviación estándar $\sigma$ es una constante más un ruido blanco,

$$X_t = \mu + \sigma \varepsilon_t,$$

donde $\mu$ es lo que se espera cada año y $\sigma \varepsilon_t$, la sorpresa. Es la caminata aleatoria de la sección 1.2 con una tendencia $\mu$: Bachelier suponía $\mu = 0$. En el S&P 500, la media de **11.86%** estima $\mu$ y $s = 19.40\%$ estima $\sigma$. Los T-bills cumplen peor el supuesto, porque su rendimiento sigue a la tasa de interés, que cambia despacio, pero para la cartera pesa poco: lo que importa de ellos es que su volatilidad es pequeña frente a la del índice.

**Por qué es difícil en finanzas.** Los dos procesos ponen límites que más datos no siempre resuelven.

- **No se puede repetir la historia** y el mecanismo cambia mientras se observa: la regulación, la tecnología, las empresas del índice y los propios inversionistas, que dejan de ganar con un patrón en cuanto se vuelve conocido.
- **La señal es débil frente al ruido:** un promedio de $11.86\%$ frente a una dispersión de $19.40\%$ en un solo año exige muchos años para estimarlo, y los eventos extremos, los que más importan para el riesgo, son los que menos se observan.
- **El registro tiene trampas:** bases que solo guardan a las empresas que sobrevivieron, precios que no se ajustan por dividendos o por divisiones de acciones, y fechas mal etiquetadas.

Como solo hay una historia, quien prueba muchas estrategias con los mismos datos termina encontrando alguna que funcionó por suerte. Linton (2019) lo resume con una broma, los datos son el plural de las anécdotas: el $-43.84\%$ de 1931 es una anécdota y 98 años juntos son datos.

<!-- diapositivas: conservar -->
- **Probabilidad (nota 1_):** con el modelo conocido se calculan $E[R]$, $\sigma$, el VaR y el CVaR.
- **Estadística:** con los datos se estiman $E[R]$, $\sigma$, la correlación, el VaR y el CVaR de cada activo, y se mide qué tan lejos pueden estar de los parámetros del modelo.
- **Los datos como realización:** 98 pares de rendimientos son una de muchas trayectorias posibles; con estacionariedad e independencia se tratan como una muestra aleatoria, $X_t = \mu + \sigma \varepsilon_t$.
- **Reconocer lo que no sabemos:** el promedio de 98 años, $11.86\%$, es solo una estimación de $E[R]$; la respuesta es un intervalo, de $8.01\%$ a $15.70\%$ al 95% de confianza, y su ancho pasa a lo que se le promete al inversionista en la sección 4.

#### 1.4 Los modelos

Con los datos en la mano, hay que decidir qué distribuciones se consideran posibles para ellos. Esa decisión responde tres preguntas: qué es un modelo, qué tipos hay y cómo se elige uno.

**Qué es un modelo.** Un **modelo** es la colección $\mathcal{M}$ de distribuciones que se consideran posibles para los datos $X_1, X_2, \dots$: las candidatas a ser la población. Cada supuesto deja fuera distribuciones. Por ejemplo, como una acción no puede perder más de lo invertido, su rendimiento no baja de $-100\%$, y un modelo que dé probabilidad a pérdidas mayores no es razonable.

**Definición (parámetro).** Un **parámetro** es una característica numérica de la distribución, $\theta = T(F_X)$: la esperanza $\mu$, la desviación estándar $\sigma$, un cuantil $q_p$ como el VaR o la probabilidad de perder, $P(X < 0)$. Existe en cualquier modelo y es lo que la estadística trata de estimar.

**Qué tipos hay.** Se distinguen por cuánto fijan de antemano.

- **Paramétrico:** un número fijo de parámetros $\theta = (\theta_1, \dots, \theta_k)$ determina la distribución completa, $\mathcal{M} = \{ F(x; \theta) : \theta \in \Theta \}$, donde $\Theta$, el **espacio paramétrico**, es el conjunto de valores posibles. Se escribe $X \sim F(x; \theta)$, "$X$ se distribuye como $F(x; \theta)$". La caminata aleatoria con choques normales de la sección 1.2 es el ejemplo: $\theta = (\mu, \sigma)$, con $\Theta = \mathbb{R} \times (0, \infty)$. El más simple es el de Bernoulli: si $D = 1$ cuando el S&P 500 pierde en el año, **un solo parámetro, la probabilidad de perder $p = P(X < 0)$, determina la distribución de $D$.**
- **No paramétrico:** ningún número fijo de parámetros determina la distribución, porque $\mathcal{M}$ contiene todas o casi todas. Los parámetros se estiman uno por uno con la distribución empírica, como el VaR histórico, que lee el cuantil de los datos ordenados. Su costo es que pide muchos datos: **con los 98 años del S&P 500, el VaR al 99% descansa en un solo dato, 1931, con $-43.84\%$.**
- **Semiparamétrico:** fija la forma de una parte y deja libre el resto, como la regresión del CAPM, $R_i = \alpha + \beta R_m + \varepsilon$, que fija la relación con el mercado y deja libre la distribución del error (nota 3_).
- **Bayesiano:** a un modelo paramétrico le agrega lo que se cree del parámetro antes de ver los datos, una **distribución a priori** $g(\theta)$. Un analista que cree que el rendimiento esperado del S&P 500 está cerca de $8\%$ lo combina con los datos en la sección 5.1.

En los modelos de **localización y escala**, de la forma $X_t = \mu + \sigma \varepsilon_t$ de la sección 1.3 con la distribución de $\varepsilon_t$ fija, $\mu$ mueve la distribución, $\sigma$ la estira y los cuantiles se mueven igual: si $z_p$ es el cuantil de $\varepsilon_t$, el de $X_t$ es $q_p = \mu + \sigma z_p$. Así sale el VaR de la sección 1.2: con $\mu = 0$ y $z_{0.01} = -2.326$, $q_{0.01} = -2.326 \times 1.2\% = -2.79\%$.

La elección es un intercambio: si la forma supuesta es razonable, el paramétrico aprovecha mejor pocos datos; si no lo es, carga con su error. El no paramétrico supone menos, pero pide muchos más datos, sobre todo en las colas.

**Cómo se elige.** Elegir la familia $\mathcal{M}$ y sus supuestos es **especificar** el modelo. Los supuestos son **estructurales**, cómo se relacionan las observaciones entre sí, como la independencia de la sección 1.3, o **distribucionales**, cuál es la distribución de cada una, como la normal. Los datos solos no deciden: la mayor parte viene del conocimiento del mercado, como muestran los modelos clásicos de las finanzas.

| Modelo                               | Lo que aporta el contexto                                                      | Qué se estima con datos                    |
| ------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------ |
| Caminata aleatoria, Bachelier (1900) | Si los cambios de precio fueran predecibles, alguien ya los habría aprovechado | Media y desviación estándar de los cambios |
| Media y varianza, Markowitz (1952)   | Al inversionista le importan la ganancia esperada y su dispersión              | $E[R]$, $\sigma$ y covarianzas             |
| CAPM, Sharpe (1964)                  | Solo se paga el riesgo que no se elimina diversificando                        | La beta, pendiente de una regresión        |
| VaR normal, Basilea (1996)           | Los bancos deben reservar capital contra la pérdida de un día malo             | $\sigma$ y el cuantil al 99%               |

Un modelo no es correcto ni equivocado, sino más o menos razonable para su uso: uno bueno es consistente con lo que se sabe del mercado, se comporta bien en los casos extremos y tiene parámetros con una interpretación clara. Hay un **error de especificación** cuando la población no está en el modelo, $F_X \notin \mathcal{M}$, y más datos no lo corrigen, porque el estimador sigue respondiendo la pregunta del modelo, no la del mercado. En sentido estricto casi ningún modelo contiene a la población: la normal admite pérdidas de más de $100\%$, aunque con los datos anuales del S&P 500 les da una probabilidad de cuatro en mil millones. Lo que importa es qué tan lejos queda.

<!-- diapositivas: conservar -->
- **Modelo:** las distribuciones que se consideran posibles para los datos; cada supuesto deja fuera algunas.
- **Tipos:** paramétrico, como la caminata con choques normales; no paramétrico, como el VaR histórico; semiparamétrico, como el CAPM; bayesiano, con una a priori sobre los parámetros. El primero rinde más con pocos datos si es razonable; el segundo supone menos pero pide más.
- **Especificar:** elegir la familia y sus supuestos; lo decide sobre todo el conocimiento del mercado.
- **Error de especificación:** la población no está en el modelo, $F_X \notin \mathcal{M}$; más datos no lo corrigen.

#### 1.5 Los problemas de la inferencia

Con los datos y un modelo, lo que sigue es la inferencia.

**Definición (inferencia).** La **inferencia** es el proceso de obtener conclusiones sobre la población a partir de la muestra observada.

Casi siempre interesa un parámetro, como el rendimiento esperado o la probabilidad de perder. Las conclusiones son inciertas porque poblaciones distintas pudieron generar los mismos datos, y la pregunta se puede plantear de varias formas:

| Problema                 | Qué busca                                                        | Ejemplo en finanzas                                        |
| ------------------------ | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| Estimación puntual       | Un número para el parámetro                                      | El rendimiento esperado del S&P 500, $11.86\%$ (sección 5) |
| Intervalo de confianza   | Un rango que atrapa al parámetro con una probabilidad fijada     | De $8.01\%$ a $15.70\%$ al 95% (sección 5)                 |
| Prueba de hipótesis      | Qué tan fuerte es la evidencia de los datos contra una hipótesis | ¿Pierde el mercado la mitad de los años?                   |
| Regresión                | Cómo cambia, en promedio, una variable con otra                  | La beta del CAPM (nota 3_)                                 |
| Selección y ordenamiento | Cuál de varias poblaciones tiene el mejor parámetro              | Cuál de 20 fondos tiene el mayor rendimiento esperado      |

Esta nota resuelve los dos primeros y los usa para elegir la cartera; la nota 3_ resuelve la regresión.

- **Estimación puntual:** da un número para el parámetro con base en la muestra. Toda estimación tiene un **error de estimación**, $\hat{\theta} - \theta$, que no se conoce porque el parámetro tampoco; la sección 5 mide su tamaño típico.
- **Intervalo de confianza:** dice qué tan precisa es la estimación. Es un rango calculado con la muestra que contiene al parámetro con una probabilidad fijada de antemano, su **nivel de confianza**. Lo aleatorio es el intervalo y el parámetro es fijo: "de $8.01\%$ a $15.70\%$ al 95%" quiere decir que el método atrapa al rendimiento esperado en 95 de cada 100 historias posibles, no que $\mu$ tenga 95% de probabilidad de estar ahí.
- **Prueba de hipótesis:** mide qué tan fuerte es la evidencia contra una hipótesis $H$ sobre el parámetro. Ninguna hipótesis es literalmente cierta; la pregunta es si los datos la contradicen lo suficiente para dejar de usarla.

> Ejemplo: Si el mercado fuera una moneda, un año de pérdida sería tan probable como uno de ganancia: en el modelo de Bernoulli de la sección 1.4, $H: p = 1/2$. Se esperarían unos 49 de los 98 años con pérdida, y hubo 26. **Si $p = 1/2$, ver 26 pérdidas o menos en 98 años independientes ocurriría en unas 2 de cada millón de historias** (Apéndice): los datos contradicen la hipótesis.

Confundir los problemas hace perder el control de la incertidumbre. Si se elige el mejor de 20 fondos por su promedio histórico y se reporta su intervalo como si fuera el único analizado, el intervalo promete más de lo que da, porque el ganador es en parte el que tuvo más suerte. Con la cartera pasa algo parecido: la cartera que se elige en la sección 3 hereda el error de estimación de $\mu$ y $\sigma$, y la sección 5 mide cuánto.

La sección 2 describe cada activo con los datos, las secciones 3 y 4 plantean cómo combinarlos en una cartera, con la varianza, el VaR y el CVaR, y la sección 5 pregunta cuánto confiar en ella.

### 2. Rendimiento y riesgo de cada activo

Antes de combinar dos activos hay que saber cuánto rinde y cuánto varía cada uno. Para eso basta un **estadístico**: una función de los datos, $g(x_1, \dots, x_n)$, que no depende de ningún parámetro desconocido. Describir no necesita un modelo específico: los estadísticos de esta sección valen para cualquier distribución, como en el modelo no paramétrico de la sección 1.4; leer los estadísticos como estimaciones de los parámetros es el trabajo de la sección 5. Cada uno es la versión con datos de algo que la nota de probabilidad calculaba con el modelo:

| Con el modelo (nota 1_)      | Con los datos (estadístico)      |
| ---------------------------- | -------------------------------- |
| Densidad $f_X$               | Histograma                       |
| Esperanza $\mu = E[X]$       | Media muestral $\bar{x}$         |
| Desviación estándar $\sigma$ | Desviación estándar muestral $s$ |

#### 2.1 Media, desviación estándar y media geométrica

**Definición (histograma).** Se divide el rango de los datos en intervalos del mismo ancho y se cuenta cuántas observaciones caen en cada uno. El **histograma** dibuja una barra por intervalo con esa cuenta: es la versión con datos de la densidad.

**Definición (media y desviación estándar muestrales).** Para los datos $x_1, \dots, x_n$,

$$\bar{x} = \frac{1}{n} \sum_{t=1}^{n} x_t, \qquad s = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} (x_t - \bar{x})^2}.$$

La media es el centro de los datos y $s$, qué tan lejos de él caen típicamente: la volatilidad observada. Las desviaciones se miden respecto a $\bar{x}$ porque $\mu$ no se conoce, y se divide entre $n - 1$ por una razón de estimación que retoma la sección 5.1; con 98 datos, la diferencia con dividir entre $n$ es de medio por ciento.

**Definición (media geométrica).** Es el rendimiento constante que habría dejado la misma riqueza final que la historia real (nota de probabilidad, sección 4.3),

$$\bar{x}_g = \left( \prod_{t=1}^{n} (1 + x_t) \right)^{1/n} - 1.$$

**Ejemplo (el S&P 500 y los T-bills, 1928 a 2025).** Con los rendimientos anuales de Damodaran (2026) de los dos activos de la cartera:

| Estadístico             | S&P 500           | T-bills a 3 meses |
| ----------------------- | ----------------- | ----------------- |
| Media $\bar{x}$         | $11.86\%$         | $3.42\%$          |
| Desviación estándar $s$ | $19.40\%$         | $3.04\%$          |
| Media geométrica        | $10.02\%$         | $3.37\%$          |
| Peor año                | $-43.84\%$ (1931) | $0.03\%$ (2014)   |
| Mejor año               | $52.56\%$ (1954)  | $14.04\%$ (1981)  |
| Años con pérdida        | 26 de 98          | 0 de 98           |

**El S&P 500 rindió en promedio 8.44 puntos más que los T-bills al año, a cambio de una volatilidad seis veces mayor**, y quedó por debajo de ellos en 32 de los 98 años. Ese intercambio entre premio y riesgo es lo que la cartera de la sección 3 reparte.

<!-- diapositivas: figura sola -->
![Histograma de los 98 rendimientos anuales del S&P 500 con dividendos entre 1928 y 2025, en barras de 10 puntos de ancho desde -50% hasta 60%; una línea dorada marca la media de 11.86%, una línea roja de rayas y puntos marca la media geométrica de 10.02%, un poco a su izquierda, y una franja dorada clara, entre líneas punteadas en -7.55% y 31.26%, marca una desviación estándar de 19.40% a cada lado, con la leyenda 65 de 98 años dentro de la franja](img/sp500_histograma_media_desviacion.png)

Tres lecturas de la tabla sirven para lo que sigue:

- **La forma:** en el histograma, 65 de los 98 años (66%) caen a una desviación estándar de la media y 94 (96%) a dos; una normal tendría 68% y 95%. Con datos anuales la normal no es mala aproximación; la sección 5 y la nota 3_ muestran dónde falla, en la cola.
- **La brecha geométrica:** la media geométrica del S&P 500 queda 1.84 puntos por debajo de la aritmética, y la de los T-bills, menos de una décima. Una pérdida pesa más que una ganancia del mismo tamaño (perder 20% y luego ganar 20% deja 96 de cada 100 pesos), y la brecha crece con la volatilidad: aproximadamente, $\bar{x}_g \approx \bar{x} - s^2/2$, que para el S&P 500 da $9.98\%$. La media aritmética dice cuánto se espera ganar en un año, y es la que entra en la cartera; la geométrica, cuánto creció el dinero que se quedó invertido.
- **La volatilidad de los T-bills no es riesgo para quien los compra:** su $s = 3.04\%$ mide cuánto cambió la tasa a lo largo de la historia, no la sorpresa de un año. Quien compra un T-bill a tres meses conoce de antemano lo que recibirá, y la tasa del año siguiente se parece mucho a la de este: la correlación entre años consecutivos es de 0.92, frente a $-0.02$ en el S&P 500. Por eso en la sección 3 los T-bills hacen el papel de activo libre de riesgo.

> **Nota técnica (media geométrica).** Si $\log(1 + X)$ tiene media $m$, la media geométrica converge a $e^m - 1$. Un desarrollo de Taylor de segundo orden, $\log(1 + x) \approx x - x^2/2$, da $m \approx \mu - (\sigma^2 + \mu^2)/2$; al deshacer el logaritmo, $e^m - 1 \approx m + m^2/2$, los términos en $\mu^2$ se cancelan y queda $\bar{x}_g \approx \mu - \sigma^2/2$. La justificación completa se migra del Apéndice de 2_.

<!-- diapositivas: conservar -->
- **Estadísticos:** la media $\bar{x}$, la desviación estándar $s$ y la media geométrica describen cada activo sin suponer un modelo.
- **El intercambio:** el S&P 500 rindió 8.44 puntos más que los T-bills al año, con una volatilidad seis veces mayor.
- **Media aritmética o geométrica:** la aritmética es lo que se espera en un año y entra en la cartera; la geométrica, lo que creció el dinero, y queda abajo por aproximadamente $s^2/2$.

#### 2.2 Anualizar

Para combinar activos, todo tiene que estar en la misma escala, la anual. Si el año tiene $n$ periodos y los rendimientos de periodos distintos son independientes, la media y la varianza del año son la suma de las de cada periodo (nota de probabilidad, sección 5.2), y

$$\mu_{anual} = n\,\mu_{per}, \qquad \sigma_{anual} = \sigma_{per}\sqrt{n},$$

la raíz del tiempo de la sección 1.2. Para componer un rendimiento, en lugar de sumarlo, se usa la TEA de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md), $1 + TEA = (1 + r_{per})^n$.

**Ejemplo (el S&P 500 en tres frecuencias).** Con los cierres de 1928 a 2025, sin dividendos:

| Frecuencia | $n$ | $s$ por periodo | $s\sqrt{n}$ | Media geométrica por periodo | Anualizada con la TEA |
| ---------- | --- | --------------- | ----------- | ---------------------------- | --------------------- |
| Diaria     | 252 | $1.19\%$        | $18.94\%$   | $0.0242\%$                   | $6.29\%$              |
| Mensual    | 12  | $5.33\%$        | $18.48\%$   | $0.508\%$                    | $6.27\%$              |
| Anual      | 1   | $18.96\%$       | $18.96\%$   | $6.27\%$                     | $6.27\%$              |

**Las tres frecuencias dan casi la misma volatilidad anual, entre 18.5% y 19.0%, y el mismo rendimiento geométrico, 6.3%.** La regla no sirve para los T-bills, cuya tasa de un periodo se parece mucho a la del anterior (sección 2.1).

<!-- diapositivas: conservar -->
- **Anualizar:** $\mu_{anual} = n\mu_{per}$ y $\sigma_{anual} = \sigma_{per}\sqrt{n}$, si los periodos son independientes; en el S&P 500, diaria, mensual y anual dan casi 19%.

### 3. La cartera de media-varianza

**El problema de la cartera.** Un inversionista tiene un capital $a$ y $n$ activos a su alcance. Debe decidir hoy qué fracción $w_i$ de su capital pone en cada uno, con $w_i \geq 0$ para todo $i$ y $w_1 + \dots + w_n = 1$, sin conocer los rendimientos del próximo año, que son variables aleatorias $R_1, \dots, R_n$. El rendimiento de la cartera es

$$R_c = w_1 R_1 + \dots + w_n R_n.$$

Como $R_c$ también es aleatorio, no se puede elegir la cartera que más rendirá, solo la distribución de su rendimiento. Markowitz (1952) propuso resumir esa distribución con dos números, el rendimiento esperado y la varianza, y quedarse con las carteras que dan el mayor rendimiento esperado para cada nivel de varianza. El cambio de fondo fue pasar de preguntar qué acción comprar a preguntar qué cartera tener, porque el riesgo de una cartera no es el promedio del riesgo de sus activos: depende de cómo se mueven juntos.

En esta nota $n = 2$. La cartera principal combina el S&P 500 con los T-bills, y la sección 3.2 cambia los T-bills por FEMSA para ver la diversificación entre dos activos riesgosos. La sección 2 ya dio la media y la volatilidad de cada activo; lo que falta es cómo se mueven juntos, la covarianza.

> **Nota técnica (el espacio de activos).** Las carteras posibles son los vectores de pesos $\mathbf{w} = (w_1, \dots, w_n)$ con $\mathbf{1}^\top \mathbf{w} = 1$. Antes de optimizar hay que fijar dos cosas. La primera es el **universo de inversión**, qué activos entran: los que el inversionista puede comprar según su mandato, la regulación (como el régimen de inversión de las afores), la liquidez y la moneda. La segunda son las **restricciones sobre los pesos**: la de arriba, $w_i \geq 0$, prohíbe las ventas en corto (con $w_i < 0$ se vende en corto, nota 0_, Apéndice C); también puede haber límites por activo o por clase de activo. Con un activo libre de riesgo, su peso es $w_0 = 1 - \sum_{i} w_i$. La frontera eficiente depende de ese espacio: agregar un activo nunca la empeora, porque las carteras que había siguen siendo posibles, y agregar una restricción nunca la mejora.

#### 3.1 Rendimiento y riesgo de una cartera

Con dos activos, la cartera pone $w$ en el activo $A$ y $1 - w$ en el $B$, y su rendimiento es $R_c = wR_A + (1 - w)R_B$. Su media y su varianza dependen de las de cada activo y de cómo se mueven juntos. Esos valores no se conocen, y nada garantiza que el futuro repita el pasado. Se usan estimaciones porque los datos son la única información disponible y porque, si el comportamiento se mantiene, los estimadores se acercan al valor real conforme crece la muestra (sección 5).

> **¿De dónde sale la fórmula?** La esperanza es lineal (nota de probabilidad, sección 4.2), así que $E[wR_A + (1-w)R_B] = wE[R_A] + (1-w)E[R_B]$. Para la varianza, se desarrolla el cuadrado de $w(R_A - \mu_A) + (1-w)(R_B - \mu_B)$ y se toma esperanza término a término: quedan las dos varianzas, cada una por el cuadrado de su peso, y dos veces el producto cruzado, que es la covarianza (sección 5.2).

**Rendimiento y varianza de una cartera de dos activos.** Con $\sigma_{AB} = \rho\,\sigma_A\sigma_B$,

$$E[R_c] = w\mu_A + (1 - w)\mu_B, \qquad \sigma_c^2 = w^2\sigma_A^2 + (1 - w)^2\sigma_B^2 + 2w(1 - w)\rho\,\sigma_A\sigma_B.$$

El rendimiento esperado es el promedio ponderado de los dos; la volatilidad no lo es. Como $\rho \leq 1$, $\sigma_c \leq w\sigma_A + (1 - w)\sigma_B$, con igualdad solo si $\rho = 1$: combinar dos activos nunca da más riesgo que el promedio de sus riesgos, y da menos cuanto menor es la correlación. Es la fórmula detrás de la tabla de la nota de probabilidad (sección 5.2), donde la misma cartera mitad y mitad pasaba de $27.5\%$ de volatilidad con $\rho = 1$ a $12.5\%$ con $\rho = -0.6$.

**La herramienta estadística: la covarianza muestral.** La fórmula pide $\rho$, que no se conoce. Su versión con datos, para dos series observadas en los mismos periodos, es

$$s_{xy} = \frac{1}{n-1}\sum_{t=1}^{n}(x_t - \bar{x})(y_t - \bar{y}), \qquad \hat{\rho}_{x,y} = \frac{s_{xy}}{s_x s_y}.$$

Cada producto es positivo cuando las dos series quedan del mismo lado de su media y negativo cuando quedan de lados opuestos; por eso la muestra tiene que ser de pares del mismo periodo (sección 1.3).

**Ejemplo (FEMSA frente al S&P 500).** Con los 80 rendimientos mensuales de febrero de 2020 a septiembre de 2026, $x_t$ para el S&P 500 (cierres de fin de mes en dólares, sin dividendos) y $y_t$ para FEMSA (precios ajustados por dividendos),

$$s_x = 4.89\%, \qquad s_y = 6.35\%, \qquad s_{xy} = 0.000981, \qquad \hat{\rho}_{x,y} = \frac{0.000981}{0.0489 \times 0.0635} = 0.32.$$

En el panel izquierdo de la figura la nube se inclina hacia arriba, pero poco: FEMSA comparte con el mercado estadounidense parte de su riesgo, como la caída de marzo de 2020, el punto de abajo a la izquierda, y el resto es propio de México y de la emisora. El panel derecho muestra cómo luce la falta de relación: dos ruidos blancos independientes con las mismas desviaciones estándar, con correlación muestral de 0.03. Contar puntos no los distingue; lo que los distingue es el tamaño de los productos $(x_t - \bar{x})(y_t - \bar{y})$, que en los datos caen del mismo lado en los meses de movimientos grandes y en el ruido blanco se cancelan. **Con una correlación de 0.32, combinar FEMSA con el S&P 500 sí reduce el riesgo**, y es la pareja con la que la sección 3.2 traza la frontera.

<!-- diapositivas: figura sola -->
![Dos diagramas de dispersión lado a lado, en la misma escala, cada uno con una línea vertical y una horizontal en las medias que dividen el plano en cuatro cuadrantes, puntos dorados del mismo lado de las dos medias y grises en lados opuestos. A la izquierda, 80 rendimientos mensuales de febrero de 2020 a septiembre de 2026, con el S&P 500 en el eje horizontal y FEMSA en el vertical: 40 puntos dorados y 40 grises en una nube poco inclinada, con un punto aislado abajo a la izquierda, marzo de 2020, y otro arriba a la derecha; el título indica una correlación de 0.32. A la derecha, 80 pares simulados de dos ruidos blancos normales e independientes, con media 0 y las desviaciones estándar del S&P 500 y de FEMSA: 48 puntos dorados y 32 grises en una nube redonda sin inclinación; el título indica una correlación de 0.03](img/femsa_sp500_ruido_blanco_dispersion.png)

**Ejemplo (la cartera del hilo).** Entre el S&P 500 y los T-bills, de 1928 a 2025, $s_{AB} = -0.000126$ y $\hat{\rho} = -0.02$: prácticamente no se mueven juntos. Con la mitad en cada uno y los estadísticos de la sección 2,

$$\bar{x}_c = 0.5 \times 11.86\% + 0.5 \times 3.42\% = 7.64\%, \qquad s_c = \sqrt{0.25 \times 0.1940^2 + 0.25 \times 0.0304^2 + 2 \times 0.25 \times (-0.000126)} = 9.79\%.$$

**La cartera mitad y mitad rinde en promedio 7.64% con una volatilidad de 9.79%**: la mitad de la volatilidad del S&P 500, a cambio de 4.22 puntos menos de rendimiento. La volatilidad casi coincide con $w s_A = 9.70\%$ porque los T-bills casi no varían y no se mueven con el índice; es la recta de la sección 3.3. Calcular la serie $0.5x_t + 0.5y_t$ año por año da exactamente las mismas dos cifras: la fórmula también es una identidad con los datos.

La media muestral es una cartera del mismo tipo, con peso $1/n$ en cada año: $\bar{x} = \tfrac{1}{n}x_1 + \dots + \tfrac{1}{n}x_n$. La sección 5 usa la misma fórmula de la varianza para saber cuánto se equivoca.

> **Nota técnica ($n$ activos).** Con el vector de pesos $\mathbf{w}$, el de rendimientos esperados $\boldsymbol{\mu}$ y la matriz de varianzas y covarianzas $\boldsymbol{\Sigma}$ de la nota de probabilidad (sección 5.2), $E[R_c] = \mathbf{w}^\top\boldsymbol{\mu}$ y $\sigma_c^2 = \mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$. Con $n = 2$ se recupera la fórmula de arriba. Con $n$ activos hay $n(n-1)/2$ covarianzas que estimar, lo que la sección 5 vuelve un problema.

<!-- diapositivas: conservar -->
- **Rendimiento:** el promedio ponderado, $E[R_c] = w\mu_A + (1-w)\mu_B$.
- **Riesgo:** $\sigma_c^2 = w^2\sigma_A^2 + (1-w)^2\sigma_B^2 + 2w(1-w)\rho\sigma_A\sigma_B$; menor que el promedio de las volatilidades salvo si $\rho = 1$.
- **Con datos:** la correlación muestral; S&P 500 y T-bills, $-0.02$; FEMSA y S&P 500, $0.32$.
- **Mitad y mitad:** 7.64% de rendimiento esperado y 9.79% de volatilidad.

#### 3.2 Diversificación y frontera eficiente

**El problema de Markowitz.** Entre todas las carteras con el mismo rendimiento esperado $m$, se elige la de menor varianza:

$$\min_{w}\ \sigma_c^2 \quad \text{sujeto a} \quad E[R_c] = m.$$

O, al revés, entre todas las carteras con la misma varianza $k$, se elige la de mayor rendimiento esperado:

$$\max_{w}\ E[R_c] \quad \text{sujeto a} \quad \sigma_c^2 = k.$$

Al resolver el primer problema para cada $m$ y graficar la volatilidad mínima contra $m$ se obtiene la **frontera de mínima varianza**. Su parte de arriba, donde ninguna cartera da más rendimiento esperado con el mismo riesgo, es la **frontera eficiente**, y es la misma que da el segundo problema.

Con dos activos no hace falta optimizar: si $\mu_A \neq \mu_B$, la restricción $E[R_c] = m$ solo se cumple con $w = (m - \mu_B)/(\mu_A - \mu_B)$. Cada $m$ corresponde a una sola cartera, así que la frontera es la curva que dibujan $\sigma_c$ y $E[R_c]$ al mover $w$.

La figura lo muestra con el S&P 500 y FEMSA del ejemplo de abajo. A la izquierda, fijar $m$ deja una sola cartera, aunque sea ineficiente; a la derecha, fijar la volatilidad deja dos, y el segundo problema elige la de arriba.

<!-- diapositivas: figura sola -->
![Dos paneles con la misma curva de carteras entre FEMSA y el S&P 500, con la volatilidad en el eje horizontal y el rendimiento esperado en el vertical: va de FEMSA, en 21.98% y 9.30%, a la cartera de mínima varianza, con 68.3% en el S&P 500, en 15.28% y 12.81%, como línea gris de rayas (parte ineficiente), y de ahí al S&P 500, en 16.95% y 14.45%, como línea azul sólida (frontera eficiente). En el panel izquierdo, Mínima varianza con E[R_c] = m, una recta dorada horizontal en 11.87% corta la curva en un solo punto, la cartera con 50% en el S&P 500 y volatilidad de 15.86%, marcada como ineficiente. En el panel derecho, Máximo rendimiento con σ_c² = k, una recta dorada vertical en 15.86% corta la curva en dos puntos: abajo la de 50%, con 11.87%, que se descarta, y arriba la de 86.6%, con 13.76%, de mayor rendimiento esperado](img/markowitz_dos_problemas_frontera.png)

> **¿De dónde sale la fórmula?** La varianza de la 3.1 es una parábola en $w$. Su derivada es $2w\sigma_A^2 - 2(1-w)\sigma_B^2 + 2(1-2w)\sigma_{AB}$; al igualarla a cero y despejar sale el peso de la fórmula. La segunda derivada, $2(\sigma_A^2 + \sigma_B^2 - 2\sigma_{AB}) = 2\operatorname{Var}(R_A - R_B)$, es positiva salvo que $R_A - R_B$ sea constante, así que el punto es un mínimo.

**Definición (cartera de mínima varianza).** Es la cartera de menor varianza entre todas las posibles, la punta izquierda de la frontera, con

$$w_{min} = \frac{\sigma_B^2 - \sigma_{AB}}{\sigma_A^2 + \sigma_B^2 - 2\sigma_{AB}}, \qquad \sigma_A^2 + \sigma_B^2 - 2\sigma_{AB} > 0.$$

Si $\mu_A > \mu_B$, las carteras con $w \geq w_{min}$ forman la frontera eficiente. Las de $w < w_{min}$ son ineficientes: alguna cartera con el mismo riesgo rinde más.

**Ejemplo (S&P 500 y FEMSA).** Con los 80 meses de la sección 3.1, la media y la varianza mensuales se multiplican por 12, como en la 2.2, para llevarlas a escala anual sin cambiar la fórmula de la cartera: $\mu_A = 14.45\%$ y $\sigma_A = 16.95\%$ para el S&P 500, $\mu_B = 9.30\%$ y $\sigma_B = 21.98\%$ para FEMSA, y $\rho = 0.32$.

| $w$ en el S&P 500      | $E[R_c]$  | $\sigma_c$ |
| ---------------------- | --------- | ---------- |
| $0\%$ (solo FEMSA)     | $9.30\%$  | $21.98\%$  |
| $25\%$                 | $10.58\%$ | $18.27\%$  |
| $50\%$                 | $11.87\%$ | $15.86\%$  |
| $68.3\%$               | $12.81\%$ | $15.28\%$  |
| $75\%$                 | $13.16\%$ | $15.36\%$  |
| $100\%$ (solo S&P 500) | $14.45\%$ | $16.95\%$  |

**La cartera de mínima varianza pone 68.3% en el S&P 500 y 31.7% en FEMSA, con una volatilidad de 15.28%, menor que la de cualquiera de los dos por separado.** Esa es la diversificación: con una correlación de 0.32, las caídas de uno se compensan en parte con el otro. FEMSA sola es ineficiente, porque la cartera mitad y mitad rinde más con menos riesgo. La frontera eficiente va de $68.3\%$ a $100\%$ en el S&P 500. Las cifras vienen de solo 80 meses y mezclan dólares con pesos; la sección 5 mide cuánto confiar en ellas.

> **Nota técnica (frontera con $n$ activos).** El problema es $\min_{\mathbf{w}} \mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ sujeto a $\mathbf{w}^\top\boldsymbol{\mu} = m$ y $\mathbf{1}^\top\mathbf{w} = 1$, y se resuelve con multiplicadores de Lagrange. Con $a = \mathbf{1}^\top\boldsymbol{\Sigma}^{-1}\mathbf{1}$, $b = \mathbf{1}^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}$, $c = \boldsymbol{\mu}^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}$ y $d = ac - b^2 > 0$, la varianza mínima para cada $m$ es $\sigma^2(m) = (am^2 - 2bm + c)/d$, una hipérbola en el plano $(\sigma, m)$, y la cartera de mínima varianza es $\mathbf{w}_{min} = \boldsymbol{\Sigma}^{-1}\mathbf{1}/a$ (Merton, 1972). Si se prohíben las ventas en corto, $w_i \geq 0$, ya no hay fórmula cerrada y se resuelve numéricamente como un programa cuadrático.

<!-- diapositivas: conservar -->
- **Problema de Markowitz:** para cada rendimiento esperado, la cartera de menor varianza; las de arriba forman la frontera eficiente.
- **Mínima varianza:** $w_{min} = (\sigma_B^2 - \sigma_{AB})/(\sigma_A^2 + \sigma_B^2 - 2\sigma_{AB})$.
- **S&P 500 y FEMSA:** 68.3% en el S&P 500 da 15.28% de volatilidad, menos que cualquiera de los dos solo.

#### 3.3 El activo libre de riesgo y la proporción elegida

**La recta.** Para la decisión de un año, el T-bill rinde una tasa conocida $r_f$, así que su varianza y su covarianza con el S&P 500 se toman como cero (sección 2.1). Con $\sigma_B = 0$ en la 3.1, $E[R_c] = r_f + w(\mu_A - r_f)$ y $\sigma_c = w\sigma_A$; al eliminar $w$,

$$E[R_c] = r_f + \frac{\mu_A - r_f}{\sigma_A}\,\sigma_c,$$

la **línea de asignación de capital**. Su pendiente es la **razón de Sharpe** (Sharpe, 1966), el premio por cada punto de volatilidad: en el hilo, $(11.86\% - 3.42\%)/19.40\% = 0.435$. Falta elegir el punto de la recta, y hay dos formas usuales.

**Con un límite de volatilidad.**

$$\max_{w}\ E[R_c] \quad \text{sujeto a} \quad \sigma_c \leq \sigma_{max}.$$

Si $\mu_A > r_f$, $E[R_c]$ crece con $w$, así que se usa todo el riesgo permitido: $w = \sigma_{max}/\sigma_A$. **Con $\sigma_{max} = 10\%$, $w = 51.5\%$ y $E[R_c] = 7.76\%$.**

**Con aversión al riesgo.** Un coeficiente $\gamma > 0$ penaliza la varianza:

$$\max_{w}\ E[R_c] - \frac{\gamma}{2}\sigma_c^2 \quad \Longrightarrow \quad w^* = \frac{\mu_A - r_f}{\gamma\,\sigma_A^2},$$

que sale de igualar a cero la derivada, $\mu_A - r_f - \gamma w\sigma_A^2$. **Con $\gamma = 4$, $w^* = 0.0844/(4 \times 0.1940^2) = 56.0\%$**, con $E[R_c] = 8.15\%$ y $\sigma_c = 10.87\%$. Con $\gamma = 2$ saldría $112\%$, un peso negativo en los T-bills (pedir prestado), que la restricción $w_i \geq 0$ deja en $100\%$.

**Separación (Tobin, 1958).** Con varios activos riesgosos, la mejor recta es la de mayor razón de Sharpe, la que toca la frontera eficiente en la **cartera tangente**. La decisión se separa en dos pasos: elegir la cartera tangente, que es la misma para todos, y repartir entre ella y los T-bills con $\sigma_{max}$ o con $\gamma$, lo único que depende del inversionista.

> **Nota técnica (cartera tangente).** $\mathbf{w}_{tan} = \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} - r_f\mathbf{1}) / \mathbf{1}^\top\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} - r_f\mathbf{1})$ maximiza la razón de Sharpe cuando el denominador es positivo. Con aversión $\gamma$, la parte en activos riesgosos es $\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} - r_f\mathbf{1})/\gamma$, proporcional a $\mathbf{w}_{tan}$; con $n = 1$ se recupera $w^*$.

Las dos proporciones usan estimaciones: la primera solo $\sigma_A$, y la segunda depende linealmente de $\mu_A - r_f$, lo que peor se estima (sección 5).

<!-- diapositivas: conservar -->
- **Recta:** $E[R_c] = r_f + \text{Sharpe} \times \sigma_c$; en el hilo, la razón de Sharpe es 0.435.
- **Dos formas de elegir:** con un límite de 10% de volatilidad, $w = \sigma_{max}/\sigma_A = 51.5\%$; con aversión $\gamma = 4$, $w^* = (\mu_A - r_f)/(\gamma\sigma_A^2) = 56.0\%$.
- **Separación:** primero la cartera tangente, igual para todos; después cuánto en ella, según el inversionista.

### 4. Las carteras de media-VaR y media-CVaR

La varianza cuenta igual los años buenos y los malos, así que un activo puede tener una varianza grande con rendimientos casi siempre positivos. Uno que rinde 2% o 40% con la misma probabilidad tiene una volatilidad de 19%, como la del S&P 500, sin un solo año de pérdida. Al inversionista le preocupa la cola de pérdidas, no la dispersión hacia arriba.

#### 4.1 La cartera de media-VaR

**Definición (VaR de la cartera).** Para un nivel $p$, el VaR es la pérdida que solo se supera con probabilidad $p$: $\text{VaR}_p(R_c) = -q_p(R_c)$, con $q_p$ el cuantil de la nota de probabilidad (sección 6.1).

**El problema.**

$$\max_{w}\ E[R_c] \quad \text{sujeto a} \quad \text{VaR}_p(R_c) \leq \ell,$$

donde $\ell$ es la pérdida máxima que el inversionista acepta. La idea viene de Roy (1952), que propuso elegir la cartera con la menor probabilidad de caer por debajo de un nivel de desastre $d$, $P(R_c < d)$, en lugar de la de menor varianza. El problema de media-VaR invierte los papeles: fija la pérdida $\ell$ y pide que la probabilidad de perder más que ella no pase de $p$, porque $\text{VaR}_p(R_c) \leq \ell$ equivale a $P(R_c < -\ell) \leq p$. Así usa el VaR la regulación (Jorion, 2007). Campbell, Huisman y Koedijk (2001) lo plantean así para repartir entre acciones y bonos, y Alexander y Baptista (2002) muestran que la cartera elegida por VaR puede tener más volatilidad que la elegida por varianza. El cuantil de la cartera no sale de la media y la varianza de cada activo: hace falta la distribución conjunta, o los datos de la sección 5.

**Ejemplo (el S&P 500 y los T-bills).** Con los 98 años de la sección 2.1, el rendimiento de la cartera en cada año es $wx_t + (1 - w)y_t$, y su VaR al 5% es la pérdida del quinto peor año, como en la nota de probabilidad (sección 6.1). Con todo en el S&P 500, el quinto peor año es 1930, con $-25.12\%$, y el VaR es de $25.12\%$. Al bajar $w$ baja el VaR, y se busca la mayor $w$ que cumple el límite. **Con $\ell = 10\%$, la cartera pone $w = 49.3\%$ en el S&P 500, con un rendimiento esperado estimado de $7.58\%$.** Sus cinco peores años son 1931, 2008, 1937, 1930 y 2002, y el quinto, 2002, perdió justo $10.00\%$. Con el límite de volatilidad de 10% de la 3.3, la proporción era de $51.5\%$.

En la figura, cada $w$ da un punto con el VaR de la cartera y su rendimiento esperado estimado; la franja son las carteras que cumplen el límite, y el problema elige la de más rendimiento dentro de ella.

<!-- diapositivas: figura sola -->
![Curva de las carteras entre los T-bills y el S&P 500 de 1928 a 2025, con el VaR al 5% de la cartera, como pérdida, en el eje horizontal y el rendimiento esperado estimado en el vertical: va de solo T-bills, con un VaR cercano a 0% y 3.42%, a solo S&P 500, con un VaR de 25.12% y 11.86%, siempre creciente; una franja dorada a la izquierda de una línea punteada en el límite de 10% marca las carteras permitidas, y un punto dorado sobre la línea marca la elegida, con 49.3% en el S&P 500 y un rendimiento esperado de 7.58%](img/sp500_tbills_media_var.png)

**El límite del VaR.** Dice dónde empieza la cola, pero no qué tan malos son los años que caen en ella, y puede castigar la diversificación.

> **Nota técnica (el VaR no es subaditivo).** Dos bonos independientes, cada uno con probabilidad de incumplir de 4%: el VaR al 95% de cada uno es 0, porque incumplir es menos probable que 5%. En la cartera con los dos, la probabilidad de que al menos uno incumpla es $1 - 0.96^2 = 7.84\% > 5\%$, y el VaR de la cartera es positivo: mayor que la suma de los VaR (Artzner et al., 1999).

<!-- diapositivas: conservar -->
- **Problema:** máximo rendimiento esperado con $\text{VaR}_p(R_c) \leq \ell$; viene de Roy, que limitaba la probabilidad de un desastre en lugar de la varianza.
- **S&P 500 y T-bills:** con un VaR al 5% de a lo más 10%, 49.3% en el S&P 500.
- **Límite:** el VaR no mira dentro de la cola y puede castigar la diversificación.

#### 4.2 La cartera de media-CVaR

**Definición (CVaR de la cartera).** Es la pérdida promedio en el peor $100p\%$ de los casos: $\text{CVaR}_p(R_c) = -E[R_c \mid R_c \leq q_p(R_c)]$ (nota de probabilidad, sección 6.2). Nunca es menor que el VaR.

**El problema.**

$$\max_{w}\ E[R_c] \quad \text{sujeto a} \quad \text{CVaR}_p(R_c) \leq \ell.$$

Krokhmal, Palmquist y Uryasev (2002) lo plantean así, maximizando el rendimiento esperado con uno o varios límites de CVaR, y Alexander y Baptista (2004) muestran que, con el mismo nivel $p$ y el mismo límite $\ell$, la restricción de CVaR es más estricta que la de VaR.

**Ejemplo (el S&P 500 y los T-bills).** Con los mismos años, el CVaR al 5% es el promedio de las pérdidas de los cinco peores años; con todo en el S&P 500 es de $33.35\%$ (nota de probabilidad, sección 6.2). **Con $\ell = 10\%$, la cartera pone $w = 34.8\%$ en el S&P 500, con un rendimiento esperado estimado de $6.35\%$**: 14.5 puntos menos en acciones que con el VaR, porque el límite se aplica al promedio de los cinco peores años y no solo al quinto.

La figura repite la de la sección 4.1 con el CVaR: su curva queda a la derecha de la del VaR, porque el CVaR nunca es menor, y por eso cruza el límite con menos acciones.

<!-- diapositivas: figura sola -->
![Dos curvas de las carteras entre los T-bills y el S&P 500 de 1928 a 2025, con la pérdida al 5% en el eje horizontal y el rendimiento esperado estimado en el vertical: la del CVaR, sólida, va de solo T-bills, cerca de 0% y 3.42%, a solo S&P 500, con un CVaR de 33.35% y 11.86%; la del VaR, gris de rayas, queda a su izquierda y termina en 25.12%. Una franja dorada a la izquierda del límite de 10% marca las carteras permitidas; la curva del CVaR lo cruza en 34.8% en el S&P 500, con un rendimiento esperado de 6.35%, y la del VaR, más arriba, en 49.3%](img/sp500_tbills_media_cvar.png)

**Por qué el CVaR.** Una **medida de riesgo** es una regla $\rho$ que a cada pérdida aleatoria $L$ le asigna un número $\rho(L)$, como el capital que conviene reservar para cubrirla; la volatilidad, el VaR y el CVaR son medidas de riesgo. Artzner, Delbaen, Eber y Heath (1999) piden cuatro propiedades a una medida de riesgo para llamarla coherente: **monotonía**, más pérdida da más riesgo; **subaditividad**, diversificar no aumenta el riesgo; **homogeneidad positiva**, el doble de posición da el doble de riesgo; e **invariancia ante traslaciones**, una pérdida segura se suma tal cual al riesgo. El CVaR las cumple (Acerbi y Tasche, 2002); el VaR falla la subaditividad. Por eso Basilea cambió el VaR al 99% por el déficit esperado al 97.5% en el capital por riesgo de mercado (Comité de Supervisión Bancaria de Basilea, 2019).

> **Nota técnica (coherencia).** Para pérdidas $L_1$ y $L_2$, las cuatro propiedades son: monotonía, si $L_1 \leq L_2$ siempre, $\rho(L_1) \leq \rho(L_2)$; subaditividad, $\rho(L_1 + L_2) \leq \rho(L_1) + \rho(L_2)$; homogeneidad positiva, $\rho(\lambda L) = \lambda\rho(L)$ para $\lambda \geq 0$; e invariancia ante traslaciones, $\rho(L + c) = \rho(L) + c$ para una constante $c$.

> **Nota técnica (Rockafellar y Uryasev).** Con la pérdida $L = -R_c$, $\text{CVaR}_p = \min_{c} \{c + \tfrac{1}{p}E[(L - c)^+]\}$, y el mínimo se alcanza en el VaR. Con los años observados como escenarios, la esperanza es un promedio, y elegir la cartera con un límite de CVaR es un programa lineal (Rockafellar y Uryasev, 2000, 2002); el planteamiento va en el Apéndice.

<!-- diapositivas: conservar -->
- **Problema:** máximo rendimiento esperado con $\text{CVaR}_p(R_c) \leq \ell$.
- **Coherente:** el CVaR cumple las cuatro propiedades de Artzner et al.; es el estándar de Basilea.
- **Más estricto:** con un CVaR al 5% de a lo más 10%, 34.8% en el S&P 500, 14.5 puntos menos que con el VaR.

### 5. Estimar y comparar con datos

Pregunta de la sección: las secciones 3 y 4 plantearon los problemas con parámetros que se estiman; aquí se mide el error de esas estimaciones, se calculan el VaR y el CVaR con los datos y se comparan las tres carteras. La estadística entra como medida del error, no como fin.

#### 5.1 Estimadores y error estándar

(Se condensa 2_ §3.1 y §3.3.) El estimador como variable aleatoria; la media muestral como la cartera de los años de la sección 3.1, de modo que su varianza sale con la misma fórmula: $\operatorname{Var}(\bar{X}) = \sigma^2/n$ y el error estándar es $s/\sqrt{n}$. Sesgo.

> **Nota técnica (principios de estimación).** Sustitución, máxima verosimilitud y Bayes, con el analista de $8\% \pm 2\%$ que da $9.97\%$; se migra de 2_ §3.1 en forma compacta, con el desarrollo en el Apéndice.

#### 5.2 Por qué funciona: ley de los grandes números y teorema central del límite

(Se condensa 2_ §4.1 y §4.2.) En el cuerpo, solo los dos enunciados y lo que dicen de la cartera: con más años, $\bar{x}$ se acerca a $\mu$, y su error es aproximadamente normal.

> **Nota técnica (convergencia).** Convergencia en probabilidad y desigualdad de Chebyshev, Glivenko-Cantelli para la distribución empírica (la base del VaR histórico de la sección 5.5), convergencia en distribución y Slutsky para usar $s$ en lugar de $\sigma$. Se migra de 2_ §4.1-4.2 como enunciados con una línea de intuición cada uno.

#### 5.3 El intervalo de confianza y la cartera

- Intervalo de Wald para $\mu$ (se migra de 2_ §4.3): **de 8.01% a 15.70% al 95%**.
- **Llevarlo a la cartera:** con $w = 51.5\%$, el rendimiento esperado de la cartera, $r_f + w(\mu - r_f)$, hereda el intervalo; la proporción elegida con un límite de volatilidad no depende de $\mu$, pero lo que se le promete al inversionista sí.
- **El error de estimación en la optimización:** si la proporción se eligiera maximizando media menos varianza, cambiaría mucho dentro del intervalo. Chopra y Ziemba (1993) encontraron que los errores en las medias dañan la cartera más de diez veces que los errores en las varianzas; Michaud (1989) llamó al optimizador un "maximizador de errores", y DeMiguel, Garlappi y Uppal (2009) estiman que, con 25 activos, harían falta unos 3,000 meses de datos para que la cartera estimada supere a repartir en partes iguales ($1/N$).

> **Nota técnica (sensibilidad de la proporción óptima).** La $w^* = (\mu - r_f)/(\gamma\sigma^2)$ de la sección 3.3 es lineal en $\mu - r_f$, así que el ancho del intervalo de $\mu$ pasa completo a $w^*$: con $\gamma = 4$, los extremos de 8.01% y 15.70% darían proporciones de 30.5% y 81.6% en el S&P 500.

#### 5.4 Dinámica: la bolsa del S&P 500

(Se migra de 2_ §4.4.) La práctica en clase: estimar con 4, con 20 y con todo el grupo, y ver el error estándar en acción.

#### 5.5 El VaR y el CVaR con los datos

(Se migra de 2_ §2.2, §3.2 y la parte de remuestreo de §4.3.) Distribución empírica, cuantil empírico y VaR histórico; el VaR con la normal, con la Cauchy y con los datos. Las proporciones de los ejemplos de las secciones 4.1 y 4.2 dependen de los cinco peores años. Intervalo por remuestreo (Efron, 1979): con 98 años, el CVaR al 5% promedia solo unos cinco datos, y su intervalo es ancho. Las colas pesadas, que la nota de hechos estilizados documenta, hacen que el CVaR pida menos acciones que la volatilidad.

#### 5.6 Comparar las tres carteras

- **Las tres proporciones:** con un límite de 10%, $51.5\%$ en el S&P 500 con la volatilidad (sección 3.3), $49.3\%$ con el VaR (sección 4.1) y $34.8\%$ con el CVaR (sección 4.2).
- **Cierre del objetivo:** tabla con la proporción elegida con volatilidad, VaR y CVaR para el mismo inversionista, con los datos, el rendimiento esperado de cada cartera y su intervalo, con las cifras en negritas.

## Apéndice: Complementos

(Se migra el Apéndice de 2_.) Con la reestructura recibe además la frontera de $n$ activos con solución cerrada (Merton, 1972), el desarrollo de los principios de estimación y de la convergencia, y el programa lineal del CVaR. De la sección 2.2 salen, como material opcional, la varianza de una suma con correlación, $n\sigma^2[1 + 2\sum_{k}(1 - k/n)\rho_k]$, y el efecto de los dividendos, que suman 3.75 puntos al rendimiento geométrico del S&P 500. Al migrar, la nota de probabilidad (sección 5.2) deja de decir "la fórmula se ve en la 3_" y apunta a la sección 3.1 de esta nota. Recibe también lo que sale de la sección 1.3: la población como lista finita (emisoras de la BMV), por qué el muestreo sin reemplazo no da una muestra aleatoria y la regla del 5%, la independencia escrita como probabilidad condicional, y los ejemplos de registro (precios rancios de acciones poco operadas, la autocorrelación que crea el promedio mensual de Shiller, las fechas de FEMSA y las observaciones de Linton sobre 1987 y 2008). De la sección 1.4 recibe: la teoría de valores extremos como modelo semiparamétrico, la escritura formal del modelo bayesiano y su a posteriori, los dos extremos del espacio de modelos (una sola distribución y todas) con la normal y la Cauchy como hilos, la diferencia entre independientes y no correlacionados, las filas de Gordon e incumplimientos de la tabla de modelos clásicos, y la identificabilidad con el ejemplo de Gordon. De la sección 1.5 recibe las filas de clasificación y agrupamiento de la tabla de problemas, y que la estimación puntual también puede apuntar a la distribución completa o a un valor futuro. Se agregan la cartera de $n$ activos en forma matricial, $\sigma_c^2 = \mathbf{w}^\top \Sigma \mathbf{w}$; la minimización del CVaR como programa lineal; y la línea del mercado de capitales con el CAPM, solo como mención.

## Fuentes y referencias recomendadas

(Se migran las de 2_; de las de 4_ se quedan Luenberger, Linton y las de teoría de portafolios, ya listadas abajo, y Sharpe (1964), Mehra y Prescott, Fama y French y Bessembinder pasan a la nota de valuación.) Abajo, las de la sección 1 y las de teoría de portafolios de las secciones 3 a 5, verificadas entre el 2026-10-31 y el 2026-11-04 salvo Markowitz (1952), Tobin (1958), Sharpe (1966), Merton (1972), Artzner et al. (1999), Rockafellar y Uryasev (2000) y Jorion (2007), citadas de memoria y por verificar:

- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 17, 21-86: el cambio de precio como variable aleatoria.
- Cowles, A. (1933). Can stock market forecasters forecast? *Econometrica*, 1(3), 309-324: los pronosticadores profesionales no superan al azar.
- Keynes, J. M. (1936). *The General Theory of Employment, Interest and Money*. Macmillan: el mercado como concurso de belleza.
- Williams, J. B. (1938). *The Theory of Investment Value*. Harvard University Press: el precio como valor presente de los dividendos esperados.
- Kendall, M. G. (1953). The analysis of economic time series, Part I: Prices. *Journal of the Royal Statistical Society, Series A*, 116(1), 11-34: los cambios de precio parecen aleatorios.
- Osborne, M. F. M. (1959). Brownian motion in the stock market. *Operations Research*, 7(2), 145-173: la caminata aleatoria sobre el logaritmo del precio.
- Samuelson, P. A. (1965). Proof that properly anticipated prices fluctuate randomly. *Industrial Management Review*, 6(2), 41-49: si el precio incorpora lo esperado, su cambio es impredecible.
- Hayek, F. A. (1989). The pretence of knowledge. *American Economic Review*, 79(6), 3-7: ante fenómenos complejos solo se predicen patrones (conferencia Nobel de 1974).
- Harris, L., & Gurel, E. (1986). Price and volume effects associated with changes in the S&P 500 list: New evidence for the existence of price pressures. *Journal of Finance*, 41(4), 815-829: la subida al entrar al índice se revierte.
- Shleifer, A. (1986). Do demand curves for stocks slope down? *Journal of Finance*, 41(3), 579-590: la entrada al S&P 500 como choque de demanda sin información.
- Campbell, J. Y., & Shiller, R. J. (1988). The dividend-price ratio and expectations of future dividends and discount factors. *Review of Financial Studies*, 1(3), 195-228: el rendimiento como noticias de flujos y de tasa de descuento.
- Cutler, D. M., Poterba, J. M., & Summers, L. H. (1989). What moves stock prices? *Journal of Portfolio Management*, 15(3), 4-12: las noticias explican menos de un tercio de la varianza.
- Bernanke, B. S., & Kuttner, K. N. (2005). What explains the stock market's reaction to Federal Reserve policy? *Journal of Finance*, 60(3), 1221-1257: la política monetaria mueve el índice por la prima de riesgo.
- Cochrane, J. H. (2011). Presidential address: Discount rates. *Journal of Finance*, 66(4), 1047-1108: la tasa de descuento domina la variación de la razón precio-dividendo.
- Boudoukh, J., Feldman, R., Kogan, S., & Richardson, M. (2019). Information, trading, and volatility: Evidence from firm-specific news. *Review of Financial Studies*, 32(3), 992-1033: las noticias de la emisora explican cerca de la mitad de la volatilidad nocturna.
- Baker, S. R., Bloom, N., Davis, S. J., & Sammon, M. (2021). *What triggers stock market jumps?* (NBER Working Paper No. 28687). National Bureau of Economic Research: los detonantes de los saltos del mercado según la prensa.
- Gabaix, X., & Koijen, R. S. J. (2021). *In search of the origins of financial fluctuations: The inelastic markets hypothesis* (NBER Working Paper No. 28967). National Bureau of Economic Research: un dólar que entra al mercado eleva su valor en unos cinco.
- Markowitz, H. (1952). Portfolio selection. *Journal of Finance*, 7(1), 77-91: la cartera se elige por su media y su varianza, que dependen de las covarianzas.
- Roy, A. D. (1952). Safety first and the holding of assets. *Econometrica*, 20(3), 431-449: elegir la cartera que minimiza la probabilidad de un desastre.
- Tobin, J. (1958). Liquidity preference as behavior towards risk. *Review of Economic Studies*, 25(2), 65-86: con un activo libre de riesgo, todos combinan la misma cartera riesgosa.
- Sharpe, W. F. (1966). Mutual fund performance. *Journal of Business*, 39(1), 119-138: la razón de Sharpe.
- Merton, R. C. (1972). An analytic derivation of the efficient portfolio frontier. *Journal of Financial and Quantitative Analysis*, 7(4), 1851-1872: la frontera de $n$ activos con solución cerrada.
- Michaud, R. O. (1989). The Markowitz optimization enigma: Is "optimized" optimal? *Financial Analysts Journal*, 45(1), 31-42: el optimizador como maximizador de errores.
- Chopra, V. K., & Ziemba, W. T. (1993). The effect of errors in means, variances, and covariances on optimal portfolio choice. *Journal of Portfolio Management*, 19(2), 6-11: los errores en las medias pesan más de diez veces que los de las varianzas.
- Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1999). Coherent measures of risk. *Mathematical Finance*, 9(3), 203-228: las propiedades de una medida de riesgo coherente.
- Rockafellar, R. T., & Uryasev, S. (2000). Optimization of conditional value-at-risk. *Journal of Risk*, 2(3), 21-41: elegir la cartera de menor CVaR como un programa lineal.
- Campbell, R., Huisman, R., & Koedijk, K. (2001). Optimal portfolio selection in a Value-at-Risk framework. *Journal of Banking & Finance*, 25(9), 1789-1804: el problema de media-VaR entre acciones y bonos; con la normal, casi la misma cartera que la de media-varianza.
- Acerbi, C., & Tasche, D. (2002). On the coherence of expected shortfall. *Journal of Banking & Finance*, 26(7), 1487-1503: el déficit esperado es coherente.
- Alexander, G. J., & Baptista, A. M. (2002). Economic implications of using a mean-VaR model for portfolio selection: A comparison with mean-variance analysis. *Journal of Economic Dynamics and Control*, 26(7-8), 1159-1193: elegir por VaR cambia la cartera frente a elegir por varianza.
- Rockafellar, R. T., & Uryasev, S. (2002). Conditional value-at-risk for general loss distributions. *Journal of Banking & Finance*, 26(7), 1443-1471: el CVaR para distribuciones con saltos, como las de datos históricos.
- Krokhmal, P., Palmquist, J., & Uryasev, S. (2002). Portfolio optimization with conditional value-at-risk objective and constraints. *Journal of Risk*, 4(2), 43-68: el problema de media-CVaR, con el máximo rendimiento esperado sujeto a límites de CVaR.
- Alexander, G. J., & Baptista, A. M. (2004). A comparison of VaR and CVaR constraints on portfolio selection with the mean-variance model. *Management Science*, 50(9), 1261-1273: con el mismo nivel y el mismo límite, la restricción de CVaR es más estricta que la de VaR.
- Jorion, P. (2007). *Value at Risk: The New Benchmark for Managing Financial Risk* (3ª ed.). McGraw-Hill: VaR de una cartera, histórico y normal.
- DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy? *Review of Financial Studies*, 22(5), 1915-1953: con 25 activos harían falta unos 3,000 meses de datos para superar a $1/N$.
- Comité de Supervisión Bancaria de Basilea. (2019). *Minimum capital requirements for market risk*. Banco de Pagos Internacionales: el déficit esperado al 97.5% sustituye al VaR al 99%.

## Cierre de la unidad — Lo esencial para recordar

> **Por redactar.** Tres o cuatro puntos que vayan de qué mueve el precio a la proporción elegida con volatilidad, VaR y CVaR.
