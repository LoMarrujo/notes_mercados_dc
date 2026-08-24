# Unidad 1 · Clasificación de Activos y Mercados Financieros

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante clasifique un activo financiero según quién lo emite (deuda directa, deuda indirecta o participación de capital) y según su plazo (mercado de dinero o de capitales).

## Contenido

|     | Tema                                          | Qué cubre                                                                  |
|-----|-----------------------------------------------|----------------------------------------------------------------------------|
| I   | Clasificación de los activos financieros      | Deuda directa, deuda indirecta y participación de capital, según el emisor |
| II  | Mercado de dinero y mercado de capitales      | Plazo, función, emisores e instrumentos de cada mercado                    |
| III | Agentes económicos y su acceso a los mercados | Cómo participa cada tipo de agente en el mercado de dinero y de capitales  |
| IV  | Fuentes y referencias                         | Bibliografía del curso                                                     |

> La práctica de este tema está en [`practica_unidad1.md`](../../practicas/unidad1/practica_unidad1.md).

---

### 1. Clasificación de los activos financieros

El título que recibe la unidad superavitaria a cambio de sus recursos es el activo financiero. Adopta una de tres formas, según quién emite la obligación y, en el caso de la deuda, según quién asume frente al inversionista el riesgo de que no se pague.

| Tipo                     | Emisor                                      | Descripción                                                                                                                                                                          | Ejemplos                                                            | Riesgo   | Liquidez |
|--------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|----------|----------|
| Deuda directa            | El propio deudor final (empresa o gobierno) | El deudor que necesita los recursos coloca su propio título directamente con el inversionista, quien asume el riesgo de crédito frente a ese emisor, sin intermediario de por medio. | Bonos gubernamentales, papel comercial, Bonos M, UDIBONOS           | Variable | Media    |
| Deuda indirecta          | Institución financiera (intermediario)      | El intermediario capta recursos emitiendo una obligación propia y es él (no el deudor final al que luego presta) quien asume el riesgo de crédito frente al inversionista.           | Pagarés bancarios, certificados de depósito, aceptaciones bancarias | Bajo     | Alta     |
| Participación de capital | Empresa (acciones)                          | Título que representa una parte del capital de la empresa y da derecho a sus utilidades.                                                                                             | Acciones ordinarias y preferentes, FIBRAs                           | Alto     | Baja     |

Esta distinción es la misma que separa el **crédito directo** del **crédito indirecto** (intermediación bancaria) vista en [`0_activo_financiero.md`](0_activo_financiero.md#4-dos-caminos-para-el-crédito): lo que define a la deuda como directa o indirecta no es solo quién la emite formalmente, sino si ese emisor es el deudor final o un intermediario que se interpone y absorbe el riesgo por él.

> **Ejemplo resuelto.** Clasificar un instrumento por emisor es preguntar quién firma la obligación, y si esa persona es el deudor final o un intermediario que se interpone y absorbe el riesgo por él.
>
> - *Pagaré entre particulares* frente a *cuenta de ahorro en el banco* (ver [`0_activo_financiero.md`](0_activo_financiero.md#4-dos-caminos-para-el-crédito)). En el pagaré, quien pide prestado firma directamente con quien presta → deuda directa. En la cuenta de ahorro, el banco firma la obligación con el ahorrador y luego presta esos recursos a un tercero, absorbiendo el riesgo de ese tercero → deuda indirecta.
> - *Un fondo de crédito privado (*direct lending*, ej. Blackstone, Apollo) presta directamente a una empresa mediana, sin que un banco participe.* A primera vista el fondo parece un intermediario, como el banco del ejemplo anterior: capta recursos de inversionistas institucionales y los coloca en créditos. Pero esos inversionistas siguen expuestos al riesgo de crédito de la empresa que recibe el préstamo, no al del fondo; si la empresa no paga, ellos absorben la pérdida. Por eso el auge del *direct lending* (2023-2025), aunque se sienta como una categoría nueva, sigue siendo deuda directa de la empresa: el fondo actúa como vehículo del inversionista, no como el banco que absorbe el riesgo en su lugar.

### 2. Mercado de dinero y mercado de capitales

El mercado financiero se divide, por convención, según el plazo de los recursos que canaliza.

|              | Mercado de dinero                                                                                                | Mercado de capitales                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Plazo        | Corto plazo: vencimiento ≤ 1 año (la mayoría, menos de 120 días).                                                | Largo plazo                                                                                                   |
| Función      | Dar liquidez de corto plazo a la economía y servir de canal a la política monetaria.                             | Financiar la inversión productiva de largo plazo y diversificar el riesgo entre ahorradores e inversionistas. |
| Emisores     | Instituciones monetarias (bancos comerciales) emiten pasivos usables como medios de pago.                        | Instituciones no monetarias (banca de inversión, aseguradoras, bolsa) emiten bonos y acciones.                |
| Instrumentos | CETES, papel comercial, certificados de depósito, reportos, aceptaciones bancarias, fondeo interbancario (TIIE). | Bonos hipotecarios, acciones ordinarias y preferentes, FIBRAs, certificados bursátiles de largo plazo.        |

> **Ejemplo resuelto.** Clasificar un instrumento combina los dos criterios anteriores: primero quién lo emite, luego a qué plazo.
>
> - *Papel comercial de una empresa a 60 días.* ¿Quién emite? La propia empresa que necesita liquidez → deuda directa. ¿A qué plazo? 60 días, menos de un año → mercado de dinero. Conclusión: deuda directa de mercado de dinero.
> - *Certificado bursátil bancario a 10 años.* ¿Quién emite? Un banco que capta recursos con su propia obligación, no el deudor final al que luego presta → deuda indirecta. ¿A qué plazo? 10 años → mercado de capitales. Conclusión: deuda indirecta de mercado de capitales; el plazo largo no lo convierte en deuda directa.

- En México, los bancos múltiples integran ambas funciones desde principios de la década de 1970.
- Los **mercados de derivados** (futuros, opciones, swaps) son un tercer segmento, definido por el instrumento y no por el plazo; se estudian aparte más adelante en el curso.
- Es, sobre todo, un mercado **mayorista**: operaciones grandes entre bancos, gobierno y empresas, no pensado para el ahorrador individual. En México, CETES es la excepción visible: es accesible al público a través de Cetesdirecto.
- El banco central lo usa como canal de política monetaria: Banxico compra y vende valores gubernamentales en operaciones de mercado abierto, lo que mueve la **TIIE** (tasa de interés interbancaria de equilibrio), la tasa de referencia de corto plazo de la economía.

### 3. Agentes económicos y su acceso a los mercados

Cada tipo de agente participa en el mercado de dinero y en el de capitales de forma distinta.

| Agente económico               | Mercado de dinero (corto plazo)                                      | Mercado de capitales (largo plazo)                                                      |
|--------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Gobierno                       | CETES y otros instrumentos de deuda de corto plazo.                  | Bonos M y Udibonos: deuda de largo plazo.                                               |
| Grandes empresas               | Papel comercial para financiar capital de trabajo.                   | Emisión de obligaciones y colocación de acciones en bolsa.                              |
| PyMEs                          | Crédito bancario de corto plazo, factoraje y crédito de proveedores. | Acceso muy limitado; recurren a banca de desarrollo (NAFIN) en vez de la bolsa pública. |
| Bancos e intermediarios        | Captación de depósitos; actúan como creadores de mercado.            | Colocación y garantía de emisiones (banca de inversión).                                |
| Personas físicas               | Cuentas de ahorro y depósitos a la vista o a plazo.                  | Acceso indirecto vía fondos de inversión, Afores o casas de bolsa.                      |
| Inversionistas institucionales | Instrumentos líquidos de tesorería de corto plazo.                   | Principal fuente de demanda de largo plazo: bonos y acciones.                           |

*Elaboración propia a partir de Mántey de Anguiano (2024), Lección 2, y la organización del mercado de valores mexicano.*

---

## Fuentes y referencias recomendadas

- Mántey de Anguiano, G. (2024). *Lecciones de Economía Monetaria*. UNAM. Lección 2: clasificación de activos y mercado de dinero/capitales.
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 11, "The Money Markets".

---

## Cierre de la unidad — Lo esencial para recordar

- El activo financiero es **deuda directa**, **deuda indirecta** o **participación de capital**, según quién emite la obligación, no según su plazo.
- El **mercado de dinero** (corto plazo, liquidez) y el **mercado de capitales** (largo plazo, inversión productiva) canalizan el ahorro según el plazo; los derivados son un tercer segmento, definido por el instrumento y no por el plazo.
- Cada agente económico (gobierno, empresas, PyMEs, bancos, personas físicas, institucionales) accede de forma distinta a ambos mercados.
- **Plazo y tipo de emisor son clasificaciones independientes**: un instrumento de largo plazo puede seguir siendo deuda indirecta si lo emite un intermediario financiero, no el deudor final.
