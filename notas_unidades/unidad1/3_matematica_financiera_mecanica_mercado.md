# Unidad 1.1 · Matemática Financiera y Mecánica del Mercado

**Mercados de Deuda y Capitales** — Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante pueda calcular el valor de un flujo en el tiempo y entienda cómo se emite, negocia y liquida un instrumento financiero, antes de entrar a la Unidad de Deuda.

## Contenido

| | Tema | Qué cubre |
| --- | --- | --- |
| I | Matemática financiera básica | Interés simple/compuesto, valor presente y futuro, tasas nominal/efectiva, anualidades |
| II | Mecánica operativa del mercado | Mercado primario/secundario, BMV/BIVA, Indeval, calificadoras |

> La práctica de este tema (ejercicios y taller) está en [`practica_unidad1.md`](../../practicas/unidad1/practica_unidad1.md).

---

## Parte I — Teoría: Matemática financiera básica

### 1. Interés simple vs. interés compuesto

- **Interés simple** — el interés se retira al final de cada periodo; el capital permanece constante y no genera "interés sobre interés".
- **Interés compuesto** — el interés se queda invertido junto con el capital, así que en el siguiente periodo también genera rendimiento. Es el supuesto que se usa en casi toda la valuación financiera del curso.

*Fuente: Fabozzi, F. J. y Peterson Drake, P. (2009). Finance, Cap. 2 "Mathematics of Finance", p. 13, Wiley.*

### 2. Valor futuro y valor presente de un flujo único

**¿De dónde sale la fórmula?** Parte del interés compuesto de la sección anterior: cada periodo, el capital que tienes crece un factor $(1+r)$ respecto al periodo anterior.

- Al final del periodo 1: $VF_1 = VP(1+r)$
- Al final del periodo 2, ese $VF_1$ vuelve a crecer un factor $(1+r)$: $VF_2 = VF_1(1+r) = VP(1+r)(1+r) = VP(1+r)^2$
- Repitiendo el mismo paso N veces: $VF_N = VP(1+r)^N$

Para despejar VP solo se invierte la operación: dividir entre $(1+r)^N$ deshace exactamente los N pasos de crecimiento compuesto, es decir, trae el flujo futuro de vuelta al presente ("descontarlo").

$$VF = VP(1+r)^N \qquad VP = \dfrac{VF}{(1+r)^N}$$

- **r** — tasa de interés por periodo.
- **N** — número de periodos.

> **Ejemplo:** ¿cuánto necesitas invertir hoy para tener \$100,000 en 3 años, si la tasa es 8% anual compuesta?
> VP = 100,000 / (1.08)³ ≈ **\$79,383**

*Fuente: Fabozzi, F. J. y Peterson Drake, P. (2009). Finance, Cap. 2, Ec. (2.1) p. 15 y Ec. (2.5) p. 21, Wiley.*

### 3. Tasa nominal (TNA) vs. tasa efectiva (TEA)

**¿De dónde sale la fórmula?** La TNA es solo la tasa por periodo multiplicada por el número de periodos del año — una simple regla de tres que ignora que esos intereses también generan intereses. La TEA sí lo considera: aplica la fórmula de la sección anterior con la tasa periódica $r = TNA/n$ capitalizada durante los $n$ periodos del año ($VF = VP(1+r)^n$), y le resta el capital inicial para quedarse solo con el rendimiento neto del año:

$$TNA = r \times n \qquad TEA = (1+r)^n - 1$$

- **TNA** (tasa nominal anual) — la tasa "de etiqueta", sin considerar cuántas veces al año se capitaliza.
- **TEA** (tasa efectiva anual) — la tasa que realmente se gana/paga en un año, ya con el efecto de la capitalización.
- **n** — número de periodos de capitalización al año.
- **r** — tasa de interés por periodo de capitalización, $r = TNA/n$.

> **Ejemplo:** un banco ofrece una tasa nominal anual del 12%, capitalizable mensualmente (n = 12, r = 0.12/12 = 0.01).
> TEA = (1.01)¹² − 1 ≈ **12.68%**
>
> La tasa efectiva siempre es mayor o igual a la nominal cuando hay más de una capitalización al año — la diferencia es "el interés que gana el interés".

*Fuente: Fabozzi, F. J. y Peterson Drake, P. (2009). Finance, Cap. 2, Ec. (2.15) p. 48, Wiley.*

### 4. Valor presente de una serie de flujos (anualidad)

**¿De dónde sale la fórmula?** Una anualidad no es más que varios flujos únicos, cada uno descontado con la fórmula de la sección 2 según cuántos periodos falten para recibirlo, y luego sumados:

$$VP = \dfrac{FC}{(1+r)^1} + \dfrac{FC}{(1+r)^2} + \dots + \dfrac{FC}{(1+r)^N} = FC\sum_{t=1}^{N}\dfrac{1}{(1+r)^t}$$

Esa suma es una serie geométrica; al resolverla término por término se simplifica en una sola fracción (válida para $r \neq 0$, ya que se divide entre $r$; si $r = 0$ no hay descuento que aplicar y simplemente $VP = FC \cdot N$), lo que evita sumar a mano cuando N es grande:

$$VP = FC \cdot \dfrac{1-(1+r)^{-N}}{r} \qquad VF = FC \cdot \dfrac{(1+r)^N-1}{r} \qquad (r \neq 0)$$

- **FC** — el flujo (pago) constante que se repite cada periodo.
- Esta es la fórmula que en la Unidad de Deuda se convierte en "el precio de un bono": los cupones son justamente una serie de flujos constantes.

> **Ejemplo:** un instrumento paga \$5,000 de cupón anual durante 5 años. Si la tasa de descuento es 9%:
> VP = 5,000 × [1 − (1.09)⁻⁵] / 0.09 ≈ **\$19,448**

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
