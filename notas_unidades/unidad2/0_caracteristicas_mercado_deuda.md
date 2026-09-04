# Unidad 2 · Características del Mercado de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante distinga las características del mercado de deuda (quién emite, a qué plazo y cómo paga) frente a las de otros mercados financieros.

## Contenido

|     | Tema                                                            | Qué cubre                                                                                                                                                                    |
| --- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I   | Introducción institucional y funcional al mercado de deuda      | Para qué existe el mercado de deuda, cómo se coloca (subasta gubernamental, oferta pública, colocación privada) y dónde se negocia después                                   |
| II  | Qué es un instrumento de deuda                                  | Vocabulario común: capital, cupón, valor nominal, plazo; las mecánicas de pago (descuento, cupón fijo, cupón variable) y de amortización de capital (bullet vs. amortizable) |
| III | El mercado de deuda frente a otros mercados financieros         | Plazo (Unidad 1) y tipo de promesa de pago (Unidades 2-3): dos criterios distintos                                                                                           |
| IV  | Tres preguntas para caracterizar cualquier instrumento de deuda | Quién emite, a qué plazo, cómo paga: vista previa de los 6 instrumentos mexicanos y su análogo en EUA                                                                        |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. Introducción institucional y funcional al mercado de deuda

La Unidad 1 ya explicó la mecánica que comparte cualquier instrumento bursátil: mercado primario y secundario, casas de bolsa como intermediario, Indeval como custodio ([`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md)). Esta sección no repite esa mecánica general, la especializa al mercado de deuda: quién coloca deuda y por qué, y cómo cambia el canal de colocación según quién emite.

El mercado de deuda cumple dos funciones económicas distintas, y esa función es justamente el criterio de plazo de la Unidad 1 ([`0_activo_financiero.md`](../unidad1/0_activo_financiero.md#3-mercado-de-dinero-y-mercado-de-capitales)):

- **Mercado de dinero (corto plazo):** administra necesidades de liquidez inmediata. El Gobierno Federal cubre faltantes temporales de caja entre lo que recauda y lo que gasta; una empresa financia capital de trabajo (nómina, inventario) sin comprometerse a un plazo largo. Banxico, además, usa este mismo mercado como herramienta de política monetaria: compra y vende CETES a los bancos en **operaciones de mercado abierto** para inyectar o retirar liquidez del sistema bancario y así mantener su tasa de referencia en el nivel que decide.
- **Mercado de capitales, en su vertiente de deuda (largo plazo):** financia proyectos que tardan años en pagarse solos. El Gobierno Federal financia déficit presupuestal plurianual; una empresa financia una planta, una expansión o una adquisición.

Quién emite determina el canal de colocación primaria:

- **Deuda gubernamental:** Banxico, como agente financiero del Gobierno Federal, coloca CETES, Bonos M y UDIBONOS (y también Bondes, un cuarto instrumento de cupón variable que existe en el mismo mercado pero que esta unidad no cubre a fondo) en una **subasta primaria** semanal (con calendario público), a la que solo pueden postular directamente los **Formadores de Mercado**, un grupo de bancos y casas de bolsa autorizados; el resto de los inversionistas participa a través de ellos.
- **Deuda corporativa:** una empresa coloca papel comercial, bonos corporativos o certificados bursátiles de dos formas. La **oferta pública** requiere autorización de la CNBV, prospecto de colocación y una casa de bolsa que la suscriba (underwriting, ver [`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md#2-quién-interviene-bmv-biva-casas-de-bolsa-indeval)); la **colocación privada** se coloca directamente entre inversionistas institucionales calificados, sin oferta pública, lo que la hace más rápida y barata pero también menos líquida en el secundario.

> **Ejemplo resuelto.** El Banco Centroamericano de Integración Económica (BCIE) colocó en 2026 un certificado bursátil de hasta \$3,000 millones de pesos a un plazo de 3.5 años, con cupón cada 28 días referenciado a la TIIE de fondeo a 28 días más una sobretasa, y amortización bullet (todo el capital en un solo pago) al vencimiento en 2029. Es exactamente el canal de colocación privada/institucional: no es una subasta gubernamental ni una oferta pública al gran público inversionista.

Colocada la deuda, el mercado secundario donde se revende es mayoritariamente de mostrador (over the counter), como documentan los propios manuales operativos de la BMV: bancos y casas de bolsa negocian entre sí en sus mesas de dinero, no en un libro de órdenes público como el de una acción en la bolsa. Esos mismos manuales son donde la BMV documenta qué tan líquido es cada instrumento, un punto que se retoma a fondo como riesgo de liquidez en [`3_riesgos_mercado_deuda.md`](3_riesgos_mercado_deuda.md#4-riesgo-de-liquidez). Para que ese mercado disperso tenga un precio de referencia diario, existen **proveedores de precios** (empresas especializadas, autorizadas por la CNBV) que publican el precio de valuación de cada instrumento en circulación; ese precio es el insumo que un banco o una Siefore usa para valorar su portafolio de deuda todos los días, y el punto de partida de la valuación que se estudia en [`2_valuacion_instrumentos_deuda.md`](2_valuacion_instrumentos_deuda.md).

Dos cifras ilustran el tamaño y la forma de este mercado a inicios de septiembre de 2026: en la subasta del 1 de septiembre, el CETE a 28 días rindió 6.49%, prácticamente igual a la tasa de referencia de Banxico (6.50%) porque es casi el mismo plazo que decide la política monetaria; el Bono M a 10 años, en cambio, cotizaba en el mercado secundario en un rango de 8.5%-9.3% durante 2026, muy por encima de la tasa de corto plazo, porque un inversionista exige más rendimiento por comprometer su dinero una década en vez de 28 días.

### 2. Qué es un instrumento de deuda

Un **instrumento de deuda** (también llamado de **renta fija**) es un flujo de efectivo fijo salvo por variaciones debidas a circunstancias contingentes bien definidas, como un cupón indexado a una tasa de referencia: el emisor promete ese calendario de pagos (determinístico o no), y el instrumento no es más que ese flujo.

Recordemos el vocabulario que adoptamos para instrumentos de deuda:

- **Capital (principal, $v_0$):** el monto originalmente prestado; es el mismo $v_0$ al momento de la emisión, no el cupón ($c$).
- **Valor nominal ($v_N$):** el monto de referencia sobre el que se calculan los pagos, y el monto que se liquida al vencimiento.
- **Cupón ($c$):** el pago periódico de interés que promete el emisor. La **tasa cupón** es ese pago expresado como porcentaje del valor nominal.
- **Plazo (vencimiento):** la fecha en que el emisor debe liquidar el valor nominal, junto con el último cupón si lo hay.

Con ese vocabulario, cualquier instrumento de deuda se caracteriza por dos decisiones de diseño independientes: cómo paga interés y cómo liquida el capital.

**Cómo paga interés**, según Mishkin hay tres mecánicas:

- **A descuento (o cupón cero):** no paga ningún cupón. Se compra por debajo del valor nominal y se cobra el valor nominal completo al vencimiento; la ganancia es esa diferencia.
- **Con cupones periódicos, cupón fijo:** paga el mismo cupón $c$ cada periodo, pactado desde la emisión.
- **Con cupones periódicos, cupón variable (flotante):** paga un cupón que se recalcula cada periodo según una tasa de referencia vigente (típicamente la TIIE), así que a diferencia de las otras dos mecánicas, no es completamente determinístico: el cupón más próximo suele estar ya fijo (se determinó en el último reseteo), pero los siguientes dependen de una tasa que todavía no se conoce.

**Cómo liquida el capital**, hay dos mecánicas:

- **Bullet:** todo el valor nominal se liquida de golpe, junto con el último cupón si lo hay. Es la mecánica de los seis instrumentos mexicanos de esta unidad.
- **Con amortización de capital:** el capital se reparte en abonos antes del vencimiento (sistema francés, sistema alemán, fondo de amortización o *sinking fund*), como un crédito hipotecario o un préstamo de auto. Ningún instrumento de esta unidad usa esta mecánica, pero conviene nombrarla porque Fabozzi la documenta como otra característica más de los bonos, y porque cierra los cuatro tipos de instrumento de crédito de Mishkin.

Las fórmulas de precio de cada una de estas mecánicas (a partir del valor presente de un flujo único y de la anualidad de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md)) se calculan a fondo, con datos reales de mercado, en [`2_valuacion_instrumentos_deuda.md`](2_valuacion_instrumentos_deuda.md).

> **Ejemplo resuelto.** Un CETE a 28 días con valor nominal \$10 se compra hoy en \$9.95 y no paga nada más hasta el vencimiento, cuando el gobierno paga los \$10 completos: es a descuento, bullet, la ganancia es \$0.05 (el precio exacto, a partir de la tasa de la subasta, se calcula en [`2_valuacion_instrumentos_deuda.md`](2_valuacion_instrumentos_deuda.md#1-valuación-a-descuento)). Un Bono M paga una tasa cupón fija cada seis meses durante toda su vida, más el valor nominal el día del vencimiento: es cupón fijo, bullet. El certificado bursátil del BCIE del ejemplo anterior también paga cupones periódicos, pero de cupón variable referenciado a la TIIE de fondeo: cada cupón depende de la tasa vigente ese periodo, no de una tasa fija pactada desde la emisión, aunque también liquida el capital bullet.

*Fuente: Luenberger, D. G. (2013). Investment Science (2ª ed.). Oxford University Press. Cap. 3, "Fixed-Income Securities", pp. 42-43: definición de instrumento de deuda como flujo de efectivo. Mishkin, F. S. y Eakins, S. G. (2014). Financial Markets and Institutions (8ª ed.). Pearson. Cap. 3, "What Do Interest Rates Mean and What Is Their Role in Valuation?", "Four Types of Credit Market Instruments", p. 39. Fabozzi, F. J. (2009). Capital Markets, Financial Management, and Investment Management. Wiley. Cap. 19, "Bond Portfolio Management", "Features of Bonds", "Coupon Rate" y "Provisions for Paying off Bonds", pp. 681-685.*

### 3. El mercado de deuda frente a otros mercados financieros

"Frente a qué otro mercado" depende de qué criterio se use para dividir los mercados financieros, y este curso usa dos criterios distintos que no hay que confundir:

| Criterio                    | Divide en...                                                              | Dónde se estudia                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Plazo**                   | Mercado de dinero (≤ 1 año) / Mercado de capitales (> 1 año)              | Unidad 1, [`0_activo_financiero.md`](../unidad1/0_activo_financiero.md#3-mercado-de-dinero-y-mercado-de-capitales) |
| **Tipo de promesa de pago** | Mercado de deuda (renta fija) / Mercado de participación (renta variable) | Unidades 2 y 3 (esta nota y las siguientes)                                                                        |

El segundo criterio es el que separa esta unidad de la de participación de capital: un instrumento de deuda promete, desde la emisión, un monto que no depende de cómo le vaya al negocio (aunque el emisor pueda incumplir, ver riesgo de crédito en [`3_riesgos_mercado_deuda.md`](3_riesgos_mercado_deuda.md)); una acción, una FIBRA, un CKD o un CERPI no prometen ningún monto fijo, su pago depende del desempeño del negocio o los proyectos que respaldan.

Esa promesa fija también le da al tenedor de deuda una **prioridad de cobro** frente al accionista, un derecho que los manuales para inversionistas de las propias casas de bolsa (BBVA, Skandia) explican al comparar ambos instrumentos: si el emisor se liquida, primero se paga a los acreedores (tenedores de deuda) y solo si sobra algo después de cubrirlos a todos, el accionista tiene derecho al remanente. Por esas dos razones (monto prometido fijo y prioridad de cobro), la deuda se considera una inversión de riesgo conservador frente a la acción.

> **Cuidado con el nombre.** La Unidad 3 de este curso se llama "Mercado de Capitales", pero ahí ese nombre usa el segundo criterio (solo instrumentos de participación: acciones, FIBRAs, CKD, CERPIs), no el de plazo de la Unidad 1. Un Bono M es "mercado de capitales" por su plazo largo (Unidad 1) pero sigue siendo mercado de deuda, no mercado de capitales en el sentido de la Unidad 3. En estas notas, "mercado de capitales" sin calificar siempre usa el criterio de plazo (Unidad 1); al segundo criterio se le llama aquí **mercado de participación** o **mercado accionario**, precisamente para no chocar con el nombre de la Unidad 3.
>
> **Ejemplo resuelto.** Un Bono M a 10 años: por plazo (Unidad 1) es mercado de capitales; por tipo de promesa de pago (esta unidad) es mercado de deuda, porque paga un cupón fijo pactado desde la emisión. Los dos criterios conviven sin contradecirse, solo responden preguntas distintas.

*Fuente: Mishkin, F. S. y Eakins, S. G. (2014). Financial Markets and Institutions (8ª ed.). Pearson. Cap. 2, "Overview of the Financial System", "Debt and Equity Markets", p. 18 y "Money and Capital Markets", p. 20.*

### 4. Tres preguntas para caracterizar cualquier instrumento de deuda

Con el vocabulario de la sección 2 y los dos criterios de la sección 3, cualquier instrumento de deuda queda caracterizado con tres preguntas:

1. **¿Quién emite?** Gobierno federal, empresa privada, o un intermediario financiero (deuda directa o indirecta, Unidad 1).
2. **¿A qué plazo?** Corto (mercado de dinero) o largo (mercado de capitales), por el criterio de plazo de la Unidad 1.
3. **¿Cómo paga?** A descuento o con cupones periódicos, fijos o variables (sección 2 de esta nota).

| Instrumento          | ¿Quién emite?      | ¿A qué plazo? | ¿Cómo paga?                                          | Análogo en EUA                                                                 |
| -------------------- | ------------------ | ------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------ |
| CETE                 | Gobierno federal   | Corto         | A descuento                                          | Treasury bill                                                                  |
| Bono M               | Gobierno federal   | Largo         | Cupones periódicos, cupón fijo                       | Treasury note / Treasury bond                                                  |
| UDIBONO              | Gobierno federal   | Largo         | Cupones periódicos, cupón fijo (en UDIs)             | Treasury Inflation-Protected Securities (TIPS)                                 |
| Bono corporativo     | Empresa privada    | Largo         | Cupones periódicos, fijos o variables                | Corporate bond                                                                 |
| Papel comercial      | Empresa privada    | Corto         | A descuento                                          | Commercial paper                                                               |
| Certificado bursátil | Empresa o gobierno | Corto o largo | Cupones periódicos (o descuento en emisiones cortas) | Sin equivalente exacto; el más cercano es el corporate bond / medium-term note |

La columna "Análogo en EUA" ubica cada instrumento mexicano dentro de la taxonomía de instrumentos de deuda que usan los libros de texto del curso, mayormente centrados en el mercado estadounidense.

> Esta tabla es solo una vista previa: la siguiente nota, [`1_instrumentos_deuda.md`](1_instrumentos_deuda.md), responde estas tres preguntas a fondo para cada uno de estos seis instrumentos, incluyendo por qué UDIBONO y Bono M pagan distinto aunque comparten emisor y plazo.

---

## Fuentes y referencias recomendadas

- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 2, "Overview of the Financial System", "Debt and Equity Markets" (p. 18) y "Money and Capital Markets" (p. 20): los dos criterios de clasificación de mercados financieros. Cap. 11, "The Money Markets" y Cap. 12, "The Bond Market": función económica del mercado de deuda de corto y largo plazo, y su mecánica de colocación y negociación.
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 3, "What Do Interest Rates Mean and What Is Their Role in Valuation?", "Four Types of Credit Market Instruments", p. 39: los cuatro tipos de instrumento de crédito según su flujo (préstamo simple, préstamo de pago fijo amortizado, bono con cupón, bono a descuento).
- Fabozzi, F. J. (2009). *Capital Markets, Financial Management, and Investment Management*. Wiley. Cap. 19, "Bond Portfolio Management", "Features of Bonds", p. 679: vocabulario de valor nominal, cupón y plazo. "Coupon Rate" y "Provisions for Paying off Bonds", pp. 681-685: cupón variable/flotante y estructura de amortización del principal.
- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press. Cap. 3, "Fixed-Income Securities", pp. 42-46: definición de instrumento de deuda como flujo de efectivo (p. 42) y taxonomía de instrumentos de deuda estadounidenses usada como análogo de los instrumentos mexicanos ("The Market for Future Cash", pp. 43-46).
- Banco de México: ficha técnica y mecánica de CETES, Bonos M, UDIBONOS y Bondes; resultados de subasta de valores gubernamentales y calendario de subastas; operaciones de mercado abierto como instrumento de política monetaria; consultado el 3 de septiembre de 2026 para las tasas citadas en la sección 1.
- Portal BMV: manuales operativos y sección educativa sobre el funcionamiento del mercado secundario, la liquidez de los instrumentos y la estructura de emisiones corporativas (certificados bursátiles) y gubernamentales; prospectos de colocación (ejemplo del BCIE citado en la sección 1).
- Manuales para inversionistas de casas de bolsa e instituciones financieras (por ejemplo, BBVA y Skandia): perfil de riesgo conservador, mecánica de pago de cupón (fijo, variable o real) y derechos legales del tenedor de deuda frente al accionista (prioridad de cobro).

---

## Cierre de la unidad — Lo esencial para recordar

- El mercado de deuda financia **liquidez de corto plazo** (mercado de dinero) o **proyectos de largo plazo** (mercado de capitales); el Gobierno Federal coloca su deuda en **subasta primaria** (vía Banxico y los Formadores de Mercado), una empresa la coloca por **oferta pública** (autorizada por la CNBV) o **colocación privada** (más rápida, menos líquida); después, casi todo se revende en un mercado secundario de **mostrador**, con precio de referencia diario de un **proveedor de precios**.
- Un **instrumento de deuda (renta fija)** se caracteriza por dos decisiones de diseño independientes: cómo paga interés (**a descuento**, **cupón fijo** o **cupón variable**) y cómo liquida el capital (**bullet**, todo de golpe al vencimiento, o **con amortización de capital**, repartido antes). Los seis instrumentos de esta unidad son todos bullet.
- **Plazo** (Unidad 1: mercado de dinero/capitales) y **tipo de promesa de pago** (esta unidad: mercado de deuda/participación) son dos criterios independientes; un instrumento de deuda puede caer en cualquiera de los dos plazos. Esa promesa fija también le da al tenedor de deuda **prioridad de cobro** sobre el accionista si el emisor se liquida.
- "Mercado de capitales" tiene dos usos en este curso: por plazo (Unidad 1, incluye deuda larga como el Bono M) y por tipo de instrumento (nombre de la Unidad 3, solo participación). No son lo mismo.
- Cualquier instrumento de deuda se caracteriza con tres preguntas: quién emite, a qué plazo, y cómo paga.

**Próxima sesión:** instrumentos concretos del mercado de deuda mexicano (CETES, Bonos M, UDIBONOS, bonos corporativos, papel comercial, certificados bursátiles), respondiendo estas tres preguntas para cada uno.
