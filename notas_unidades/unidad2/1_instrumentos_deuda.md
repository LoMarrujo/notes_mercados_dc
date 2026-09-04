# Unidad 2 · Instrumentos de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante clasifique un instrumento de deuda (CETES, Bonos gubernamentales, UDIBONOS, Bonos corporativos, Papel comercial, Certificados bursátiles) según su emisor y su mecánica de pago.

## Contenido

|     | Tema                                                          | Qué cubre                                                                                     |
| --- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| I   | Instrumentos gubernamentales: CETES, Bono M y UDIBONO         | Mismo emisor y canal de colocación, tres mecánicas de pago distintas                          |
| II  | Instrumentos corporativos: bono corporativo y papel comercial | Mismo emisor, distinto plazo y por eso distinta mecánica de pago                              |
| III | Certificado bursátil: el instrumento híbrido                  | Por qué no tiene análogo exacto en EUA: lo puede emitir empresa o gobierno, a cualquier plazo |
| IV  | Los seis instrumentos lado a lado                             | Comparativo final por emisor, plazo, mecánica de pago y canal de colocación                   |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. Instrumentos gubernamentales: CETES, Bono M y UDIBONO

Los tres los emite el Gobierno Federal y los coloca Banxico como su agente financiero, en la misma subasta primaria semanal descrita en [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#1-introducción-institucional-y-funcional-al-mercado-de-deuda). Comparten emisor y canal de colocación; lo que los distingue es el plazo y la mecánica de pago.

**CETES (Certificados de la Tesorería):** mercado de dinero, a plazos de 28, 91, 182 y 364 días. Pagan a descuento: no llevan cupón, se colocan por debajo de su valor nominal de \$10 y liquidan el valor nominal completo al vencimiento. Financian el faltante de caja de corto plazo del Gobierno Federal. En la subasta del 1 de septiembre de 2026 rindieron 6.49% a 28 días y 7.00% a 350 días, casi la misma tasa de referencia de Banxico (6.50%) en el extremo corto de la curva.

**Bono M:** mercado de capitales, a plazos de 3, 5, 10, 20 y 30 años. Pagan un cupón fijo cada 182 días, pactado en pesos nominales desde la emisión, más el valor nominal al vencimiento. Financian el déficit presupuestal plurianual del Gobierno Federal, y su tasa a 10 años es la referencia que el mercado sigue para juzgar el costo de financiamiento del gobierno a largo plazo (durante 2026, en un rango de 8.5%-9.3%).

**UDIBONO (Bono de Desarrollo del Gobierno Federal denominado en UDIs):** mismo emisor y plazos largos que el Bono M (3, 10, 20 y 30 años), pero su valor nominal está denominado en Unidades de Inversión (UDIs), no en pesos; el cupón fijo (también cada 182 días) es una **tasa real**, y tanto el cupón como el valor nominal al vencimiento se convierten a pesos multiplicando por el valor de la UDI vigente ese día. Como la UDI se ajusta con la inflación, quien compra un UDIBONO protege su poder adquisitivo, algo que el Bono M no ofrece: si la inflación sorprende al alza, el cupón fijo en pesos del Bono M pierde valor real, mientras que el cupón del UDIBONO se ajusta con la UDI.

> **Por qué UDIBONO y Bono M pagan distinto aunque comparten emisor y plazo.** La diferencia no es de riesgo de crédito (el mismo Gobierno Federal respalda a ambos), es de **qué tasa se pacta**: el Bono M pacta una tasa nominal fija sobre pesos; el UDIBONO pacta una tasa real fija sobre UDIs. Por eso la tasa cupón del Bono M (nominal) es mayor que la del UDIBONO (real): la diferencia aproxima la inflación que el mercado espera durante la vida del bono, más cualquier prima por la incertidumbre de esa inflación. En la subasta de junio de 2026, el UDIBONO a 10 años rindió una tasa real de 4.60% y el de 30 años, 4.29%; comparados contra el Bono M nominal del mismo plazo (secciones anteriores), la brecha da una idea de cuánta inflación espera el mercado a cada horizonte.

### 2. Instrumentos corporativos: bono corporativo y papel comercial

Ambos los emite una empresa privada, no el gobierno, y por lo tanto ambos requieren la autorización de la CNBV para su oferta pública (o califican para colocación privada) descrita en [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#1-introducción-institucional-y-funcional-al-mercado-de-deuda), y ambos están sujetos al riesgo de crédito del emisor que se calificó en [`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md#3-calificadoras-y-riesgo-de-crédito). Lo que los distingue es el plazo, y de ahí se sigue casi automáticamente la mecánica de pago.

**Papel comercial:** mercado de dinero, plazo corto (hasta 360 días, típicamente unas cuantas semanas). Suele pagar a descuento, igual que un CETE, porque a un plazo tan corto no vale la pena la complejidad administrativa de un cupón periódico. Financia capital de trabajo: nómina, inventario, cuentas por cobrar. Muchas empresas mantienen un **programa autorizado** vigente por varios años, bajo el cual reemiten papel comercial una y otra vez (revolvente) sin pedir una nueva autorización cada vez.

**Bono corporativo:** mercado de capitales, plazo largo (varios años). Paga cupones periódicos, fijos o variables (referenciados a TIIE), porque a un plazo largo el emisor prefiere un costo de financiamiento predecible o, si elige tasa variable, transferir al inversionista el riesgo de que la tasa de referencia suba. Financia proyectos de largo plazo: una planta, una expansión, una adquisición.

> Que el papel comercial sea a descuento y el bono corporativo sea con cupón no es una regla universal, es la mecánica que domina en México dado el plazo típico de cada uno; nada impide, en principio, un papel comercial con cupón o un bono corporativo a descuento. Lo que sí es constante es el emisor: una empresa privada en ambos casos, nunca el gobierno.

### 3. Certificado bursátil: el instrumento híbrido

El certificado bursátil (CEBUR) es el instrumento más flexible de los seis, y por eso la tabla comparativa de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#4-tres-preguntas-para-caracterizar-cualquier-instrumento-de-deuda) no le encontró un análogo exacto en EUA: el corporate bond y el medium-term note se le acercan, pero ninguno cubre exactamente el mismo rango de casos.

A diferencia de los cuatro instrumentos anteriores, el certificado bursátil no tiene un emisor ni un plazo fijos por diseño:

- **Lo puede emitir una empresa privada** (el caso más común) **o un gobierno estatal o municipal**, algo que ningún otro instrumento de esta unidad permite: el Bono M, el UDIBONO y el CETE son exclusivos del Gobierno Federal, y solo el gobierno federal, nunca un estado o municipio, los emite.
- **Puede pactarse a cualquier plazo**, desde certificados de corto plazo (que compiten directamente con el papel comercial) hasta certificados a varios años (que compiten con el bono corporativo).
- **Puede pagar bajo cualquiera de las tres mecánicas** de la sección 2 de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#2-qué-es-un-instrumento-de-deuda): a descuento en emisiones cortas, cupón fijo, o cupón variable referenciado a TIIE.

> **Ejemplo resuelto.** El certificado bursátil del Banco Centroamericano de Integración Económica (BCIE) presentado en la sección 1 de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#1-introducción-institucional-y-funcional-al-mercado-de-deuda) clasifica así: emisor, un organismo financiero internacional que coloca en México (tratado como emisor privado para efectos de este curso, no es el Gobierno Federal mexicano); plazo, 3.5 años (mercado de capitales); mecánica de pago, cupón variable referenciado a TIIE de fondeo a 28 días más sobretasa, con amortización bullet.

### 4. Los seis instrumentos lado a lado

| Instrumento          | ¿Quién emite?                  | ¿A qué plazo? | ¿Cómo paga?                              | ¿Cómo se coloca?                               |
| -------------------- | ------------------------------ | ------------- | ---------------------------------------- | ---------------------------------------------- |
| CETE                 | Gobierno federal               | Corto         | A descuento                              | Subasta primaria (Banxico)                     |
| Bono M               | Gobierno federal               | Largo         | Cupón fijo                               | Subasta primaria (Banxico)                     |
| UDIBONO              | Gobierno federal               | Largo         | Cupón fijo real (en UDIs)                | Subasta primaria (Banxico)                     |
| Bono corporativo     | Empresa privada                | Largo         | Cupón fijo o variable                    | Oferta pública (CNBV) o colocación privada     |
| Papel comercial      | Empresa privada                | Corto         | A descuento                              | Oferta pública bajo programa autorizado (CNBV) |
| Certificado bursátil | Empresa o gobierno subnacional | Corto o largo | A descuento, cupón fijo o cupón variable | Oferta pública (CNBV) o colocación privada     |

Esta tabla responde las tres preguntas de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#4-tres-preguntas-para-caracterizar-cualquier-instrumento-de-deuda) para cada instrumento, y agrega una cuarta columna (canal de colocación) que distingue el único emisor gubernamental (subasta vía Banxico) de los emisores privados o subnacionales (CNBV).

---

## Fuentes y referencias recomendadas

- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 11, "The Money Markets": CETES y papel comercial como instrumentos de mercado de dinero. Cap. 12, "The Bond Market": Bono M, UDIBONO, bono corporativo y certificado bursátil como instrumentos de mercado de capitales.
- Banco de México: ficha técnica de CETES, Bonos M y UDIBONOS (plazos, mecánica de pago, calendario de subastas); resultados de subasta consultados el 3 de septiembre de 2026 para las tasas citadas en la sección 1.
- Portal cetesdirecto: características de cada instrumento gubernamental para el pequeño inversionista.
- Portal BMV: prospectos de colocación de certificados bursátiles y programas de papel comercial (ejemplo del BCIE citado en la sección 3).
- Fabozzi, F. J. (2009). *Capital Markets, Financial Management, and Investment Management*. Wiley. Cap. 19, "Bond Portfolio Management": estructura de bonos corporativos y papel comercial usada como análogo de los instrumentos mexicanos.

---

## Cierre de la unidad — Lo esencial para recordar

- Los tres instrumentos gubernamentales (**CETE**, **Bono M**, **UDIBONO**) comparten emisor y canal de colocación (subasta primaria vía Banxico); el plazo decide la mecánica de pago: **CETE** a descuento (corto plazo), **Bono M** cupón fijo nominal (largo plazo), **UDIBONO** cupón fijo real en UDIs (largo plazo, protegido de la inflación).
- Los dos instrumentos corporativos (**papel comercial**, **bono corporativo**) comparten emisor (empresa privada) y canal (CNBV); el plazo también decide la mecánica: corto plazo y a descuento el papel comercial, largo plazo y con cupón el bono corporativo.
- El **certificado bursátil** es el más flexible de los seis: lo puede emitir una empresa o un gobierno subnacional, a cualquier plazo, bajo cualquier mecánica de pago, por lo que no tiene un análogo exacto en el mercado estadounidense.
- Cualquiera de los seis se clasifica con las mismas tres preguntas de la nota anterior: quién emite, a qué plazo, y cómo paga.

**Próxima sesión:** cómo se calcula el precio de cada uno de estos instrumentos a partir de sus flujos y su valor nominal.
