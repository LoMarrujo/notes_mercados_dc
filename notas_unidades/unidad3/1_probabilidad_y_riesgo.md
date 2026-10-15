# Unidad 3 · Probabilidad y Riesgo

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante calcule el rendimiento esperado y la desviación estándar de una acción a partir de escenarios con probabilidad.

## Contenido

|      | Tema                                | Qué cubre                                                                                                                                                                                                                                                                       |
| ---- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I    | Un juego interrumpido               | El problema de los puntos: cómo repartir la apuesta de un juego que se detiene antes de terminar (Pacioli, Cardano); la correspondencia de Pascal y Fermat en 1654 lo resuelve repartiendo según la probabilidad de ganar de cada jugador                                       |
| II   | De los dados a los axiomas          | Huygens (1657) llama esperanza al valor justo de una apuesta y Kolmogorov (1933) da los axiomas con los que hoy se define la probabilidad                                                                                                                                       |
| III  | La dirección contraria: estadística | La probabilidad parte del modelo y predice los datos; la estadística parte de los datos e infiere el modelo. Graunt (1662) y sus tablas de mortalidad, la ley de los grandes números de Bernoulli (1713) como puente entre las dos, y Fisher (1925); población frente a muestra |
| IV   | Del casino a la bolsa               | Bachelier (1900) modela por primera vez los precios con probabilidad; el cupón de un bono se conoce hoy y el precio de mañana de una acción no: el rendimiento como variable aleatoria $R$                                                                                      |
| V    | Rendimiento esperado                | Promedio de los rendimientos posibles ponderado por su probabilidad, con escenarios de auge, normalidad y recesión                                                                                                                                                              |
| VI   | Riesgo como dispersión              | Varianza y desviación estándar de $R$: qué tanto se aleja el resultado de lo esperado                                                                                                                                                                                           |
| VII  | Sistemático o idiosincrático        | Riesgo que golpea a toda la economía (tasas, recesión) frente al de una sola emisora (fraude, huelga); diversificar solo elimina el segundo                                                                                                                                     |
| VIII | La campana y sus colas              | Distribución normal y la regla 68-95-99.7; los rendimientos reales tienen colas largas: las caídas extremas son más frecuentes de lo que predice la normal                                                                                                                      |
| IX   | 2008: cuando todo cae junto         | Modelos que suponían normalidad y poca correlación entre hipotecas subestimaron las colas y el riesgo sistemático                                                                                                                                                               |

> La práctica de este tema está en [`practica_1_probabilidad_y_riesgo.md`](../../practicas/unidad3/practica_1_probabilidad_y_riesgo.md).

> **Por redactar.** Esta nota solo tiene el objetivo y la estructura; falta la teoría. Es la base de [`2_rendimiento_y_riesgo_acciones.md`](2_rendimiento_y_riesgo_acciones.md): aquí la desviación estándar sale de escenarios con probabilidad (el lado de la probabilidad); allá se estima con precios históricos y se lleva a escala anual (el lado de la estadística, que la sección III anuncia). En la práctica nadie conoce las probabilidades de los escenarios: se estiman con datos, y esa es la razón de ser de la estadística en finanzas. La sección VII solo distingue los dos riesgos; por qué la diversificación elimina uno y no el otro se ve en la 2_. Las secciones I a IV, VIII y IX motivan, no se calculan. El reparto de Pascal y Fermat es el primer valor esperado de la historia y adelanta la idea de la Unidad 2: el valor justo de un activo es lo que se espera recibir de él. El caso de 2008 se retoma como burbuja en [`4_lecciones_modernas.md`](4_lecciones_modernas.md). La cita de "movimientos de 25 desviaciones estándar" (David Viniar, Goldman Sachs, agosto de 2007) y la cifra del lunes negro de 1987 están por verificar.

## 1 Contexto Epistemologico

La incertidumbre es parte de la realidad. En otras palabras, pocas veces podemos anticipar exactamente que sucederá en el futuro para la gran mayoría de procesos naturales.
Por lo tanto, cualquier modelo realístico de fenómenos naturales debe tomar en cuenta la posibilidad de la aleatoriedad. La actividad humana de la modelación busca simplificar alguna parte de la realidad para definir, entender, cuantificar, visualizar o simular. La modelación es una actividad humana íntimamente relacionada con todas las disciplinas científicas. El lenguaje fundamental de la modelación científica son las matemáticas. Al hacer uso de las matemáticas y sus interpretaciones verbales, se espera que sea más fácil cumplir los objetivos de la modelación de manera razonable. En otras palabras, los modelos deben tener una variación inherente y ser probabilísticos en su naturaleza. Entonces, la probabilidad nos provee el lenguaje fundamental para la modelación científica al permitirnos incorporar la incertidumbre en nuestra actividad de modelación.

La **probabilidad** es el lenguaje matemático para modelar y estudiar experimentos donde el resultado no puede ser previsto con una certidumbre perfecta. Uno de los objetivos de estudiar probabilidad es construir un marco teórico y conceptual para modelar fenómenos reales. El complemento empirico de la probalidad es la **estadística**, que se ocupa de los métodos de recolección, análisis, y obtención conclusiones con base en datos (u observaciones). Brown y Kass (2009) tienen un artículo que examina a profundidad la pregunta "¿Qué es la estadística?". Aquí, consideramos la estadística como el conjunto de conocimientos que nos permiten extraer información, en condiciones de incertidumbre, para resolver problemas/preguntas de investigación en algún contexto (tal contexto puede corresponder a una o varias  disciplinas).

La probabilidad se puede ver como la base de la estadística al darnos el lenguaje para incorporar la aleatoriedad. Mientras tanto, la estadística retroalimenta los modelos probabilísticos con base en los datos observados.

Básicamente, el método científico  nos llama a comenzar con una conjetura sobre el estado de la naturaleza, relaciones de causa y efecto, o diferencias entre fenómenos. Cuando hacemos observaciones, es decir, obtenemos los datos, para confirmar o rechazar tal conjetura. Esto debe hacerse de una  manera en que los resultados son reproducibles por otros. Así, construimos el conocimiento sobre el estado del universo al confirmar o rechazar conjeturas.

Esto puede parecer obvio hoy en día  ya que el progreso estadístico ya ha sido incorporado (al menos una parte) en el 'inconsciente colectivo' de la cultura moderna.

### 1.1 Basicos de Probabilidad: Espacio Muestral

Lo primero a saber es que las  probabilidades siempre están asociadas a eventos. Las probabilidades siempre están entre 0 y 1 (inclusivo), por definición, y nos dan idea de qué tan posible es que ocurra tal evento. El evento imposible tiene probabilidad cero y el evento seguro tiene probabilidad 1, pero lo contrario no se cumple: en un espacio muestral continuo, un evento con probabilidad cero puede ocurrir. Por ejemplo, la probabilidad de que el rendimiento de una acción mañana sea exactamente $3\%$, ni un decimal más ni uno menos, es cero, y aun así algún valor exacto tiene que salir. Dada la relación con la ciencia, es útil hacer las siguientes definiciones.

Un **experimento** es un procedimiento con un conjunto de posibles resultados bien definidos, del que no sabemos de antemano cuál ocurrirá. En las ciencias naturales suele poder repetirse (lanzar un dado mil veces); en finanzas casi nunca: el precio de una acción mañana se observa una sola vez. Por eso, en finanzas la probabilidad de un escenario es un supuesto del modelo, no una frecuencia que se observe.

El **espacio muestral** $\Omega$ es un conjunto que representa la colección de todos los resultados posibles del experimento.

Por ahora, para asignar probabilidades hacemos una distinción entre espacios muestrales discretos y continuos.

- Un espacio muestral discreto es un conjunto contable, es decir, finito (las caras de un dado, o los escenarios de auge, normalidad y recesión) o numerable, como los números naturales (el número de días hasta que una emisora anuncie un dividendo).
- Un espacio muestral continuo es un conjunto no numerable, por ejemplo un intervalo de los números reales: el rendimiento de una acción puede tomar cualquier valor en $[-100\%, \infty)$.

Algunos ejemplos, los dos primeros clásicos y los tres siguientes de la materia:

| Experimento                                           | Espacio muestral $\Omega$                             | Tipo            |
| ----------------------------------------------------- | ----------------------------------------------------- | --------------- |
| Lanzar una moneda                                     | $\{\text{águila}, \text{sol}\}$                       | Discreto finito |
| Lanzar un dado                                        | $\{1, 2, 3, 4, 5, 6\}$                                | Discreto finito |
| Estado de la economía el próximo año                  | $\{\text{auge}, \text{normalidad}, \text{recesión}\}$ | Discreto finito |
| Al vencimiento de un bono, la emisora paga o incumple | $\{\text{paga}, \text{incumple}\}$                    | Discreto finito |
| Tipo de cambio FIX peso-dólar de mañana               | $(0, \infty)$                                         | Continuo        |

Más adelante formalizaremos cómo asignar probabilidades. Por ahora, es suficiente apelar a la intuición cuando todos los resultados en el espacio muestral (finito) son igual de probables (como en el caso de una moneda justa o un dado justo). Así, es razonable definir intuitivamente

$$P(A) = \frac{|A|}{|\Omega|},$$

donde $|A|$ denota el número de resultados en el evento $A$, y $|\Omega| < \infty$ denota el número de resultados en todo el espacio muestral.

> **Observación.** Las probabilidades son una construcción matemática. Cuando aplicamos ideas de probabilidad a situaciones reales siempre tenemos supuestos (en ocasiones supuestos muy rígidos y en otras supuestos flexibles). Así, las afirmaciones probabilísticas que hacemos son afirmaciones respecto a un modelo matemático, no son afirmaciones completas sobre la realidad.
>
> En cierto sentido, un modelo matemático es espurio (comparado con la realidad en su totalidad). Por lo tanto, las matemáticas son un arte, ya que, como dice Pablo Picasso:
>
> > *"We all know that Art is not truth. Art is a lie that makes us realize truth, at least the truth that is given us to understand. The artist must know the manner whereby to convince others of the truthfulness of his lies."*
>
> Esto no quiere decir que las matemáticas no tengan ninguna utilidad en la realidad. Tales modelos, o simplificaciones de la realidad, si están bien hechos, tienen alguna revelación relevante al fenómeno de interés. Tales revelaciones nos permiten entender el mundo que nos rodea, y ocasionalmente nos permiten cambiar la realidad por medio de este entendimiento mejorado.

### 1.2 Basicos de Probabilidad: Relaciones entre Eventos

Ahora suponemos que un espacio muestral arbitrario, pero fijo, $\Omega$ es dado. Utilizamos las capitales para denotar eventos, eso es, conjuntos de puntos muestrales. el hecho de que un punto $\omega$ es contenido en el evento A es denotado por $\omega \in A$. Por lo tanto $\omega \in \Omega$ para todo $\omega$.  Escribiremos $A = B$ si y sólo si los dos eventos consisten exactamente de los mismos puntos.

Las operaciones entre eventos se leen como "no", "o" e "y". Para verlas con un ejemplo, clasifiquemos el rendimiento del S&P/BMV IPC el próximo año en pérdida, sin mucho cambio (un rendimiento cercano a cero) o ganancia, de modo que $\Omega = \{\text{pérdida}, \text{sin cambio}, \text{ganancia}\}$.

| Notación    | Se lee            | Ejemplo                                                                                                                        |
| ----------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| $A^c$       | no ocurre $A$     | $A = \{\text{pérdida}\}$ (perder); $A^c = \{\text{sin cambio}, \text{ganancia}\}$ (no perder)                                  |
| $A \cup B$  | ocurre $A$ o $B$  | $\{\text{pérdida}\} \cup \{\text{ganancia}\}$: el precio se movió                                                              |
| $A \cap B$  | ocurren $A$ y $B$ | $\{\text{pérdida}, \text{sin cambio}\} \cap \{\text{sin cambio}, \text{ganancia}\} = \{\text{sin cambio}\}$: ni ganó ni perdió |
| $\emptyset$ | evento imposible  | $\{\text{pérdida}\} \cap \{\text{ganancia}\} = \emptyset$: excluyentes                                                         |

### 1.3 ¿A qué eventos les asignamos probabilidad?

Si podemos decir qué tan probable es perder, también deberíamos poder decir qué tan probable es no perder. Si podemos hablar de "el FIX rebasa 20 pesos el lunes" y de "lo rebasa el martes", también deberíamos poder hablar de "lo rebasa algún día". La colección de eventos a los que asignamos probabilidad debe ser cerrada bajo estas operaciones. A esa colección se le llama σ-álgebra.

Una **σ-álgebra** $\mathcal{F}$ sobre $\Omega$ es una colección de eventos que cumple:

1. $\Omega \in \mathcal{F}$: siempre podemos preguntar "¿ocurre alguno de los resultados posibles?".
2. Si $A \in \mathcal{F}$, entonces $A^c \in \mathcal{F}$: si podemos preguntar "¿ocurre $A$?", podemos preguntar "¿no ocurre?".
3. Si $A_1, A_2, \dots \in \mathcal{F}$, entonces $A_1 \cup A_2 \cup \cdots \in \mathcal{F}$: si podemos preguntar por cada evento, podemos preguntar si ocurre alguno.

De estas tres reglas se deduce que $\emptyset \in \mathcal{F}$ y, por las leyes de De Morgan, que las intersecciones también están en $\mathcal{F}$.

**Ejemplo (dos inversionistas).** Con $\Omega = \{\text{pérdida}, \text{sin cambio}, \text{ganancia}\}$, un inversionista que solo se entera de si perdió o no distingue los eventos

$$\mathcal{F}_1 = \{\emptyset, \{\text{pérdida}\}, \{\text{sin cambio}, \text{ganancia}\}, \Omega\}.$$

Otro que ve el rendimiento completo distingue los 8 subconjuntos de $\Omega$; esa es su σ-álgebra $\mathcal{F}_2$. Las dos cumplen las tres reglas, pero $\mathcal{F}_2$ contiene más eventos: más información. El primero no puede contestar "¿hubo ganancia?", porque $\{\text{ganancia}\} \notin \mathcal{F}_1$.

Cuando $\Omega$ es discreto, siempre podemos tomar todos sus subconjuntos como σ-álgebra. Cuando es continuo, como el rendimiento en $[-100\%, \infty)$, no es posible asignar probabilidad de forma consistente a todos los subconjuntos, y se usan los intervalos y lo que se construye con ellos (Apéndice).

### 1.4 Medida de Probabilidad

Con $\Omega$ y $\mathcal{F}$ ya sabemos qué preguntas podemos hacer sobre el experimento; falta una regla que le asigne a cada pregunta un número. Para que esa regla sea coherente, Kolmogorov (1933) le pide cumplir tres axiomas.

**Definición (espacio de probabilidad).** La terna $(\Omega, \mathcal{F}, P)$ es un **espacio de probabilidad** si

- $\Omega$ es el espacio muestral;
- $\mathcal{F}$ es una σ-álgebra de eventos sobre $\Omega$;
- $P$ es una **medida de probabilidad**: una función que a cada evento $A \in \mathcal{F}$ le asigna un número $P(A)$ y que cumple los axiomas de Kolmogorov:
  1. Para cualquier $A \in \mathcal{F}$, $P(A) \geq 0$: ningún evento tiene probabilidad negativa.
  2. $P(\Omega) = 1$: algún resultado tiene que ocurrir.
  3. Si $A_1, A_2, \dots \in \mathcal{F}$ son disjuntos dos a dos ($A_i \cap A_j = \emptyset$ para $i \neq j$), entonces

     $$P\Big( \bigcup_{n=1}^{\infty} A_n \Big) = \sum_{n=1}^{\infty} P(A_n),$$

     es decir, si los eventos no pueden ocurrir juntos, la probabilidad de que ocurra alguno es la suma de sus probabilidades.

Todo lo demás se deduce de estos tres axiomas. Por ejemplo:

- **Complemento:** $P(A^c) = 1 - P(A)$. Como $A$ y $A^c$ son disjuntos y $A \cup A^c = \Omega$, los axiomas 2 y 3 dan $P(A) + P(A^c) = 1$.
- **Evento imposible:** $P(\emptyset) = 0$. Es el complemento de $\Omega$: $P(\emptyset) = 1 - P(\Omega) = 0$.
- **Cota superior:** $P(A) \leq 1$, porque $P(A) = 1 - P(A^c)$ y $P(A^c) \geq 0$.
- **Monotonía:** si $A \subseteq B$, entonces $P(A) \leq P(B)$. El evento $B$ se parte en $A$ y en lo que le falta a $A$ para llegar a $B$; la segunda parte tiene probabilidad mayor o igual a cero.

Así, que una probabilidad esté entre 0 y 1, como dijimos en 1.1, no es una convención: es una consecuencia de los axiomas.

**Ejemplo (escenarios para el IPC).** Con $\Omega = \{\text{pérdida}, \text{sin cambio}, \text{ganancia}\}$ y $\mathcal{F}$ formada por sus 8 subconjuntos, una analista asigna

$$P(\{\text{pérdida}\}) = 0.3, \qquad P(\{\text{sin cambio}\}) = 0.2, \qquad P(\{\text{ganancia}\}) = 0.5.$$

Por el axioma 3, la probabilidad de cualquier otro evento es la suma de las de sus resultados; por ejemplo, $P(\{\text{sin cambio}, \text{ganancia}\}) = 0.7$, que coincide con la regla del complemento: $1 - P(\{\text{pérdida}\}) = 0.7$. Los axiomas se cumplen: ningún número es negativo y $0.3 + 0.2 + 0.5 = 1$.

La regla de Laplace de 1.1, que le da $1/3$ a cada resultado, también cumple los axiomas. Las dos son medidas de probabilidad válidas sobre el mismo $(\Omega, \mathcal{F})$, y los axiomas no dicen cuál es la correcta. Esa no es una pregunta matemática sino una pregunta sobre el mercado, que se contesta con juicio o con datos. Estos pesos son los que usaremos para calcular el rendimiento esperado en la sección V.

> **Observación (¿de dónde salen las probabilidades?).** Los axiomas dicen qué reglas debe cumplir cualquier asignación de probabilidades, no cómo hacer la asignación. Para eso hay tres enfoques:
>
> 1. **Probabilidad clásica.** $P(A) = |A| / |\Omega|$, cuando el espacio muestral es finito y los resultados son igual de probables. Funciona con monedas y dados; en finanzas casi nunca, porque los escenarios no son igual de probables.
> 2. **Probabilidad como frecuencia relativa.** $P(A)$ es la proporción de veces que ocurre $A$ cuando el experimento se repite muchas veces en las mismas condiciones: $P(A) = \lim_{n \to \infty} f_n(A)$, donde $f_n(A)$ es la proporción de las primeras $n$ repeticiones en las que ocurre $A$. En finanzas sería contar en cuántos años el IPC tuvo pérdida, pero cada año es un mercado distinto, no una repetición del mismo experimento. Aun así, es la base de la estadística (sección III).
> 3. **Probabilidad subjetiva.** $P(A)$ es el grado de creencia de una persona en que ocurra $A$. Sirve para experimentos que no se repiten, que en finanzas son la regla: los pesos $0.3$, $0.2$ y $0.5$ del ejemplo son la opinión de la analista, y el precio de una acción resume las creencias de muchos inversionistas.
>
> Los tres enfoques son formas de asignar $P$, y en un espacio muestral finito los tres producen asignaciones que cumplen los axiomas. Por eso los axiomas son el punto de partida común: valen sin importar de dónde salgan los números.

## Fuentes y referencias recomendadas

- Bernstein, P. L. (1996). *Against the Gods: The Remarkable Story of Risk*. John Wiley & Sons: historia del riesgo, del problema de los puntos a la teoría de carteras.
- Devlin, K. (2008). *The Unfinished Game: Pascal, Fermat, and the Seventeenth-Century Letter that Made the World Modern*. Basic Books: el problema de los puntos y la correspondencia de 1654.
- Stigler, S. M. (1986). *The History of Statistics: The Measurement of Uncertainty before 1900*. Belknap Press of Harvard University Press: de Graunt y Bernoulli a Galton y Pearson.
- Graunt, J. (1662). *Natural and Political Observations Made upon the Bills of Mortality*. London: primeras tablas estadísticas construidas a partir de registros.
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd: la inferencia estadística moderna a partir de muestras.
- Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Springer: los axiomas de la probabilidad.
- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 17, 21-86: primer modelo probabilístico de los precios de mercado.
- Bodie, Z., Kane, A., & Marcus, A. J. (2021). *Investments* (12ª ed.). McGraw-Hill: rendimiento esperado y desviación estándar por escenarios, riesgo sistemático y riesgo diversificable.
- Mandelbrot, B. (1963). *The Variation of Certain Speculative Prices*. Journal of Business, 36(4), 394-419: los cambios de precio tienen colas mucho más pesadas que la normal.
- Cont, R. (2001). *Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues*. Quantitative Finance, 1(2), 223-236: colas largas y otros hechos estilizados de los rendimientos.
- Taleb, N. N. (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House: eventos extremos que los modelos basados en la normal tratan como imposibles.
- Li, D. X. (2000). *On Default Correlation: A Copula Function Approach*. Journal of Fixed Income, 9(4), 43-54: la cópula gaussiana con la que se valuaron los CDO hipotecarios antes de 2008.
- Financial Crisis Inquiry Commission. (2011). *The Financial Crisis Inquiry Report*. U.S. Government Printing Office: causas de la crisis de 2008, incluida la subestimación del riesgo en los modelos.
