# Unidad 1 · Práctica: Estructura del Sistema Financiero Mexicano y Mecánica de Mercado

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Ejercicios y casos aplicando los conceptos de [`2_estructura_sfm.md`](../../notas_unidades/unidad1/2_estructura_sfm.md) y [`3_mecanica_mercado.md`](../../notas_unidades/unidad1/3_mecanica_mercado.md).

---

## Estructura del Sistema Financiero Mexicano

### Ejercicio: identifica la autoridad

Por cada institución o situación, indica qué autoridad del SFM interviene y en qué nivel actúa (regulador, supervisor, o apoyo y protección).

| Situación                                                           | Autoridad             | Nivel              | Fundamento legal                                                                  |
| ------------------------------------------------------------------- | --------------------- | ------------------ | --------------------------------------------------------------------------------- |
| Una Sofipo capta depósitos de ahorradores.                          | CNBV                  | Supervisor         | Ley de Ahorro y Crédito Popular (LACP)                                            |
| Una aseguradora vende una póliza de vida.                           | CNSF                  | Supervisor         | Ley de Instituciones de Seguros y de Fianzas (LISF)                               |
| Una Afore invierte los ahorros para el retiro en una Siefore.       | Consar                | Supervisor         | Ley de los Sistemas de Ahorro para el Retiro (LSAR)                               |
| Banxico coordina con la SHCP la estabilidad del sistema financiero. | Banxico (vía el CESF) | Regulador          | Ley para Regular las Agrupaciones Financieras (LRAF), art. 25                     |
| Un banco quiebra y sus ahorradores reclaman su seguro de depósito.  | IPAB                  | Apoyo y protección | Ley de Protección al Ahorro Bancario (LPAB), art. 6                               |
| Un usuario presenta una queja formal contra una entidad financiera. | CONDUSEF              | Apoyo y protección | Ley de Protección y Defensa al Usuario de Servicios Financieros (LPDUSF), art. 68 |

### Mini-caso: la queja de don Ernesto

Don Ernesto tiene una cuenta de ahorro en un banco. Un día nota un cobro de comisión que nunca autorizó.

1. ¿Ante quién presenta primero su queja? → Ante la propia institución, por escrito.
2. Si el banco no responde de forma satisfactoria, ¿a quién escala? → A CONDUSEF, con la documentación del caso.
3. Si CONDUSEF media y no hay acuerdo, ¿qué puede hacer? → Emitir un dictamen técnico que don Ernesto puede usar en una demanda judicial (LPDUSF, art. 68).

> **Antes de que pasara algo:** antes de abrir esa cuenta, don Ernesto pudo haber consultado dos herramientas de CONDUSEF: el **SIPRES**, para verificar que el banco está legalmente registrado, y el **Buró de Entidades Financieras**, para revisar su historial de quejas. Son preguntas distintas: "¿existe legalmente?" contra "¿qué tanto se han quejado de él?"

### Actividad: ¿le devuelven su dinero a Mariana?

Mariana tiene \$200,000 repartidos en tres productos. Para cada uno, decide si hay una garantía institucional explícita que le devuelva su dinero si algo sale mal, y cuál.

| Producto                                    | ¿Garantía institucional? | Cuál                                                                                                                                 |
| ------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Depósito a plazo en un banco                | Sí                       | IPAB, hasta 400,000 UDIs por persona por institución (LPAB, art. 6)                                                                  |
| Certificado bursátil de una empresa privada | No                       | El riesgo de crédito lo asume ella directamente frente al emisor (regulado por la LMV, que exige transparencia, no garantía de pago) |
| Acción de una empresa que cotiza en bolsa   | No                       | Ni el dividendo ni el precio de venta están garantizados                                                                             |

> **La trampa a propósito:** los tres productos están supervisados por la CNBV (banca, sector bursátil), pero solo uno tiene garantía de pago si el emisor incumple. Regular la emisión (exigir transparencia, autorizar la oferta) no es lo mismo que garantizar el pago.

---

## Mecánica Operativa del Mercado

### Ejercicio: primario o secundario

Para cada operación, indica si ocurre en el mercado primario o en el secundario, y si el emisor recibe dinero en esa operación.

| Operación                                                                     | Mercado    | ¿El emisor recibe dinero? | Fundamento legal                               |
| ----------------------------------------------------------------------------- | ---------- | ------------------------- | ---------------------------------------------- |
| Banxico subasta CETES a bancos y casas de bolsa.                              | Primario   | Sí                        | Circular 3/2012 de Banxico (reglas de subasta) |
| Un inversionista le vende su CETE a otro inversionista antes del vencimiento. | Secundario | No                        | Ley del Mercado de Valores (LMV)               |
| Una empresa hace su oferta pública inicial (OPI) de acciones.                 | Primario   | Sí                        | LMV, título III (oferta pública)               |
| Dos fondos de inversión intercambian acciones de esa empresa un año después.  | Secundario | No                        | LMV, reglas de las bolsas de valores           |

### Mini-caso: el recorrido de un CETE

Traza el camino completo de un CETE, identificando qué institución interviene en cada paso.

1. Banxico subasta el CETE a bancos y casas de bolsa. → **Banxico**
2. Una casa de bolsa vende el CETE a un cliente final. → **Casa de bolsa**
3. El título queda registrado electrónicamente a nombre del inversionista. → **Indeval**
4. El inversionista lo revende antes del vencimiento. → **Casa de bolsa** (ejecuta la operación) + **Indeval** (liquida el cambio de dueño)
5. Banxico paga el valor nominal al tenedor final registrado en Indeval. → **Banxico**

### Ejercicio: el análogo estadounidense

Completa la tabla con el equivalente funcional en Estados Unidos de cada institución mexicana.

| Función                           | México                          | Estados Unidos |
| --------------------------------- | ------------------------------- | -------------- |
| Bolsa de valores                  | BMV, BIVA                       |                |
| Intermediario bursátil            | Casa de bolsa                   |                |
| Custodia y liquidación central    | Indeval                         |                |
| Calificadora de riesgo crediticio | S&P, Moody's, HR Ratings, Fitch |                |
| Regulador del mercado de valores  | CNBV                            |                |

*Respuesta: NYSE/Nasdaq; broker-dealer; DTCC; S&P, Moody's, Fitch; SEC.*

> **La trampa a propósito:** HR Ratings no tiene "equivalente" en Estados Unidos, porque es una calificadora local sin presencia allá; S&P, Moody's y Fitch, en cambio, son las mismas firmas operando en ambos países, no un par de instituciones distintas que cumplen la misma función.
