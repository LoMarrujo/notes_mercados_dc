# Unidad 1 · Intermediación Financiera

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante explique la intermediación financiera.

## Contenido

|     | Tema                             | Qué cubre                                                                          |
| --- | -------------------------------- | ---------------------------------------------------------------------------------- |
| I   | Intermediación financiera        | Unidades superavitarias/deficitarias, por qué existen los intermediarios           |
| II  | Dos caminos para el crédito      | Intermediación bancaria (crédito indirecto) vs. mercado bursátil (crédito directo) |
| III | El ciclo de captación-colocación | Captación, colocación, recuperación y cierre del ciclo; margen financiero (spread) |
| IV  | El ciclo del crédito directo     | Emisión, negociación y liquidación de un instrumento en el mercado bursátil        |

> La práctica de este tema está en [`practica_1_intermediacion.md`](../../practicas/unidad1/practica_1_intermediacion.md).
> El riesgo de un activo financiero se trata como apéndice, al final de este documento.

---

### 1. Intermediación financiera

El mercado financiero canaliza recursos de quienes ahorran hacia quienes los necesitan.

- **Unidades superavitarias:** ahorradores e inversionistas, agentes que generan excedentes de recursos y buscan colocarlos con seguridad y liquidez.
- **Unidades deficitarias:** empresas, gobierno y personas que necesitan financiamiento para operar, invertir o consumir.

Entre ambas fluyen **recursos (dinero)** a cambio de un **activo financiero**.

**Por qué existen los intermediarios:**

Resuelven un problema concreto: ahorradores y deudores casi nunca pueden negociar directamente en condiciones favorables. El intermediario capta fondos de un lado y los coloca del otro, en dos pasos.

- **Banco comercial**: recibe depósitos de corto plazo y los transforma en créditos de largo plazo (*maturity intermediation*).
- **Fondo de inversión**: junta el dinero de muchos ahorradores pequeños y arma un portafolio diversificado que ninguno podría comprar solo.

### 2. Dos caminos para el crédito

Ya vimos que el intermediario capta de un lado y coloca del otro; falta ver qué pasa cuando el deudor final prescinde de ese intermediario y coloca su propio título directamente. La intermediación bancaria y el mercado bursátil canalizan el ahorro de formas distintas.

|                   | Intermediación bancaria (crédito indirecto)                                                      | Mercado bursátil (crédito directo)                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Mecánica          | El banco capta depósitos y emite deudas propias (indirectas): pagarés, certificados de depósito. | Empresas y gobierno emiten deudas propias (directas): bonos, papel comercial, acciones. |
| Riesgo de crédito | Lo absorbe el banco: presta directamente a empresas, personas y gobierno.                        | Lo asume el inversionista directamente frente al emisor del título.                     |
| Ejemplo           | Una persona ahorra en el banco y este otorga un crédito a una empresa.                           | Una empresa coloca certificados de deuda en la bolsa de valores.                        |

> **Ejemplo resuelto.** Distinguir crédito directo de indirecto es preguntar quién asume el riesgo de que el deudor final no pague.
>
> - *Una persona deposita \$50,000 en un banco, y el banco presta ese dinero a una PyME.* Si la PyME no paga, el banco absorbe la pérdida: al ahorrador se le devuelve su depósito de todos modos → crédito indirecto.
> - *Esa misma persona compra directamente un certificado bursátil que emitió la PyME.* Si la PyME no paga, la pérdida es de quien compró el certificado, no hay banco de por medio que la absorba → crédito directo.

Retomando los ejemplos de activos financieros de [`0_activo_financiero.md`](0_activo_financiero.md#2-qué-es-un-activo-financiero), así se clasifican según este criterio, y si su rendimiento es **estocástico** (incierto: no se conoce de antemano) o no (determinístico: se pacta desde el inicio):

| Activo financiero                                      | Tipo                     | ¿Rendimiento estocástico?                                                                                                                   |
| ------------------------------------------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| CETE (Certificado de la Tesorería)                     | Crédito directo          | No: se pacta a descuento; el monto a recibir al vencimiento se conoce desde la compra.                                                      |
| Bono gubernamental (Bono M, UDIBONO)                   | Crédito directo          | No: el cupón se fija desde la emisión.                                                                                                      |
| Bono corporativo                                       | Crédito directo          | No: el cupón se pacta desde la emisión.                                                                                                     |
| Papel comercial                                        | Crédito directo          | No: se pacta a descuento, igual que el CETE.                                                                                                |
| Certificado bursátil                                   | Crédito directo          | No: el cupón se pacta desde la emisión.                                                                                                     |
| Acción común o preferente                              | Participación de capital | Sí: ni los dividendos ni el precio de venta futuro se conocen de antemano.                                                                  |
| FIBRA (certificado del fideicomiso)                    | Participación de capital | Sí: las distribuciones dependen de la renta que generen los inmuebles, y el precio del certificado fluctúa.                                 |
| CKD (Certificado de Capital de Desarrollo)             | Participación de capital | Sí: depende del desempeño de los proyectos de infraestructura o capital privado que financia; ni el monto ni el momento están garantizados. |
| CERPI (Certificado de Proyectos de Inversión)          | Participación de capital | Sí: mismo mecanismo que el CKD, típicamente para proyectos en el extranjero.                                                                |
| Certificado bursátil a tasa variable (indexado a TIIE) | Crédito directo          | Sí: el capital se debe igual, pero el monto de cada cupón cambia con la tasa de referencia; ver apéndice de riesgo.                         |
| Pagaré entre particulares                              | Crédito directo          | No: el monto a devolver se pacta desde la firma.                                                                                            |
| Cuenta de ahorro / depósito a plazo                    | Crédito indirecto        | No: la tasa se pacta desde el depósito.                                                                                                     |
| Crédito hipotecario (visto desde el banco)             | Crédito indirecto        | No: las mensualidades se pactan desde el crédito.                                                                                           |

> "No estocástico" se refiere al **monto prometido**, no a que el instrumento esté libre de riesgo [incumplimiento] (ver apéndice). Nota también el patrón: la mayoría de la deuda (crédito directo o indirecto) es **renta fija**, de ahí el nombre del mercado de deuda; la participación de capital es **renta variable**, de ahí que el mercado de capitales también se conozca así. El certificado bursátil a tasa variable es la excepción que confirma la regla: sigue siendo deuda (el capital se debe sin importar qué pase), pero el monto del cupón sí es estocástico porque depende de una tasa de referencia futura. Se retoma en las unidades 2 y 3.

### 3. El ciclo de captación-colocación

Ya vimos que en el crédito indirecto el banco absorbe el riesgo; así es como conecta al ahorrador con el deudor, paso a paso:

1. **Captación de recursos**: el banco capta recursos del ahorrador (depósitos, pagarés, certificados) y se compromete a devolverlos con un rendimiento: la **tasa pasiva**.
2. **Colocación del crédito**: el banco presta esos recursos a empresas, personas o gobierno cobrando una **tasa activa**, mayor a la pasiva, y asume el riesgo de crédito.
3. **Recuperación del crédito**: el deudor devuelve al banco el capital más los intereses pactados conforme transcurre el plazo del crédito.
4. **Cierre del ciclo**: el banco paga al ahorrador su depósito con rendimiento; la diferencia entre tasa activa y pasiva es su **margen financiero (spread)**.

### 4. El ciclo del crédito directo

El camino directo (mercado bursátil) también tiene su propio ciclo, en espejo del de captación-colocación, pero aquí no hay intermediario que asuma el riesgo de crédito entre las dos partes.

1. **Emisión**: la empresa o el gobierno coloca el instrumento directamente con inversionistas, a cambio de sus recursos.
2. **Negociación**: el inversionista que lo compró puede revenderlo a otro inversionista antes de su vencimiento, en el mercado secundario.
3. **Liquidación**: al vencimiento, el emisor paga directamente al tenedor final registrado en ese momento.

> El detalle institucional de este ciclo (mercado primario/secundario, BMV, Indeval) se revisa en [`5_matematica_financiera_mecanica_mercado.md`](5_matematica_financiera_mecanica_mercado.md), y se practica en el taller "recorrido institucional de un CETE".

---

## Apéndice: Riesgo de un activo financiero

"Riesgo" no es una sola cosa: en este documento aparece en más de un sentido.

- **Riesgo de crédito (o de incumplimiento):** la posibilidad de que el emisor no pague lo prometido, en el monto o en la fecha pactados. Es el riesgo [incumplimiento] del que habla la tabla de la sección 2 ("Dos caminos para el crédito") cuando dice quién lo asume: en la intermediación bancaria lo absorbe el banco; en el mercado bursátil, el inversionista lo asume directamente frente al emisor.
- **Riesgo del rendimiento (variabilidad, o rendimiento estocástico):** aun si el emisor sí va a pagar, el monto que vas a recibir puede no conocerse de antemano. Es lo que identifica la columna "¿Rendimiento estocástico?" de la sección 2 para cada ejemplo: una acción no tiene garantizado ni el dividendo ni el precio de venta; un CETE, si el gobierno paga, sí tiene garantizado su valor de vencimiento desde que se compra.

> Son dos dimensiones distintas: un instrumento puede prometer un monto fijo (rendimiento no estocástico) y aun así tener riesgo de crédito alto, si el emisor es poco solvente. Por eso un bono corporativo de una empresa endeudada puede ser más riesgoso [incumplimiento] que un CETE, aunque ambos prometan pagar un monto conocido desde el inicio. Esto no significa que estén descorrelacionados: un emisor con negocio inestable, lo que eleva su riesgo de incumplimiento, también suele tener menos capacidad de comprometerse a pagos fijos, así que en la práctica es probable que ambos riesgos se muevan juntos.

Dos sentidos más de "riesgo":

- **Riesgo idiosincrático:** el riesgo específico de que un proyecto particular fracase, independiente del resto de la economía. Se reduce diversificando entre muchos proyectos: no desaparece, se reparte.
- **Riesgo transferible (asegurable):** un riesgo que no desaparece, pero que puede trasladarse a quien esté dispuesto a asumirlo a cambio de una prima, la lógica detrás de un seguro.

> El detalle de los tipos de riesgo propios de un instrumento de deuda (tasa de interés, crédito, inflación, liquidez) se estudia a fondo en la Unidad 2.

---

## Fuentes y referencias recomendadas

- Mántey de Anguiano, G. (2024). *Lecciones de Economía Monetaria*. UNAM. Lección 2: intermediación financiera y ciclos de crédito directo/indirecto.
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 2, "An Overview of the Financial System": por qué existen los intermediarios financieros.

---

## Cierre de la unidad — Lo esencial para recordar

- Los intermediarios existen porque ahorradores y deudores casi nunca negocian directamente en condiciones favorables: el banco resuelve esto transformando plazos (*maturity intermediation*), el fondo de inversión diversificando el ahorro de muchos.
- El **crédito indirecto** (intermediación bancaria) sigue el ciclo captación → colocación → recuperación → cierre; el banco asume el riesgo [incumplimiento] y su utilidad es el **margen financiero (spread)**.
- El **crédito directo** (mercado bursátil) sigue el ciclo emisión → negociación → liquidación; aquí el inversionista asume el riesgo [incumplimiento] directamente frente al emisor, sin intermediario de por medio.
- El riesgo de crédito (si el emisor paga) y el riesgo del rendimiento (si el monto se conoce de antemano) son dos dimensiones distintas: un instrumento puede prometer un monto fijo y aun así tener riesgo de crédito alto.
