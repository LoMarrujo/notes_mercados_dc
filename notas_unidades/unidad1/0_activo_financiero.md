# Unidad 1 · Activo Financiero e Intermediación Financiera

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante distinga un activo financiero de otros tipos de activo, y al emisor del inversionista en una transacción dada.

## Contenido

|      | Tema                                       | Qué cubre                                                                           |
|------|---------------------------------------------|----------------------------------------------------------------------------------------|
| I    | ¿Por qué existen los mercados financieros? | Suavizar el consumo, diversificar riesgo [idiosincrático], eficiencia del capital, transferir riesgo [transferible] |
| II   | ¿Qué es un activo financiero?              | Activo tangible/intangible, activo financiero, emisor, inversionista                |
| III  | Intermediación financiera                  | Unidades superavitarias/deficitarias, por qué existen los intermediarios            |
| IV   | Dos caminos para el crédito                | Intermediación bancaria (crédito indirecto) vs. mercado bursátil (crédito directo)  |
| V    | El ciclo de captación-colocación           | Captación, colocación, recuperación y cierre del ciclo; margen financiero (spread)  |
| VI   | El ciclo del crédito directo               | Emisión, negociación y liquidación de un instrumento en el mercado bursátil         |

> La práctica de este tema está en [`practica_unidad1.md`](../../practicas/unidad1/practica_unidad1.md).
> El riesgo de un activo financiero se trata como apéndice, al final de este documento.

---

## Parte I: Teoría

Por qué existen los mercados financieros, qué es un activo financiero, y por qué existen los intermediarios que lo hacen circular.

### 1. ¿Por qué existen los mercados financieros?

El propósito de un mercado financiero es canalizar recursos de quienes ahorran hacia quienes los necesitan para invertir o consumir.

- **Suavizar el consumo:** las personas prefieren mantener su consumo relativamente estable en el tiempo (ahorrar en los años buenos, usar esos ahorros en los años malos) y ante eventos inesperados, en vez de que su consumo dependa directamente de cuánto ganan en cada momento.
- **Diversificar el riesgo [idiosincrático] individual:** juntar los ahorros de muchas personas permite financiar proyectos productivos grandes y de largo plazo que ningún ahorrador podría costear (ni cuyo riesgo [idiosincrático] podría asumir) por sí solo.
- **Eficiencia y crecimiento económico:** hay ganancia para toda la economía cuando quienes tienen proyectos productivos (típicamente empresas y gobierno) piden prestado a quienes ahorran pero no tienen dónde invertir directamente (típicamente los hogares).
- **Transferencia de riesgo [transferible]:** los mercados también permiten que quien no quiere asumir un riesgo [transferible] se cubra o se asegure, transfiriéndoselo a alguien dispuesto a tomarlo a cambio de una prima; por eso no son necesariamente un juego de suma cero.

> Los activos financieros no son la riqueza real de una economía: son títulos sobre el ingreso que generan los activos reales (tierra, maquinaria, tecnología, conocimiento). Por eso qué tan bien o mal asigna el capital el sistema financiero, no solo cuánto se ahorra, contribuye al crecimiento de un país.

### 2. ¿Qué es un activo financiero?

**Activo**, recurso con valor económico: cualquier recurso del que se espera obtener beneficios económicos futuros.

- **Tangible:** su valor depende de sus propiedades físicas (inmuebles, maquinaria, equipo).
- **Intangible:** es un derecho legal sobre beneficios futuros, sin relación con una forma física.

**Activo financiero**: activo intangible cuyo beneficio futuro es un derecho sobre efectivo futuro. Si se negocia en mercados organizados, se le llama **valor** (*security*).

- **Emisor:** se compromete a realizar los pagos futuros.
- **Inversionista:** posee el instrumento y tiene derecho a recibir esos pagos.

> Todo instrumento financiero involucra, como mínimo, dos partes: el emisor (unidad deficitaria) y el inversionista (unidad superavitaria).

**Ejemplos de activos financieros.** En cada uno, el emisor es quien promete el pago futuro y el inversionista es quien lo compra esperando recibirlo:

| Activo financiero                                      | Emisor                                  | Inversionista          | ¿Cómo llega el rendimiento?                                                                                                        |
|-----------------------------------------------------------|--------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| CETE (Certificado de la Tesorería)                     | Gobierno federal (SHCP)                 | Comprador               | A descuento: se compra por debajo de su valor nominal y se cobra el nominal completo al vencimiento; no paga cupones.              |
| Bono gubernamental (Bono M, UDIBONO)                   | Gobierno federal                        | Comprador               | Cupones periódicos (interés) durante la vida del bono, más el valor nominal al vencimiento.                                        |
| Bono corporativo                                       | La empresa que lo coloca                | Comprador               | Igual que el bono gubernamental: cupones periódicos más el principal al vencimiento.                                               |
| Papel comercial                                        | La empresa que lo emite                 | Comprador               | A descuento, igual que el CETE: la ganancia es la diferencia entre precio de compra y valor nominal, sin cupones.                  |
| Certificado bursátil                                   | Empresa o gobierno                      | Comprador               | Normalmente cupones periódicos más el principal al vencimiento, según se pacte en la emisión.                                      |
| Acción común o preferente                              | La empresa que cotiza                   | El accionista           | Dividendos (si la empresa reparte utilidades) más la plusvalía si se vende a un precio mayor al de compra.                         |
| FIBRA (certificado del fideicomiso)                    | El fideicomiso                          | Dueño del certificado   | Distribuciones periódicas obligatorias (renta de los inmuebles) más la plusvalía del certificado.                                  |
| CKD (Certificado de Capital de Desarrollo)             | El fideicomiso que agrupa los proyectos | Dueño del certificado   | Distribuciones cuando los proyectos generan flujo o se venden, más la plusvalía del certificado; sin monto ni fecha garantizados. |
| CERPI (Certificado de Proyectos de Inversión)          | El fideicomiso que agrupa los proyectos | Dueño del certificado   | Igual que el CKD: distribuciones ligadas al desempeño de los proyectos (frecuentemente en el extranjero), sin monto garantizado.   |
| Certificado bursátil a tasa variable (indexado a TIIE) | Empresa o gobierno                      | Comprador               | Cupones periódicos, pero el monto cambia cada periodo según la tasa de referencia (p. ej. TIIE) vigente en ese momento.            |
| Pagaré entre particulares                              | Quien firma el pagaré                   | Prestamista             | Pago único al vencimiento: el capital prestado más el interés pactado.                                                             |
| Cuenta de ahorro / depósito a plazo                    | El banco                                | El ahorrador            | Interés que el banco acredita sobre el saldo, de forma periódica o al final del plazo.                                             |
| Crédito hipotecario (visto desde el banco)             | Quien pide el préstamo                  | El banco                | Mensualidades: cada pago incluye una parte de capital y una de interés.                                                            |

> Los instrumentos de deuda (CETES, bonos, papel comercial, certificados bursátiles) y los de capital (acciones, FIBRAS) se estudian a fondo en las unidades 2 y 3. Aquí solo importa reconocer que **todos** son activos financieros: un derecho intangible sobre efectivo futuro, con un emisor y un inversionista identificables.

**Lo que NO es un activo financiero**, aunque tenga valor económico:

| Ejemplo                        | Tipo de activo            | Por qué no es un activo financiero                                                                          |
|----------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------|
| La casa donde vives            | Tangible                  | Su valor depende de sus propiedades físicas, no de un derecho contractual de cobro                          |
| Un coche                       | Tangible                  | Es un bien de uso; nadie te debe un pago futuro por tenerlo                                                 |
| Maquinaria de una fábrica      | Tangible                  | Bien productivo, no un derecho financiero                                                                   |
| Oro físico                     | Tangible                  | Su valor es por sus propiedades físicas, aunque se negocie en mercados                                      |
| Un boleto de avión ya usado    | No aplica                 | Ya no genera ningún beneficio económico futuro                                                              |
| Una patente o marca registrada | Intangible, no financiero | Da derecho a beneficios futuros, pero no es un derecho de cobro sobre un tercero; es propiedad intelectual |

### 3. Intermediación financiera

El mercado financiero canaliza recursos de quienes ahorran hacia quienes los necesitan.

- **Unidades superavitarias:** ahorradores e inversionistas, agentes que generan excedentes de recursos y buscan colocarlos con seguridad y liquidez.
- **Unidades deficitarias:** empresas, gobierno y personas que necesitan financiamiento para operar, invertir o consumir.

Entre ambas fluyen **recursos (dinero)** a cambio de un **activo financiero**.

**Por qué existen los intermediarios:**

Resuelven un problema concreto: ahorradores y deudores casi nunca pueden negociar directamente en condiciones favorables. El intermediario capta fondos de un lado y los coloca del otro, en dos pasos.

- **Banco comercial**: recibe depósitos de corto plazo y los transforma en créditos de largo plazo (*maturity intermediation*).
- **Fondo de inversión**: junta el dinero de muchos ahorradores pequeños y arma un portafolio diversificado que ninguno podría comprar solo.

### 4. Dos caminos para el crédito

La intermediación bancaria y el mercado bursátil canalizan el ahorro de formas distintas.

|                    | Intermediación bancaria (crédito indirecto)                                                      | Mercado bursátil (crédito directo)                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Mecánica           | El banco capta depósitos y emite deudas propias (indirectas): pagarés, certificados de depósito. | Empresas y gobierno emiten deudas propias (directas): bonos, papel comercial, acciones. |
| Riesgo de crédito  | Lo absorbe el banco: presta directamente a empresas, personas y gobierno.                        | Lo asume el inversionista directamente frente al emisor del título.                     |
| Ejemplo            | Una persona ahorra en el banco y este otorga un crédito a una empresa.                           | Una empresa coloca certificados de deuda en la bolsa de valores.                        |

Retomando los ejemplos de activos financieros de la sección 2, así se clasifican según este criterio, y si su rendimiento es **estocástico** (incierto: no se conoce de antemano) o no (determinístico: se pacta desde el inicio):

| Activo financiero                                      | Tipo                     | ¿Rendimiento estocástico?                                                                                                                    |
|-----------------------------------------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| CETE (Certificado de la Tesorería)                     | Crédito directo          | No: se pacta a descuento; el monto a recibir al vencimiento se conoce desde la compra.                                                       |
| Bono gubernamental (Bono M, UDIBONO)                   | Crédito directo          | No: el cupón se fija desde la emisión.                                                                                                        |
| Bono corporativo                                       | Crédito directo          | No: el cupón se pacta desde la emisión.                                                                                                       |
| Papel comercial                                        | Crédito directo          | No: se pacta a descuento, igual que el CETE.                                                                                                  |
| Certificado bursátil                                   | Crédito directo          | No: el cupón se pacta desde la emisión.                                                                                                       |
| Acción común o preferente                              | Participación de capital | Sí: ni los dividendos ni el precio de venta futuro se conocen de antemano.                                                                    |
| FIBRA (certificado del fideicomiso)                    | Participación de capital | Sí: las distribuciones dependen de la renta que generen los inmuebles, y el precio del certificado fluctúa.                                   |
| CKD (Certificado de Capital de Desarrollo)             | Participación de capital | Sí: depende del desempeño de los proyectos de infraestructura o capital privado que financia; ni el monto ni el momento están garantizados. |
| CERPI (Certificado de Proyectos de Inversión)          | Participación de capital | Sí: mismo mecanismo que el CKD, típicamente para proyectos en el extranjero.                                                                  |
| Certificado bursátil a tasa variable (indexado a TIIE) | Crédito directo          | Sí: el capital se debe igual, pero el monto de cada cupón cambia con la tasa de referencia; ver apéndice de riesgo.                            |
| Pagaré entre particulares                              | Crédito directo          | No: el monto a devolver se pacta desde la firma.                                                                                              |
| Cuenta de ahorro / depósito a plazo                    | Crédito indirecto        | No: la tasa se pacta desde el depósito.                                                                                                       |
| Crédito hipotecario (visto desde el banco)             | Crédito indirecto        | No: las mensualidades se pactan desde el crédito.                                                                                             |

> "No estocástico" se refiere al **monto prometido**, no a que el instrumento esté libre de riesgo [incumplimiento] (ver apéndice). Nota también el patrón: la mayoría de la deuda (crédito directo o indirecto) es **renta fija**, de ahí el nombre del mercado de deuda; la participación de capital es **renta variable**, de ahí que el mercado de capitales también se conozca así. El certificado bursátil a tasa variable es la excepción que confirma la regla: sigue siendo deuda (el capital se debe sin importar qué pase), pero el monto del cupón sí es estocástico porque depende de una tasa de referencia futura. Se retoma en las unidades 2 y 3.

### 5. El ciclo de captación-colocación

Así es como el banco conecta al ahorrador con el deudor, paso a paso:

1. **Captación de recursos**: el banco capta recursos del ahorrador (depósitos, pagarés, certificados) y se compromete a devolverlos con un rendimiento: la **tasa pasiva**.
2. **Colocación del crédito**: el banco presta esos recursos a empresas, personas o gobierno cobrando una **tasa activa**, mayor a la pasiva, y asume el riesgo de crédito.
3. **Recuperación del crédito**: el deudor devuelve al banco el capital más los intereses pactados conforme transcurre el plazo del crédito.
4. **Cierre del ciclo**: el banco paga al ahorrador su depósito con rendimiento; la diferencia entre tasa activa y pasiva es su **margen financiero (spread)**.

### 6. El ciclo del crédito directo

El camino directo (mercado bursátil) también tiene su propio ciclo, en espejo del de captación-colocación, pero aquí no hay intermediario que asuma el riesgo de crédito entre las dos partes.

1. **Emisión**: la empresa o el gobierno coloca el instrumento directamente con inversionistas, a cambio de sus recursos.
2. **Negociación**: el inversionista que lo compró puede revenderlo a otro inversionista antes de su vencimiento, en el mercado secundario.
3. **Liquidación**: al vencimiento, el emisor paga directamente al tenedor final registrado en ese momento.

> El detalle institucional de este ciclo (mercado primario/secundario, BMV, Indeval) se revisa en [`3_matematica_financiera_mecanica_mercado.md`](3_matematica_financiera_mecanica_mercado.md), y se practica en el taller "recorrido institucional de un CETE".

---

## Apéndice: Riesgo de un activo financiero

"Riesgo" no es una sola cosa: en este documento aparece en más de un sentido.

- **Riesgo de crédito (o de incumplimiento):** la posibilidad de que el emisor no pague lo prometido, en el monto o en la fecha pactados. Es el riesgo [incumplimiento] del que habla la tabla de la sección 4 ("Dos caminos para el crédito") cuando dice quién lo asume: en la intermediación bancaria lo absorbe el banco; en el mercado bursátil, el inversionista lo asume directamente frente al emisor.
- **Riesgo del rendimiento (variabilidad, o rendimiento estocástico):** aun si el emisor sí va a pagar, el monto que vas a recibir puede no conocerse de antemano. Es lo que identifica la columna "¿Rendimiento estocástico?" de la sección 4 para cada ejemplo: una acción no tiene garantizado ni el dividendo ni el precio de venta; un CETE, si el gobierno paga, sí tiene garantizado su valor de vencimiento desde que se compra.

> Son dos dimensiones distintas: un instrumento puede prometer un monto fijo (rendimiento no estocástico) y aun así tener riesgo de crédito alto, si el emisor es poco solvente. Por eso un bono corporativo de una empresa endeudada puede ser más riesgoso [incumplimiento] que un CETE, aunque ambos prometan pagar un monto conocido desde el inicio. Esto no significa que estén descorrelacionados: un emisor con negocio inestable, lo que eleva su riesgo de incumplimiento, también suele tener menos capacidad de comprometerse a pagos fijos, así que en la práctica es probable que ambos riesgos se muevan juntos.

Dos sentidos más de "riesgo":

- **Riesgo idiosincrático:** el riesgo específico de que un proyecto particular fracase, independiente del resto de la economía. Se reduce diversificando entre muchos proyectos: no desaparece, se reparte.
- **Riesgo transferible (asegurable):** un riesgo que no desaparece, pero que puede trasladarse a quien esté dispuesto a asumirlo a cambio de una prima, la lógica detrás de un seguro.

> El detalle de los tipos de riesgo propios de un instrumento de deuda (tasa de interés, crédito, inflación, liquidez) se estudia a fondo en la Unidad 2.

---

## Fuentes y referencias recomendadas

- Linton, O. (2019). *Financial Econometrics: Models and Methods*. Cambridge University Press. Cap. 1 §1.1: por qué existen los mercados financieros.
- Fabozzi, F. J. y Peterson Drake, P. (2009). *Finance*. Wiley. Cap. 4, "The Financial System": qué es un activo financiero y funciones del mercado.
- Mántey de Anguiano, G. (2024). *Lecciones de Economía Monetaria*. UNAM. Lección 2: intermediación financiera y los ciclos de crédito indirecto y directo.

---

## Cierre de la unidad — Lo esencial para recordar

- Un **activo financiero** es un derecho sobre flujos futuros que vincula a un emisor (unidad deficitaria) con un inversionista (unidad superavitaria).
- El **crédito indirecto** (intermediación bancaria) sigue el ciclo captación → colocación → recuperación → cierre; el banco asume el riesgo [incumplimiento] y su utilidad es el **margen financiero (spread)**.
- El **crédito directo** (mercado bursátil) sigue el ciclo emisión → negociación → liquidación; aquí el inversionista asume el riesgo [incumplimiento] directamente frente al emisor, sin intermediario de por medio.
- Ambos caminos resuelven el mismo problema, conectar a quien ahorra con quien necesita financiamiento, pero difieren en quién asume el riesgo de crédito.
