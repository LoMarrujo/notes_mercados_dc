# Unidad 1 · Práctica

**Mercados de Deuda y Capitales** — Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Ejercicios, talleres y casos de la Unidad 1, aplicando los conceptos de [`0_activo_financiero.md`](../../notas_unidades/unidad1/0_activo_financiero.md), [`1_clasificacion_mercados.md`](../../notas_unidades/unidad1/1_clasificacion_mercados.md), [`2_estructura_sfm.md`](../../notas_unidades/unidad1/2_estructura_sfm.md) y [`3_matematica_financiera_mecanica_mercado.md`](../../notas_unidades/unidad1/3_matematica_financiera_mecanica_mercado.md).

---

## Activo Financiero e Intermediación Financiera

### Ejercicio: identifica el concepto

Por cada situación, indica qué concepto de la Parte I aplica.

| Situación                                                      | Concepto                                        |
|----------------------------------------------------------------|-------------------------------------------------|
| Juan compra maquinaria para su fábrica.                        | Activo tangible                                 |
| Una empresa emite un bono y se compromete a pagar intereses.   | Activo financiero (la empresa es el **emisor**) |
| Ana deposita sus ahorros en el banco esperando un rendimiento. | Unidad **superavitaria**                        |
| Una PyME solicita un crédito para comprar inventario.          | Unidad **deficitaria**                          |
| Un fondo de inversión compra el bono que emitió la empresa.    | El fondo es el **inversionista**                |

### Mini-caso: el ciclo de captación-colocación

Identifica en qué paso del ciclo (1. Captación, 2. Colocación, 3. Recuperación, 4. Cierre del ciclo) está cada situación.

1. Juan abre una cuenta de ahorro y el banco le ofrece 6% anual. → **Paso 1**
2. El banco usa esos recursos para dar un crédito a una PyME al 15% anual. → **Paso 2**
3. La PyME paga puntualmente su crédito mes con mes. → **Paso 3**
4. El banco le regresa a Juan su dinero más los intereses pactados. → **Paso 4**
5. ¿De dónde sale la ganancia del banco en esta cadena? → Del **margen financiero (spread)** entre el 15% que cobra y el 6% que paga.

---

## Clasificación de Activos y Mercados Financieros

### Ejercicio: clasifica el instrumento

Por cada instrumento, indica (a) si es deuda directa, deuda indirecta o participación de capital, y (b) si pertenece al mercado de dinero o al mercado de capitales.

| Instrumento                                         | Tipo                                             | Mercado   |
|-----------------------------------------------------|--------------------------------------------------|-----------|
| CETE a 28 días                                      | Deuda directa (emisor: gobierno)                 | Dinero    |
| Papel comercial de una empresa a 90 días            | Deuda directa (emisor: empresa)                  | Dinero    |
| Certificado de depósito bancario a 6 meses          | Deuda indirecta (emisor: banco)                  | Dinero    |
| Bono M a 10 años                                    | Deuda directa (emisor: gobierno)                 | Capitales |
| Acción común de una empresa que cotiza en la BMV    | Participación de capital                         | Capitales |
| Bono hipotecario emitido por una banca de inversión | Deuda indirecta (emisor: institución financiera) | Capitales |

> El último renglón es la trampa a propósito: un instrumento de **largo plazo** (mercado de capitales) puede seguir siendo **deuda indirecta** si quien lo emite es un intermediario financiero, no el deudor final. Plazo y tipo de emisor son dos clasificaciones independientes.

---

## Estructura del Sistema Financiero Mexicano

### Dinámica grupal: mapeo de entidades

Actividad colaborativa para fijar el organigrama del Sistema Financiero Mexicano.

1. **Trazar el organigrama** — en el pizarrón o de forma colaborativa, el grupo reconstruye la estructura completa del SFM visto en la sesión teórica.
2. **Asignar roles** — cada alumno o equipo asume el papel de una institución: SHCP, Banxico, CNBV, CNSF, Consar, IPAB o CONDUSEF.
3. **Explicación voluntaria** — se abre el micrófono: los equipos que lo deseen explican brevemente qué supervisa su institución.
4. **Verificar en el SIPRES** — buscan una institución real en el SIPRES de la CONDUSEF para comprobar si está registrada: la misma consulta que podrán hacer en el futuro antes de contratar un servicio financiero.

> SIPRES — Sistema de Registro de Prestadores de Servicios Financieros: webapps.CONDUSEF.gob.mx/SIPRES

### Análisis de casos prácticos

Tres preguntas rápidas de la vida real, sin necesidad de software.

| Caso | Situación                   | Pregunta                                                                                          | Respuesta |
|------|-----------------------------|---------------------------------------------------------------------------------------------------|-----------|
| A    | Un banco comercial quiebra  | Una persona tiene sus ahorros ahí. ¿Quién protege su dinero y hasta qué monto?                    | IPAB      |
| B    | Cobro abusivo de comisiones | Una sofom o fintech abusa en el cobro a un cliente. ¿Ante qué organismo se acude?                 | CONDUSEF  |
| C    | Emisión de deuda bursátil   | Una empresa mexicana quiere emitir certificados de deuda en la bolsa. ¿Quién autoriza la emisión? | CNBV      |

### Ejercicio: equivalencias internacionales

Por cada autoridad del SFM, indica (a) su equivalente funcional en Estados Unidos y (b) si el país donde opera se clasifica como bank-based o market-based.

| Autoridad del SFM | Equivalente en EE. UU. | Modelo del país    |
|-------------------|------------------------|--------------------|
| Banxico           | Reserva Federal (Fed)  | México: bank-based |
| CNBV              | SEC                    | México: bank-based |
| IPAB              | FDIC                   | México: bank-based |
| CONDUSEF          | CFPB                   | México: bank-based |

> Nota para el instructor: la columna "Modelo del país" es la misma en las cuatro filas a propósito — el modelo (bank-based/market-based) es una propiedad del país, no de la autoridad. El alumno debe notar que EE. UU., aunque tenga agencias equivalentes a cada una del SFM, es un sistema market-based, mientras que México es bank-based: equivalencia funcional no implica mismo modelo.

---

## Matemática Financiera y Mecánica del Mercado

### Ejercicio numérico

1. Un banco ofrece una tasa nominal anual del 18%, capitalizable trimestralmente. Calcula la tasa efectiva anual.
   *Respuesta: TEA = (1 + 0.18/4)⁴ − 1 ≈ 19.25%*
2. ¿Cuál es el valor presente de \$50,000 que recibirás en 4 años, si la tasa de descuento es 10% anual?
   *Respuesta: VP = 50,000 / (1.10)⁴ ≈ \$34,151*
3. Un instrumento paga \$2,000 anuales durante 3 años. Con una tasa de descuento de 7%, ¿cuál es su valor presente?
   *Respuesta: VP = 2,000 × [1 − (1.07)⁻³] / 0.07 ≈ \$5,247*

### Taller: recorrido institucional de un CETE

Traza el camino completo de un CETE, identificando qué institución interviene en cada paso:

1. **Subasta primaria** — Banxico subasta el CETE a bancos y casas de bolsa. → *Banxico*
2. **Colocación con el inversionista final** — una casa de bolsa vende el CETE a un cliente (persona física o institucional). → *Casa de bolsa*
3. **Custodia y registro** — el título queda registrado electrónicamente a nombre del inversionista. → *Indeval*
4. **Mercado secundario** — el inversionista decide venderlo antes de su vencimiento a otro inversionista. → *Casa de bolsa (ejecuta la operación) + Indeval (liquida el cambio de dueño)*
5. **Vencimiento** — Banxico paga el valor nominal al tenedor final registrado en Indeval. → *Banxico*
