# Unidad 3 · Probabilidad y Riesgo

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante calcule el rendimiento esperado y la desviación estándar de una acción a partir de escenarios con probabilidad.

## Contenido

|     | Tema                    | Qué cubre                                                                                                                                                           |
| --- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I   | Contexto                | Incertidumbre y modelación; la probabilidad parte del modelo y predice los datos, la estadística parte de los datos e infiere el modelo                             |
| II  | Espacio de probabilidad | Espacio muestral discreto y continuo, relaciones entre eventos con los escenarios de una acción, axiomas de Kolmogorov y enfoques clásico, frecuentista y subjetivo |
| III | Variables aleatorias    | Variable aleatoria, función de distribución y densidad (discreta, continua y mixta), vector aleatorio, probabilidad condicional e independencia                     |
| IV  | Esperanza               | Definición, rendimiento esperado con escenarios, linealidad y rendimiento de una cartera, S&P 500 y el promedio que engaña                                          |
| V   | Varianza y covarianza   | Desviación estándar (volatilidad) con escenarios, modelo normal, covarianza, correlación y matriz de varianzas y covarianzas                                        |
| VI  | Riesgo de cola          | Mediana, cuantiles y valor en riesgo (VaR); esperanza condicional y CVaR (déficit esperado), y por qué la regulación bancaria lo prefiere al VaR                    |

> La práctica de este tema está en [`practica_1_probabilidad_y_riesgo.md`](../../practicas/unidad3/practica_1_probabilidad_y_riesgo.md).

> **Por redactar.** La teoría de las secciones 1 a 6 está escrita; falta la motivación histórica, que va en la sección 1: el problema de los puntos de Pascal y Fermat (1654), el primer valor esperado de la historia, que adelanta la idea de la Unidad 2 de que el valor justo de un activo es lo que se espera recibir de él; Huygens (1657) y Bachelier (1900). Esta nota es la base de [`2_estadistica_y_datos.md`](2_estadistica_y_datos.md): aquí la esperanza y la desviación estándar salen de un modelo de probabilidad; allá se estiman con datos, con la ley de los grandes números y el teorema central del límite, y en [`3_hechos_estilizados_y_regresion.md`](3_hechos_estilizados_y_regresion.md) se contrastan con los hechos estilizados de los rendimientos. En [`4_rendimiento_y_riesgo_acciones.md`](4_rendimiento_y_riesgo_acciones.md) se llevan a escala anual con los precios del IPC, y ahí va también por qué la diversificación elimina el riesgo de una emisora y no el sistemático. Las colas largas (los rendimientos reales no son normales) y el caso de 2008 se retoman como burbuja en [`5_valuacion_acciones.md`](5_valuacion_acciones.md). La cita de "movimientos de 25 desviaciones estándar" (David Viniar, Goldman Sachs, agosto de 2007) y la cifra del lunes negro de 1987 están por verificar.

### 1. Contexto

La incertidumbre es parte de la realidad: pocas veces podemos anticipar exactamente qué sucederá en el futuro en la gran mayoría de los procesos naturales. Por lo tanto, cualquier modelo realista de fenómenos naturales debe tomar en cuenta la posibilidad de la aleatoriedad. Modelar es simplificar alguna parte de la realidad para definirla, entenderla, cuantificarla, visualizarla o simularla, y es una actividad presente en todas las disciplinas científicas. Su lenguaje fundamental son las matemáticas. Como los modelos deben incorporar la variación inherente a los fenómenos, tienen que ser probabilísticos, y la probabilidad es el lenguaje que nos permite incorporar la incertidumbre al modelar.

<!-- diapositivas: conservar -->
- **Modelar con incertidumbre:** un modelo simplifica una parte de la realidad para entenderla y cuantificarla; si el fenómeno varía, el modelo tiene que ser probabilístico.
- **Probabilidad:** el lenguaje matemático para modelar experimentos cuyo resultado no puede preverse con certeza. Parte del modelo y predice los datos.
- **Estadística:** el complemento empírico de la probabilidad; recolecta y analiza datos para extraer información y resolver preguntas en condiciones de incertidumbre. Parte de los datos e infiere el modelo. Brown y Kass (2009) examinan a fondo la pregunta "¿Qué es la estadística?".
- **Se retroalimentan:** la probabilidad le da a la estadística el lenguaje de la aleatoriedad, y la estadística ajusta los modelos probabilísticos con los datos observados.
- **Método científico:** una conjetura sobre la naturaleza, las causas o las diferencias entre fenómenos se confirma o se rechaza con datos que otros pueden reproducir.

Esto puede parecer obvio hoy en día, porque el progreso estadístico ya forma parte, al menos en parte, del "inconsciente colectivo" de la cultura moderna.

### 2. Espacio de probabilidad

#### 2.1 Espacio muestral

Lo primero que hay que saber es que las probabilidades siempre están asociadas a eventos. Siempre están entre 0 y 1 (inclusive), por definición, y nos dan idea de qué tan posible es que ocurra tal evento. El evento imposible tiene probabilidad cero y el evento seguro tiene probabilidad 1, pero lo contrario no se cumple: en un espacio muestral continuo, un evento con probabilidad cero puede ocurrir. Por ejemplo, la probabilidad de que el rendimiento de una acción mañana sea exactamente $3\%$, ni un decimal más ni uno menos, es cero, y aun así algún valor exacto tiene que salir. Dada la relación con la ciencia, es útil hacer las siguientes definiciones.

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
> > "Todos sabemos que el arte no es la verdad. El arte es una mentira que nos hace ver la verdad, al menos la verdad que nos es dado comprender. El artista debe saber cómo convencer a los demás de la veracidad de sus mentiras."
> >
> > *"We all know that Art is not truth. Art is a lie that makes us realize truth, at least the truth that is given us to understand. The artist must know the manner whereby to convince others of the truthfulness of his lies."*
>
> Esto no quiere decir que las matemáticas no tengan ninguna utilidad en la realidad. Los modelos, como simplificaciones de la realidad, si están bien hechos, revelan algo relevante del fenómeno de interés. Eso nos permite entender el mundo que nos rodea y, en ocasiones, cambiarlo gracias a ese mejor entendimiento.

#### 2.2 Relaciones entre eventos

Ahora suponemos dado un espacio muestral $\Omega$ arbitrario, pero fijo. Usamos letras mayúsculas para denotar eventos, es decir, conjuntos de puntos muestrales. Que un punto $\omega$ esté contenido en el evento $A$ se denota $\omega \in A$; por lo tanto, $\omega \in \Omega$ para todo $\omega$. Escribimos $A = B$ si y solo si los dos eventos tienen exactamente los mismos puntos.

Las operaciones entre eventos se leen como "no", "o" e "y". Para verlas con un ejemplo, clasifiquemos el rendimiento de una acción el próximo año (ilustrativa) en pérdida, sin mucho cambio (un rendimiento cercano a cero) o ganancia, de modo que $\Omega = \{\text{pérdida}, \text{sin cambio}, \text{ganancia}\}$.

| Notación    | Se lee            | Ejemplo                                                                                                                        |
| ----------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| $A^c$       | no ocurre $A$     | $A = \{\text{pérdida}\}$ (perder); $A^c = \{\text{sin cambio}, \text{ganancia}\}$ (no perder)                                  |
| $A \cup B$  | ocurre $A$ o $B$  | $\{\text{pérdida}\} \cup \{\text{ganancia}\}$: el precio se movió                                                              |
| $A \cap B$  | ocurren $A$ y $B$ | $\{\text{pérdida}, \text{sin cambio}\} \cap \{\text{sin cambio}, \text{ganancia}\} = \{\text{sin cambio}\}$: ni ganó ni perdió |
| $\emptyset$ | evento imposible  | $\{\text{pérdida}\} \cap \{\text{ganancia}\} = \emptyset$: excluyentes                                                         |

No todo conjunto de resultados recibe probabilidad: los eventos que sí la reciben forman una colección cerrada bajo estas operaciones, llamada σ-álgebra (ver el Apéndice).

#### 2.3 Medida de probabilidad

Con $\Omega$ y $\mathcal{F}$ ya sabemos qué preguntas podemos hacer; falta una regla $P$ que le asigne a cada pregunta un número. Para que esa regla sea coherente, Kolmogorov (1933) le pide cumplir tres axiomas.

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

Así, que una probabilidad esté entre 0 y 1, como dijimos en 2.1, no es una convención: es una consecuencia de los axiomas.

**Ejemplo (escenarios para una acción).** Con $\Omega = \{\text{pérdida}, \text{sin cambio}, \text{ganancia}\}$ y $\mathcal{F}$ formada por sus 8 subconjuntos, una analista asigna

$$P(\{\text{pérdida}\}) = 0.3, \qquad P(\{\text{sin cambio}\}) = 0.2, \qquad P(\{\text{ganancia}\}) = 0.5.$$

Por el axioma 3, la probabilidad de cualquier otro evento es la suma de las de sus resultados; por ejemplo, $P(\{\text{sin cambio}, \text{ganancia}\}) = 0.7$, que coincide con la regla del complemento: $1 - P(\{\text{pérdida}\}) = 0.7$. Los axiomas se cumplen: ningún número es negativo y $0.3 + 0.2 + 0.5 = 1$.

La regla de Laplace de 2.1, que le da $1/3$ a cada resultado, también cumple los axiomas. Las dos son medidas de probabilidad válidas sobre el mismo $(\Omega, \mathcal{F})$, y los axiomas no dicen cuál es la correcta. Esa no es una pregunta matemática sino una pregunta sobre el mercado, que se contesta con juicio o con datos.

> **Observación (¿de dónde salen las probabilidades?).** Los axiomas dicen qué reglas debe cumplir cualquier asignación de probabilidades, no cómo hacer la asignación. Para eso hay tres enfoques:
>
> 1. **Probabilidad clásica.** $P(A) = |A| / |\Omega|$, cuando el espacio muestral es finito y los resultados son igual de probables. Funciona con monedas y dados; en finanzas casi nunca, porque los escenarios no son igual de probables.
> 2. **Probabilidad como frecuencia relativa.** $P(A)$ es la proporción de veces que ocurre $A$ cuando el experimento se repite muchas veces en las mismas condiciones: $P(A) = \lim_{n \to \infty} f_n(A)$, donde $f_n(A)$ es la proporción de las primeras $n$ repeticiones en las que ocurre $A$. En finanzas sería contar en cuántos años la acción tuvo pérdida, pero cada año es un mercado distinto, no una repetición del mismo experimento. Aun así, es la base de la estadística (nota 2_).
> 3. **Probabilidad subjetiva.** $P(A)$ es el grado de creencia de una persona en que ocurra $A$. Sirve para experimentos que no se repiten, que en finanzas son la regla: los pesos $0.3$, $0.2$ y $0.5$ del ejemplo son la opinión de la analista, y el precio de una acción resume las creencias de muchos inversionistas.
>
> Los tres enfoques son formas de asignar $P$, y en un espacio muestral finito los tres producen asignaciones que cumplen los axiomas. Por eso los axiomas son el punto de partida común: valen sin importar de dónde salgan los números.

### 3. Variables aleatorias

#### 3.1 Variable aleatoria

Sea $(\Omega, \mathcal{F}, P)$ un espacio de probabilidad. Las variables aleatorias nos permiten enlazar números con espacios muestrales y eventos. Una definición algo informal es que una variable aleatoria es una función

$$X: \Omega \to \mathbb{R}$$

que asigna un número real $X(\omega) \in \mathbb{R}$ a cada resultado $\omega \in \Omega$.

En un nivel intuitivo, una variable aleatoria $X$ es una cantidad cuyo valor queda determinado por el resultado $\omega$ del experimento, dentro del universo $\Omega$ de todos los resultados posibles.

**Ejemplo (incumplimiento de un bono).** Con $\Omega = \{\text{paga}, \text{incumple}\}$, definimos $D(\text{paga}) := 0$ y $D(\text{incumple}) := 1$. Una variable que solo toma los valores 0 y 1 se llama variable de Bernoulli: vale 1 justo cuando ocurre el evento que nos interesa, aquí que la emisora no pague.

**Ejemplo (rendimiento por escenarios).** Volvamos a los escenarios de la acción de 2.3. Si en el escenario de pérdida la acción rinde $-15\%$, en el de sin cambio $0\%$ y en el de ganancia $20\%$ (ilustrativo), el rendimiento del año es la variable aleatoria discreta $R$ que asigna a cada escenario su rendimiento:

| Escenario $\omega$ | $R(\omega)$ | $P(\{\omega\})$ |
| ------------------ | ----------- | --------------- |
| Pérdida            | $-15\%$     | $0.3$           |
| Sin cambio         | $0\%$       | $0.2$           |
| Ganancia           | $20\%$      | $0.5$           |

Tres escenarios son un modelo discreto y muy simple; el ejemplo siguiente modela el precio de la acción de forma continua.

**Ejemplo (precio de una acción).** Hoy compramos una acción que no paga dividendo a $s_0 = 100$ pesos. Su precio dentro de un año, $S_1$, hoy no lo conocemos: puede ser cualquier número no negativo. Con $\Omega = [0, \infty)$, los precios posibles, la variable $S_1(\omega) := \omega$ es una variable aleatoria continua y no negativa. No puede ser negativa por la responsabilidad limitada del accionista: en el peor caso la acción vale cero y se pierde lo invertido, nunca más.

El rendimiento del año es una función de $S_1$:

$$R = \frac{S_1 - s_0}{s_0}.$$

Una función de una variable aleatoria también es variable aleatoria, así que $R$ lo es, y toma valores en $[-100\%, \infty)$, el intervalo de 2.1. Lo mismo ocurre con el valor final de invertir 10,000 pesos en la acción, $V = 10{,}000(1 + R)$. $S_1$, $R$ y $V$ van en mayúscula porque son inciertas; $s_0$ ya se conoce, por eso va en minúscula.

**Ejemplo (tipo de cambio).** Sea $X(\omega)$ el tipo de cambio FIX de mañana, en pesos por dólar, cuando ocurre el resultado $\omega \in \Omega$. No hace falta describir $\Omega$: basta con que cada resultado posible determine un precio.

#### 3.2 Distribución y densidad

La **distribución** de $X$ dice qué valores toma $X$ y con qué probabilidad. Una vez que la conocemos, ya no necesitamos $\Omega$: todas las preguntas sobre $X$ se contestan con ella.

> **¿De dónde sale la fórmula?** Para cada número $x$, el conjunto
>
> $$\{X \leq x\} = \{\omega \in \Omega : X(\omega) \leq x\}$$
>
> reúne los resultados que hacen que $X$ no pase de $x$. Pedimos que sea un evento de $\mathcal{F}$, para poder aplicarle $P$ (sección 2.3); esa es la condición que hace de $X$ una variable aleatoria.

**Definición (función de distribución).** La función de distribución de $X$ es

$$F_X(x) = P(X \leq x), \qquad x \in \mathbb{R}.$$

**Propiedades.** De los axiomas se deduce que $F_X$ va de 0 a 1, nunca decrece y da la probabilidad de cualquier intervalo, $P(a < X \leq b) = F_X(b) - F_X(a)$; por eso conocer $F_X$ es conocer la distribución (las demostraciones están en el Apéndice).

**Ejemplo (rendimiento por escenarios).** Para la acción de 3.1, la función de distribución acumula las probabilidades de los escenarios y es una escalera que sube en cada rendimiento posible:

$$F_R(x) = \begin{cases} 0, & x < -15\% \\ 0.3, & -15\% \leq x < 0\% \\ 0.5, & 0\% \leq x < 20\% \\ 1, & x \geq 20\% \end{cases}$$

Por ejemplo, **la probabilidad de no ganar nada es $F_R(0\%) = 0.5$**: la de los escenarios de pérdida y sin cambio juntos.

**Definición (densidad).** Para cualquier conjunto $B$ de valores (un intervalo o una unión de intervalos), la probabilidad de que $X$ caiga en $B$ es

$$P(X \in B) = \int_B dF_X(x),$$

donde $dF_X(x)$, la **densidad** de $X$, es la probabilidad que hay en $x$ o muy cerca de $x$. La densidad es no negativa y su total es 1, $\int_{\mathbb{R}} dF_X(x) = 1$. Hay tres casos:

- **$X$ discreta**, si solo toma una cantidad contable de valores $x_1, x_2, \dots$. La probabilidad está concentrada en los saltos de $F_X$: $dF_X(x_i) = P(X = x_i)$, y la integral es una suma, $P(X \in B) = \sum_{x_i \in B} dF_X(x_i)$.
- **$X$ continua**, si $P(X = x) = 0$ para cada valor exacto $x$, como vimos en 2.1. La probabilidad está repartida a lo largo de la recta: $dF_X(x) = f_X(x)\, dx$, donde $f_X = F_X'$ es la **densidad** de $X$ (la pendiente de la función de distribución), y $P(X \in B)$ es el área bajo la curva $f_X$ sobre $B$.
- **$X$ mixta**, si combina los dos casos: $F_X$ tiene saltos en algunos valores y entre ellos sube de forma continua. En los saltos, $dF_X(x_i) = P(X = x_i)$; en el resto, $dF_X(x) = f_X(x)\, dx$. Así, $P(X \in B)$ es la suma de los saltos que caen en $B$ más el área sobre $B$.

#### 3.3 Vector aleatorio e independencia

Una cartera tiene varios activos, y su riesgo no depende solo de cada uno por separado sino de cómo se mueven juntos.

**Definición (vector aleatorio).** Si $X_1, \dots, X_n$ son variables aleatorias sobre el mismo $(\Omega, \mathcal{F}, P)$, el **vector aleatorio** $\mathbf{X} = (X_1, \dots, X_n): \Omega \to \mathbb{R}^n$ asigna a cada resultado $\omega$ el punto $(X_1(\omega), \dots, X_n(\omega))$; por ejemplo, con $n = 2$, los rendimientos en un año de dos acciones, $(R_A, R_B)$. Como $\{X_1 \leq x_1, \dots, X_n \leq x_n\} = \{X_1 \leq x_1\} \cap \cdots \cap \{X_n \leq x_n\}$ es un evento (ver el Apéndice), su **función de distribución conjunta** es

$$F_{\mathbf{X}}(x_1, \dots, x_n) = P(X_1 \leq x_1, \dots, X_n \leq x_n),$$

y su **densidad conjunta** $dF_{\mathbf{X}}(\mathbf{x})$ es la probabilidad que hay en el punto $\mathbf{x} = (x_1, \dots, x_n)$ o muy cerca de él, de modo que $P(\mathbf{X} \in B) = \int_B dF_{\mathbf{X}}(\mathbf{x})$ para cualquier región $B$ de $\mathbb{R}^n$.

**Ejemplo (dos acciones).** La figura muestra una densidad conjunta ilustrativa de $(R_A, R_B)$. Cada curva cerrada une puntos con la misma densidad, y cuanto más oscura la zona, más probabilidad hay cerca de ella; la forma inclinada dice que las dos acciones tienden a subir y bajar juntas. La probabilidad de que las dos pierdan es el volumen de la densidad sobre la región $B$ en dorado, $P((R_A, R_B) \in B) = 0.26$. Las curvas de arriba y de la derecha son las marginales: lo que queda de la conjunta al acumular sobre la otra variable.

<!-- diapositivas: figura sola -->
![Densidad conjunta ilustrativa de los rendimientos de dos acciones, R_A en el eje horizontal y R_B en el vertical, dibujada como elipses concéntricas inclinadas hacia arriba a la derecha, más oscuras en el centro cerca de 5% y 8%; el cuadrante en que las dos pierden está sombreado en dorado con probabilidad 0.26, y arriba y a la derecha aparecen las densidades marginales de cada rendimiento](img/vector_rendimientos_conjunta.png)

Saber que ocurrió un evento puede cambiar la probabilidad de otro. Cuando no la cambia, decimos que los eventos son independientes.

> **¿De dónde sale la fórmula?** Si sabemos que ocurrió $B$, los resultados posibles se reducen a los de $B$. La probabilidad de $A$ pasa a ser la parte de $B$ donde también ocurre $A$, reescalada para que el total vuelva a ser 1.

**Definición (probabilidad condicional).** Si $P(B) > 0$, la probabilidad de $A$ dado $B$ es

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}.$$

**Definición (eventos independientes).** Dos eventos $A$ y $B$ son **independientes** si

$$P(A \cap B) = P(A) P(B).$$

Si $P(B) > 0$, equivale a $P(A \mid B) = P(A)$: saber que ocurrió $B$ no cambia la probabilidad de $A$.

**Ejemplo (dos acciones).** En el ejemplo anterior, sean $E_A = \{R_A < 0\}$ el evento de que la acción A pierda y $E_B = \{R_B < 0\}$ el de que pierda la B. Con el modelo de la figura, $P(E_A) = 0.42$, $P(E_B) = 0.39$ y $P(E_A \cap E_B) = 0.26$.

- **Condicional:** $P(E_B \mid E_A) = 0.26 / 0.42 = 0.63$. Si sabemos que A perdió, la probabilidad de que B también pierda sube de 39% a 63%.
- **Independencia:** si las acciones fueran independientes, perderían juntas con probabilidad $P(E_A) P(E_B) = 0.42 \times 0.39 = 0.17$, y saber que A perdió no cambiaría nada. Como $0.26 \neq 0.17$, no son independientes. La forma inclinada de la densidad conjunta lo dice a simple vista; con independencia, las curvas de nivel no estarían inclinadas.

Para una cartera con las dos acciones, la diferencia importa: perder en ambas es 1.6 veces más probable que si fueran independientes. Diversificar funciona cuando los riesgos son independientes, como el fraude o la huelga de una sola emisora; no funciona contra lo que golpea a todas a la vez, como una recesión (se ve en la 3_). Antes de 2008, los modelos de las hipotecas suponían que sus incumplimientos eran casi independientes, y en la crisis cayeron juntos (nota 5_). Cuánto se mueven juntas dos variables se mide con la covarianza y la correlación, que veremos en 5.2.

### 4. Esperanza

La esperanza resume la distribución de una variable aleatoria en un solo número: el valor que se obtiene en promedio.

#### 4.1 Definición

> **¿De dónde sale la fórmula?** Con escenarios, el promedio natural pondera cada valor posible por su probabilidad: $\sum_i x_i P(X = x_i)$. Con la notación de 3.2, cada valor $x$ se pondera por la probabilidad que hay en $x$ o muy cerca de $x$, $dF_X(x)$, y se acumula sobre todos los valores.

**Definición (esperanza).** La **esperanza**, o valor esperado, de $X$ es

$$E[X] = \int x\, dF_X(x) = \begin{cases} \displaystyle\sum_i x_i\, P(X = x_i), & X \text{ discreta} \\[2ex] \displaystyle\int_{\mathbb{R}} x\, f_X(x)\, dx, & X \text{ continua} \end{cases}$$

siempre que $\int |x|\, dF_X(x) < \infty$; si no, la esperanza no está definida. También se le llama media o primer momento de $X$, y se escribe $\mu$ o $\mu_X$.

**Ejemplo (rendimiento esperado con escenarios).** Para la acción de 3.1, la esperanza pondera el rendimiento de cada escenario por su probabilidad:

$$E[R] = 0.3(-15\%) + 0.2(0\%) + 0.5(20\%) = -4.5\% + 0\% + 10\% = 5.5\%.$$

En promedio, la acción rinde **5.5% al año**, aunque ningún escenario rinde exactamente eso.

> **Observación.** La esperanza tiene dos lecturas. La primera es el promedio a la larga: si el experimento se repitiera muchas veces, el promedio de los valores observados se acercaría a $E[X]$ (la ley de los grandes números, nota 2_). La segunda es el centro de masa: si la densidad fuera una lámina, $E[X]$ es el punto donde se equilibra. Por eso es una medida de ubicación de la distribución.

#### 4.2 Propiedades y linealidad

**Proposición (propiedades de la esperanza).** Siempre que las esperanzas estén definidas:

1. Si $X \geq 0$, entonces $E[X] \geq 0$.
2. Si $X \geq Y$, entonces $E[X] \geq E[Y]$.
3. Linealidad: para constantes $a_1, \dots, a_n$, $E[a_1 X_1 + \cdots + a_n X_n] = a_1 E[X_1] + \cdots + a_n E[X_n]$.
4. Si $X_1, \dots, X_n$ son independientes, $E[X_1 \cdots X_n] = E[X_1] \cdots E[X_n]$.

**Esperanza de un vector aleatorio.** Para un vector aleatorio $\mathbf{X} = (X_1, \dots, X_n)$ (sección 3.3), la esperanza se toma componente por componente, cada una con su marginal:

$$E[\mathbf{X}] = \big( E[X_1], \dots, E[X_n] \big).$$

**Ejemplo (esperanza de dos rendimientos).** En el modelo de las dos acciones de 3.3, el rendimiento esperado de A es $E[R_A] = 5\%$ y el de B es $E[R_B] = 8\%$, así que la esperanza del vector es el punto

$$E[(R_A, R_B)] = (5\%, 8\%).$$

La figura repite la de 3.3 con la esperanza marcada en dorado: la línea vertical es $E[R_A]$, la horizontal es $E[R_B]$, y se cruzan en el centro de las curvas de nivel, el centro de masa de la densidad conjunta. Cada componente se calcula solo con su marginal; la inclinación de las curvas, que dice cómo se mueven juntas las dos acciones, no cambia la esperanza.

<!-- diapositivas: figura sola -->
![La misma densidad conjunta ilustrativa de los rendimientos de dos acciones de la sección 3.3, con dos líneas punteadas doradas: una vertical en E[R_A] = 5% y una horizontal en E[R_B] = 8%, que se cruzan en un punto dorado en el centro de las elipses](img/vector_rendimientos_esperanza.png)

La linealidad dice que el rendimiento esperado de una cartera es el promedio ponderado de los rendimientos esperados, sean o no independientes los activos. Con las dos acciones de 3.3, cuyos rendimientos esperados en el modelo de la figura son $5\%$ y $8\%$, y mitad del dinero en cada una: $E[0.5 R_A + 0.5 R_B] = 0.5(5\%) + 0.5(8\%) = 6.5\%$.

#### 4.3 El S&P 500 y el promedio que engaña

**Ejemplo (rendimiento anual esperado del S&P 500).** El S&P 500 es un índice que sigue el precio de las 500 empresas más grandes que cotizan en las bolsas de Estados Unidos, cada una con un peso proporcional a su valor de mercado; es el equivalente estadounidense del S&P/BMV IPC. Su nivel resume en un solo número cuánto vale el mercado accionario de ese país. El índice actual se creó en 1957; la serie desde 1928 lo enlaza con sus versiones anteriores, que seguían menos empresas.

En la práctica no conocemos la distribución del rendimiento $R$ del índice; lo que sí tenemos son sus precios pasados. En la figura, arriba está el nivel del S&P 500 cada mes de 1928 a 2025: pasó de 18 a 6,846 puntos. La escala vertical es logarítmica, así que la misma distancia vertical representa el mismo cambio porcentual, sin importar el nivel. Abajo está el rendimiento de cada año $t$, que, como en 3.1, compara el precio al final del año con el del inicio y suma los dividendos que pagaron las empresas:

$$r_t = \frac{p_t + d_t - p_{t-1}}{p_{t-1}}.$$

De 1928 a 2025 hay 98 rendimientos anuales, según los datos que publica Aswath Damodaran, profesor de NYU Stern (Damodaran, 2026).[^damodaran] Su promedio,

$$\bar{r} = \frac{1}{98} \sum_{t=1928}^{2025} r_t = 11.86\%,$$

es la estimación más simple de $E[R]$ (estimar a partir de datos es el tema de la estadística, nota 2_). Detrás del promedio hay mucha dispersión: 26 de los 98 años, uno de cada cuatro, tuvieron pérdida; el peor fue 1931, con $-43.84\%$, y el mejor 1954, con $52.56\%$.

<!-- diapositivas: figura sola -->
![Dos paneles del S&P 500 entre 1928 y 2025: arriba, el nivel mensual del índice en escala logarítmica, que sube de 18 puntos en 1928 a 6,846 en 2025 con caídas visibles en 1929-1932, 2000-2002 y 2008; abajo, una barra por año con el rendimiento anual con dividendos, en dorado los años con ganancia y en rojo los años con pérdida, y una línea punteada en el promedio de 11.86%](img/sp500_precio_y_rendimientos.png)

<!-- diapositivas: figura sola -->
![Histograma de los 98 rendimientos anuales del S&P 500 con dividendos entre 1928 y 2025, en barras de 10 puntos de ancho desde -50% hasta 60%, con la mayoría de los años entre -10% y 40%; una línea dorada marca el promedio aritmético de 11.86% y una línea punteada el rendimiento geométrico de 10.02%](img/sp500_rendimientos_anuales.png)

Sin embargo, 100 dólares invertidos a inicios de 1928 se convirtieron en 1,157,591 dólares a fines de 2025, lo que equivale a crecer $10.02\%$ cada año, no $11.86\%$. La riqueza no crece al ritmo del promedio.

**Ejemplo (el promedio que engaña).** Un fondo gana 60%, 100%, 40% y 80% en cuatro años y en el quinto lo pierde todo, $-100\%$. Su rendimiento promedio es

$$\frac{60\% + 100\% + 40\% + 80\% - 100\%}{5} = 36\% \text{ anual},$$

tres veces el promedio del S&P 500, y el fondo podría anunciar "36% de rendimiento promedio anual" sin mentir. Pero quien invirtió 100 pesos terminó con

$$100 \times 1.60 \times 2.00 \times 1.40 \times 1.80 \times 0 = 0 \text{ pesos},$$

mientras que en el peor periodo de cinco años del S&P 500, de 1928 a 1932, con la Gran Depresión, 100 dólares quedaron en 51.

La riqueza depende del producto $\prod_t (1 + r_t)$, no de la suma de los rendimientos. El rendimiento que la describe es el **geométrico**, $\left( \prod_{t=1}^{n} (1 + r_t) \right)^{1/n} - 1$, la misma idea de la TEA de la Unidad 1, y nunca es mayor que el promedio aritmético. En el fondo es $-100\%$; en el S&P 500, $10.02\% < 11.86\%$. Cuanto más dispersos los rendimientos, mayor la brecha entre los dos: por eso la dispersión, que mide la varianza (sección 5.1), también es riesgo.

[^damodaran]: Damodaran, A. (2026). *Historical Returns on Stocks, Bonds and Bills: 1928-2025*. NYU Stern School of Business. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html

### 5. Varianza y covarianza

La esperanza dice dónde está el centro de la distribución; la varianza dice qué tan lejos de ese centro suelen caer los valores. Dos acciones con el mismo rendimiento esperado pueden tener riesgos muy distintos.

#### 5.1 Varianza y volatilidad

> **¿De dónde sale la fórmula?** Queremos medir qué tan lejos cae $X$ de su media $\mu = E[X]$. El promedio de las desviaciones $X - \mu$ no sirve: por linealidad, $E[X - \mu] = E[X] - \mu = 0$, porque las desviaciones positivas y las negativas se cancelan. Para que no se cancelen, se elevan al cuadrado, con lo que todas son positivas y las lejanas pesan más, y después se promedian.

**Definición (varianza y desviación estándar).** La **varianza** de $X$ es

$$\operatorname{Var}(X) = E[(X - \mu)^2] = \int (x - \mu)^2\, dF_X(x) = \begin{cases} \displaystyle\sum_i (x_i - \mu)^2\, P(X = x_i), & X \text{ discreta} \\[2ex] \displaystyle\int_{\mathbb{R}} (x - \mu)^2 f_X(x)\, dx, & X \text{ continua} \end{cases}$$

siempre que $E[X^2] < \infty$. Se escribe $\sigma^2$ o $\sigma_X^2$. La **desviación estándar** es su raíz,

$$\sigma_X = \sqrt{\operatorname{Var}(X)},$$

y está en las mismas unidades que $X$ (pesos, o puntos porcentuales si $X$ es un rendimiento), por eso es la que se reporta. En finanzas, la desviación estándar de un rendimiento se llama **volatilidad**.

**Ejemplo (desviación estándar con escenarios).** Para la acción de 3.1, con rendimiento esperado $E[R] = 5.5\%$ (sección 4.1), se mide qué tanto se aleja cada escenario de la media; los cuadrados van en decimales:

| Escenario  | $P$   | $r$     | $r - E[R]$ | $(r - E[R])^2$ |
| ---------- | ----- | ------- | ---------- | -------------- |
| Pérdida    | $0.3$ | $-15\%$ | $-20.5\%$  | $0.042025$     |
| Sin cambio | $0.2$ | $0\%$   | $-5.5\%$   | $0.003025$     |
| Ganancia   | $0.5$ | $20\%$  | $14.5\%$   | $0.021025$     |

$$\operatorname{Var}(R) = 0.3(0.042025) + 0.2(0.003025) + 0.5(0.021025) = 0.023725,$$

$$\sigma_R = \sqrt{0.023725} = 15.40\%.$$

La acción rinde **5.5% en promedio, con una volatilidad de 15.40%**: en un año cualquiera, su rendimiento suele alejarse unos 15 puntos porcentuales de su media.

**Ejemplo (dos rendimientos con el modelo normal).** Un modelo común para el rendimiento anual de un activo es la distribución **normal**, con forma de campana. Su densidad es

$$f_R(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right), \qquad x \in \mathbb{R},$$

y se puede demostrar que $E[R] = \mu$ y $\operatorname{Var}(R) = \sigma^2$. Como la fórmula solo depende de $\mu$ y $\sigma$, una normal queda **completamente determinada** por su esperanza y su varianza: conocidas esas dos, se conoce cualquier probabilidad sobre $R$. Se escribe $R \sim N(\mu, \sigma^2)$.

Comparemos dos activos con el mismo rendimiento esperado (valores ilustrativos): una acción C con $R_C \sim N(8\%, (15\%)^2)$ y una acción D con $R_D \sim N(8\%, (25\%)^2)$. Las dos campanas tienen el mismo centro, pero la de D es más ancha: su desviación estándar es 25% contra 15%. La probabilidad de perder en el año es el área bajo cada densidad a la izquierda de cero:

$$P(R_C < 0) = 0.297, \qquad P(R_D < 0) = 0.374.$$

Con la misma esperanza, la varianza decide qué tan probable es una pérdida: en C, unos tres años de cada diez; en D, casi cuatro de cada diez.

<!-- diapositivas: figura sola -->
![Dos densidades normales con el mismo centro en 8%: una más angosta y alta para la acción C, con desviación estándar de 15%, y una más ancha y baja para la acción D, con desviación estándar de 25%; el área a la izquierda de cero está sombreada en cada una, con probabilidad de perder de 0.297 para C y de 0.374 para D](img/normal_dos_rendimientos.png)

#### 5.2 Covarianza y correlación

> **¿De dónde sale la fórmula?** Con dos variables, además de qué tanto se aleja cada una de su media, importa si se alejan al mismo tiempo y en la misma dirección. El producto $(X - \mu_X)(Y - \mu_Y)$ es positivo cuando las dos están por arriba o las dos por abajo de su media, y negativo cuando una está arriba y la otra abajo. Su promedio resume cuál de los dos casos domina.

**Definición (covarianza y correlación).** La **covarianza** de $X$ y $Y$ es

$$\operatorname{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = \int (x - \mu_X)(y - \mu_Y)\, dF_{X,Y}(x, y),$$

y su **correlación** es la covarianza dividida entre las dos desviaciones estándar,

$$\rho_{X,Y} = \frac{\operatorname{Cov}(X, Y)}{\sigma_X \sigma_Y}, \qquad -1 \leq \rho_{X,Y} \leq 1.$$

La covarianza de una variable consigo misma es su varianza, $\operatorname{Cov}(X, X) = \operatorname{Var}(X)$. La correlación no tiene unidades: vale 1 si las variables se mueven juntas en línea recta, $-1$ si se mueven en sentidos opuestos y 0 si no hay relación lineal. Si $X$ y $Y$ son independientes (sección 3.3), su covarianza es 0, por la propiedad 4 de la esperanza; lo contrario no siempre es cierto.

**Definición (matriz de varianzas y covarianzas).** Para un vector aleatorio $\mathbf{X} = (X_1, \dots, X_n)$, la **matriz de varianzas y covarianzas** reúne todas las covarianzas entre sus componentes:

$$\boldsymbol{\Sigma} = \begin{pmatrix} \operatorname{Var}(X_1) & \operatorname{Cov}(X_1, X_2) & \cdots & \operatorname{Cov}(X_1, X_n) \\ \operatorname{Cov}(X_2, X_1) & \operatorname{Var}(X_2) & \cdots & \operatorname{Cov}(X_2, X_n) \\ \vdots & \vdots & \ddots & \vdots \\ \operatorname{Cov}(X_n, X_1) & \operatorname{Cov}(X_n, X_2) & \cdots & \operatorname{Var}(X_n) \end{pmatrix}.$$

En la diagonal están las varianzas de cada componente y fuera de ella las covarianzas entre pares. Es simétrica, porque $\operatorname{Cov}(X_i, X_j) = \operatorname{Cov}(X_j, X_i)$. Así como $E[\mathbf{X}]$ dice dónde está el centro del vector, $\boldsymbol{\Sigma}$ dice qué tan disperso está y cómo se mueven juntas sus componentes.

**Ejemplo (las dos acciones de 3.3).** En el modelo de la figura de 3.3, las desviaciones estándar son $\sigma_A = 25\%$ y $\sigma_B = 30\%$, y la correlación es $\rho_{A,B} = 0.6$. La covarianza es

$$\operatorname{Cov}(R_A, R_B) = \rho_{A,B}\, \sigma_A \sigma_B = 0.6 \times 0.25 \times 0.30 = 0.045,$$

y la matriz de varianzas y covarianzas es

$$\boldsymbol{\Sigma} = \begin{pmatrix} 0.25^2 & 0.045 \\ 0.045 & 0.30^2 \end{pmatrix} = \begin{pmatrix} 0.0625 & 0.045 \\ 0.045 & 0.09 \end{pmatrix}.$$

La covarianza positiva es la inclinación de las curvas de nivel: cuando una acción sube, la otra tiende a subir. Con correlación 0, las curvas no estarían inclinadas.

En finanzas, una correlación de 0.6 dice que las dos acciones comparten buena parte de su riesgo: las mueven las mismas noticias, como una recesión o un alza de tasas, que es el riesgo sistemático. La correlación decide cuánto sirve combinarlas. En una cartera con mitad del dinero en cada una, la desviación estándar resulta (la fórmula se ve en la 3_):

| Correlación $\rho_{A,B}$ | Desviación estándar de la cartera |
| ------------------------ | --------------------------------- |
| $1$                      | $27.5\%$                          |
| $0.6$                    | $24.6\%$                          |
| $0$                      | $19.5\%$                          |
| $-0.6$                   | $12.5\%$                          |

Con correlación 1, la cartera es tan riesgosa como el promedio de las dos acciones, 27.5%, y combinarlas no reduce nada. Cuanto menor la correlación, más se compensan las caídas de una con las subidas de la otra, y menor el riesgo, con el mismo rendimiento esperado de 6.5%. Una correlación negativa, como la que a veces tienen los bonos de gobierno con las acciones en una crisis, funciona como cobertura. Por eso diversificar sirve contra el riesgo propio de cada emisora y casi nada contra lo que mueve a todas juntas. Y así como una normal queda determinada por $\mu$ y $\sigma^2$, la densidad conjunta de la figura, una normal de dos variables, queda determinada por su esperanza $E[(R_A, R_B)] = (5\%, 8\%)$ y su matriz $\boldsymbol{\Sigma}$.

### 6. Riesgo de cola

#### 6.1 Cuantiles y valor en riesgo

**Ejemplo (¿qué tan mal puede ir un año?).** A quien invierte en el S&P 500 no solo le importa cuánto gana en promedio, sino qué tan mal le puede ir en un año malo. El promedio de 11.86% y la desviación estándar no contestan esa pregunta directamente. Los datos ordenados sí. De los 98 años entre 1928 y 2025, los cinco peores fueron 1931 ($-43.84\%$), 2008 ($-36.55\%$), 1937 ($-35.34\%$), 1974 ($-25.90\%$) y 1930 ($-25.12\%$): en esos 5 de 98 años, alrededor del 5%, el índice perdió 25.12% o más. Y si ordenamos los 98 años del peor al mejor, el que queda a la mitad rindió 14.82%: la mitad de los años rindió eso o menos, y la otra mitad, más. Este valor central es mayor que el promedio, porque las pocas caídas grandes jalan el promedio hacia abajo. Los números 25.12% y 14.82% son cuantiles de los rendimientos.

> **¿De dónde sale la fórmula?** La función de distribución contesta "dado un valor $x$, ¿qué probabilidad hay de no pasarlo?". El cuantil contesta la pregunta inversa: "dada una probabilidad $p$, ¿qué valor no se pasa con probabilidad $p$?". Es invertir $F_X$: buscar el $x$ en el que $F_X(x) = p$. Si $F_X$ tiene saltos, como en las variables discretas y mixtas de 3.2, puede que ningún $x$ dé exactamente $p$, y se toma el primer valor en el que $F_X$ alcanza $p$.

**Definición (cuantil).** Para $0 < p < 1$, el **cuantil** $p$ de $X$ es

$$q_p = \min\{x : F_X(x) \geq p\}.$$

Si $F_X$ es continua y creciente, es simplemente su inversa: $q_p = F_X^{-1}(p)$. Algunos cuantiles tienen nombre propio: la **mediana** es $q_{0.5}$, el valor que deja la mitad de la probabilidad de cada lado; los **cuartiles** son $q_{0.25}$ y $q_{0.75}$; y los **percentiles** son los cuantiles $0.01, 0.02, \dots, 0.99$.

**Ejemplo (el S&P 500 con el modelo normal).** Si $R \sim N(\mu, \sigma^2)$, sus cuantiles son $q_p = \mu + \sigma z_p$, donde $z_p$ es el cuantil de la normal con media 0 y desviación 1; para el 5%, $z_{0.05} = -1.645$. Modelemos el S&P 500 con una normal que tenga el promedio y la desviación estándar de sus 98 rendimientos, $\mu = 11.86\%$ y $\sigma = 19.40\%$:

$$q_{0.05} = 11.86\% - 1.645 \times 19.40\% = -20.1\%.$$

El modelo dice que en el peor año de cada veinte se pierde 20.1% o más.

<!-- diapositivas: figura sola -->
![Dos paneles para el rendimiento anual del S&P 500 con una normal de media 11.86% y desviación 19.40%: a la izquierda, la densidad con la cola izquierda de 5% sombreada en rojo hasta el cuantil de -20.1%, sobre un histograma de fondo; a la derecha, la parte baja de la función de distribución, con una flecha horizontal desde p = 0.05 hasta la curva y otra vertical hasta el cuantil de -20.1%](img/normal_cuantil_var.png)

> **Observación (valor en riesgo).** En finanzas, el cuantil bajo de un rendimiento, o el alto de una pérdida, se llama **valor en riesgo** (VaR, por *value at risk*): la pérdida que solo se supera con probabilidad $1 - p$. Con 10,000 pesos en el S&P 500, el VaR anual al 95% según el modelo normal es de unos 2,006 pesos: en uno de cada veinte años se pierde más que eso. Bancos y casas de bolsa lo usan para medir y poner límites al riesgo de sus posiciones. Su limitación es que dice dónde empieza la cola, pero no qué tan grandes son las pérdidas una vez que se cruza (sección 6.2); las colas largas, más pesadas que las de la normal, son justo ese problema.

#### 6.2 Valor en riesgo condicional (CVaR)

El VaR al 95% del modelo normal del S&P 500 dice que en uno de cada veinte años se pierde 20.1% o más, pero no cuánto se pierde en promedio en esos años malos. Dos inversiones con el mismo VaR pueden tener colas muy distintas: en una, los años malos apenas pasan del umbral; en la otra, lo pasan por mucho.

> **¿De dónde sale la fórmula?** Queremos el promedio de $X$ solo en los casos de un evento, como la cola de los años malos. Es la esperanza de 4.1 restringida a ese evento, como en la probabilidad condicional de 3.3: se acumula $x\, dF_X(x)$ solo sobre el evento y se reescala dividiendo entre su probabilidad, para que los pesos vuelvan a sumar 1.

**Definición (esperanza condicional).** Si $P(X \in A) > 0$, la esperanza de $X$ dado que cae en $A$ es

$$E[X \mid X \in A] = \frac{1}{P(X \in A)} \int_A x\, dF_X(x).$$

**Definición (CVaR).** Para un rendimiento $R$ y un nivel $p$, como 0.05, el **valor en riesgo condicional** es el rendimiento promedio en el peor $100p\%$ de los casos:

$$\text{CVaR}_p = E[R \mid R \leq q_p] = \frac{1}{p} \int_{(-\infty, q_p]} x\, dF_R(x).$$

También se le llama déficit esperado (*expected shortfall*). Como promedia valores que están todos por debajo de $q_p$, el CVaR siempre es igual o peor que el VaR. Para una pérdida $L$, la cola mala es la de arriba, y el CVaR es $E[L \mid L \geq q_{1-p}]$.

**Ejemplo (el S&P 500).** En 6.1, el cuantil 5% de los 98 rendimientos del S&P 500 fue $-25.12\%$, el quinto peor año. El CVaR al 5% es el promedio de esos cinco peores años:

$$\frac{-43.84\% - 36.55\% - 35.34\% - 25.90\% - 25.12\%}{5} = -33.35\%.$$

En el peor 5% de los años, el índice no perdió "25% o más" en abstracto: perdió en promedio un tercio de su valor.

**Ejemplo (rendimientos normales).** Si $R \sim N(\mu, \sigma^2)$, se puede demostrar que $\text{CVaR}_p = \mu - \sigma\, \varphi(z_p)/p$, donde $\varphi$ es la densidad de la normal con media 0 y desviación 1; para el 5%, $\varphi(z_{0.05})/0.05 = 2.063$. Con la normal del S&P 500 de 6.1, $\mu = 11.86\%$ y $\sigma = 19.40\%$:

$$\text{CVaR}_{0.05} = 11.86\% - 19.40\% \times 2.063 = -28.2\%.$$

Con 10,000 pesos, el VaR anual al 95% es de unos 2,006 pesos y el CVaR de unos 2,817: el primero dice dónde empieza la cola; el segundo, cuánto se pierde en promedio una vez dentro de ella. En la figura, el CVaR es el centro de masa de la cola sombreada.

<!-- diapositivas: figura sola -->
![Densidad normal del rendimiento anual del S&P 500, con media 11.86% y desviación 19.40%, sobre un histograma de fondo, con la cola izquierda de 5% sombreada en rojo; una línea punteada roja marca el VaR en -20.1%, donde empieza la cola, y una línea azul marino marca el CVaR en -28.2%, el promedio de la cola](img/normal_cvar.png)

> **Observación (por qué se prefiere el CVaR).** El VaR solo mira el borde de la cola; el CVaR mira toda la cola. Por eso el Comité de Basilea, que fija los estándares internacionales de capital de los bancos, sustituyó en su revisión de las reglas de riesgo de mercado el VaR al 99% por el CVaR al 97.5%. Con esto se cierra la nota: la esperanza y la varianza resumen el centro y la dispersión de una distribución; los cuantiles y el CVaR, su cola, que es donde está el riesgo que más importa.

## Apéndice: Complementos de probabilidad

Esta sección amplía el núcleo; no forma parte del objetivo ni se evalúa. Precisa a qué eventos se les asigna probabilidad, completa las definiciones de vector aleatorio e independencia, muestra los casos en que la esperanza no basta o no existe, y reúne los ejemplos continuos y de riesgo de crédito que no caben en la clase.

**¿A qué eventos les asignamos probabilidad?** Si podemos decir qué tan probable es perder, también deberíamos poder decir qué tan probable es no perder. Si podemos hablar de "el FIX rebasa 20 pesos el lunes" y de "lo rebasa el martes", también deberíamos poder hablar de "lo rebasa algún día". La colección de eventos a los que asignamos probabilidad debe ser cerrada bajo estas operaciones. A esa colección se le llama σ-álgebra.

Una **σ-álgebra** $\mathcal{F}$ sobre $\Omega$ es una colección de eventos que cumple:

1. $\Omega \in \mathcal{F}$: siempre podemos preguntar "¿ocurre alguno de los resultados posibles?".
2. Si $A \in \mathcal{F}$, entonces $A^c \in \mathcal{F}$: si podemos preguntar "¿ocurre $A$?", podemos preguntar "¿no ocurre?".
3. Si $A_1, A_2, \dots \in \mathcal{F}$, entonces $A_1 \cup A_2 \cup \cdots \in \mathcal{F}$: si podemos preguntar por cada evento, podemos preguntar si ocurre alguno.

De estas tres reglas se deduce que $\emptyset \in \mathcal{F}$ y, por las leyes de De Morgan, que las intersecciones también están en $\mathcal{F}$.

**Ejemplo (dos inversionistas).** Con $\Omega = \{\text{pérdida}, \text{sin cambio}, \text{ganancia}\}$, un inversionista que solo se entera de si perdió o no distingue los eventos

$$\mathcal{F}_1 = \{\emptyset, \{\text{pérdida}\}, \{\text{sin cambio}, \text{ganancia}\}, \Omega\}.$$

Otro que ve el rendimiento completo distingue los 8 subconjuntos de $\Omega$; esa es su σ-álgebra $\mathcal{F}_2$. Las dos cumplen las tres reglas, pero $\mathcal{F}_2$ contiene más eventos: más información. El primero no puede contestar "¿hubo ganancia?", porque $\{\text{ganancia}\} \notin \mathcal{F}_1$.

Cuando $\Omega$ es discreto, siempre podemos tomar todos sus subconjuntos como σ-álgebra. Cuando es continuo, como el rendimiento en $[-100\%, \infty)$, no es posible asignar probabilidad de forma consistente a todos los subconjuntos, y se usan los intervalos y lo que se construye con ellos; los detalles quedan fuera del alcance de esta nota.

**Definición (distribución marginal).** La distribución de una sola componente $X_k$, sin importar lo que valgan las demás, es su **marginal**. Su densidad se obtiene acumulando la conjunta sobre todos los valores de las otras componentes: $dF_{X_k}(x_k) = \int dF_{\mathbf{X}}(\mathbf{x})$, integrando en todas las coordenadas menos la $k$-ésima. De la conjunta salen las marginales, pero las marginales no determinan la conjunta.

**Definición (variables independientes).** Las componentes de un vector aleatorio $(X_1, \dots, X_n)$ son **independientes** si los eventos $\{X_1 \leq x_1\}, \dots, \{X_n \leq x_n\}$ lo son para cualesquiera $x_1, \dots, x_n$, es decir, si la conjunta es el producto de las marginales:

$$F_{\mathbf{X}}(x_1, \dots, x_n) = F_{X_1}(x_1) \cdots F_{X_n}(x_n), \qquad \text{o bien} \qquad dF_{\mathbf{X}}(\mathbf{x}) = dF_{X_1}(x_1) \cdots dF_{X_n}(x_n).$$

Con independencia, las marginales sí determinan la conjunta: basta multiplicarlas.

**Propiedades de la función de distribución.** De los axiomas se deduce que:

1. $0 \leq F_X(x) \leq 1$.
2. $F_X$ nunca decrece: si $a < b$, entonces $\{X \leq a\} \subseteq \{X \leq b\}$, y por la monotonía de 2.3, $F_X(a) \leq F_X(b)$.
3. $F_X(x)$ se acerca a 0 cuando $x \to -\infty$ y a 1 cuando $x \to \infty$.
4. Como $\{X \leq b\}$ se parte en $\{X \leq a\}$ y $\{a < X \leq b\}$, la aditividad da

   $$P(a < X \leq b) = F_X(b) - F_X(a), \qquad a < b.$$

Por la propiedad 4, $F_X$ basta para calcular la probabilidad de cualquier intervalo: conocer $F_X$ es conocer la distribución.

**Una variable sin esperanza.** No toda variable tiene esperanza: la distribución de Cauchy, con densidad $f_X(x) = 1 / (\pi(1 + x^2))$, cumple $\int |x|\, dF_X(x) = \infty$ y no tiene esperanza.

**Ejemplo (paradoja de San Petersburgo).** Se lanza una moneda justa hasta que sale sol. Si eso ocurre en el lanzamiento $x$, se paga un premio de $2^{x-1}$ pesos. La probabilidad de necesitar $x$ lanzamientos es $1/2^x$, así que el premio esperado es

$$E[\text{premio}] = \sum_{x=1}^{\infty} 2^{x-1} \frac{1}{2^x} = \sum_{x=1}^{\infty} \frac{1}{2} = \infty.$$

Si el valor justo de una apuesta fuera su valor esperado, como proponía Huygens (1657), habría que pagar cualquier cantidad por jugar, y casi nadie pagaría más de unos cuantos pesos. Daniel Bernoulli (1738) resolvió la paradoja proponiendo que la gente no valora el dinero sino la utilidad que le da, y que cada peso adicional vale menos que el anterior.

**Esperanza como área.** Si $X \geq 0$, $E[X] = \int_0^\infty (1 - F_X(x))\, dx$: el área entre la función de distribución y la recta de altura 1.

**Ejemplo (precio de la acción).** Si ignoramos la posibilidad de quiebra, un modelo común para $S_1$ es la distribución **lognormal**. El rendimiento continuo del año, $X = \ln(S_1 / s_0)$, se supone repartido en forma de campana (una normal, sección 5.1) alrededor de una media $\mu$ y con desviación estándar $\sigma$; el precio es entonces $S_1 = s_0 e^{X}$, que nunca es negativo porque $e^{X} > 0$. Su densidad es

$$dF_{S_1}(x) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\left( -\frac{(\ln(x / s_0) - \mu)^2}{2\sigma^2} \right) dx, \qquad x > 0,$$

y $dF_{S_1}(x) = 0$ para $x \leq 0$: no hay probabilidad por debajo de cero. Con $s_0 = 100$, $\mu = 5\%$ y $\sigma = 25\%$ (valores ilustrativos):

- $F_{S_1}(100) = 0.421$ es la probabilidad de perder: que en un año la acción no valga más de lo que pagamos.
- $P(90 < S_1 \leq 110) = \int_{90}^{110} dF_{S_1}(x) = F_{S_1}(110) - F_{S_1}(90) = 0.572 - 0.267 = 0.305$: el área en dorado bajo la densidad, o la subida de $F_{S_1}$ entre 90 y 110.

![Dos paneles para el precio de la acción en un año con distribución lognormal, s0 = 100, mu = 5% y sigma = 25%: a la izquierda, la densidad, una curva asimétrica con su máximo cerca de 100 y cola larga a la derecha, con el área entre 90 y 110 sombreada en dorado (0.305); a la derecha, la función de distribución, una curva en S que pasa por F(90) = 0.267 y F(110) = 0.572](img/accion_lognormal_densidad_distribucion.png)

**Teorema (ley del estadístico inconsciente).** Si $Y = g(X)$, entonces

$$E[Y] = \int g(x)\, dF_X(x).$$

No hace falta encontrar la distribución de $Y$: basta ponderar cada valor $g(x)$ con la densidad de $X$. Por ejemplo, el precio lognormal del ejemplo anterior es $S_1 = s_0 e^{X}$ con $X$ el rendimiento continuo, y $E[S_1] = \int s_0 e^{x}\, dF_X(x)$. Con $s_0 = 100$, $\mu = 5\%$ y $\sigma = 25\%$, esta integral da $E[S_1] = 108.46$ pesos (su cálculo usa la normal, sección 5.1).

**Riesgo de crédito con una variable mixta.** Los ejemplos siguientes siguen al bono de 3.1, cuya emisora puede incumplir: la variable de incumplimiento $D$, la pérdida $L$ del inversionista y lo que esa pérdida implica para el precio del bono, su cuantil y su CVaR.

**Ejemplo (incumplimiento de un bono).** Supongamos que la emisora del bono incumple con probabilidad $0.05$. La variable $D$ de 3.1 es discreta, con dos valores posibles:

| Resultado | $x$ | $dF(x) = P(D = x)$ |
| --------- | --- | ------------------ |
| Paga      | $0$ | $0.95$             |
| Incumple  | $1$ | $0.05$             |

Sumando estas probabilidades, la función de distribución de $D$ es una escalera que sube en cada valor posible:

$$F(x) = \begin{cases} 0, & x < 0 \\ 0.95, & 0 \leq x < 1 \\ 1, & x \geq 1 \end{cases}$$

Así, $F(0) = 0.95$ es la probabilidad de que la emisora pague.

![Dos paneles para el incumplimiento de un bono con probabilidad 0.05: a la izquierda, la densidad con una barra de 0.95 en x = 0 (paga) y otra de 0.05 en x = 1 (incumple); a la derecha, la función de distribución, una escalera que vale 0 antes de 0, salta a 0.95 en x = 0 y a 1 en x = 1](img/incumplimiento_masa_distribucion.png)

**Ejemplo (pérdida con incumplimiento).** Volvamos al bono, ahora con valor nominal de 100 pesos, y midamos la pérdida $L$ del inversionista. Con probabilidad $0.95$ la emisora paga y no hay pérdida: $L = 0$. Con probabilidad $0.05$ incumple, y como algo se recupera, la pérdida queda en algún punto entre 20 y 100 pesos, cualquiera con la misma posibilidad (ilustrativo). $L$ es mixta: tiene un salto en 0 y una parte continua entre 20 y 100.

$$dF_L(x) = \begin{cases} 0.95, & x = 0 \quad \text{(salto: paga)} \\ \dfrac{0.05}{80}\, dx, & 20 < x \leq 100 \quad \text{(continua: incumple)} \\ 0, & \text{en otro caso} \end{cases}$$

La parte continua reparte la probabilidad de incumplir, $0.05$, de manera pareja sobre los 80 pesos que van de 20 a 100. Sumando el salto y el área, el total es $0.95 + 0.05 = 1$. Por ejemplo, la probabilidad de perder más de la mitad del bono es

$$P(L > 50) = \int_{(50, 100]} dF_L(x) = \frac{0.05}{80} \times 50 = 0.03125,$$

y la de perder algo es $P(L > 0) = 1 - F_L(0) = 1 - 0.95 = 0.05$.

![Dos paneles para la pérdida de un bono de 100 pesos que incumple con probabilidad 0.05: a la izquierda, la densidad, con una flecha en 0 que representa el salto P(L = 0) = 0.95 y un rectángulo dorado de área 0.05 entre 20 y 100; a la derecha, la función de distribución, que salta de 0 a 0.95 en x = 0, se queda plana hasta 20 y sube en línea recta hasta 1 en 100](img/perdida_incumplimiento_mixta.png)

**Ejemplo (pérdida esperada).** Para la pérdida mixta $L$ de arriba, el salto en 0 no aporta y la parte continua sí:

$$E[L] = 0(0.95) + \int_{20}^{100} x\, \frac{0.05}{80}\, dx = 0.05 \times 60 = 3 \text{ pesos}.$$

Es la probabilidad de incumplir por la pérdida promedio si se incumple (60 pesos, el punto medio entre 20 y 100). Así calculan los bancos su pérdida esperada por crédito.

**Ejemplo (precio de un bono con riesgo de crédito).** Volvamos al bono de 100 pesos con la pérdida mixta $L$ de arriba. Al vencimiento paga $100 - L$, así que por linealidad su pago esperado es

$$E[100 - L] = 100 - E[L] = 100 - 3 = 97 \text{ pesos}.$$

Si al inversionista solo le importa el valor esperado (la idea de Huygens, 1657, de la paradoja de San Petersburgo) y el CETE a un año paga 10% (ilustrativo), el precio justo hoy es el pago esperado descontado:

$$\frac{97}{1.10} = 88.18 \text{ pesos},$$

contra $100 / 1.10 = 90.91$ pesos si el bono no pudiera incumplir. La diferencia, 2.73 pesos, es el descuento por riesgo de crédito.

> **Observación.** La esperanza es fácil de calcular e interpretar, pero puede engañar como medida de ubicación cuando la distribución es asimétrica o es una mezcla de dos poblaciones muy distintas. En la pérdida $L$, la esperanza es 3 pesos, un valor que $L$ nunca toma: o no se pierde nada o se pierden entre 20 y 100. En esos casos, la mediana (sección 6.1) suele describir mejor el centro.

**Ejemplo (pérdida con incumplimiento).** Para la pérdida mixta $L$, $F_L(0) = 0.95$, así que la mediana es $q_{0.5} = 0$: en un año típico no se pierde nada, aunque la pérdida esperada sea $E[L] = 3$ pesos (la observación anterior). Para el cuantil 99%, se busca dónde la parte continua de $F_L$ alcanza 0.99:

$$0.95 + \frac{0.05}{80}(x - 20) = 0.99 \quad \Longrightarrow \quad q_{0.99} = 84 \text{ pesos}.$$

Con probabilidad 99%, la pérdida del bono no pasa de 84 pesos.

**Ejemplo (pérdida con incumplimiento).** Para la pérdida $L$, el cuantil 99% fue $q_{0.99} = 84$ pesos. Por encima de 84, la pérdida se reparte de manera pareja hasta 100, así que

$$\text{CVaR} = E[L \mid L \geq 84] = \frac{84 + 100}{2} = 92 \text{ pesos}:$$

en el peor 1% de los casos, el inversionista pierde en promedio 92 de cada 100 pesos.

## Fuentes y referencias recomendadas

- Brown, E. N., & Kass, R. E. (2009). *What Is Statistics?* The American Statistician, 63(2), 105-110: qué es la estadística y cómo se relaciona con la probabilidad.
- Bernstein, P. L. (1996). *Against the Gods: The Remarkable Story of Risk*. John Wiley & Sons: historia del riesgo, del problema de los puntos a la teoría de carteras.
- Devlin, K. (2008). *The Unfinished Game: Pascal, Fermat, and the Seventeenth-Century Letter that Made the World Modern*. Basic Books: el problema de los puntos y la correspondencia de 1654.
- Stigler, S. M. (1986). *The History of Statistics: The Measurement of Uncertainty before 1900*. Belknap Press of Harvard University Press: de Graunt y Bernoulli a Galton y Pearson.
- Graunt, J. (1662). *Natural and Political Observations Made upon the Bills of Mortality*. London: primeras tablas estadísticas construidas a partir de registros.
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd: la inferencia estadística moderna a partir de muestras.
- Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Springer: los axiomas de la probabilidad.
- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 17, 21-86: primer modelo probabilístico de los precios de mercado.
- Shiller, R. J. (2023). *U.S. Stock Markets 1871-Present and CAPE Ratio* [datos]. Yale University. http://www.econ.yale.edu/~shiller/data.htm: nivel mensual del S&P 500 hasta septiembre de 2023 (promedio mensual de los cierres diarios).
- Yahoo Finance. (2026). *S&P 500 (^GSPC), historial mensual* [datos]. https://finance.yahoo.com/quote/%5EGSPC/history: cierre mensual del S&P 500 de octubre de 2023 a diciembre de 2025.
- Damodaran, A. (2026). *Historical Returns on Stocks, Bonds and Bills: 1928-2025*. NYU Stern School of Business. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html: rendimientos anuales del S&P 500 con dividendos.
- Basel Committee on Banking Supervision. (2019, 14 de enero). *Minimum capital requirements for market risk*. Bank for International Settlements. https://www.bis.org/bcbs/publ/d457.htm: sustitución del VaR al 99% por el expected shortfall al 97.5% en el riesgo de mercado.
- Bodie, Z., Kane, A., & Marcus, A. J. (2021). *Investments* (12ª ed.). McGraw-Hill: rendimiento esperado y desviación estándar por escenarios, riesgo sistemático y riesgo diversificable.
- Mandelbrot, B. (1963). *The Variation of Certain Speculative Prices*. Journal of Business, 36(4), 394-419: los cambios de precio tienen colas mucho más pesadas que la normal.
- Cont, R. (2001). *Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues*. Quantitative Finance, 1(2), 223-236: colas largas y otros hechos estilizados de los rendimientos.
- Taleb, N. N. (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House: eventos extremos que los modelos basados en la normal tratan como imposibles.
- Li, D. X. (2000). *On Default Correlation: A Copula Function Approach*. Journal of Fixed Income, 9(4), 43-54: la cópula gaussiana con la que se valuaron los CDO hipotecarios antes de 2008.
- Financial Crisis Inquiry Commission. (2011). *The Financial Crisis Inquiry Report*. U.S. Government Printing Office: causas de la crisis de 2008, incluida la subestimación del riesgo en los modelos.

## Cierre de la unidad — Lo esencial para recordar

- La probabilidad modela la incertidumbre con un **espacio muestral**, sus eventos y una **medida de probabilidad** $P$ que cumple los axiomas de Kolmogorov, sin importar si los números salen del juicio o de los datos.
- Una **variable aleatoria** convierte escenarios en números, y su **distribución** dice qué valores toma y con qué probabilidad.
- Con escenarios, el **rendimiento esperado** $E[R] = \sum_i p_i r_i$ y la **volatilidad** $\sigma_R$, la raíz de $\sum_i p_i (r_i - E[R])^2$, resumen el centro y la dispersión del rendimiento, 5.5% y 15.40% para la acción del ejemplo; la **correlación** decide cuánto ayuda combinar activos.
- El **VaR** dice dónde empieza la cola de pérdidas y el **CVaR** cuánto se pierde en promedio dentro de ella, algo que la media y la volatilidad no cuentan.
