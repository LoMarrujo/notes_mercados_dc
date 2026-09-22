# Unidad 2 · Mercado e Instrumentos de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante clasifique un instrumento de deuda (CETES, Bonos gubernamentales, UDIBONOS, Bonos corporativos, Papel comercial, Certificados bursátiles) según su emisor, su plazo y su mecánica de pago, y lo distinga de un instrumento de participación de capital.

## Contenido

|     | Tema                                                   | Qué cubre                                                                                                            |
| --- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| I   | Qué es un instrumento de deuda                         | Un flujo de efectivo fijo que se negocia en el mercado; vocabulario común y lo que queda fuera de esta unidad        |
| II  | Cómo paga un instrumento: mecánicas y vector de flujos | Descuento, cupón fijo, cupón variable, bullet y amortización, cada uno construido y dibujado como vector de flujos   |
| III | Deuda o participación de capital                       | Por qué existe el financiamiento, y la primera decisión: prometer un pago fijo o ceder parte del negocio             |
| IV  | Deuda directa o indirecta                              | Emitir el título uno mismo frente a pedirle el crédito a un banco, y por qué esta unidad vive del lado directo       |
| V   | Cómo se coloca y se negocia la deuda                   | Subasta gubernamental, oferta pública, colocación privada, y el mercado secundario donde se revende después          |
| VI  | Los seis instrumentos                                  | CETES, Bono M y UDIBONO; bono corporativo y papel comercial; el certificado bursátil como instrumento híbrido        |
| VII | Tres preguntas y los seis instrumentos lado a lado     | Quién emite, a qué plazo, cómo paga: comparativo por emisor, plazo, mecánica, colocación, comprador y análogo en EUA |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. Qué es un instrumento de deuda

Un **instrumento de deuda** (también llamado de **renta fija**) es un instrumento financiero que promete al poseedor un ingreso fijo durante un lapso de tiempo; en otras palabras, quien lo posee es dueño de un flujo de efectivo definido. Si además existe un mercado desarrollado donde se compra y se vende con facilidad, se le llama **valor negociable** (*security*).

La palabra "fijo" no es totalmente precisa. Originalmente significaba que el flujo prometido estaba definido por completo y que la única incertidumbre era si el emisor incumpliría; hoy se usa en un sentido más amplio: un flujo de efectivo fijo salvo por variaciones debidas a circunstancias contingentes bien definidas, como un cupón indexado a una tasa de referencia. El emisor promete ese calendario de pagos (determinístico o no), y el instrumento no es más que ese flujo.

Para describir cualquier instrumento de deuda basta un vocabulario común. Tres cantidades describen su dinero, y conviene no confundirlas:

| Cantidad            | Símbolo | Qué es                                                                                        | ¿Cambia después de la emisión? |
| ------------------- | ------- | --------------------------------------------------------------------------------------------- | ------------------------------ |
| Capital (principal) | $a$     | Lo que el inversionista paga al comprar; un hecho del contrato                                | No                             |
| Valor presente      | $v_0$   | Lo que valen hoy los flujos futuros, descontados a la tasa de mercado                         | Sí, con la tasa                |
| Valor nominal       | $v_N$   | El monto de referencia sobre el que se calculan los pagos, y el que se liquida al vencimiento | No                             |

Al emitir, el mercado fija el precio igual al valor presente de los flujos, así que $a=v_0$; cuando la tasa cambia, el valor presente ($v_0$) cambia en el tiempo, pero no el capital pagado ($a$).

Dos datos más completan la descripción:

- **Cupón ($c$):** el pago periódico de interés que promete el emisor. La **tasa cupón** es ese pago expresado como porcentaje del valor nominal.
- **Plazo (vencimiento):** la fecha en que el emisor debe liquidar el valor nominal, junto con el último cupón si lo hay.

Bajo esta definición cabe más de lo que esta unidad cubre. Los depósitos a plazo, las hipotecas y las anualidades también prometen un flujo definido, pero son contratos entre dos partes y no se negocian como valores; una hipoteca solo se vuelve negociable cuando se empaqueta con otras en valores respaldados por hipotecas. Esta unidad se limita a los valores de deuda que se negocian en el mercado mexicano, los seis instrumentos de la sección 6.

> **Ejemplo resuelto.** Un CETE a 28 días con valor nominal \$10 promete un solo pago de \$10 en 28 días: flujo fijo sin salvedad alguna. Un certificado bursátil con cupón referenciado a la TIIE promete pagar un cupón cada 28 días, pero su monto depende de la TIIE vigente en cada fecha: fijo salvo una contingencia bien definida, la tasa de referencia. Ambos son instrumentos de deuda.

> **Ejemplo resuelto, en la emisión.** Un Bono M a 10 años, con cupón de 8% y valor nominal $v_N=$ \$100, se emite el día en que la tasa de mercado es 8%. Como el cupón coincide con la tasa, el bono se valúa exactamente a la par: el valor presente de sus flujos (los diez cupones de \$8 y el pago final de \$100 al vencimiento) es $v_0=$ \$100. Ese valor presente es justo lo que el inversionista paga por el bono, así que el capital pagado también es \$100: el día de la emisión, $a=v_0=v_N=$ \$100.
>
> **Después, cuando cambia la tasa.** Un año después, la tasa de mercado sube a 9%. Los flujos que faltan por cobrar son los mismos de siempre (el mismo cupón de 8%, el mismo valor nominal al vencimiento), pero ahora se descuentan a una tasa distinta, así que el valor presente se recalcula: $v_0=$ \$93.58 (el cálculo está en [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#2-valuación-con-cupón-fijo)). El capital pagado no se recalcula, porque no depende de ninguna fórmula: es un hecho ya ocurrido, lo que el inversionista efectivamente pagó hace un año, y sigue siendo $a=$ \$100. El valor nominal tampoco cambia, $v_N=$ \$100, porque es el monto que el contrato promete liquidar al vencimiento sin importar qué pase con las tasas en el camino. La consecuencia es concreta: si ese inversionista quisiera vender el bono hoy, solo conseguiría \$93.58 por él, aunque haya pagado \$100.

Si el instrumento no es más que su flujo, describirlo es describir ese flujo: cómo se paga el interés y cómo se devuelve el capital.

### 2. Cómo paga un instrumento: mecánicas y vector de flujos

Un instrumento de deuda se caracteriza por dos decisiones de diseño independientes: cómo paga interés y cómo liquida el capital. Dicho con números, es un **vector de flujos** $(c_0, c_1, \ldots, c_N)$: un monto por cada periodo entre la compra ($t=0$) y el vencimiento ($t=N$), negativo si sale de tu bolsillo, positivo si entra. El primer monto es siempre la compra, $c_0=-a$: el capital, lo que sale de tu bolsillo; lo que distingue una mecánica de otra es, nada más, qué forma toma el resto del vector. Este es el mismo vector que [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md) va a descontar término por término para llegar al valor presente $v_0$, con el que se compara el capital $a$; aquí solo se construye y se dibuja, todavía sin poner una tasa de por medio.

**Cómo paga interés** hay tres mecánicas.

**A descuento (o cupón cero).** No paga ningún cupón: se compra por debajo del valor nominal y se cobra el valor nominal completo al vencimiento; la ganancia es esa diferencia. El vector tiene un solo flujo distinto de cero, el valor nominal al vencimiento:

$$(c_0, c_1, \ldots, c_N) = (-a,\ 0,\ \ldots,\ 0,\ v_N)$$

![Diagrama de flujo de efectivo a descuento: salida de $90.91 en t=0 y entrada de $100 en t=1, con valor nominal 100 y tasa 10%](img/flujo_descuento.png)

Construirlo es una sola decisión: cuánto se paga hoy ($a$) por recibir un monto ya fijo ($v_N$) al final, sin nada en medio. El diagrama tiene, por eso, solo dos flechas: una hacia abajo en $t=0$, una hacia arriba en $t=N$.

**Con cupones periódicos, cupón fijo.** Paga el mismo cupón $c$ cada periodo, pactado desde la emisión, y el último periodo además liquida el valor nominal:

$$(c_0, c_1, \ldots, c_N) = (-a,\ c,\ c,\ \ldots,\ c,\ c+v_N)$$

![Diagrama de flujo de efectivo con cupón fijo de un Bono M: salida de $100 en t=0, cupones de $10 en t=1 y t=2, y $110 en t=3, con valor nominal 100 y tasa 10%](img/flujo_cupon_fijo.png)

Construirlo agrega un paso al anterior: entre $t=0$ y $t=N$ aparece una flecha del mismo tamaño ($c$) en cada periodo intermedio, y solo la última flecha crece, porque ahí se suman dos cosas que llegan el mismo día: el último cupón y el valor nominal. El diagrama lo muestra directo: una fila de flechas parejas, y una última flecha más alta que las demás.

**Con cupones periódicos, cupón variable (flotante).** Paga un cupón que se recalcula cada periodo según una tasa de referencia vigente (típicamente la TIIE), así que, a diferencia de las otras dos mecánicas, no es completamente determinístico: el cupón más próximo ya quedó fijo desde el último reseteo, así que ese sí es un número; los siguientes dependen de una tasa que todavía no existe, así que son inciertos:

$$(c_0, c_1, \ldots, c_N) = (-a,\ c_1,\ C_2,\ \ldots,\ C_{N-1},\ C_N+v_N)$$

![Diagrama de flujo de efectivo con cupón variable de un certificado bursátil: salida de $100 en t=0, entrada conocida de $10 en t=1, y entradas inciertas C2 en t=2 y C3+100 en t=3](img/flujo_cupon_variable.png)

La mayúscula en $C_2, \ldots, C_N$ no es un capricho de notación: marca justo la diferencia con los dos vectores anteriores, siguiendo la misma regla que ya distingue un dato cierto de una variable aleatoria en esta unidad. Construir este vector es, entonces, dibujar la primera flecha como las de un cupón fijo (ya se conoce) y las siguientes con una línea punteada, porque su tamaño todavía no existe; solo se sabrá conforme se cumplan las fechas de reseteo.

**Cómo liquida el capital** hay dos mecánicas. No son mecánicas de interés, son dos formas distintas de acomodar el capital dentro del mismo vector:

- **Bullet:** todo el valor nominal se liquida de golpe, junto con el último cupón si lo hay; es el mismo vector de cupón fijo de arriba. Es la mecánica de los seis instrumentos mexicanos de esta unidad.
- **Con amortización de capital:** el capital se reparte en abonos $k_t$ a lo largo de la vida del instrumento (sistema francés, sistema alemán, fondo de amortización o *sinking fund*), como un crédito hipotecario o un préstamo de auto, junto con el interés que corresponde al saldo insoluto de ese periodo:

$$(c_0, c_1, \ldots, c_N) = (-a,\ k_1+rs_0,\ k_2+rs_1,\ \ldots,\ k_N+rs_{N-1}) \qquad \left(\sum_{t=1}^N k_t = a\right)$$

![Diagrama comparativo en tres paneles: bullet con flechas de $10 y un pago final de $110 en t=3; amortización alemana con pagos decrecientes de $43.33, $40.00 y $36.67; y amortización francesa con tres pagos iguales de $40.21, todos sobre capital 100 y tasa 10%](img/flujo_amortizacion.png)

Construir el vector amortizado es, paso a paso: decidir el calendario de abonos $k_t$ (constante en el sistema alemán, calculado para que el pago total sea constante en el sistema francés), calcular el interés de cada periodo sobre lo que todavía se debe ($rs_{t-1}$), y sumar ambas partes flujo por flujo. El diagrama deja ver la diferencia de un vistazo: el vector bullet es plano y termina en una flecha mucho más alta que las demás; el vector amortizado no tiene ese pico final, sus flechas ya vienen repartidas (y, en el sistema alemán, decrecen, porque el interés baja conforme baja el saldo insoluto; en el francés son todas iguales).

Los dos sistemas más usados reparten el capital de forma opuesta. En el **sistema alemán** el abono $k_t$ es constante y el pago total decrece. En el **sistema francés** es el pago total $c$ el que es constante, $(-a,\ c,\ c,\ \ldots,\ c)$, y el abono crece: al principio casi todo el pago es interés, y conforme baja el saldo insoluto el interés baja y el abono sube. Con el mismo capital de \$100, tasa de 10% y 3 periodos, el sistema francés paga \$40.21 cada periodo (interés de \$10.00, \$6.98 y \$3.66; abono de \$30.21, \$33.23 y \$36.56), frente a los \$43.33, \$40.00 y \$36.67 del alemán. El valor de $c$ se deriva en [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#4-amortización-de-capital).

Ninguno de los seis instrumentos de esta unidad usa amortización, todos son bullet; el vector amortizado se construye aquí solo para completar el panorama de mecánicas.

> **Ejemplo resuelto.** Un CETE a 28 días con valor nominal \$10 se compra hoy en \$9.95 y no paga nada más hasta el vencimiento, cuando el gobierno paga los \$10 completos: es a descuento, bullet, la ganancia es \$0.05 (el precio exacto, a partir de la tasa de la subasta, se calcula en [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#1-valuación-a-descuento)). Un Bono M paga una tasa cupón fija cada seis meses durante toda su vida, más el valor nominal el día del vencimiento: es cupón fijo, bullet. Un certificado bursátil también puede pagar cupones periódicos de cupón variable referenciado a la TIIE de fondeo: cada cupón depende de la tasa vigente ese periodo, no de una tasa fija pactada desde la emisión, aunque también liquida el capital bullet.

### 3. Deuda o participación de capital

Un flujo fijo es una decisión contractual, no un rasgo natural del financiamiento. Hay quien tiene un proyecto y no tiene el dinero para realizarlo; hay quien tiene el dinero y, por ahora, no tiene dónde ponerlo a trabajar. El mercado financiero existe para cerrar ese desfase entre ahorro y proyecto de inversión, la misma intermediación entre unidades superavitarias y deficitarias que presentó [`1_intermediacion_financiera.md`](../unidad1/1_intermediacion_financiera.md#1-intermediación-financiera).

Cerrar ese desfase, sin embargo, no fija todavía los términos del trato. Si tienes el proyecto y consigues quien te dé el dinero, la primera decisión no es institucional (a quién acudir), es contractual: ¿se lo pides prestado, o lo haces tu socio? Pedirlo prestado es prometer el flujo fijo de la sección 1; hacerlo socio es ceder parte del negocio. Esa disyuntiva, deuda o participación de capital, es el criterio que divide toda la materia en dos: esta unidad recorre el lado de la deuda, la Unidad 3 (Mercado de Capitales, en el sentido de participación) recorrerá el lado de la participación. Cuatro rasgos del trato cambian según el lado que se elija:

| Rasgo     | Deuda                                                                                                                 | Participación de capital                                                                       |
| --------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Flujo     | Fijo: un monto pactado desde el inicio (cupón, capital), sin importar el desempeño del proyecto, salvo incumplimiento | Residual: lo que sobra después de cubrir a todos los demás compromisos, incluida la deuda      |
| Prelación | Cobra primero si el emisor se liquida                                                                                 | Cobra al final, solo si sobra algo después de pagar a todos los acreedores                     |
| Control   | Ninguno: el tenedor no vota ni participa en las decisiones del proyecto mientras se le pague                          | Voto y voz en las decisiones, proporcional a la parte del capital que se posea                 |
| Horizonte | Definido: la relación termina en la fecha de vencimiento pactada                                                      | Indefinido: dura mientras la empresa exista, o hasta que el socio venda su parte a alguien más |

Por prometer un flujo fijo y cobrar antes que el socio, la deuda es la opción de menor riesgo para quien presta el dinero, pero también la de menor participación en las ganancias del proyecto si a este le va excepcionalmente bien: un tenedor de deuda no gana más porque el negocio prospere, un socio sí.

> **Cuidado con el nombre.** La Unidad 3 de este curso se llama "Mercado de Capitales", pero ahí ese nombre usa el criterio de esta sección (solo instrumentos de participación: acciones, FIBRAs, CKD, CERPIs), no el de plazo de la Unidad 1. Un Bono M es "mercado de capitales" por su plazo largo ([`0_activo_financiero.md`](../unidad1/0_activo_financiero.md#3-mercado-de-dinero-y-mercado-de-capitales)) pero sigue siendo mercado de deuda, no mercado de capitales en el sentido de la Unidad 3. En estas notas, "mercado de capitales" sin calificar siempre usa el criterio de plazo; al criterio de esta sección se le llama aquí **mercado de participación** o **mercado accionario**, precisamente para no chocar con el nombre de la Unidad 3.
>
> **Ejemplo resuelto.** Un Bono M a 10 años: por plazo es mercado de capitales (Unidad 1); por tipo de promesa de pago (esta sección) es mercado de deuda, porque paga un cupón fijo pactado desde la emisión y su tenedor no tiene voto en las decisiones del Gobierno Federal ni en cuándo termina esa relación. Los dos criterios conviven sin contradecirse, solo responden preguntas distintas.

### 4. Deuda directa o indirecta

Elegido el lado de la deuda, queda una segunda pregunta: ¿a quién se la pides? [`1_intermediacion_financiera.md`](../unidad1/1_intermediacion_financiera.md#2-deuda-directa-indirecta-y-capital) ya distinguió las dos rutas: pedirla **indirectamente**, a un banco que capta de muchos ahorradores y absorbe el riesgo de crédito por ti, o pedirla **directamente**, emitiendo tú mismo un título que el público inversionista compra sin que nadie más absorba ese riesgo en medio.

Los seis instrumentos de esta unidad, sin excepción, están del lado directo: un CETE, un Bono M o un certificado bursátil los coloca el propio emisor (Gobierno Federal o empresa) con el inversionista final; si el emisor incumple, la pérdida es del inversionista, no de un banco intermediario. Un crédito bancario no aparece como instrumento propio de esta unidad, pero no porque su análisis sea distinto: en lo estructural sigue siendo el mismo problema que resuelve el resto de esta nota (un flujo prometido a cambio de un capital, a un plazo dado, con un riesgo de que no se cumpla); lo único que cambia es el canal y quién absorbe ese riesgo, la intermediación indirecta que ya cubrió Unidad 1.

### 5. Cómo se coloca y se negocia la deuda

Ya establecido que esta unidad es toda deuda directa (sección 4), queda ver cómo se emite y se negocia en la práctica. El mercado de deuda cumple dos funciones económicas distintas, y esa función es justamente el criterio de plazo de la Unidad 1 ([`0_activo_financiero.md`](../unidad1/0_activo_financiero.md#3-mercado-de-dinero-y-mercado-de-capitales)):

- **Mercado de dinero (corto plazo):** administra necesidades de liquidez inmediata. El Gobierno Federal cubre faltantes temporales de caja entre lo que recauda y lo que gasta; una empresa financia capital de trabajo (nómina, inventario) sin comprometerse a un plazo largo. Banxico, además, usa este mismo mercado como herramienta de política monetaria: compra y vende CETES a los bancos en **operaciones de mercado abierto** para inyectar o retirar liquidez del sistema bancario y así mantener su tasa de referencia en el nivel que decide.
- **Mercado de capitales, en su vertiente de deuda (largo plazo):** financia proyectos que tardan años en pagarse solos. El Gobierno Federal financia déficit presupuestal plurianual; una empresa financia una planta, una expansión o una adquisición.

Quién emite determina el canal de colocación primaria:

- **Deuda gubernamental:** Banxico, como agente financiero del Gobierno Federal, coloca CETES, Bonos M y UDIBONOS (y también Bondes, un cuarto instrumento de cupón variable que existe en el mismo mercado pero que esta unidad no cubre a fondo) en una **subasta primaria** semanal (con calendario público), a la que solo pueden postular directamente los **Formadores de Mercado**, un grupo de bancos y casas de bolsa autorizados; el resto de los inversionistas participa a través de ellos.
- **Deuda corporativa:** una empresa coloca papel comercial, bonos corporativos o certificados bursátiles de dos formas. La **oferta pública** requiere autorización de la CNBV, prospecto de colocación y una casa de bolsa que la suscriba (underwriting, ver [`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md#2-quién-interviene-bmv-biva-casas-de-bolsa-indeval)); la **colocación privada** se coloca directamente entre inversionistas institucionales calificados, sin oferta pública, lo que la hace más rápida y barata pero también menos líquida en el secundario.

> **Ejemplo resuelto.** El Banco Centroamericano de Integración Económica (BCIE) colocó en 2026 un certificado bursátil de hasta \$3,000 millones de pesos a un plazo de 3.5 años, con cupón cada 28 días referenciado a la TIIE de fondeo a 28 días más una sobretasa, y amortización bullet (todo el capital en un solo pago) al vencimiento en 2029. Es exactamente el canal de colocación privada/institucional: no es una subasta gubernamental ni una oferta pública al gran público inversionista.

Colocada la deuda, el mercado secundario donde se revende es mayoritariamente de mostrador (over the counter), como documentan los propios manuales operativos de la BMV: bancos y casas de bolsa negocian entre sí en sus mesas de dinero, no en un libro de órdenes público como el de una acción en la bolsa. Esos mismos manuales son donde la BMV documenta qué tan líquido es cada instrumento, un punto que se retoma a fondo como riesgo de liquidez en [`3_riesgos_mercado_deuda.md`](3_riesgos_mercado_deuda.md#4-riesgo-de-liquidez). Para que ese mercado disperso tenga un precio de referencia diario, existen **proveedores de precios** (empresas especializadas, autorizadas por la CNBV) que publican el precio de valuación de cada instrumento en circulación; ese precio es el insumo que un banco o una Siefore usa para valorar su portafolio de deuda todos los días, y el punto de partida de la valuación que se estudia en [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md).

Dos cifras ilustran el tamaño y la forma de este mercado en septiembre de 2026: en la subasta del 15 de septiembre, el CETE a 28 días rindió 6.25%, cerca de la tasa de referencia de Banxico (6.50%) porque es casi el plazo que decide la política monetaria; el Bono M a 10 años, en cambio, rendía 9.16% el 21 de septiembre, casi tres puntos porcentuales por encima, porque un inversionista exige más rendimiento por comprometer su dinero una década en vez de 28 días.

### 6. Los seis instrumentos

Con el instrumento definido (secciones 1 y 2), el lado de la deuda elegido (3 y 4) y el canal de colocación conocido (5), toca ponerle nombre a los seis instrumentos concretos de este mercado. Cada uno se caracteriza por quién lo emite, a qué plazo y cómo paga. Se empieza por los tres que comparten emisor.

**Instrumentos gubernamentales: CETES, Bono M y UDIBONO.** Los emite el Gobierno Federal y los coloca Banxico como su agente financiero, en la misma subasta primaria semanal de la sección 5. Comparten emisor y canal de colocación; lo que los distingue es el plazo y la mecánica de pago.

**CETES (Certificados de la Tesorería):** mercado de dinero, a plazos de 28, 91, 182 y 364 días. Pagan a descuento: no llevan cupón, se colocan por debajo de su valor nominal de \$10 y liquidan el valor nominal completo al vencimiento. Financian el faltante de caja de corto plazo del Gobierno Federal. En la subasta del 15 de septiembre de 2026 rindieron 6.25% a 28 días y 7.24% a 364 días, con el extremo corto cerca de la tasa de referencia de Banxico (6.50%). Lo compran, sobre todo, bancos y casas de bolsa en la propia subasta (los Formadores de Mercado), que después lo revenden a fondos de inversión de mercado de dinero y a tesorerías corporativas que estacionan ahí su efectivo de corto plazo; el pequeño inversionista también puede comprarlo directamente a través de cetesdirecto.

**Bono M:** mercado de capitales, a plazos de 3, 5, 10, 20 y 30 años. Pagan un cupón fijo cada 182 días, pactado en pesos nominales desde la emisión, más el valor nominal al vencimiento. Financian el déficit presupuestal plurianual del Gobierno Federal, y su tasa a 10 años es la referencia que el mercado sigue para juzgar el costo de financiamiento del gobierno a largo plazo (9.16% el 21 de septiembre de 2026, según cetesdirecto). Sus principales compradores son inversionistas institucionales con pasivos de largo plazo, Afores/Siefores y aseguradoras a la cabeza, además de fondos de inversión de deuda; una porción considerable también la tienen inversionistas extranjeros, atraídos por el rendimiento de un instrumento soberano en pesos frente al de otras economías.

**UDIBONO (Bono de Desarrollo del Gobierno Federal denominado en UDIs):** mismo emisor y plazos largos que el Bono M (3, 10, 20 y 30 años), pero su valor nominal está denominado en Unidades de Inversión (UDIs), no en pesos; el cupón fijo (también cada 182 días) es una **tasa real**, y tanto el cupón como el valor nominal al vencimiento se convierten a pesos multiplicando por el valor de la UDI vigente ese día. Como la UDI se ajusta con la inflación, quien compra un UDIBONO protege su poder adquisitivo, algo que el Bono M no ofrece: si la inflación sorprende al alza, el cupón fijo en pesos del Bono M pierde valor real, mientras que el cupón del UDIBONO se ajusta con la UDI. Lo compran, en buena medida, los mismos inversionistas institucionales que el Bono M (Afores/Siefores, aseguradoras), pero por una razón más puntual: son quienes tienen pasivos de largo plazo sensibles a la inflación (pensiones, seguros), y el UDIBONO les permite calzar ese pasivo con un activo que corre el mismo riesgo.

> **Por qué UDIBONO y Bono M pagan distinto aunque comparten emisor y plazo.** La diferencia no es de riesgo de crédito (el mismo Gobierno Federal respalda a ambos), es de **qué tasa se pacta**: el Bono M pacta una tasa nominal fija sobre pesos; el UDIBONO pacta una tasa real fija sobre UDIs. Por eso la tasa cupón del Bono M (nominal) es mayor que la del UDIBONO (real): la diferencia aproxima la inflación que el mercado espera durante la vida del bono, más cualquier prima por la incertidumbre de esa inflación. El 21 de septiembre de 2026, el UDIBONO a 10 años rendía una tasa real de 4.75% y el de 30 años, 4.90%, contra 9.16% y 9.87% del Bono M nominal del mismo plazo: una brecha de 4.41 y 4.97 puntos porcentuales que da una idea de cuánta inflación espera el mercado a cada horizonte.

**Instrumentos corporativos: bono corporativo y papel comercial.** Ambos los emite una empresa privada, no el gobierno, y por lo tanto ambos requieren la autorización de la CNBV para su oferta pública (o califican para colocación privada) descrita en la sección 5, y ambos están sujetos al riesgo de crédito del emisor que se calificó en [`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md#3-calificadoras-y-riesgo-de-crédito). Lo que los distingue es el plazo, y de ahí se sigue casi automáticamente la mecánica de pago.

**Papel comercial:** mercado de dinero, plazo corto (hasta 360 días, típicamente unas cuantas semanas). Suele pagar a descuento, igual que un CETE, porque a un plazo tan corto no vale la pena la complejidad administrativa de un cupón periódico. Financia capital de trabajo: nómina, inventario, cuentas por cobrar. Muchas empresas mantienen un **programa autorizado** vigente por varios años, bajo el cual reemiten papel comercial una y otra vez (revolvente) sin pedir una nueva autorización cada vez. Lo compran, sobre todo, fondos de inversión de mercado de dinero y tesorerías de otras empresas que necesitan estacionar efectivo por unas semanas a una tasa mejor que un depósito bancario.

**Bono corporativo:** mercado de capitales, plazo largo (varios años). Paga cupones periódicos, fijos o variables (referenciados a TIIE), porque a un plazo largo el emisor prefiere un costo de financiamiento predecible o, si elige tasa variable, transferir al inversionista el riesgo de que la tasa de referencia suba. Financia proyectos de largo plazo: una planta, una expansión, una adquisición. Lo compran los mismos inversionistas institucionales que el Bono M (Afores/Siefores, aseguradoras, fondos de deuda), atraídos por el rendimiento adicional (spread) sobre la deuda gubernamental del mismo plazo, que compensa el riesgo de crédito que el bono corporativo sí carga.

Además del emisor, el plazo y la mecánica de pago, un bono lleva consigo un **contrato de emisión** (*indenture*) con sus condiciones. Tres cláusulas típicas, según la describen los textos estadounidenses, son:

- **Rescatable (*callable*):** el emisor tiene el derecho de recomprar el bono a un precio pactado, que suele bajar con el tiempo; a menudo hay un periodo inicial de protección en el que no puede hacerlo.
- **Fondo de amortización (*sinking fund*):** en vez de asumir la obligación de pagar todo el valor nominal al vencimiento, el emisor reparte esa obligación en el tiempo, recomprando cada año una fracción de los bonos en circulación a un precio pactado (la mecánica de amortización de la sección 2).
- **Subordinación de deuda (*debt subordination*):** para proteger a los tenedores, se puede limitar cuánta deuda adicional contrae el emisor, y garantizar que en una quiebra a los tenedores se les paga antes que a otra deuda, la deuda subordinada.

Cada emisión pacta las suyas en su prospecto; que un bono corporativo sea rescatable o no cambia su flujo, y por eso cambia su precio.

> Que el papel comercial sea a descuento y el bono corporativo sea con cupón no es una regla universal, es la mecánica que domina en México dado el plazo típico de cada uno; nada impide, en principio, un papel comercial con cupón o un bono corporativo a descuento. Lo que sí es constante es el emisor: una empresa privada en ambos casos, nunca el gobierno.

**Certificado bursátil (CEBUR): el instrumento híbrido.** Es el instrumento más flexible de los seis, y por eso la tabla de la sección 7 no le encuentra un análogo exacto en EUA: el bono corporativo y la nota de mediano plazo (*medium-term note*) se le acercan, pero ninguno cubre exactamente el mismo rango de casos. A diferencia de los cuatro instrumentos anteriores, no tiene un emisor ni un plazo fijos por diseño:

- **Lo puede emitir una empresa privada** (el caso más común) **o un gobierno estatal o municipal**, algo que ningún otro instrumento de esta unidad permite: el Bono M, el UDIBONO y el CETE son exclusivos del Gobierno Federal, y solo el gobierno federal, nunca un estado o municipio, los emite.
- **Puede pactarse a cualquier plazo**, desde certificados de corto plazo (que compiten directamente con el papel comercial) hasta certificados a varios años (que compiten con el bono corporativo).
- **Puede pagar bajo cualquiera de las tres mecánicas** de la sección 2: a descuento en emisiones cortas, cupón fijo, o cupón variable referenciado a TIIE.

Quién lo compra depende, otra vez, del diseño de cada emisión: uno colocado por oferta pública a plazo largo atrae al mismo tipo de inversionista institucional que un bono corporativo (Afores/Siefores, aseguradoras, fondos de deuda); uno de plazo corto atrae a los mismos compradores que un papel comercial (fondos de mercado de dinero, tesorerías corporativas); y uno colocado de forma privada, como el ejemplo del BCIE de la sección 5, se coloca directamente entre inversionistas institucionales calificados, la única audiencia que ese canal permite.

> **Ejemplo resuelto.** El certificado bursátil del Banco Centroamericano de Integración Económica (BCIE) presentado en la sección 5 clasifica así: emisor, un organismo financiero internacional que coloca en México (tratado como emisor privado para efectos de este curso, no es el Gobierno Federal mexicano); plazo, 3.5 años (mercado de capitales); mecánica de pago, cupón variable referenciado a TIIE de fondeo a 28 días más sobretasa, con amortización bullet.

### 7. Tres preguntas y los seis instrumentos lado a lado

Con lo visto en esta nota, cualquier instrumento de deuda queda caracterizado con tres preguntas:

1. **¿Quién emite?** Gobierno federal, empresa privada o, en el certificado bursátil, también un gobierno subnacional; en esta unidad, siempre deuda directa (sección 4).
2. **¿A qué plazo?** Corto (mercado de dinero) o largo (mercado de capitales), por el criterio de plazo de la Unidad 1.
3. **¿Cómo paga?** A descuento o con cupones periódicos, fijos o variables (sección 2).

| Instrumento          | ¿Quién emite?                  | ¿A qué plazo? | ¿Cómo paga?                              | ¿Cómo se coloca?                               | ¿Quién lo compra, sobre todo?                                                                           | Análogo en EUA                                                                                              |
| -------------------- | ------------------------------ | ------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| CETE                 | Gobierno federal               | Corto         | A descuento                              | Subasta primaria (Banxico)                     | Bancos y casas de bolsa, fondos de mercado de dinero, tesorerías corporativas, cetesdirecto             | Letra del Tesoro (Treasury bill)                                                                            |
| Bono M               | Gobierno federal               | Largo         | Cupón fijo                               | Subasta primaria (Banxico)                     | Afores/Siefores, aseguradoras, fondos de deuda, inversionistas extranjeros                              | Nota o bono del Tesoro (Treasury note o bond)                                                               |
| UDIBONO              | Gobierno federal               | Largo         | Cupón fijo real (en UDIs)                | Subasta primaria (Banxico)                     | Afores/Siefores y aseguradoras, por sus pasivos de largo plazo indexados a la inflación                 | Bono del Tesoro protegido contra la inflación (TIPS)                                                        |
| Bono corporativo     | Empresa privada                | Largo         | Cupón fijo o variable                    | Oferta pública (CNBV) o colocación privada     | Afores/Siefores, aseguradoras, fondos de deuda                                                          | Bono corporativo (corporate bond)                                                                           |
| Papel comercial      | Empresa privada                | Corto         | A descuento                              | Oferta pública bajo programa autorizado (CNBV) | Fondos de mercado de dinero, tesorerías corporativas                                                    | Papel comercial (commercial paper)                                                                          |
| Certificado bursátil | Empresa o gobierno subnacional | Corto o largo | A descuento, cupón fijo o cupón variable | Oferta pública (CNBV) o colocación privada     | Depende del diseño: institucional si es largo, mercado de dinero si es corto, calificados si es privado | Sin equivalente exacto; el más cercano es el bono corporativo o la nota de mediano plazo (medium-term note) |

Las primeras tres columnas responden las tres preguntas; la cuarta (canal de colocación) distingue el único emisor gubernamental (subasta vía Banxico) de los emisores privados o subnacionales (CNBV); la quinta (comprador típico) anticipa un patrón que se repite en toda la unidad: quien tiene pasivos de largo plazo compra deuda de largo plazo, y quien solo necesita estacionar efectivo compra deuda de corto plazo; la sexta ubica cada instrumento mexicano dentro de la taxonomía de instrumentos de deuda que usan los libros de texto del curso, mayormente centrados en el mercado estadounidense.

Esa quinta columna, en realidad, reparte nombres propios (Afores/Siefores, aseguradoras, fondos de deuda, tesorerías corporativas) dentro de los agentes económicos que [`0_activo_financiero.md`](../unidad1/0_activo_financiero.md#4-agentes-económicos-y-su-acceso-a-los-mercados) ya presentó en Unidad 1: Afores/Siefores, aseguradoras y fondos de deuda son la cara concreta de los **inversionistas institucionales** de esa tabla; las tesorerías corporativas que estacionan efectivo en CETES o papel comercial son la cara de corto plazo de las **grandes empresas**; los bancos y casas de bolsa que participan en la subasta son los mismos **bancos e intermediarios**; y cetesdirecto es el canal de acceso indirecto que esa tabla ya reservaba para las **personas físicas**.

---

## Fuentes y referencias recomendadas

- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press: definición de instrumento de renta fija y de valor negociable; taxonomía de instrumentos de deuda estadounidenses (depósitos, mercado de dinero, valores del gobierno, otros bonos, hipotecas y anualidades) usada como análogo de los instrumentos mexicanos; cláusulas del contrato de emisión de un bono.
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson: los dos criterios de clasificación de mercados financieros (deuda y capital; dinero y capitales); los cuatro tipos de instrumento de crédito según su flujo (préstamo simple, préstamo de pago fijo amortizado, bono con cupón, bono a descuento); función económica del mercado de deuda de corto y largo plazo, y su mecánica de colocación y negociación; CETES y papel comercial como instrumentos de mercado de dinero, Bono M, UDIBONO, bono corporativo y certificado bursátil como instrumentos de mercado de capitales.
- Fabozzi, F. J. (2009). *Capital Markets, Financial Management, and Investment Management*. Wiley: vocabulario de valor nominal, cupón y plazo; cupón variable y estructura de amortización del principal; el flujo de un bono como vector; estructura de bonos corporativos y papel comercial usada como análogo de los instrumentos mexicanos.
- Banco de México: ficha técnica y mecánica de CETES, Bonos M, UDIBONOS y Bondes; resultados de subasta de valores gubernamentales y calendario de subastas; operaciones de mercado abierto como instrumento de política monetaria; tenencia de valores gubernamentales por sector tenedor (bancos, Afores/Siefores, aseguradoras, fondos de inversión, extranjeros), usada como base para el comprador típico de cada instrumento gubernamental; consultado el 21 de septiembre de 2026 para las tasas citadas (subasta del 15 de septiembre y tablas de cetesdirecto del 21 de septiembre).
- Portal BMV: manuales operativos y sección educativa sobre el funcionamiento del mercado secundario, la liquidez de los instrumentos y la estructura de emisiones corporativas (certificados bursátiles) y gubernamentales; prospectos de colocación de certificados bursátiles y programas de papel comercial (ejemplo del BCIE).
- Portal cetesdirecto: características de cada instrumento gubernamental para el pequeño inversionista.
- Manuales para inversionistas de casas de bolsa e instituciones financieras (por ejemplo, BBVA y Skandia): perfil de riesgo conservador, mecánica de pago de cupón (fijo, variable o real) y derechos legales del tenedor de deuda frente al accionista (prioridad de cobro).

---

## Cierre de la unidad — Lo esencial para recordar

- Un **instrumento de deuda (renta fija)** promete un flujo de efectivo fijo, salvo variaciones por contingencias bien definidas como una tasa de referencia; si además se negocia en un mercado desarrollado, es un **valor negociable**. Depósitos a plazo, hipotecas y anualidades quedan fuera de esta unidad: no se negocian como valores.
- Se caracteriza por dos decisiones de diseño independientes: cómo paga interés (**a descuento**, **cupón fijo** o **cupón variable**) y cómo liquida el capital (**bullet** o **con amortización**, en sistema francés o alemán). En números, es un **vector de flujos** $(c_0, c_1, \ldots, c_N)$ con $c_0=-a$ (el capital pagado, que coincide con el valor presente $v_0$ solo al emitir); los seis instrumentos de esta unidad son todos bullet.
- Frente a la **participación de capital** (flujo residual, cobra al final, con voto, sin horizonte), la deuda tiene flujo fijo, prelación, sin control y horizonte definido. Del lado de la deuda, se puede pedir **directamente** al mercado (el inversionista asume el riesgo) o **indirectamente** a un banco (el banco lo absorbe y cobra un margen); los seis instrumentos son deuda directa.
- El Gobierno Federal coloca su deuda en **subasta primaria** (vía Banxico y los Formadores de Mercado); una empresa la coloca por **oferta pública** (autorizada por la CNBV) o **colocación privada**; después, casi todo se revende en un mercado secundario de **mostrador**, con precio de referencia diario de un **proveedor de precios**.
- Los seis instrumentos se clasifican con las mismas tres preguntas: quién emite, a qué plazo, y cómo paga. Los gubernamentales (**CETE**, **Bono M**, **UDIBONO**) comparten emisor y canal, y el plazo decide la mecánica; los corporativos (**papel comercial**, **bono corporativo**) también; el **certificado bursátil** es el más flexible y no tiene análogo exacto en EUA. Quien tiene pasivos de largo plazo compra deuda de largo plazo, y quien solo estaciona efectivo compra deuda de corto plazo.

**Próxima sesión:** cómo se calcula el precio de cada uno de estos instrumentos a partir de sus flujos y su valor nominal.
