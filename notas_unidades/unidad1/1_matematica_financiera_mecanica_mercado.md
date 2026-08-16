# Unidad 1.1 · Matemática Financiera y Mecánica del Mercado

**Mercados de Deuda y Capitales** — Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante pueda calcular el valor de un flujo en el tiempo y entienda cómo se emite, negocia y liquida un instrumento financiero, antes de entrar a la Unidad de Deuda.

## Contenido

| | Tema | Qué cubre |
| --- | --- | --- |
| I | Matemática financiera básica | Interés simple/compuesto, valor presente y futuro, tasas nominal/efectiva, anualidades |
| II | Mecánica operativa del mercado | Mercado primario/secundario, BMV/BIVA, Indeval, calificadoras |
| III | Taller práctico | Ejercicios numéricos y recorrido institucional de un instrumento real |

---

## Parte I — Teoría: Matemática financiera básica

### 1. Interés simple vs. interés compuesto

- **Interés simple** — el interés se retira al final de cada periodo; el principal permanece constante y no genera "interés sobre interés".
- **Interés compuesto** — el interés se queda invertido junto con el principal, así que en el siguiente periodo también genera rendimiento. Es el supuesto que se usa en casi toda la valuación financiera del curso.

*Fuente: Fabozzi, F. J. y Peterson Drake, P. (2009). Finance, Cap. 2 "Mathematics of Finance", p. 13, Wiley.*

### 2. Valor futuro y valor presente de un flujo único

$$FV = PV(1+i)^N \qquad PV = \dfrac{FV}{(1+i)^N}$$

- **i** — tasa de interés por periodo.
- **N** — número de periodos.

> **Ejemplo:** ¿cuánto necesitas invertir hoy para tener \$100,000 en 3 años, si la tasa es 8% anual compuesta?
> PV = 100,000 / (1.08)³ ≈ **\$79,383**

*Fuente: Fabozzi, F. J. y Peterson Drake, P. (2009). Finance, Cap. 2, Ec. (2.1) p. 15 y Ec. (2.5) p. 21, Wiley.*

### 3. Tasa nominal (APR) vs. tasa efectiva (EAR)

$$APR = i \times n \qquad EAR = (1+i)^n - 1$$

- **APR** (*annual percentage rate*) — la tasa "de etiqueta", sin considerar cuántas veces al año se capitaliza.
- **EAR** (*effective annual rate*) — la tasa que realmente se gana/paga en un año, ya con el efecto de la capitalización.
- **n** — número de periodos de capitalización al año.

> **Ejemplo:** un banco ofrece una tasa nominal anual del 12%, capitalizable mensualmente (n = 12, i = 0.12/12 = 0.01).
> EAR = (1.01)¹² − 1 ≈ **12.68%**
>
> La tasa efectiva siempre es mayor o igual a la nominal cuando hay más de una capitalización al año — la diferencia es "el interés que gana el interés".

*Fuente: Fabozzi, F. J. y Peterson Drake, P. (2009). Finance, Cap. 2, Ec. (2.15) p. 48, Wiley.*

### 4. Valor presente de una serie de flujos (anualidad)

$$PV = CF \cdot \dfrac{1-(1+i)^{-N}}{i} \qquad FV = CF \cdot \dfrac{(1+i)^N-1}{i}$$

- **CF** — el flujo (pago) constante que se repite cada periodo.
- Esta es la fórmula que en la Unidad de Deuda se convierte en "el precio de un bono": los cupones son justamente una serie de flujos constantes.

> **Ejemplo:** un instrumento paga \$5,000 de cupón anual durante 5 años. Si la tasa de descuento es 9%:
> PV = 5,000 × [1 − (1.09)⁻⁵] / 0.09 ≈ **\$19,448**

*Fuente: Fabozzi, F. J. y Peterson Drake, P. (2009). Finance, Cap. 2, Ec. (2.9) p. 30 y Ec. (2.11) pp. 32–33, Wiley.*

---

## Parte I — Teoría: Mecánica operativa del mercado

### 5. Mercado primario vs. mercado secundario

- **Mercado primario** — la primera vez que un instrumento se coloca. Ejemplo: Banxico subasta CETES; una empresa hace su oferta pública inicial (OPI) de acciones.
- **Mercado secundario** — la reventa del instrumento entre inversionistas después de esa colocación inicial. El emisor ya no recibe dinero en estas operaciones; solo cambia de manos el título.

### 6. Quién interviene: BMV, BIVA, casas de bolsa, Indeval

- **BMV y BIVA** — las dos bolsas de valores en México, donde se negocian acciones, bonos y otros instrumentos listados.
- **Casas de bolsa** — intermediarios bursátiles; un inversionista no puede operar directamente en la bolsa, necesita una casa de bolsa que ejecute la orden.
- **Indeval** — la institución de custodia y liquidación central. Cuando compras un instrumento, no recibes un papel físico: Indeval mantiene el registro electrónico de quién es dueño de qué, y liquida (hace efectiva) cada operación.

### 7. Calificadoras y riesgo de crédito

- Empresas como **S&P, Moody's, HR Ratings o Fitch** evalúan la capacidad de pago de quien emite deuda y le asignan una calificación (AAA, AA, BBB, etc.).
- Es central para instrumentos de deuda corporativa (papel comercial, certificados bursátiles, bonos corporativos) que se verán en la Unidad de Deuda — a diferencia de la deuda gubernamental, cuyo riesgo de crédito se asume mínimo.

*Fuente: elaboración propia a partir de la organización del mercado de valores mexicano (BMV, BIVA, Indeval, CNBV).*

---

## Parte II — Práctica

### Ejercicio numérico

1. Un banco ofrece una tasa nominal anual del 18%, capitalizable trimestralmente. Calcula la tasa efectiva anual.
   *Respuesta: EAR = (1 + 0.18/4)⁴ − 1 ≈ 19.25%*
2. ¿Cuál es el valor presente de \$50,000 que recibirás en 4 años, si la tasa de descuento es 10% anual?
   *Respuesta: PV = 50,000 / (1.10)⁴ ≈ \$34,151*
3. Un instrumento paga \$2,000 anuales durante 3 años. Con una tasa de descuento de 7%, ¿cuál es su valor presente?
   *Respuesta: PV = 2,000 × [1 − (1.07)⁻³] / 0.07 ≈ \$5,247*

### Taller: recorrido institucional de un CETE

Traza el camino completo de un CETE, identificando qué institución interviene en cada paso:

1. **Subasta primaria** — Banxico subasta el CETE a bancos y casas de bolsa. → *Banxico*
2. **Colocación con el inversionista final** — una casa de bolsa vende el CETE a un cliente (persona física o institucional). → *Casa de bolsa*
3. **Custodia y registro** — el título queda registrado electrónicamente a nombre del inversionista. → *Indeval*
4. **Mercado secundario** — el inversionista decide venderlo antes de su vencimiento a otro inversionista. → *Casa de bolsa (ejecuta la operación) + Indeval (liquida el cambio de dueño)*
5. **Vencimiento** — Banxico paga el valor nominal al tenedor final registrado en Indeval. → *Banxico*

---

## Fuentes y referencias recomendadas

- Fabozzi, F. J. y Peterson Drake, P. (2009). *Finance*. Wiley. — Cap. 2, "Mathematics of Finance": todas las fórmulas de esta unidad.
- Mántey de Anguiano, G. (2024). *Lecciones de Economía Monetaria*. UNAM.
- Portal Banxico — subastas de valores gubernamentales y resultados de CETES/Bonos M.
- Portal Indeval (S.D. Indeval) — qué es la custodia y liquidación de valores.
- Portal BMV / BIVA — cómo funciona el mercado secundario en México.

---

## Cierre de la unidad — Lo esencial para recordar

- **VP y VF son la misma fórmula vista desde los dos lados**: descontar hacia el presente o proyectar hacia el futuro. Toda la valuación de deuda de la siguiente unidad se construye sobre esto.
- La **tasa efectiva** es la que de verdad ganas o pagas en un año; la **nominal** es solo la etiqueta. Entre más frecuente la capitalización, más se separan.
- Una **anualidad** (serie de flujos constantes) es exactamente lo que es el flujo de cupones de un bono — por eso esta fórmula reaparece al valuar deuda.
- Todo instrumento nace en el **mercado primario** y, si es líquido, se revende después en el **secundario**; **Indeval** es quien realmente "guarda" el título, no tú.

**Próxima sesión:** entramos a la Unidad de Deuda — características del mercado de deuda e instrumentos gubernamentales (CETES, Bonos M, UDIBONOS).
