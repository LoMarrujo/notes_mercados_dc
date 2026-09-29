# Unidad 2 · Laboratorio: calibrar un modelo de tasas con datos

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Este laboratorio amplía el apéndice de [`1_valuacion_instrumentos_deuda.md`](../../notas_unidades/unidad2/1_valuacion_instrumentos_deuda.md), que simula precios con un modelo de tasas ya calibrado. Aquí se muestra de dónde salen esos parámetros y, sobre todo, qué tan bien predicen. No forma parte del objetivo de la unidad ni se evalúa en el examen.

El hilo del laboratorio es una sola idea: **el modelo de tasas de finanzas y la regresión de econometría son el mismo objeto**. Quien sabe correr mínimos cuadrados ya sabe calibrar un modelo de tasas, y quien sabe calibrarlo puede abrirlo a variables explicativas sin aprender ninguna técnica nueva.

## Contenido

|      | Tema                               | Qué cubre                                                                     |
| ---- | ---------------------------------- | ----------------------------------------------------------------------------- |
| I    | El modelo de tasas es un AR(1)     | Cómo la discretización de Vasicek se vuelve una regresión, y cómo se invierte |
| II   | Calibración con datos reales       | La muestra, por qué arranca en 2001, y los parámetros que salen               |
| III  | La trampa del R²                   | Por qué 0.98 en niveles y 0.007 en cambios son el mismo modelo                |
| IV   | Variables explicativas             | Abrir el nivel de largo plazo a la macro, y la trampa de la pendiente         |
| V    | ¿Predice?                          | Evaluación fuera de muestra contra la caminata aleatoria                      |
| VI   | Lo que los datos no pueden decidir | La raíz unitaria, y qué significa para el modelo que se eligió                |
| VII  | Dónde queda este modelo en el mapa | Qué no hace Vasicek, y qué corrige cada extensión de la familia               |
| VIII | Ejercicios                         | Cambiar la serie, la muestra y los regresores, y ver qué sobrevive            |

---

### 1. El modelo de tasas es un AR(1)

El modelo de Vasicek dice que la tasa corta es atraída hacia un nivel de largo plazo $r_{lp}$ con velocidad $\kappa$, y que en el camino recibe empujones aleatorios de tamaño $\sigma$. Entre una fecha de observación y la siguiente, separadas por $\Delta t$ años, su forma exacta es la que usa la simulación del apéndice:

$$R_{t+1} = r_{lp}\left(1-e^{-\kappa\Delta t}\right) + e^{-\kappa\Delta t}R_t + \varepsilon_{t+1}, \qquad \varepsilon_{t+1}\sim N\left(0,\ \sigma^2\dfrac{1-e^{-2\kappa\Delta t}}{2\kappa}\right)$$

- **$R_t$**: tasa corta observada en el mes $t$, incierta vista desde antes y por eso en mayúscula.
- **$r_{lp}$**: nivel de largo plazo hacia el que la tasa es atraída, en por ciento anual.
- **$\kappa$**: velocidad de reversión, en unidades de 1/año.
- **$\sigma$**: volatilidad de la tasa, en puntos porcentuales anuales.
- **$\Delta t$**: fracción de año entre dos observaciones. Con datos mensuales, $\Delta t = 1/12$.
- **$\varepsilon_{t+1}$**: perturbación aleatoria del periodo, normal, de media cero y varianza $\sigma^2(1-e^{-2\kappa\Delta t})/2\kappa$.

Leída con cuidado, esa expresión es una regresión lineal de la tasa de mañana contra la tasa de hoy. Escribiéndola como se escribiría cualquier regresión,

$$r_{t+1} = a + b\,r_t + \varepsilon_{t+1}$$

- **$r_t$**: la misma tasa, ahora en minúscula porque en la regresión ya es un dato observado, no una cantidad incierta.
- **$a$**: ordenada al origen de la regresión, sin interpretación económica directa por sí sola.
- **$b$**: pendiente, es decir, cuánto de la tasa de este mes sobrevive al siguiente.
- **$\varepsilon_{t+1}$**: residuo de la regresión, el mismo objeto que la perturbación de arriba.

La correspondencia entre las dos expresiones es directa: $b = e^{-\kappa\Delta t}$ y $a = r_{lp}(1-b)$. El cambio de $R$ a $r$ no es cosmético: marca el paso de un modelo sobre una cantidad incierta a una estimación hecha con datos ya observados.

¿De dónde sale la fórmula? El nivel al que revierte la tasa es una media ponderada entre su nivel de largo plazo y donde está hoy, con peso $e^{-\kappa\Delta t}$ sobre el presente: cuanto más grande $\kappa$, más rápido se olvida de dónde venía. Es el mismo descuento exponencial de la sección 2 de la nota, aplicado a la distancia que falta por recorrer en vez de a un flujo de dinero.

Invertir la correspondencia recupera los parámetros del modelo a partir de los coeficientes de la regresión:

$$\kappa = -\dfrac{\ln b}{\Delta t}, \qquad r_{lp} = \dfrac{a}{1-b}, \qquad \sigma = \text{de}(\varepsilon)\sqrt{\dfrac{2\kappa}{1-b^2}} \qquad (0 < b < 1)$$

- **$a$, $b$**: los dos coeficientes que devuelve la regresión.
- **$\text{de}(\varepsilon)$**: desviación estándar de los residuos de esa misma regresión.
- **$\kappa$, $r_{lp}$, $\sigma$**: los tres parámetros del modelo, ya definidos arriba, ahora expresados en función de lo que la regresión estimó.

La restricción $0 < b < 1$ no es un tecnicismo. Con $b \geq 1$ el logaritmo da cero o un número negativo, $\kappa$ deja de existir y el proceso no revierte: se aleja. La función que hace esta conversión en [`calibracion.py`](../../notas_unidades/unidad2/codigo/calibracion.py) rechaza ese caso en vez de devolver un número sin sentido, y la sección 4 muestra cuándo aparece.

Una medida más legible que $\kappa$ es la **vida media**, $\ln 2/\kappa$: los años que tarda la tasa en cerrar la mitad de la distancia que la separa de su nivel de largo plazo.

### 2. Calibración con datos reales

Los datos son mensuales y vienen de FRED, que los sirve en CSV sin necesidad de registrarse. [`datos_fred.py`](../../notas_unidades/unidad2/codigo/datos_fred.py) los descarga y los guarda con su fecha en [`fred_tasas_mensual.csv`](../../notas_unidades/unidad2/datos/fred_tasas_mensual.csv), para que los resultados no cambien solos con el paso de los meses.

La muestra arranca en julio de 2001 por dos razones que coinciden. Es cuando Banxico adopta formalmente el esquema de objetivos de inflación, así que la forma en que se determinan las tasas cambia a partir de ahí; y es donde empieza la serie del bono a 10 años. Incluir 1997 a 2000 metería el periodo posterior a la crisis del Tequila, con tasas arriba de 20%, y eso triplica la volatilidad estimada: el modelo describiría un régimen que ya no existe.

![Dos paneles: a la izquierda, la tasa interbancaria mexicana a 3 meses de 2001 a 2026, oscilando entre 3% y 12%, con una línea horizontal en el nivel de largo plazo estimado de 6.11%; a la derecha, el RMSE relativo de dos modelos contra la caminata aleatoria, por arriba de 1 a 1 y 6 meses y por debajo a 12 y 24 meses](../../notas_unidades/unidad2/img/calibracion_tasas.png)

Corriendo la regresión sobre la tasa interbancaria a 3 meses:

| Coeficiente o parámetro | Valor         |
| ----------------------- | ------------- |
| $a$                     | 0.1094        |
| $b$                     | 0.9821        |
| $\kappa$                | 0.217         |
| Vida media              | 3.2 años      |
| Nivel de largo plazo    | 6.11%         |
| $\sigma$                | 1.24 pp anual |
| Observaciones           | 301           |

El nivel de largo plazo de 6.11% es creíble: la tasa de referencia de Banxico estaba en 6.50% en la decisión del 6 de agosto de 2026. La vida media de 3.2 años dice que, si hoy la tasa está dos puntos por encima de su nivel, en poco más de tres años se espera que solo quede un punto de esa diferencia.

Hay un detalle sobre el cual la nota es explícita y conviene repetir. La simulación del apéndice usa **dos** niveles de largo plazo distintos, porque hacen cosas distintas. El de 6.11%, el estimado aquí, gobierna hacia dónde se mueven las tasas en los escenarios. Para descontar, en cambio, se usa un nivel de 10.91%, elegido para que la curva del modelo reproduzca el 9.16% que el Bono M a 10 años rendía el 21 de septiembre. La diferencia entre ambos no es un error: es la prima que el mercado paga por cargar riesgo de tasa, y es lo que hace que la mediana del precio del Bono M suba en la simulación en vez de quedarse plana.

### 3. La trampa del R²

La regresión de la sección anterior tiene un $R^2$ de 0.977. Suena a un modelo excelente, y no lo es. La tasa de interés se mueve poco de un mes al siguiente, así que predecir la tasa del mes que viene con la de este mes acierta casi siempre por una razón que no tiene nada que ver con el modelo: la variable explicativa ya es, prácticamente, la variable que se quiere explicar.

La forma de ver cuánto explica de verdad es escribir la misma regresión en cambios, $r_{t+1}-r_t$, en vez de en niveles. Las tres especificaciones, estimadas sobre la misma muestra de 226 meses para que los números sean comparables:

| Especificación                             | $R^2$ en niveles | $R^2$ en cambios |
| ------------------------------------------ | ---------------- | ---------------- |
| Solo la tasa de hoy                        | 0.9755           | 0.0065           |
| Más la pendiente de la curva               | 0.9760           | 0.0217           |
| Más depreciación del peso y tasa de EE.UU. | 0.9774           | 0.0673           |

En niveles las tres parecen iguales y magníficas. En cambios se ve el modelo real: el mejor explica menos del 7% de la variación mensual de las tasas, y el más simple explica menos del 1%. Es la misma información escrita de dos maneras, y solo una de las dos es honesta.

> **La regla que queda.** Un $R^2$ alto sobre una serie muy persistente no dice nada. Antes de celebrarlo, hay que preguntarse cuánto de ese ajuste lo produce la inercia de la serie y cuánto el modelo.

### 4. Variables explicativas

El nivel de largo plazo de la sección 2 es una constante, y eso es difícil de defender: hacia dónde revierten las tasas depende de la inflación, de lo que hace la Reserva Federal y de qué tan presionado esté el peso. Abrirlo es extender la misma regresión con más regresores,

$$r_{t+1} = a + b\,r_t + \gamma' x_t + \varepsilon_{t+1}$$

- **$x_t$**: vector con las variables explicativas del mes $t$ (pendiente de la curva, depreciación del peso, tasa de EE.UU., inflación).
- **$\gamma$**: vector de coeficientes, uno por cada variable de $x_t$. La comilla en $\gamma'$ indica que se transpone para multiplicar vector por vector y dar un número: es la suma de cada variable por su coeficiente.
- **$a$, $b$, $r_t$, $\varepsilon_{t+1}$**: los mismos de la sección 1.

El modelo sigue siendo Vasicek, pero ahora el nivel hacia el que revierte se mueve con la macro: $r_{lp,t} = (a + \gamma'x_t)/(1-b)$. Leído así, los coeficientes describen la función de reacción de Banxico, en el espíritu de una regla de Taylor: cuánto sube la tasa cuando sube la inflación.

Con la pendiente de la curva, la depreciación anual del peso y el bono de EE.UU. a 10 años, sobre 226 meses:

| Regresor                 | Coeficiente | $t$   |
| ------------------------ | ----------- | ----- |
| Constante                | -0.1788     | -1.03 |
| Tasa corta               | +1.0375     | 34.44 |
| Pendiente de la curva    | +0.0877     | 2.19  |
| Depreciación del peso    | -0.0069     | -1.98 |
| Bono de EE.UU. a 10 años | -0.0454     | -1.33 |

La pendiente y la depreciación salen significativas. La tasa de EE.UU. no, lo cual sorprende y es un buen punto de discusión: probablemente su efecto ya viene incorporado en la pendiente y en el tipo de cambio.

Con la inflación, que en FRED solo llega hasta julio de 2024, sobre 213 meses el coeficiente es +0.0666 con $t$ de 2.32. Más inflación este mes, tasa más alta el que viene, que es lo que una regla de Taylor predice.

> **Una trampa que cuesta caro.** El coeficiente de la tasa corta en esa tabla es 1.0375, mayor que 1. Leído directamente daría $\kappa$ negativa, es decir, un proceso explosivo en el que las tasas se alejan de su nivel para siempre. No es lo que dicen los datos: es un artefacto de cómo se construyó la pendiente, que es la tasa larga menos la corta y por lo tanto ya contiene la tasa corta con signo negativo. Reagrupando,
>
> $$a + b\,r_t + c(r_{larga,t} - r_t) = a + (b-c)\,r_t + c\,r_{larga,t}$$
>
> el coeficiente que de verdad gobierna la reversión es $b - c = 1.0375 - 0.0877 = 0.9498$, que da $\kappa = 0.618$ y vida media de 1.12 años. Condicionada a la tasa larga, la tasa corta revierte casi tres veces más rápido. La función `kappa_efectiva` hace esta suma automáticamente, y hay una prueba que la fija, porque es el tipo de error que no avisa: produce un número perfectamente plausible y completamente equivocado.

### 5. ¿Predice?

Todo lo anterior es ajuste dentro de muestra, que es donde cualquier modelo se ve bien. La prueba de verdad es pronosticar datos que el modelo no vio.

El procedimiento es de ventana expansiva: para cada mes se reestima el modelo usando solo la información disponible hasta entonces, se pronostica la tasa $h$ meses adelante y se compara con la que realmente ocurrió. El punto de comparación es la **caminata aleatoria**, que pronostica que la tasa dentro de $h$ meses será la de hoy. La **U de Theil** es el cociente entre el error cuadrático medio del modelo y el de la caminata aleatoria: por debajo de 1, el modelo gana; por arriba, pierde.

| Horizonte | AR(1) / Vasicek | ARDL con macro |
| --------- | --------------- | -------------- |
| 1 mes     | 1.02            | 1.09           |
| 6 meses   | 1.00            | 1.05           |
| 12 meses  | 0.91            | 0.97           |
| 24 meses  | 0.80            | 0.88           |

Dos resultados, y ninguno es el que se esperaría después de ver los coeficientes significativos de la sección 4.

**A corto plazo, la caminata aleatoria no se deja vencer.** A uno y a seis meses, los dos modelos pierden contra la regla más tonta posible, la de suponer que nada va a cambiar. La reversión a la media solo empieza a pagar a doce meses, y a veinticuatro ya recorta el error una quinta parte. Tiene sentido: en un mes la tasa casi no se mueve, así que adivinar que se queda igual es muy difícil de mejorar; en dos años, saber que tiende a volver a 6% sí aporta.

**Las variables explicativas empeoran el pronóstico.** El modelo con macro ajusta diez veces mejor dentro de muestra que el AR(1) simple (0.067 contra 0.0065 de $R^2$ en cambios), y sin embargo pierde contra él en los cuatro horizontes. Es sobreajuste: los coeficientes están capturando relaciones que valieron en el pasado de esta muestra y no se sostienen adelante. Cada regresor que se agrega hay que estimarlo, y el ruido de esa estimación se paga en el pronóstico.

> **La regla que queda.** Significativo no es lo mismo que útil. Un coeficiente con $t$ de 2.19 puede ser real y aun así hacer peor el pronóstico. La única forma de saberlo es probar fuera de muestra, y hay que estar dispuesto a reportar que el modelo perdió.

### 6. Lo que los datos no pueden decidir

Queda una pregunta incómoda. El modelo se cambió de caminata aleatoria a Vasicek por un argumento teórico: las tasas no vagan sin rumbo, se mueven alrededor de un nivel ligado a la inflación y a la política monetaria. ¿Confirman los datos ese argumento?

La prueba que responde es la de **raíz unitaria** (prueba de Dickey-Fuller aumentada), que contrasta si una serie revierte a un nivel o si vaga sin rumbo. Sobre estos datos, el estadístico es -2.283 con un valor p de 0.177. Con 301 observaciones mensuales, veinticinco años de historia, **no se puede rechazar que la tasa siga una caminata aleatoria**.

Esto no invalida el cambio de modelo, y conviene entender por qué. Una prueba que no rechaza no demuestra que la hipótesis sea cierta, solo que los datos no alcanzan para descartarla; y distinguir una reversión lenta (vida media de 3.2 años) de una ausencia total de reversión requiere muchas más observaciones de las que hay. La decisión se sostiene por otros lados: la teoría económica, el hecho de que la reversión sí mejora el pronóstico a 12 y 24 meses, y que una caminata aleatoria implica que la tasa puede llegar a cualquier valor, lo cual ninguna economía con banco central permite.

Lo honesto es decir las dos cosas a la vez: el modelo con reversión es el más defendible, y los datos por sí solos no lo habrían escogido.

### 7. Dónde queda este modelo en el mapa

Vasicek es el más simple de una familia grande, y conviene saber qué le falta antes de usarlo para algo más serio que una comparación de dispersión. Brigo y Mercurio recorren esa familia completa; lo que sigue es el mapa mínimo para ubicarse.

**Lo que este modelo no hace.**

- **Un solo factor.** Toda la curva se mueve a partir de la tasa corta, así que solo puede producir una forma de curva, fijada por $\kappa$. El apéndice de la nota muestra el costo: anclado al plazo de 10 años, el modelo se queda hasta 63 puntos base corto en los demás plazos. Brigo y Mercurio son explícitos en que este supuesto es peligroso justamente cuando lo que se valúa depende de cómo se mueven unos plazos respecto a otros.
- **No reproduce la curva de hoy.** Los tres parámetros no alcanzan para pasar por todos los puntos observados, y por eso hubo que elegir a cuál anclarse.
- **Permite tasas negativas.** Como la perturbación es normal y no depende del nivel, nada impide que $R_k$ baje de cero. Con tasas mexicanas alrededor de 7% es irrelevante, pero no lo sería en otros mercados.

**Qué corrige cada extensión.**

| Modelo                      | Qué cambia respecto a Vasicek                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Cox, Ingersoll y Ross (CIR) | La volatilidad se vuelve proporcional a $\sqrt{R}$, así que la tasa no puede cruzar cero                        |
| Hull y White                | El nivel de largo plazo pasa a ser una función del tiempo, ajustada para reproducir la curva observada completa |
| De dos factores (G2++)      | Un segundo factor permite que la curva cambie de pendiente, no solo de nivel                                    |
| Heath, Jarrow y Morton      | Modela la curva forward entera en vez de la tasa corta                                                          |
| Modelos de mercado (LMM)    | Modela directamente las tasas que el mercado cotiza, en vez de una tasa corta que nadie observa                 |

**Un puente que este laboratorio ya cruzó sin nombrarlo.** La sección 2 usa dos niveles de largo plazo, el estimado con historia y el que ancla la curva al precio de mercado. Esa separación tiene nombre propio en la literatura: lo que conecta el mundo objetivo, donde las tasas se observan y se estiman con econometría, con el mundo neutral al riesgo, donde se forman los precios, es el **precio de mercado del riesgo** (market price of risk). Brigo y Mercurio señalan que elegir una forma para ese precio es lo que permite aplicar las dos cosas al mismo modelo, técnicas econométricas por un lado y calibración a precios de mercado por el otro, que es exactamente lo que se hizo aquí: mínimos cuadrados para $\kappa$ y $\sigma$, calibración al 9.16% observado para el nivel de descuento.

### 8. Ejercicios

1. **Cambiar la serie.** Repetir la calibración de la sección 2 con la TIIE a 28 días en vez de la interbancaria a 3 meses. ¿Cambian $\kappa$ y el nivel de largo plazo? ¿Cuál de las dos series se parece más a la tasa que Banxico controla directamente?
2. **Cambiar la muestra.** Estimar con datos desde 1997 en vez de 2001 y comparar los tres parámetros. ¿Cuánto sube $\sigma$? Justificar cuál de las dos muestras usarías para valuar un bono hoy.
3. **Partir la muestra.** Estimar por separado antes y después de 2020 y comparar. ¿Hay evidencia de que el régimen cambió?
4. **Agregar una explicativa propia.** Elegir una variable que en teoría debería predecir las tasas mexicanas, agregarla a la regresión de la sección 4 y evaluarla fuera de muestra con el procedimiento de la sección 5. La pregunta a responder no es si el coeficiente es significativo, sino si baja la U de Theil.
5. **Recalcular la trampa.** Sustituir la pendiente por la tasa larga directamente, de modo que ningún regresor contenga a la tasa corta. Verificar que el coeficiente de la tasa corta ahora sí queda por debajo de 1 y que da la misma $\kappa$ efectiva que la corrección de la sección 4.
6. **El contraste de la hipótesis de expectativas.** El apéndice de [`2_rendimiento_y_curva_de_rendimientos.md`](../../notas_unidades/unidad2/2_rendimiento_y_curva_de_rendimientos.md) deja abierta la pregunta de si la tasa forward es un pronóstico de la tasa futura o solo el precio de amarrarla hoy. Contrastarla con datos: regresar el cambio de la tasa corta en los próximos 12 meses contra la pendiente actual de la curva. Bajo la hipótesis de expectativas el coeficiente debería ser cercano a 1. Estimarlo y discutir qué implica el valor que sale.
7. **Cambiar el supuesto que no se estimó.** La volatilidad del margen de crédito del certificado (0.3 pp) es el único supuesto de la simulación que no viene de datos. Correr la simulación con 0.1 y con 1.0 y ver cuánto cambia la conclusión de que el certificado se mantiene cerca de la par.

---

## Cómo reproducir todo

Desde la raíz del repositorio:

```sh
python notas_unidades/unidad2/codigo/datos_fred.py       # descarga y guarda las series
python notas_unidades/unidad2/codigo/calibracion.py      # imprime todas las tablas de aquí
python -m pytest notas_unidades/unidad2/codigo -q        # pruebas de las fórmulas y del modelo
python notas_unidades/unidad2/img/generar_figuras.py     # regenera las figuras
```

Todo corre con semilla fija, así que dos corridas dan resultados idénticos. La descarga de FRED solo hace falta la primera vez: después, los scripts leen el CSV guardado.

---

## Fuentes y referencias recomendadas

- Vasicek, O. (1977). An equilibrium characterization of the term structure. *Journal of Financial Economics*, 5(2), 177-188: el modelo que se calibra en este laboratorio.
- Brigo, D. y Mercurio, F. (2006). *Interest Rate Models: Theory and Practice. With Smile, Inflation and Credit* (2ª ed.). Springer: la referencia estándar del tema. De ahí sale el mapa de la sección 7, la limitación de los modelos de un solo factor y el papel del precio de mercado del riesgo como puente entre la estimación con datos y la calibración a precios.
- Duffee, G. R. (2002). Term premia and interest rate forecasts in affine models. *The Journal of Finance*, 57(1), 405-443: el resultado de que los modelos de estructura temporal tienen dificultades para vencer a la caminata aleatoria fuera de muestra.
- Diebold, F. X. y Li, C. (2006). Forecasting the term structure of government bond yields. *Journal of Econometrics*, 130(2), 337-364: cómo convertir los tres parámetros de Nelson-Siegel en series de tiempo para pronosticar la curva completa, el paso siguiente natural a este laboratorio.
- Campbell, J. Y. y Shiller, R. J. (1991). Yield spreads and interest rate movements: a bird's eye view. *The Review of Economic Studies*, 58(3), 495-514: el contraste de la hipótesis de expectativas del ejercicio 6.
- Federal Reserve Bank of St. Louis (FRED): series mensuales consultadas el 21 de septiembre de 2026. Las series mexicanas son el espejo que publica la OCDE, no la fuente primaria; Banxico es la autoridad, y comprobar estos números contra su Sistema de Información Económica es parte del ejercicio 1.
