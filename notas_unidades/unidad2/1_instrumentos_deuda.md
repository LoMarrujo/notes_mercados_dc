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
| IV  | Los seis instrumentos lado a lado                             | Comparativo final por emisor, plazo, mecánica de pago, canal de colocación y comprador típico |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. Instrumentos gubernamentales: CETES, Bono M y UDIBONO

Con las tres preguntas de la nota anterior en mano (quién emite, a qué plazo, cómo paga), toca aplicarlas a los seis instrumentos concretos de este mercado, empezando por los tres que comparten emisor. Los emite el Gobierno Federal y los coloca Banxico como su agente financiero, en la misma subasta primaria semanal descrita en [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda). Comparten emisor y canal de colocación; lo que los distingue es el plazo y la mecánica de pago.

**CETES (Certificados de la Tesorería):** mercado de dinero, a plazos de 28, 91, 182 y 364 días. Pagan a descuento: no llevan cupón, se colocan por debajo de su valor nominal de \$10 y liquidan el valor nominal completo al vencimiento. Financian el faltante de caja de corto plazo del Gobierno Federal. En la subasta del 1 de septiembre de 2026 rindieron 6.49% a 28 días y 7.00% a 350 días, casi la misma tasa de referencia de Banxico (6.50%) en el extremo corto de la curva. Lo compran, sobre todo, bancos y casas de bolsa en la propia subasta (los Formadores de Mercado), que después lo revenden a fondos de inversión de mercado de dinero y a tesorerías corporativas que estacionan ahí su efectivo de corto plazo; el pequeño inversionista también puede comprarlo directamente a través de cetesdirecto.

**Bono M:** mercado de capitales, a plazos de 3, 5, 10, 20 y 30 años. Pagan un cupón fijo cada 182 días, pactado en pesos nominales desde la emisión, más el valor nominal al vencimiento. Financian el déficit presupuestal plurianual del Gobierno Federal, y su tasa a 10 años es la referencia que el mercado sigue para juzgar el costo de financiamiento del gobierno a largo plazo (durante 2026, en un rango de 8.5%-9.3%). Sus principales compradores son inversionistas institucionales con pasivos de largo plazo, Afores/Siefores y aseguradoras a la cabeza, además de fondos de inversión de deuda; una porción considerable también la tienen inversionistas extranjeros, atraídos por el rendimiento de un instrumento soberano en pesos frente al de otras economías.

**UDIBONO (Bono de Desarrollo del Gobierno Federal denominado en UDIs):** mismo emisor y plazos largos que el Bono M (3, 10, 20 y 30 años), pero su valor nominal está denominado en Unidades de Inversión (UDIs), no en pesos; el cupón fijo (también cada 182 días) es una **tasa real**, y tanto el cupón como el valor nominal al vencimiento se convierten a pesos multiplicando por el valor de la UDI vigente ese día. Como la UDI se ajusta con la inflación, quien compra un UDIBONO protege su poder adquisitivo, algo que el Bono M no ofrece: si la inflación sorprende al alza, el cupón fijo en pesos del Bono M pierde valor real, mientras que el cupón del UDIBONO se ajusta con la UDI. Lo compran, en buena medida, los mismos inversionistas institucionales que el Bono M (Afores/Siefores, aseguradoras), pero por una razón más puntual: son quienes tienen pasivos de largo plazo sensibles a la inflación (pensiones, seguros), y el UDIBONO les permite calzar ese pasivo con un activo que corre el mismo riesgo.

> **Por qué UDIBONO y Bono M pagan distinto aunque comparten emisor y plazo.** La diferencia no es de riesgo de crédito (el mismo Gobierno Federal respalda a ambos), es de **qué tasa se pacta**: el Bono M pacta una tasa nominal fija sobre pesos; el UDIBONO pacta una tasa real fija sobre UDIs. Por eso la tasa cupón del Bono M (nominal) es mayor que la del UDIBONO (real): la diferencia aproxima la inflación que el mercado espera durante la vida del bono, más cualquier prima por la incertidumbre de esa inflación. En la subasta de junio de 2026, el UDIBONO a 10 años rindió una tasa real de 4.60% y el de 30 años, 4.29%; comparados contra el Bono M nominal del mismo plazo (secciones anteriores), la brecha da una idea de cuánta inflación espera el mercado a cada horizonte.

### 2. Instrumentos corporativos: bono corporativo y papel comercial

Ambos los emite una empresa privada, no el gobierno, y por lo tanto ambos requieren la autorización de la CNBV para su oferta pública (o califican para colocación privada) descrita en [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda), y ambos están sujetos al riesgo de crédito del emisor que se calificó en [`3_mecanica_mercado.md`](../unidad1/3_mecanica_mercado.md#3-calificadoras-y-riesgo-de-crédito). Lo que los distingue es el plazo, y de ahí se sigue casi automáticamente la mecánica de pago.

**Papel comercial:** mercado de dinero, plazo corto (hasta 360 días, típicamente unas cuantas semanas). Suele pagar a descuento, igual que un CETE, porque a un plazo tan corto no vale la pena la complejidad administrativa de un cupón periódico. Financia capital de trabajo: nómina, inventario, cuentas por cobrar. Muchas empresas mantienen un **programa autorizado** vigente por varios años, bajo el cual reemiten papel comercial una y otra vez (revolvente) sin pedir una nueva autorización cada vez. Lo compran, sobre todo, fondos de inversión de mercado de dinero y tesorerías de otras empresas que necesitan estacionar efectivo por unas semanas a una tasa mejor que un depósito bancario.

**Bono corporativo:** mercado de capitales, plazo largo (varios años). Paga cupones periódicos, fijos o variables (referenciados a TIIE), porque a un plazo largo el emisor prefiere un costo de financiamiento predecible o, si elige tasa variable, transferir al inversionista el riesgo de que la tasa de referencia suba. Financia proyectos de largo plazo: una planta, una expansión, una adquisición. Lo compran los mismos inversionistas institucionales que el Bono M (Afores/Siefores, aseguradoras, fondos de deuda), atraídos por el rendimiento adicional (spread) sobre la deuda gubernamental del mismo plazo, que compensa el riesgo de crédito que el bono corporativo sí carga.

> Que el papel comercial sea a descuento y el bono corporativo sea con cupón no es una regla universal, es la mecánica que domina en México dado el plazo típico de cada uno; nada impide, en principio, un papel comercial con cupón o un bono corporativo a descuento. Lo que sí es constante es el emisor: una empresa privada en ambos casos, nunca el gobierno.

### 3. Certificado bursátil: el instrumento híbrido

El certificado bursátil (CEBUR) es el instrumento más flexible de los seis, y por eso la tabla comparativa de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#6-tres-preguntas-para-caracterizar-cualquier-instrumento-de-deuda) no le encontró un análogo exacto en EUA: el corporate bond y el medium-term note se le acercan, pero ninguno cubre exactamente el mismo rango de casos.

A diferencia de los cuatro instrumentos anteriores, el certificado bursátil no tiene un emisor ni un plazo fijos por diseño:

- **Lo puede emitir una empresa privada** (el caso más común) **o un gobierno estatal o municipal**, algo que ningún otro instrumento de esta unidad permite: el Bono M, el UDIBONO y el CETE son exclusivos del Gobierno Federal, y solo el gobierno federal, nunca un estado o municipio, los emite.
- **Puede pactarse a cualquier plazo**, desde certificados de corto plazo (que compiten directamente con el papel comercial) hasta certificados a varios años (que compiten con el bono corporativo).
- **Puede pagar bajo cualquiera de las tres mecánicas** de la sección 3 de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#3-qué-es-un-instrumento-de-deuda): a descuento en emisiones cortas, cupón fijo, o cupón variable referenciado a TIIE.

Quién lo compra depende, otra vez, del diseño de cada emisión: uno colocado por oferta pública a plazo largo atrae al mismo tipo de inversionista institucional que un bono corporativo (Afores/Siefores, aseguradoras, fondos de deuda); uno de plazo corto atrae a los mismos compradores que un papel comercial (fondos de mercado de dinero, tesorerías corporativas); y uno colocado de forma privada, como el ejemplo del BCIE de abajo, se coloca directamente entre inversionistas institucionales calificados, la única audiencia que ese canal permite ([`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda)).

> **Ejemplo resuelto.** El certificado bursátil del Banco Centroamericano de Integración Económica (BCIE) presentado en la sección 5 de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#5-cómo-se-coloca-y-se-negocia-la-deuda) clasifica así: emisor, un organismo financiero internacional que coloca en México (tratado como emisor privado para efectos de este curso, no es el Gobierno Federal mexicano); plazo, 3.5 años (mercado de capitales); mecánica de pago, cupón variable referenciado a TIIE de fondeo a 28 días más sobretasa, con amortización bullet.

### 4. Los seis instrumentos lado a lado

| Instrumento          | ¿Quién emite?                  | ¿A qué plazo? | ¿Cómo paga?                              | ¿Cómo se coloca?                               | ¿Quién lo compra, sobre todo?                                                                           |
| -------------------- | ------------------------------ | ------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| CETE                 | Gobierno federal               | Corto         | A descuento                              | Subasta primaria (Banxico)                     | Bancos y casas de bolsa, fondos de mercado de dinero, tesorerías corporativas, cetesdirecto             |
| Bono M               | Gobierno federal               | Largo         | Cupón fijo                               | Subasta primaria (Banxico)                     | Afores/Siefores, aseguradoras, fondos de deuda, inversionistas extranjeros                              |
| UDIBONO              | Gobierno federal               | Largo         | Cupón fijo real (en UDIs)                | Subasta primaria (Banxico)                     | Afores/Siefores y aseguradoras, por sus pasivos de largo plazo indexados a la inflación                 |
| Bono corporativo     | Empresa privada                | Largo         | Cupón fijo o variable                    | Oferta pública (CNBV) o colocación privada     | Afores/Siefores, aseguradoras, fondos de deuda                                                          |
| Papel comercial      | Empresa privada                | Corto         | A descuento                              | Oferta pública bajo programa autorizado (CNBV) | Fondos de mercado de dinero, tesorerías corporativas                                                    |
| Certificado bursátil | Empresa o gobierno subnacional | Corto o largo | A descuento, cupón fijo o cupón variable | Oferta pública (CNBV) o colocación privada     | Depende del diseño: institucional si es largo, mercado de dinero si es corto, calificados si es privado |

Esta tabla responde las tres preguntas de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#6-tres-preguntas-para-caracterizar-cualquier-instrumento-de-deuda) para cada instrumento, agrega una cuarta columna (canal de colocación) que distingue el único emisor gubernamental (subasta vía Banxico) de los emisores privados o subnacionales (CNBV), y una quinta (comprador típico) que anticipa un patrón que se repite en toda la unidad: quien tiene pasivos de largo plazo compra deuda de largo plazo, y quien solo necesita estacionar efectivo compra deuda de corto plazo.

Esa quinta columna, en realidad, reparte nombres propios (Afores/Siefores, aseguradoras, fondos de deuda, tesorerías corporativas) dentro de los agentes económicos que [`0_activo_financiero.md`](../unidad1/0_activo_financiero.md#4-agentes-económicos-y-su-acceso-a-los-mercados) ya presentó en Unidad 1: Afores/Siefores, aseguradoras y fondos de deuda son la cara concreta de los **inversionistas institucionales** de esa tabla; las tesorerías corporativas que estacionan efectivo en CETES o papel comercial son la cara de corto plazo de las **grandes empresas**; los bancos y casas de bolsa que participan en la subasta son los mismos **bancos e intermediarios**; y cetesdirecto es el canal de acceso indirecto que esa tabla ya reservaba para las **personas físicas**.

---

## Fuentes y referencias recomendadas

- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 11, "The Money Markets": CETES y papel comercial como instrumentos de mercado de dinero. Cap. 12, "The Bond Market": Bono M, UDIBONO, bono corporativo y certificado bursátil como instrumentos de mercado de capitales.
- Banco de México: ficha técnica de CETES, Bonos M y UDIBONOS (plazos, mecánica de pago, calendario de subastas); resultados de subasta consultados el 3 de septiembre de 2026 para las tasas citadas en la sección 1.
- Portal cetesdirecto: características de cada instrumento gubernamental para el pequeño inversionista.
- Banco de México: tenencia de valores gubernamentales por sector tenedor (bancos, Afores/Siefores, aseguradoras, fondos de inversión, extranjeros), usada como base para el comprador típico de cada instrumento gubernamental.
- Portal BMV: prospectos de colocación de certificados bursátiles y programas de papel comercial (ejemplo del BCIE citado en la sección 3).
- Fabozzi, F. J. (2009). *Capital Markets, Financial Management, and Investment Management*. Wiley. Cap. 19, "Bond Portfolio Management": estructura de bonos corporativos y papel comercial usada como análogo de los instrumentos mexicanos.

---

## Cierre de la unidad — Lo esencial para recordar

- Los tres instrumentos gubernamentales (**CETE**, **Bono M**, **UDIBONO**) comparten emisor y canal de colocación (subasta primaria vía Banxico); el plazo decide la mecánica de pago: **CETE** a descuento (corto plazo), **Bono M** cupón fijo nominal (largo plazo), **UDIBONO** cupón fijo real en UDIs (largo plazo, protegido de la inflación).
- Los dos instrumentos corporativos (**papel comercial**, **bono corporativo**) comparten emisor (empresa privada) y canal (CNBV); el plazo también decide la mecánica: corto plazo y a descuento el papel comercial, largo plazo y con cupón el bono corporativo.
- El **certificado bursátil** es el más flexible de los seis: lo puede emitir una empresa o un gobierno subnacional, a cualquier plazo, bajo cualquier mecánica de pago, por lo que no tiene un análogo exacto en el mercado estadounidense.
- Cualquiera de los seis se clasifica con las mismas tres preguntas de la nota anterior: quién emite, a qué plazo, y cómo paga.
- Quién compra cada instrumento sigue un patrón: deuda de corto plazo (CETE, papel comercial) la compran bancos, fondos de mercado de dinero y tesorerías que solo estacionan efectivo; deuda de largo plazo (Bono M, UDIBONO, bono corporativo) la compran inversionistas institucionales con pasivos de largo plazo (Afores/Siefores, aseguradoras); el certificado bursátil, otra vez, depende del diseño de cada emisión.

**Próxima sesión:** cómo se calcula el precio de cada uno de estos instrumentos a partir de sus flujos y su valor nominal.
