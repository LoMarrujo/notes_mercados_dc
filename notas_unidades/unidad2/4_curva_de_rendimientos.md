# Unidad 2 · Curva de Rendimientos

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante construya la curva de rendimientos cupón cero mediante bootstrapping a partir de Cetes y Bonos M, y la estime con el modelo paramétrico de Nelson-Siegel.

## Contenido

|     | Tema                                          | Qué cubre                                                                                   |
| --- | --------------------------------------------- | ------------------------------------------------------------------------------------------- |
| I   | La curva observada, y su error clásico        | Graficar rendimiento contra plazo, y por qué eso no es todavía una curva cupón cero         |
| II  | La curva se mueve                             | El mismo gráfico en varias fechas: nivel, pendiente y curvatura a simple vista              |
| III | Bootstrapping y tasas forward                 | Despejar la curva spot con Cetes y Bonos M, y extraer de ahí la tasa forward implícita      |
| IV  | Ajuste paramétrico: Nelson-Siegel             | Estimar la curva completa con tres parámetros que resumen nivel, pendiente y curvatura      |
| V   | Extra: la curva real y la inflación implícita | La misma curva con UDIBONOS, y la diferencia nominal menos real como pronóstico del mercado |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. La curva observada, y su error clásico

[`2_valuacion_instrumentos_deuda.md`](2_valuacion_instrumentos_deuda.md#1-valuación-a-descuento) calculó el precio de un CETE a 28 días con su propia tasa, y el de un Bono M a 10 años con la suya, como si fueran dos problemas sueltos. No lo son: graficar el rendimiento cotizado de cada instrumento contra su plazo (Cetes a 28, 91, 182 y 364 días; Bono M a 3, 5, 10, 20 y 30 años, todos el mismo día) traza una sola curva ascendente, del 6.49% en el extremo más corto a más de 9% en el más largo.

Esa curva, sin embargo, todavía no es la curva que hace falta para descontar cualquier flujo futuro con precisión. Es una **curva de rendimiento al vencimiento (YTM)**: cada punto es la tasa interna de retorno de un instrumento completo, no la tasa que le corresponde a un solo peso pagadero en una fecha exacta. Para el CETE (cupón cero) las dos cosas coinciden, porque solo hay un flujo. Para el Bono M no: su rendimiento a 10 años ya mezcla el descuento de los cupones que paga antes del año 10 (a las tasas, más bajas, de esos plazos intermedios) con el descuento del pago final. Dos bonos del mismo plazo pero con cupón distinto pueden cotizar una YTM ligeramente distinta aunque el mercado esté valuando el mismo dinero en el mismo momento de la misma forma; a esa distorsión se le llama **efecto cupón**, y es la razón por la que una curva de YTM y una curva cupón cero (o **curva spot**) no son la misma curva, aunque a menudo se confundan.

> **Ejemplo resuelto.** El 3 de septiembre de 2026, la curva de rendimiento observada fue aproximadamente: CETE 28 días, 6.49%; CETE 91 días, 6.65%; CETE 182 días, 6.85%; CETE 364 días, 7.00%; Bono M 3 años, 7.80%; Bono M 5 años, 8.20%; Bono M 10 años, 9.00%; Bono M 20 años, 9.40%; Bono M 30 años, 9.55%. Graficada, sube con el plazo (pendiente positiva) y se aplana en el tramo largo. Los cuatro puntos de Cetes sí son puntos de la curva spot, porque un CETE no paga cupón; los cinco puntos de Bono M son YTM, contaminados por el efecto cupón de cada bono.

### 2. La curva se mueve

La misma gráfica repetida para cinco o seis fechas distintas (por ejemplo, un corte mensual durante 2026) deja ver, a simple vista y sin nombrarlos todavía, los tres movimientos que puede sufrir la curva completa:

- **Nivel:** la curva entera sube o baja de forma más o menos pareja en todos los plazos, típicamente cuando Banxico mueve su tasa de referencia o cambian las expectativas de inflación de largo plazo.
- **Pendiente:** la diferencia entre el extremo largo y el corto se abre o se cierra; una curva más empinada suele reflejar más incertidumbre o más expectativa de alza futura en el corto plazo.
- **Curvatura:** el tramo intermedio (2 a 5 años, aproximadamente) se aparta hacia arriba o hacia abajo de la línea recta que unen el corto y el largo plazo.

Estos tres movimientos son la observación que la sección 4 va a resumir en tres números.

### 3. Bootstrapping y tasas forward

**Por qué los Cetes regalan la curva spot hasta un año.** Un CETE no paga cupón: su tasa de rendimiento cotizada, convertida de la convención día/360 de [`2_valuacion_instrumentos_deuda.md`](2_valuacion_instrumentos_deuda.md#1-valuación-a-descuento) a una tasa efectiva anual (el mismo tipo de conversión de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md)), es exactamente la tasa spot $r_t$ de ese plazo: no hay ningún cupón intermedio que mezclarle. Con los cuatro Cetes (28, 91, 182 y 364 días) ya se tienen cuatro puntos de la curva spot sin resolver ninguna ecuación.

**Por qué el Bono M no regala nada, hay que despejarlo.** Un Bono M sí paga cupón, así que su precio observado $v_0$ es la suma de cada cupón descontado a la tasa spot de *su propio* plazo, más el principal descontado a la tasa spot del plazo final:

$$v_0 = \sum_{i=1}^{N-1} c(1+r_{t_i})^{-t_i} + (c+v_N)(1+r_{t_N})^{-t_N}$$

¿De dónde sale la fórmula? Es la misma suma de valor presente de un flujo único de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md#6-valor-futuro-y-valor-presente-de-un-flujo-único) aplicada cupón por cupón, con una sola diferencia frente a la fórmula de precio de [`2_valuacion_instrumentos_deuda.md`](2_valuacion_instrumentos_deuda.md#2-valuación-con-cupón-fijo): ahí se usaba una sola tasa $r$ para descontar todos los flujos; aquí cada flujo se descuenta con la tasa spot que le corresponde a su propio plazo $t_i$, porque es justamente esa curva la que todavía no se conoce.

De esa ecuación, todas las tasas spot $r_{t_i}$ con $t_i < t_N$ ya se conocen (son plazos más cortos, ya bootstrapeados con un Bono M o un CETE anterior); la única incógnita es $r_{t_N}$, la tasa spot del plazo más largo que se está agregando. Se despeja de forma recursiva: primero el Bono M más corto (usando solo tasas Cete ya conocidas), luego el siguiente (usando las tasas Cete y la spot recién despejada), y así hasta el plazo más largo disponible. Este método, de resolver la curva un plazo a la vez a partir de instrumentos cada vez más largos, se llama **bootstrapping**.

Con la curva spot completa, se puede despejar la **tasa forward**: la tasa que el mercado ya trae implícita hoy para un periodo futuro. Entre los plazos $t_1$ y $t_2$ ($t_1<t_2$):

$$(1+r_{t_2})^{t_2} = (1+r_{t_1})^{t_1}(1+f_{t_1,t_2})^{t_2-t_1}$$

¿De dónde sale la fórmula? Invertir \$1 hoy a la tasa spot $r_{t_2}$ durante $t_2$ años debe dar el mismo resultado que invertirlo a $r_{t_1}$ durante $t_1$ años y luego reinvertir lo obtenido durante el periodo restante $(t_2-t_1)$ a la tasa $f_{t_1,t_2}$ que se amarra hoy para ese futuro; si no fuera así, habría una forma de ganar dinero sin riesgo solo cambiando de estrategia, algo que el propio mercado corrige de inmediato.

> **La pregunta que más rinde.** ¿La tasa forward es un pronóstico del mercado sobre la tasa que va a haber en ese periodo futuro, o es simplemente el precio al que hoy se puede amarrar una tasa para entonces, sin decir nada sobre qué va a pasar? Las dos lecturas conviven: la fórmula solo garantiza que $f_{t_1,t_2}$ es el precio de no-arbitraje de amarrar hoy esa tasa futura; que además sea un buen pronóstico depende de si el mercado, en promedio, acierta al anticipar hacia dónde se mueven las tasas, algo que no se puede resolver solo con álgebra.

### 4. Ajuste paramétrico: Nelson-Siegel

La curva spot bootstrapeada trae un punto por instrumento disponible, con huecos entre plazos (por ejemplo, nada entre 1 y 3 años si no hay un Bono M ahí) y algo de ruido propio de cada subasta. El modelo de **Nelson-Siegel** ajusta una curva continua y suave sobre esos puntos:

$$\hat{r}(t) = \beta_0 + \beta_1\left(\dfrac{1-e^{-t/\tau}}{t/\tau}\right) + \beta_2\left(\dfrac{1-e^{-t/\tau}}{t/\tau}-e^{-t/\tau}\right) \qquad (t>0,\ \tau>0)$$

¿De dónde sale la fórmula? No se deriva de una fórmula anterior de esta unidad, es una forma funcional propuesta directamente por Nelson y Siegel para que tres parámetros solamente ($\beta_0$, $\beta_1$, $\beta_2$) reproduzcan las formas de curva más comunes en la práctica; lo que sí se deriva es su interpretación, a partir de lo ya visto a simple vista en la sección 2: cuando $t\to\infty$, $\hat{r}(t)\to\beta_0$ (el **nivel** de largo plazo); cuando $t\to0$, $\hat{r}(t)\to\beta_0+\beta_1$ (el nivel de corto plazo, así que $\beta_1$ es la **pendiente**, la diferencia corto menos largo); y el término que multiplica a $\beta_2$ crece y luego decae con $t$, la forma de joroba que produce la **curvatura** del tramo intermedio.

$\tau$ fija a qué plazo ocurre esa joroba y normalmente se fija primero por prueba (o con un valor típico del mercado que se estudia), dejando a $\beta_0$, $\beta_1$ y $\beta_2$ como los únicos parámetros libres. Se ajustan minimizando la suma de errores de valuación al cuadrado entre el precio observado de cada instrumento y el precio que resultaría de descontar sus flujos con $\hat{r}(t)$, un problema de optimización numérica (con Solver en la hoja de cálculo, el mismo tipo de herramienta que ya resolvió la TIR de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md)) en vez de una fórmula cerrada.

> No es un ejercicio de salón: los bancos centrales, incluido Banxico, publican su curva cupón cero ajustada con esta familia de modelos o con su extensión de cuatro parámetros (Svensson, que agrega una segunda joroba), precisamente porque tres o cuatro números bastan para resumir y comparar la forma completa de la curva de un día a otro.

### 5. Extra: la curva real y la inflación implícita

Los pasos 1 a 4 de esta nota se repiten, sin cambiar ninguna fórmula, con UDIBONOS en vez de Bono M: el resultado es una curva spot **real**, no nominal, porque el UDIBONO ya paga en unidades que se ajustan con la inflación (ver [`1_instrumentos_deuda.md`](1_instrumentos_deuda.md#1-instrumentos-gubernamentales-cetes-bono-m-y-udibono)).

Con las dos curvas (nominal, de Cetes y Bono M; real, de UDIBONOS) al mismo plazo, la diferencia entre ambas es la **inflación implícita** (o *breakeven inflation*) que el mercado está poniendo con dinero de verdad a ese horizonte:

$$\hat{r}_{inf} \approx r_{nom} - r_{real}$$

¿De dónde sale la fórmula? Es la misma ecuación de Fisher usada en [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md), aplicada punto por punto a lo largo de la curva en vez de a una sola tasa: si la tasa nominal es, aproximadamente, la tasa real más la inflación esperada, despejar la inflación esperada dado ambos rendimientos de mercado es una resta.

> **Por qué engancha.** Esta $\hat{r}_{inf}$ no sale de una encuesta ni de una opinión, sale de lo que miles de inversionistas pagaron hoy por protegerse o no de la inflación futura. Comparar esta curva de inflación implícita, plazo por plazo, contra la Encuesta de Expectativas de Banxico (que sí es una encuesta de opinión a especialistas) y explicar la brecha entre ambas es, con datos reales, la pregunta que cierra el laboratorio.

---

## Fuentes y referencias recomendadas

- Fabozzi, F. J., & Fabozzi, F. A. (2021). *Bond Markets, Analysis, and Strategies* (10ª ed.). MIT Press. Capítulos sobre la estructura de plazos de las tasas de interés: curva de rendimiento a vencimiento frente a curva spot, efecto cupón, bootstrapping y tasas forward.
- Nelson, C. R., & Siegel, A. F. (1987). *Parsimonious Modeling of Yield Curves*. Journal of Business, 60(4), 473-489: la forma funcional de tres parámetros y su interpretación como nivel, pendiente y curvatura.
- Banco de México: metodología de estimación de la curva de rendimientos cupón cero (familia Nelson-Siegel/Svensson) y Sistema de Información Económica (SIE) para series históricas de Cetes, Bonos M y UDIBONOS; Encuesta de Expectativas de los Especialistas en Economía del Sector Privado, para el pronóstico de inflación con el que se compara la inflación implícita de la curva.
- Luenberger, D. G. (1998). *Investment Science*. Oxford University Press. Capítulo sobre la estructura de tasas de interés: tasas spot y forward, y la relación de no arbitraje entre ambas.

---

## Cierre de la unidad — Lo esencial para recordar

- Graficar rendimiento contra plazo con Cetes y Bono M da una **curva de YTM**, no todavía una **curva spot (cupón cero)**: el efecto cupón contamina cada punto de Bono M, aunque los puntos de Cetes (sin cupón) sí son spot desde el inicio.
- A simple vista, la curva completa se mueve de tres formas: **nivel** (sube o baja pareja), **pendiente** (se abre o cierra entre corto y largo plazo) y **curvatura** (el tramo intermedio se aparta de la línea recta entre los extremos).
- El **bootstrapping** despeja la curva spot un plazo a la vez: los Cetes la regalan hasta un año, cada Bono M agrega una tasa spot nueva usando las ya conocidas. Con la curva spot completa se despeja la **tasa forward**, el precio de amarrar hoy una tasa futura, que puede o no ser también un buen pronóstico.
- **Nelson-Siegel** ajusta la curva completa con tres parámetros ($\beta_0$, $\beta_1$, $\beta_2$) que son, literalmente, el nivel, la pendiente y la curvatura ya vistos a simple vista; se estima minimizando errores de valuación al cuadrado, y es la misma familia que usan los bancos centrales, incluido Banxico.
- La misma curva construida con UDIBONOS da la curva **real**; la diferencia contra la curva **nominal** es la **inflación implícita** que el mercado está pagando por protegerse, comparable contra la encuesta de expectativas de Banxico.

**Próxima sesión:** los riesgos a los que queda expuesto quien compra un instrumento de deuda, y por qué la duración (una idea que ya rondó esta nota, al ver cómo se mueve la curva) es la forma de medir uno de ellos.
