# Unidad 2 · Riesgos del Mercado de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante distinga el tipo de riesgo (tasa de interés, crédito, inflación, liquidez) al que está expuesto un instrumento de deuda dado.

## Contenido

|     | Tema                                              | Qué cubre                                                                            |
| --- | ------------------------------------------------- | ------------------------------------------------------------------------------------ |
| I   | Riesgo de tasa de interés                         | Por qué el precio de un bono se mueve en sentido contrario a la tasa de mercado      |
| II  | Riesgo de crédito y calificaciones                | Probabilidad de incumplimiento, investment grade vs. junk, y a quién le aplica       |
| III | Riesgo de inflación                               | Por qué un cupón fijo pierde poder adquisitivo, y cómo el UDIBONO lo evita           |
| IV  | Riesgo de liquidez                                | Qué tan rápido y a qué precio se puede vender un instrumento antes de su vencimiento |
| V   | Los seis instrumentos frente a los cuatro riesgos | Matriz de qué riesgo domina en cada instrumento de esta unidad                       |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. Riesgo de tasa de interés

Hasta aquí, comprar un instrumento de deuda se trató como un problema resuelto en cuanto se calculaba su precio. Pero comprarlo no cierra el trato para siempre: entre la compra y el vencimiento puede pasar algo que cambie lo que ese instrumento vale, o lo que se esperaba cobrar. ¿Qué puede salir mal, y quién absorbe la pérdida si sale mal? Cuatro riesgos distintos responden esa pregunta para un instrumento de deuda.

**Definición:** riesgo de tasa de interés es la posibilidad de que la tasa de mercado cambie después de comprar un instrumento de deuda, y que ese cambio mueva su precio en sentido contrario.

La razón es de competencia entre instrumentos: el cupón $c$ de un bono ya emitido es fijo, así que si la tasa de mercado sube, ese cupón queda por debajo de lo que ofrecen los bonos nuevos, y nadie paga el precio anterior por un flujo que ahora rinde menos que la alternativa; el precio tiene que bajar hasta que, comprado a ese precio menor, el mismo cupón fijo rinda lo mismo que exige el mercado nuevo. La fórmula de la sección 3 de [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#3-valuación-con-cupón-fijo) muestra el mismo efecto desde el descuento: con $c$ fijo, subir la tasa de descuento $r$ baja $v_0$ (cada flujo futuro se descuenta más fuerte), y bajar $r$ lo sube. Quien compra un bono de cupón fijo y necesita venderlo antes del vencimiento queda expuesto a ese movimiento; quien lo conserva hasta el vencimiento no realiza esa pérdida o ganancia, pero sí enfrenta el riesgo simétrico de **reinversión**: si las tasas bajan, los cupones que va cobrando en el camino se reinvierten a una tasa menor a la que esperaba.

Ese riesgo no es del mismo tamaño para cualquier plazo. Con más periodos $N$ por descontar, un mismo cambio en $r$ mueve más el término $(1+r)^{-N}$: un CETE a 28 días apenas se mueve si Banxico cambia su tasa de referencia, porque en 28 días ese cambio se descuenta una sola vez y por poco tiempo; un Bono M a 10 años, con el mismo cambio de tasa, puede mover su precio de forma mucho más pronunciada, porque el cambio afecta diez periodos de descuento en vez de uno.

> **Con datos reales.** El ciclo de alzas de 2021-2023 subió la tasa corta mexicana 7.2 puntos porcentuales (de 4.2% a 11.5%), un 40% más que el alza de la Fed en su ciclo más reciente (+5.1 pp, 2022-2024). El recorte que siguió ha sido todavía más desigual: México ha bajado 4.6 pp desde abril de 2024 contra 1.5 pp de la Fed, así que el diferencial de tasas entre los dos países cayó a 3.16 pp en agosto de 2026, de los niveles más bajos del historial desde 2001 (que promedia 5.2 pp) aunque sin llegar al mínimo de 2.23 pp que tocó en 2006. El riesgo de tasa de interés no es una posibilidad abstracta: los ciclos de política monetaria en México se han movido, en sus episodios más recientes, en un rango bastante más amplio que los de Estados Unidos.

**Ejemplos:**

- Un inversionista compra un Bono M a 10 años con cupón fijo de 8%, a \$93.58 (ver la tabla de [`4_duracion_convexidad.md`](4_duracion_convexidad.md#1-cuánto-se-mueve-el-precio)); si la tasa de mercado sube 100 pb, los bonos nuevos ofrecen más que ese 8%, así que su bono solo se vende si su precio baja lo suficiente para igualar ese nuevo rendimiento, hasta \$87.71.
- Un ahorrador reinvierte los cupones semestrales de un Bono M a medida que los cobra; si la tasa de mercado baja de 9% a 6% en el camino, cada cupón que reinvierte gana 6% en vez del 9% original: es el riesgo de reinversión, el lado simétrico del riesgo de tasa de interés.

*Fuente: Mishkin, F. S. y Eakins, S. G. (2014). Financial Markets and Institutions (8ª ed.). Pearson. Cap. 3, "What Do Interest Rates Mean and What Is Their Role in Valuation?": riesgo de tasa de interés y riesgo de reinversión.*

### 2. Riesgo de crédito y calificaciones

**Definición:** riesgo de crédito (o de incumplimiento) es la posibilidad de que el emisor no pague el cupón o el valor nominal prometido, en parte o por completo.

La Unidad 1 ya presentó a las calificadoras (S&P, Moody's, HR Ratings, Fitch) y su conflicto de interés ([`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md#3-calificadoras-y-riesgo-de-crédito)). Lo que agrega esta sección es la escala misma: cada calificadora ordena a los emisores en una escala de letras (de AAA, la más alta, hasta D, incumplimiento), y esa escala se divide en dos grandes categorías:

- **Grado de inversión (investment grade):** de AAA hasta BBB- (o el equivalente Baa3 en la escala de Moody's). El emisor tiene una capacidad de pago que la calificadora considera sólida.
- **Grado especulativo o "chatarra" (junk):** de BB+ hacia abajo. El emisor tiene una probabilidad de incumplimiento considerablemente mayor, y por eso el mercado le exige una sobretasa (spread) más alta sobre la tasa libre de riesgo para compensar ese riesgo adicional.

> **Aplicación a los instrumentos de esta unidad.** La deuda gubernamental (CETE, Bono M, UDIBONO) se trata como de riesgo de crédito mínimo, el mismo supuesto de la Unidad 1: el Gobierno Federal mexicano no se califica de la misma forma que un emisor corporativo. La deuda corporativa (bono corporativo, papel comercial, certificado bursátil emitido por una empresa) sí carga riesgo de crédito, y ese riesgo es justamente lo que califican S&P, Moody's, HR Ratings o Fitch; la sobretasa que paga por encima de un Bono M o un CETE del mismo plazo es, en buena medida, el precio de ese riesgo.

**Ejemplos:**

- Un bono corporativo calificado BBB- (el último escalón de grado de inversión) es rebajado a BB+ (el primer escalón de junk) tras un mal reporte financiero del emisor; el mercado le exige una sobretasa mayor y su precio cae de inmediato.
- Una empresa mediana emite papel comercial y, al vencimiento, no logra refinanciarse ni cubrir el principal; el tenedor pierde parte o todo el monto invertido, el riesgo de crédito materializado.

*Fuente: Luenberger, D. G. (2013). Investment Science (2ª ed.). Oxford University Press. Cap. 3, "Fixed-Income Securities", "Quality Ratings", pp. 53-54: la escala de calificaciones y la división entre grado de inversión y grado especulativo.*

### 3. Riesgo de inflación

**Definición:** riesgo de inflación (o riesgo de poder adquisitivo) es la posibilidad de que la inflación real resulte mayor a la que el mercado esperaba al fijar la tasa cupón, de modo que el pago prometido, aunque se cumpla al pie de la letra, compre menos de lo que el inversionista esperaba.

Un instrumento con cupón fijo nominal (Bono M, bono corporativo, papel comercial, CETE) no ajusta ese pago si la inflación sorprende al alza: el monto en pesos es el que es, pero su poder de compra cae con la inflación no anticipada. El UDIBONO, presentado en [`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#6-los-seis-instrumentos), es exactamente el instrumento que este curso usa para evitar ese riesgo: al pactar una tasa real sobre un valor nominal denominado en UDIs (que se ajustan con la inflación observada), el cupón y el capital que recibe el inversionista mantienen su poder de compra sin importar qué tan alta resulte la inflación.

> Este riesgo es más relevante mientras más largo es el plazo del instrumento (más tiempo para que la inflación observada se aleje de la esperada) y mientras más fijo es el cupón en términos nominales; por eso un CETE a 28 días apenas lo enfrenta (muy poco tiempo para que la inflación sorprenda), mientras que un Bono M a 30 años sí queda expuesto de forma relevante.

**Ejemplos:**

- Un Bono M con cupón nominal fijo de 8% se compró esperando una inflación de 5%; si la inflación observada resulta 12%, el cupón sigue pagando el mismo monto en pesos, pero compra menos de lo que el inversionista anticipaba.
- Un UDIBONO comprado en el mismo momento, con la misma sorpresa inflacionaria de 12%, no pierde poder de compra: su valor nominal en UDIs se ajusta con la inflación observada, así que el cupón y el capital mantienen su valor real.

### 4. Riesgo de liquidez

**Definición:** riesgo de liquidez es la posibilidad de no poder vender un instrumento rápidamente, o de tener que aceptar un precio desfavorable para lograrlo, antes de su vencimiento.

[`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda) ya explicó que el mercado secundario de deuda es mayoritariamente de mostrador, no un libro de órdenes público como el de una acción; esa estructura por sí sola vuelve a la deuda, en general, menos líquida que una acción de una empresa grande. Dentro del propio mercado de deuda, la liquidez tampoco es uniforme:

- Los instrumentos gubernamentales (CETE, Bono M, UDIBONO) son los más líquidos: se colocan en montos grandes y periódicos, y los Formadores de Mercado ([`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda)) están obligados a cotizar precio de compra y venta de forma continua.
- Una emisión colocada por **oferta pública** suele ser más líquida que una **colocación privada** ([`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda)), porque hay más inversionistas que la conocen y pueden comprarla en el secundario.
- Una emisión corporativa pequeña o poco conocida (un papel comercial de una empresa mediana, un certificado bursátil colocado de forma privada) suele ser la menos líquida de todas: si el tenedor necesita vender antes del vencimiento, puede no encontrar comprador, o solo a un precio con un descuento considerable.

**Ejemplos:**

- El tenedor de un CETE puede venderlo el mismo día a un precio muy cercano al de mercado, porque los Formadores de Mercado cotizan compra y venta de forma continua.
- El tenedor de un certificado bursátil colocado de forma privada por una empresa poco conocida intenta venderlo antes del vencimiento y solo encuentra comprador con un descuento considerable, o no encuentra comprador en absoluto.

### 5. Los seis instrumentos frente a los cuatro riesgos

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

## Fuentes y referencias recomendadas

- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 3, "What Do Interest Rates Mean and What Is Their Role in Valuation?": riesgo de tasa de interés y riesgo de reinversión.
- Mishkin, F. S. (2019). *The Economics of Money, Banking, and Financial Markets* (Business School Edition, 5ª ed.). Pearson. Cap. 5, "The Risk and Term Structure of Interest Rates": riesgo de crédito (default risk) y su efecto en la sobretasa (spread) sobre la tasa libre de riesgo.
- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press. Cap. 3, "Fixed-Income Securities", "Quality Ratings", pp. 53-54: escala de calificaciones crediticias y la división entre grado de inversión y grado especulativo (junk).
- Banco de México: ficha técnica de UDIBONOS, mecánica de protección contra la inflación vía la UDI.
- Federal Reserve Bank of St. Louis (FRED): series mensuales de la tasa interbancaria mexicana y de la fed funds estadounidense, 2001-07 a 2026-08, la misma fuente que usa el apéndice de [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#apéndice-verificación-numérica-con-código-y-datos). Los ciclos de alza y baja y el diferencial de tasas del comentario de la sección 1 se reproducen con `codigo/analisis_tasas_mx_eu.py`.

---

## Cierre de la unidad — Lo esencial para recordar

- **Riesgo de tasa de interés**: el precio de un bono de cupón fijo se mueve en sentido contrario a la tasa de mercado, y ese movimiento es más fuerte mientras más largo es el plazo por vencer.
- **Riesgo de crédito**: la posibilidad de que el emisor incumpla; las calificadoras (S&P, Moody's, HR Ratings, Fitch) lo resumen en una escala de grado de inversión (AAA a BBB-) o grado especulativo/junk (BB+ o menor); la deuda gubernamental mexicana se asume de riesgo mínimo, la corporativa no.
- **Riesgo de inflación**: un cupón fijo nominal pierde poder de compra si la inflación sorprende al alza; el UDIBONO es el instrumento diseñado específicamente para evitarlo, al pactar una tasa real sobre un valor denominado en UDIs.
- **Riesgo de liquidez**: qué tan rápido y a qué precio se puede vender un instrumento antes de su vencimiento; los instrumentos gubernamentales son los más líquidos, una colocación privada o una emisión corporativa poco conocida son las menos líquidas.
- Ningún instrumento de esta unidad enfrenta los cuatro riesgos por igual: caracterizarlo bien significa identificar cuáles aplican y cuáles no, no asumir que todos los riesgos aplican a todos los instrumentos por igual.

**Próxima sesión:** cuánto se mueve el precio de un bono ante un cambio de tasa, no solo en qué dirección: la duración y la convexidad.
