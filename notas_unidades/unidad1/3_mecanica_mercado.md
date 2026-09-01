# Unidad 1 · Mecánica Operativa del Mercado

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante trace el recorrido institucional de un instrumento en el mercado bursátil mexicano (mercado primario/secundario, custodia en Indeval, intermediación de casas de bolsa, BMV/BIVA), ubique el papel de las calificadoras en su riesgo de crédito, y reconozca el equivalente funcional de cada institución en el mercado estadounidense.

## Contenido

|     | Tema                                                 | Qué cubre                                                  |
| --- | ---------------------------------------------------- | ---------------------------------------------------------- |
| I   | Mercado primario vs. mercado secundario              | Quién recibe el dinero en cada uno                         |
| II  | Quién interviene: BMV, BIVA, casas de bolsa, Indeval | Bolsas, intermediarios bursátiles, custodia y liquidación  |
| III | Calificadoras y riesgo de crédito                    | S&P, Moody's, HR Ratings, Fitch; a qué instrumentos aplica |
| IV  | El análogo estadounidense                            | Equivalente funcional de cada institución en EE. UU.       |

> La práctica de este tema (taller) está en [`practica_unidad1.md`](../../practicas/unidad1/practica_unidad1.md).

---

### 1. Mercado primario vs. mercado secundario

- **Mercado primario**: la primera vez que un instrumento se coloca. Ejemplo: Banxico subasta CETES; una empresa hace su oferta pública inicial (OPI) de acciones.
- **Mercado secundario**: la reventa del instrumento entre inversionistas después de esa colocación inicial. El emisor ya no recibe dinero en estas operaciones; solo cambia de manos el título.

### 2. Quién interviene: BMV, BIVA, casas de bolsa, Indeval

- **BMV y BIVA**: las dos bolsas de valores en México, donde se negocian acciones, bonos y otros instrumentos listados.
- **Casas de bolsa**: intermediarios bursátiles; un inversionista no puede operar directamente en la bolsa, necesita una casa de bolsa que ejecute la orden. Ejemplos en México: GBM, Actinver, Kuspit, Vector y Banorte Casa de Bolsa. También son quienes colocan (*underwrite*) una emisión nueva en el mercado primario: le garantizan un precio al emisor y luego revenden el título al público. Dentro de esa función hay dos papeles distintos:
  - **De corretaje**: conecta comprador y vendedor, cobra comisión, nunca es dueña del título, como un agente inmobiliario.
  - **De distribuidor**: compra y vende por cuenta propia, gana el diferencial entre precio de compra y venta, como un agente de autos usados.
- **Indeval**: la institución de custodia y liquidación central. Cuando compras un instrumento, no recibes un papel físico: Indeval mantiene el registro electrónico de quién es dueño de qué, y liquida (hace efectiva) cada operación.

> El mercado organizado (bolsa, subasta pública) no es el único canal: también existe el mercado de mostrador (*over the counter*), donde bancos y casas de bolsa negocian entre sí sin publicar sus cotizaciones. De hecho, el mercado de deuda mueve más volumen que el de acciones y opera mayormente en mostrador: la bolsa es más visible, pero no es donde se negocia más.

### 3. Calificadoras y riesgo de crédito

- Empresas como **S&P, Moody's, HR Ratings o Fitch** evalúan la capacidad de pago de quien emite deuda y le asignan una calificación (AAA, AA, BBB, etc.).
- Es central para instrumentos de deuda corporativa (papel comercial, certificados bursátiles, bonos corporativos) que se verán en la Unidad de Deuda; a diferencia de la deuda gubernamental, cuyo riesgo de crédito se asume mínimo.
- **Conflicto de interés**: quien le paga a la calificadora es el propio emisor que quiere colocar su deuda, no el inversionista que confía en la calificación para decidir. Eso crea un incentivo perverso: la calificadora compite por conservar clientes (emisores) que prefieren calificaciones favorables.

> **Ejemplo resuelto.** En la crisis financiera de 2007-2009, muchos instrumentos respaldados por hipotecas subprime tenían calificación AAA (la más alta) y terminaron degradados varias veces hasta quedar en categoría "basura" (*junk*). Como respuesta, la SEC exigió a las calificadoras separar el negocio de calificar del de asesorar en la estructuración de esos mismos instrumentos.

### 4. El análogo estadounidense

Conviene ubicar qué institución cumple cada función en el mercado más grande del mundo, el de Estados Unidos.

| Función                           | México                          | Estados Unidos                                 |
| --------------------------------- | ------------------------------- | ---------------------------------------------- |
| Bolsa de valores                  | BMV, BIVA                       | NYSE, Nasdaq                                   |
| Intermediario bursátil            | Casa de bolsa                   | Broker-dealer                                  |
| Custodia y liquidación central    | Indeval                         | DTCC (Depository Trust & Clearing Corporation) |
| Calificadora de riesgo crediticio | S&P, Moody's, HR Ratings, Fitch | S&P, Moody's, Fitch                            |
| Regulador del mercado de valores  | CNBV                            | SEC                                            |

> Las calificadoras globales (S&P, Moody's, Fitch) no tienen "equivalente": son las mismas firmas operando en ambos países. HR Ratings sí es una calificadora local, sin presencia en EE. UU. La mecánica es la misma en ambos mercados (primario/secundario, intermediario, custodio), lo que cambia es el nombre de la institución que cumple cada función.
>
> Ni siquiera "bolsa de valores" es una sola mecánica: NYSE es un mercado **dirigido por órdenes** (los precios los fijan las órdenes de compra/venta del público, con un especialista que ordena el libro), mientras que Nasdaq es **dirigido por cotizaciones** (varios *market makers* cotizan precio de compra y venta, y el inversionista opera contra esas cotizaciones). La BMV se parece más al primero.
>
> **Addendum: más allá de NYSE y Nasdaq.** El mercado accionario estadounidense ya no se limita a dos bolsas. Los **dark pools** son plataformas privadas donde se negocian bloques grandes de acciones sin publicar cotizaciones, para no mover el precio antes de completar la operación; los **ECN** (*electronic communication networks*) son redes electrónicas que cruzan órdenes de compra y venta directamente, fuera de la bolsa tradicional. El **NBBO** (*National Best Bid and Offer*) obliga a que toda orden se ejecute al mejor precio disponible entre *todas* las plataformas, no solo en la que recibió la orden. Gran parte de ese cruce de órdenes hoy lo hace **trading algorítmico**, en microsegundos. México no tiene un equivalente de esta fragmentación: BMV y BIVA concentran prácticamente toda la negociación.

---

## Fuentes y referencias recomendadas

- Mántey de Anguiano, G. (2024). *Lecciones de Economía Monetaria*. UNAM. Lección 2, §4 "Componentes del mercado financiero": mercado primario/secundario, mercado organizado (bolsa) vs. de mostrador (OTC).
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 2, "Overview of the Financial System", pp. 18-19: mercado primario/secundario, bolsas vs. mercado de mostrador; Cap. 22, "Investment Banks, Security Brokers and Dealers, and Venture Capital Firms", pp. 546-547: bróker vs. dealer, colocación de emisiones; Cap. 7, mini-caso "Credit Rating Agencies and the 2007–2009 Financial Crisis", pp. 157-158: conflicto de interés en el modelo emisor-paga.
- Fabozzi, F. J. y Peterson Drake, P. (2009). *Finance*. Wiley. Cap. 18, "Equity Portfolio Management", pp. 646-664: estructura de los mercados accionarios, bolsas vs. mercado de mostrador, mecánica de trading.
- Portal Banxico: subastas de valores gubernamentales y resultados de CETES/Bonos M.
- Portal Indeval (S.D. Indeval): qué es la custodia y liquidación de valores.
- Portal BMV / BIVA: cómo funciona el mercado secundario en México.
- Portal DTCC (Depository Trust & Clearing Corporation): custodia y liquidación en el mercado estadounidense, el análogo de Indeval.

---

## Cierre de la unidad — Lo esencial para recordar

- Todo instrumento nace en el **mercado primario** (el emisor recibe el dinero) y, si es líquido, se revende después en el **secundario** (el emisor ya no recibe nada).
- Un inversionista no opera directamente en la bolsa: necesita una **casa de bolsa**; **Indeval** es quien realmente custodia y liquida el título, no el propio inversionista.
- Las **calificadoras** (S&P, Moody's, HR Ratings, Fitch) evalúan el riesgo de crédito de la deuda corporativa, cobrándole al propio emisor que califican, lo que genera un conflicto de interés evidenciado en la crisis de 2008; la deuda gubernamental se asume de riesgo mínimo y no se califica de la misma forma.
- La mecánica se repite en cualquier país, solo cambia el nombre de la institución: en EE. UU., NYSE/Nasdaq hacen de BMV/BIVA, el broker-dealer hace de casa de bolsa, y DTCC hace de Indeval.
