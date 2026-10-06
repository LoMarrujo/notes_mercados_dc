# Unidad 2 · Riesgos del Mercado de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

> **Lectura complementaria, no evaluada.** Por calendario, este tema sale del examen de la unidad; se conserva como consulta.

## Objetivo de la unidad

Que el estudiante distinga el tipo de riesgo (tasa de interés, crédito, inflación, liquidez) al que está expuesto un instrumento de deuda dado.

## Contenido

|     | Tema                                              | Qué cubre                                                                                   |
| --- | ------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| I   | Qué puede salir mal al comprar deuda              | De dónde sale el rendimiento de un bono, qué parte de él ataca cada riesgo y cómo se reduce |
| II  | Riesgo de tasa de interés                         | Por qué el precio de un bono se mueve en sentido contrario a la tasa de mercado             |
| III | Riesgo de crédito y calificaciones                | Escala de calificaciones, probabilidad de incumplimiento de cada una y tasa de recuperación |
| IV  | Riesgo de inflación                               | Por qué un cupón fijo pierde poder adquisitivo, y cómo el UDIBONO lo evita                  |
| V   | Riesgo de liquidez                                | Qué tan rápido y a qué precio se puede vender un instrumento antes de su vencimiento        |
| VI  | Los seis instrumentos frente a los cuatro riesgos | Matriz de qué riesgo domina en cada instrumento de esta unidad                              |

---

### 1. Qué puede salir mal al comprar deuda

Hasta aquí, comprar un instrumento de deuda se trató como un problema resuelto en cuanto se calculaba su precio. Pero el precio se calcula con lo que se espera hoy, y comprarlo no cierra el trato: entre la compra y el vencimiento puede pasar algo que cambie lo que el instrumento vale, o lo que se esperaba cobrar. [`2_rendimiento_y_curva_de_rendimientos.md`](2_rendimiento_y_curva_de_rendimientos.md#2-qué-mide-y-qué-no-mide-el-rendimiento) ya lo advirtió: el YTM solo se gana si el bono se conserva hasta el vencimiento y los cupones se reinvierten a esa misma tasa.

**Definición:** el riesgo de un instrumento de deuda es la posibilidad de que el rendimiento que obtiene su tenedor, entre la compra y la venta (o el vencimiento), sea distinto del que esperaba al comprarlo, por causas que el tenedor no controla.

Quien compra a precio $a$, cobra un cupón $c$ y vende en $v_1$ un periodo después obtiene $r_h=(c+v_1-a)/a$, el rendimiento a horizonte que [`4_estrategias_renta_fija.md`](4_estrategias_renta_fija.md#2-elegir-el-plazo-según-el-escenario-de-tasas) usa para elegir plazo. Su numerador separa las dos partes en las que puede fallar ese rendimiento: los **flujos** que se cobran (cupones y valor nominal, más lo que rinda reinvertir los cupones) y el **precio** al que se vende el instrumento si se vende antes del vencimiento. Cada riesgo de esta nota ataca una de esas partes, o el poder de compra de ambas, y cada uno tiene su forma de reducirlo:

| Riesgo          | Qué cambia después de comprar                | Origen                     | Qué parte del rendimiento afecta                                  | Cómo se mitiga                                            |
| --------------- | -------------------------------------------- | -------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------- |
| Tasa de interés | La tasa de mercado                           | La economía en su conjunto | El precio de venta, y la tasa a la que se reinvierten los cupones | Calzar el plazo con la fecha en que se necesita el dinero |
| Crédito         | La capacidad de pago del emisor              | El emisor y la emisión     | Los flujos: el cupón o el valor nominal pueden no pagarse         | Calificación, garantías y diversificación entre emisores  |
| Inflación       | El nivel general de precios                  | La economía en su conjunto | El poder de compra de los flujos y del precio                     | UDIBONO, o plazo corto o cupón variable                   |
| Liquidez        | Cuántos compradores hay dispuestos a comprar | El emisor y la emisión     | El precio de venta: vender rápido obliga a aceptar un descuento   | Emisiones gubernamentales o grandes de oferta pública     |

Los de tasa de interés e inflación golpean a la vez a todos los instrumentos de cupón fijo, sin importar quién los emitió. Los de crédito y liquidez, en cambio, explican por qué dos bonos del mismo plazo no rinden lo mismo: la sobretasa del bono corporativo sobre el Bono M en la sección 4 de [`2_rendimiento_y_curva_de_rendimientos.md`](2_rendimiento_y_curva_de_rendimientos.md#4-la-curva-de-rendimientos-ubicar-un-bono) es lo que el mercado cobra por esos dos riesgos. A esa diferencia entre bonos del mismo plazo se le llama **estructura de riesgo de las tasas de interés** (risk structure of interest rates), en contraste con la estructura temporal que describe la curva de rendimientos.

Las fuentes de renta fija enumeran más riesgos que estos cuatro:

- **Amortización anticipada (call risk):** el emisor puede recomprar el bono antes del vencimiento.
- **Tipo de cambio:** afecta a quien mide su rendimiento en otra moneda, como un fondo extranjero que compra Bonos M.
- **Eventos o cambios legales:** alteran de golpe la capacidad de pago de un emisor.

Esta nota se concentra en los cuatro que aplican a los seis instrumentos de la unidad vistos por un inversionista en pesos. Para cada uno, las preguntas son las mismas: ¿qué puede salir mal, en qué instrumentos pesa más y quién absorbe la pérdida?

### 2. Riesgo de tasa de interés

El primero es también el más importante para quien puede necesitar vender antes del vencimiento.

**Definición:** riesgo de tasa de interés es la posibilidad de que la tasa de mercado cambie después de comprar un instrumento de deuda, y que ese cambio mueva su precio en sentido contrario.

La sección 3 de [`2_rendimiento_y_curva_de_rendimientos.md`](2_rendimiento_y_curva_de_rendimientos.md#3-relación-entre-rendimiento-y-precio) ya mostró el mecanismo: el cupón de un bono emitido es fijo, así que si el rendimiento que exige el mercado sube, su precio baja hasta que, comprado a ese precio menor, rinda lo mismo que los bonos nuevos. También mostró que el efecto crece con el plazo: de 8% a 9%, el precio de un bono con cupón de 8% cae 2.53% a 3 años, 6.42% a 10 años y 10.27% a 30 años, mientras que un CETE a 28 días apenas se mueve. Quien necesita vender antes del vencimiento queda expuesto a ese movimiento; quien conserva el bono hasta el vencimiento no realiza la pérdida o ganancia de precio, pero enfrenta el riesgo simétrico de **reinversión**: si las tasas bajan, los cupones que cobra en el camino se reinvierten a una tasa menor a la que esperaba.

> **Con datos reales.** El Bono M hipotético de la figura de la sección 1 de la nota de rendimiento, emitido a la par en septiembre de 2020 con cupón de 5.68%, valdría cerca de \$88.77 en septiembre de 2026 descontado al 9.16% que exigía el mercado (una comparación ilustrativa): el alza de tasas le quitó unos \$11 por cada \$100. Esa alza no fue pequeña. En su episodio de alzas de 2021-2023, la tasa interbancaria mexicana a 3 meses subió 7.2 puntos porcentuales (de 4.3% a 11.5%), un 40% más que la tasa de fondos federales de EE.UU. en el suyo (+5.1 pp, 2022-2024). El recorte que siguió fue más desigual: 4.6 pp en México desde abril de 2024 contra 1.5 pp en EE.UU., y el diferencial entre las dos tasas cayó a 3.16 pp en agosto de 2026, frente a un promedio de 5.2 pp desde 2001. Los episodios se miden con `codigo/analisis_tasas_mx_eu.py`, que suaviza la serie para no confundir el ruido de un mes con un ciclo; por eso no coinciden exactamente con el mínimo y el máximo de cada serie.

**Cómo se mitiga.** La forma más directa es calzar el plazo con la fecha en que se necesita el dinero, el calce de flujos de la nota de estrategias: quien no tiene que vender antes del vencimiento no realiza la pérdida de precio. Si se espera que las tasas suban, se acorta el plazo o se prefiere un cupón variable (sección 4 de la nota de valuación), que se recalcula con la tasa de mercado y por eso apenas cambia de precio. Sin una opinión sobre las tasas, la escalera reparte el dinero entre plazos, y la inmunización del apéndice de esa misma nota elige el plazo en el que la pérdida de precio y la ganancia por reinversión se compensan. Las instituciones también cubren este riesgo con derivados (swaps de tasa, futuros sobre el Bono M), que quedan fuera de esta unidad.

**Ejemplos:**

- Un inversionista compra un Bono M hipotético a 10 años con cupón fijo de 8%, a \$93.58, con un rendimiento de 9% (la tabla de la sección 3 de [`2_rendimiento_y_curva_de_rendimientos.md`](2_rendimiento_y_curva_de_rendimientos.md#3-relación-entre-rendimiento-y-precio)); si el rendimiento que exige el mercado sube 100 pb, el bono solo se vende si su precio baja hasta igualar ese nuevo rendimiento: \$87.71.
- Un ahorrador reinvierte los cupones semestrales de un Bono M a medida que los cobra; si la tasa de mercado baja de 9% a 6% en el camino, cada cupón que reinvierte gana 6% en vez del 9% original: es el riesgo de reinversión, el lado simétrico del riesgo de tasa de interés.

### 3. Riesgo de crédito y calificaciones

**Definición:** riesgo de crédito (o de incumplimiento) es la posibilidad de que el emisor no pague el cupón o el valor nominal prometido, en parte o por completo.

La Unidad 1 ya presentó a las calificadoras (S&P, Moody's, HR Ratings, Fitch) y su conflicto de interés ([`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md#3-calificadoras-y-riesgo-de-crédito)). Lo que agrega esta sección es la escala misma: cada calificadora ordena a los emisores en una escala de letras (de AAA, la más alta, hasta D, incumplimiento), y esa escala se divide en dos grandes categorías:

- **Grado de inversión (investment grade):** de AAA hasta BBB- (o el equivalente Baa3 en la escala de Moody's). El emisor tiene una capacidad de pago que la calificadora considera sólida.
- **Grado especulativo o "chatarra" (junk):** de BB+ hacia abajo. El emisor tiene una probabilidad de incumplimiento considerablemente mayor, y por eso el mercado le exige una sobretasa (spread) más alta sobre la tasa libre de riesgo para compensar ese riesgo adicional.

Cada letra se divide en tres escalones: Moody's agrega un número (Aa1 > Aa2 > Aa3) y S&P y Fitch un signo (AA+ > AA > AA-). Por eso la frontera del grado de inversión es BBB- o Baa3, el escalón más bajo de su letra. Las calificaciones de los extremos (Aaa o AAA arriba; Ca, CC y C abajo) no se dividen. En México, las calificadoras publican además una **escala nacional** (por ejemplo, mxAAA de S&P o HR AAA de HR Ratings), que ordena a los emisores mexicanos entre sí y no se compara directamente con la escala global.

**Qué tan probable es el incumplimiento en cada calificación.** La calificación no es una opinión suelta: las calificadoras publican con qué frecuencia incumplieron, en el pasado, los emisores de cada letra. La **probabilidad de incumplimiento** (probability of default, PD) acumulada es la proporción de emisores que incumplieron dentro de los primeros $t$ años desde que tenían esa calificación:

| Calificación (Moody's) | Equivalente S&P/Fitch | 1 año  | 5 años | 10 años |
| ---------------------- | --------------------- | ------ | ------ | ------- |
| Aaa                    | AAA                   | 0.00%  | 0.11%  | 0.50%   |
| A                      | A                     | 0.06%  | 0.87%  | 2.48%   |
| Baa                    | BBB                   | 0.18%  | 1.88%  | 4.74%   |
| Ba                     | BB                    | 1.11%  | 10.19% | 19.71%  |
| B                      | B                     | 4.05%  | 24.61% | 41.95%  |
| Caa-C                  | CCC a C               | 16.45% | 50.37% | 69.48%  |

Tasas promedio de incumplimiento acumuladas de Moody's, 1970-2012, según Hull. Bajar un solo escalón, de Baa (el último de grado de inversión) a Ba (el primero especulativo), multiplica por seis la probabilidad de incumplir en un año y por cuatro la de incumplir en diez. Esa diferencia explica el salto de sobretasa que sufre un bono cuando lo rebajan a chatarra.

**Cuánto se pierde si el emisor incumple.** Un incumplimiento no suele significar perderlo todo: los acreedores presentan sus reclamaciones contra los activos de la empresa y recuperan una parte. La **tasa de recuperación** $r_{rec}$ es la fracción del valor nominal que se recupera; en un bono se mide como su precio de mercado unos días después del incumplimiento, como porcentaje del valor nominal. Lo que no se recupera es la **pérdida dado el incumplimiento** (loss given default, LGD):

$$r_{rec} = 1 - LGD \qquad (0 \leq r_{rec} \leq 1)$$

¿De dónde sale la fórmula? Es una identidad: lo que se recupera más lo que se pierde suma el valor nominal completo, $r_{rec}+LGD=1$.

Cuánto se recupera depende sobre todo de las garantías del crédito y de su prelación (si se cobra antes o después que otros acreedores), y baja en las recesiones, cuando muchas empresas incumplen a la vez y venden activos al mismo tiempo. El supuesto habitual para un bono corporativo sin garantía es $r_{rec}=40\%$, es decir, $LGD=60\%$.

> **Aplicación a los instrumentos de esta unidad.** La deuda gubernamental (CETE, Bono M, UDIBONO) se trata como de riesgo de crédito mínimo, el mismo supuesto de la Unidad 1: en pesos, el Gobierno Federal es el emisor de referencia, con la calificación más alta de la escala nacional (mxAAA). Eso no quiere decir que no se califique: en la escala global, que lo compara con otros países, tiene su propia calificación soberana. La deuda corporativa (bono corporativo, papel comercial, certificado bursátil emitido por una empresa) sí carga riesgo de crédito, y ese riesgo es justamente lo que califican S&P, Moody's, HR Ratings o Fitch; la sobretasa que paga por encima de un Bono M o un CETE del mismo plazo es, en buena medida, el precio de ese riesgo.

**Cómo se mitiga.** El riesgo de crédito no se elimina comprando deuda corporativa, pero se reduce de cuatro formas:

- **Elegir por calificación:** comprar solo grado de inversión, o exigir una sobretasa acorde a la probabilidad de incumplimiento de la tabla.
- **Diversificar:** repartir el dinero entre varios emisores y sectores, para que un solo incumplimiento pese poco en el portafolio.
- **Revisar el contrato de emisión:** preferir emisiones con garantía o con cláusulas de protección, como la subordinación de deuda de la sección 6 de la nota de instrumentos, que pone al tenedor antes que otros acreedores y sube la tasa de recuperación.
- **Acortar el plazo:** la probabilidad acumulada de incumplir crece con los años, por eso el papel comercial carga menos riesgo de crédito que un bono del mismo emisor.

**Ejemplos:**

- Un bono corporativo calificado BBB- (el último escalón de grado de inversión) es rebajado a BB+ (el primer escalón de junk) tras un mal reporte financiero del emisor; el mercado le exige una sobretasa mayor y su precio cae de inmediato.
- Una empresa mediana emite papel comercial y, al vencimiento, no logra refinanciarse ni pagar el valor nominal. Si en la liquidación el tenedor recupera \$40 de cada \$100 de valor nominal, $r_{rec}=40\%$ y pierde $LGD=60\%$: el riesgo de crédito materializado.

### 4. Riesgo de inflación

**Definición:** riesgo de inflación (o riesgo de poder adquisitivo) es la posibilidad de que la inflación observada resulte mayor a la que el mercado esperaba al fijar la tasa cupón, de modo que el pago prometido, aunque se cumpla al pie de la letra, compre menos de lo que el inversionista esperaba.

Un instrumento con cupón fijo nominal (Bono M, bono corporativo, papel comercial, CETE) no ajusta ese pago si la inflación sorprende al alza: el monto en pesos es el que es, pero su poder de compra cae con la inflación no anticipada. El UDIBONO, presentado en [`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#6-los-seis-instrumentos), es exactamente el instrumento que este curso usa para evitar ese riesgo: al pactar una tasa real sobre un valor nominal denominado en UDIs (que se ajustan con la inflación observada), el cupón y el capital que recibe el inversionista mantienen su poder de compra sin importar qué tan alta resulte la inflación.

Cuánta inflación espera hoy el mercado se ve en la sección 4 de la nota de rendimiento: el 21 de septiembre de 2026, el UDIBONO a 10 años rendía 4.75% real y el Bono M del mismo plazo 9.16% nominal, una diferencia de unos 4.4 puntos que es, aproximadamente, la inflación esperada a 10 años. El riesgo de inflación es que la observada resulte mayor que esa cifra.

> Este riesgo es más relevante mientras más largo es el plazo del instrumento (más tiempo para que la inflación observada se aleje de la esperada) y mientras más fijo es el cupón en términos nominales; por eso un CETE a 28 días apenas lo enfrenta (muy poco tiempo para que la inflación sorprenda), mientras que un Bono M a 30 años sí queda expuesto de forma relevante.

**Cómo se mitiga.** Hay tres formas, de más a menos directa:

- **Indexar a la inflación:** el UDIBONO cubre el riesgo por diseño.
- **Plazo corto:** un CETE que se renueva cada 28 días se vuelve a comprar a la tasa nueva, que ya incorpora la inflación observada.
- **Cupón variable:** si la inflación sube y Banxico responde subiendo su tasa, el cupón variable sube con ella; cubre la inflación solo en la medida en que la tasa de referencia la siga.

**Ejemplos:**

- Un Bono M con cupón nominal fijo de 8% se compró esperando una inflación de 5%; si la inflación observada resulta 12%, el cupón sigue pagando el mismo monto en pesos, pero compra menos de lo que el inversionista anticipaba.
- Un UDIBONO comprado en el mismo momento, con la misma sorpresa inflacionaria de 12%, no pierde poder de compra: su valor nominal en UDIs se ajusta con la inflación observada, así que el cupón y el capital mantienen su valor real.

### 5. Riesgo de liquidez

**Definición:** riesgo de liquidez es la posibilidad de no poder vender un instrumento rápidamente, o de tener que aceptar un precio desfavorable para lograrlo, antes de su vencimiento.

[`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda) ya explicó que el mercado secundario de deuda es mayoritariamente de mostrador, no un libro de órdenes público como el de una acción; esa estructura por sí sola vuelve a la deuda, en general, menos líquida que una acción de una empresa grande. Dentro del propio mercado de deuda, la liquidez tampoco es uniforme:

- Los instrumentos gubernamentales (CETE, Bono M, UDIBONO) son los más líquidos: se colocan en montos grandes y periódicos, y los Formadores de Mercado ([`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda)) están obligados a cotizar precio de compra y venta de forma continua.
- Una emisión colocada por **oferta pública** suele ser más líquida que una **colocación privada** ([`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda)), porque hay más inversionistas que la conocen y pueden comprarla en el secundario.
- Una emisión corporativa pequeña o poco conocida (un papel comercial de una empresa mediana, un certificado bursátil colocado de forma privada) suele ser la menos líquida de todas: si el tenedor necesita vender antes del vencimiento, puede no encontrar comprador, o solo a un precio con un descuento considerable.

**Cómo se mitiga.** Si existe la posibilidad de necesitar el dinero antes del vencimiento, se prefieren instrumentos gubernamentales o emisiones grandes de oferta pública. Si no, se calza el plazo con la fecha en que se necesita el dinero, como en el riesgo de tasa, para no tener que vender. Un portafolio con instrumentos menos líquidos suele guardar una parte en CETES como colchón: se venden primero si hace falta efectivo, sin malbaratar el resto.

**Ejemplos:**

- El tenedor de un CETE puede venderlo el mismo día a un precio muy cercano al de mercado, porque los Formadores de Mercado cotizan compra y venta de forma continua.
- El tenedor de un certificado bursátil colocado de forma privada por una empresa poco conocida intenta venderlo antes del vencimiento y solo encuentra comprador con un descuento considerable, o no encuentra comprador en absoluto.

### 6. Los seis instrumentos frente a los cuatro riesgos

| Instrumento          | Riesgo de tasa de interés                                              | Riesgo de crédito                     | Riesgo de inflación                      | Riesgo de liquidez                                  |
| -------------------- | ---------------------------------------------------------------------- | ------------------------------------- | ---------------------------------------- | --------------------------------------------------- |
| CETE                 | Bajo (plazo muy corto)                                                 | Prácticamente nulo (soberano)         | Bajo (plazo muy corto)                   | Muy bajo (el más líquido de los seis)               |
| Bono M               | Alto (plazo largo, cupón fijo)                                         | Prácticamente nulo (soberano)         | Alto (cupón nominal fijo a largo plazo)  | Bajo (líquido, benchmark de la curva)               |
| UDIBONO              | Alto en precio, pero cubierto en poder de compra                       | Prácticamente nulo (soberano)         | Cubierto por diseño (cupón real en UDIs) | Medio (menos negociado que el Bono M)               |
| Bono corporativo     | Alto si el plazo es largo                                              | Sí, según su calificación             | Alto si el cupón es fijo                 | Medio, depende del tamaño de la emisión             |
| Papel comercial      | Bajo (plazo corto)                                                     | Sí, aunque acotado por el plazo corto | Bajo (plazo corto)                       | Medio, depende de qué tan conocido es el emisor     |
| Certificado bursátil | Depende del cupón (bajo si es variable, alto si es fijo a largo plazo) | Sí, si lo emite una empresa           | Depende del cupón (bajo si es variable)  | Depende del canal de colocación (pública o privada) |

El certificado bursátil vuelve a ser el caso que no se puede resolver con una sola palabra por fila, la misma flexibilidad que ya se vio en [`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#6-los-seis-instrumentos): su exposición a cada riesgo depende de las decisiones de diseño de esa emisión en particular (plazo, mecánica de cupón, emisor, canal de colocación), no de una regla fija como en los otros cinco instrumentos.

---

## Apéndice: Supervivencia y estimación de la probabilidad de incumplimiento

La tabla de la sección 3 da probabilidades **acumuladas**: la de incumplir en algún momento entre hoy y el año $t$, vista desde hoy. Para valuar un bono o comparar emisores suele interesar otra pregunta: si el emisor sobrevivió hasta hoy, ¿qué tan probable es que incumpla en el próximo periodo?

**Probabilidad condicional.** Con la misma tabla: un emisor Baa incumple en los dos primeros años con probabilidad 0.495% y en el primero con 0.177%, así que incumple *durante el segundo año* con probabilidad $0.495\% - 0.177\% = 0.318\%$. Condicionada a que sobrevivió el primer año (probabilidad $1-0.00177$), es $0.318\%/(1-0.00177) \approx 0.319\%$. Para grado de inversión, esta probabilidad condicional crece con los años (un emisor sano tiene más tiempo para deteriorarse); para las peores calificaciones, decrece: los primeros uno o dos años son críticos, y el que sobrevive tiende a recuperarse.

**Tasa de riesgo.** El momento del incumplimiento $T$ es incierto hoy, una variable aleatoria (por eso va en mayúscula). La **tasa de riesgo** (hazard rate) $\lambda(t)$, también llamada intensidad de incumplimiento, es la probabilidad condicional anterior llevada a un intervalo muy corto, por unidad de tiempo:

$$\lambda(t) = \lim_{\Delta t \to 0} \dfrac{\Pr(t < T \leq t+\Delta t \mid T > t)}{\Delta t}$$

Con ella, la probabilidad acumulada de incumplimiento hasta $t$, $p(t)=\Pr(T\leq t)$, es

$$p(t) = 1 - e^{-\int_0^t \lambda(u)\,du} = 1 - e^{-\bar{\lambda}t}$$

con $\bar{\lambda}$ la tasa de riesgo promedio entre $0$ y $t$.

¿De dónde sale la fórmula? Sobrevivir hasta $t+\Delta t$ es sobrevivir hasta $t$ y no incumplir en el intervalo siguiente: $1-p(t+\Delta t) = [1-p(t)][1-\lambda(t)\Delta t]$. Restando $1-p(t)$ de los dos lados y dividiendo entre $\Delta t$, en el límite queda $\dfrac{d}{dt}\ln[1-p(t)] = -\lambda(t)$. Integrando de $0$ a $t$, con $p(0)=0$, sale la fórmula. Es la misma forma que la capitalización continua de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md#10-tasa-nominal-y-tasa-efectiva) ($e^{TNA}$), con la tasa de riesgo en lugar de la tasa de interés: la probabilidad de sobrevivir "se descuenta" a la tasa $\lambda$.

> **Ejemplo resuelto.** Despejando de la fórmula anterior, $\bar{\lambda} = -\ln[1-p(t)]/t$. Con la columna de 10 años de la tabla, un emisor Baa ($p=4.74\%$) tiene $\bar{\lambda} = -\ln(0.9526)/10 \approx 0.49\%$ al año; uno Ba ($p=19.71\%$), $\bar{\lambda}\approx 2.20\%$; uno B ($p=41.95\%$), $\bar{\lambda}\approx 5.44\%$.

**Estimación con la sobretasa.** La tabla es histórica. El mercado da otra estimación, hoy y para un emisor concreto, a partir de la sobretasa $s$ de su bono sobre un bono gubernamental del mismo plazo:

$$\bar{\lambda} \approx \dfrac{s}{1-r_{rec}} \qquad (r_{rec}<1)$$

¿De dónde sale la fórmula? En cada año, el emisor incumple con probabilidad aproximada $\bar{\lambda}$, y si incumple el tenedor pierde $LGD = 1-r_{rec}$ del valor nominal. La pérdida esperada por año es entonces $\bar{\lambda}(1-r_{rec})$, y la sobretasa es lo que el mercado cobra de más para compensarla: $s \approx \bar{\lambda}(1-r_{rec})$. Despejando $\bar{\lambda}$ sale la fórmula.

> **Ejemplo resuelto.** El bono corporativo a 10 años de la sección 4 de la nota de rendimiento rinde 0.79 pp sobre el Bono M del mismo plazo. Con $r_{rec}=40\%$, $\bar{\lambda} \approx 0.79\%/0.60 \approx 1.32\%$ al año, y la probabilidad de incumplir en 10 años es $p(10) = 1-e^{-0.0132 \times 10} \approx 12.3\%$. Frente a la tabla, el mercado lo trata como un emisor entre Baa (4.74%) y Ba (19.71%).

Las dos estimaciones no coinciden en general: para una misma calificación, la que sale de la sobretasa es mayor que la histórica. La sobretasa no paga solo la pérdida esperada; también paga la menor liquidez del bono (sección 5) y un premio por cargar un riesgo que no se puede diversificar del todo. Por eso la estimación con la sobretasa sirve para valuar y comparar bonos, y la histórica para medir cuánto se espera perder de verdad.

---

## Fuentes y referencias recomendadas

- Fabozzi, F. J. (Ed.). (2021). *The Handbook of Fixed Income Securities* (9ª ed.). McGraw Hill: el rendimiento de un bono dividido en cambio de precio y flujos cobrados (con su reinversión), y la clasificación de los riesgos de invertir en renta fija como factores que afectan una u otra parte, y cómo se controla cada uno.
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson: riesgo de tasa de interés y riesgo de reinversión.
- Mishkin, F. S. (2019). *The Economics of Money, Banking, and Financial Markets* (Business School Edition, 5ª ed.). Pearson: estructura de riesgo de las tasas de interés (risk structure of interest rates), riesgo de crédito (default risk) y su efecto en la sobretasa (spread) sobre la tasa libre de riesgo.
- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press: escala de calificaciones crediticias y la división entre grado de inversión y grado especulativo (junk).
- Hull, J. C. (2014). *Options, Futures, and Other Derivatives* (9ª ed.). Pearson: calificaciones crediticias, tasas de incumplimiento acumuladas de Moody's por calificación, tasa de recuperación, tasa de riesgo (hazard rate) y estimación de la probabilidad de incumplimiento a partir de la sobretasa.
- Banco de México: ficha técnica de UDIBONOS, mecánica de protección contra la inflación vía la UDI.
- Federal Reserve Bank of St. Louis (FRED): series mensuales de la tasa interbancaria mexicana y de la tasa de fondos federales de EE.UU., 2001-07 a 2026-08, la misma fuente que usa el apéndice de [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#apéndice-verificación-numérica-con-código-y-datos). Los ciclos de alza y baja y el diferencial de tasas del comentario de la sección 2 se reproducen con `codigo/analisis_tasas_mx_eu.py`.

---

## Cierre de la unidad — Lo esencial para recordar

- **Riesgo de tasa de interés**: el precio de un bono de cupón fijo se mueve en sentido contrario a la tasa de mercado, y ese movimiento es más fuerte mientras más largo es el plazo por vencer. Se reduce calzando el plazo con la fecha en que se necesita el dinero.
- **Riesgo de crédito**: la posibilidad de que el emisor incumpla; las calificadoras (S&P, Moody's, HR Ratings, Fitch) lo resumen en una escala de grado de inversión (AAA a BBB-) o grado especulativo/junk (BB+ o menor). Cada calificación tiene detrás una probabilidad de incumplimiento histórica, que se multiplica al cruzar a grado especulativo, y si el emisor incumple se recupera solo una fracción $r_{rec}=1-LGD$ del valor nominal. La deuda gubernamental mexicana se asume de riesgo mínimo, la corporativa no. Se reduce eligiendo por calificación y diversificando entre emisores.
- **Riesgo de inflación**: un cupón fijo nominal pierde poder de compra si la inflación sorprende al alza. Se reduce con el UDIBONO, diseñado específicamente para evitarlo al pactar una tasa real sobre un valor denominado en UDIs, o con un plazo corto o un cupón variable.
- **Riesgo de liquidez**: qué tan rápido y a qué precio se puede vender un instrumento antes de su vencimiento; los instrumentos gubernamentales son los más líquidos, una colocación privada o una emisión corporativa poco conocida son las menos líquidas. Se reduce no teniendo que vender (calce de plazo) o guardando una parte en CETES.
- Ningún instrumento de esta unidad enfrenta los cuatro riesgos por igual: caracterizarlo bien significa identificar cuáles aplican y cuáles no.

**Próxima sesión:** las estrategias de inversión en renta fija: cubrir una obligación o elegir el plazo según el escenario de tasas. Cuánto se mueve el precio ante un cambio de tasa (duración y convexidad) queda en la lectura complementaria [`5_duracion_convexidad.md`](5_duracion_convexidad.md).
