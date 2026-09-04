# Unidad 2 · Valuación de Instrumentos de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante calcule el precio de un instrumento de deuda a partir de sus flujos y su valor nominal.

## Contenido

|     | Tema                                    | Qué cubre                                                              |
| --- | --------------------------------------- | ---------------------------------------------------------------------- |
| I   | Valuación a descuento                   | CETE y papel comercial: la convención de mercado día/360               |
| II  | Valuación con cupón fijo                | Bono M, UDIBONO y bono corporativo: anualidad más flujo único          |
| III | Valuación con cupón variable            | Por qué no hay fórmula cerrada, y qué sí se puede decir del precio     |
| IV  | Amortización de capital                 | Sistema francés, sistema alemán y fondo de amortización (sinking fund) |
| V   | Ejemplo integrador con datos de mercado | Precio de un CETE, un Bono M y un UDIBONO con tasas reales de 2026     |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. Valuación a descuento

Un instrumento a descuento (CETE, papel comercial) tiene un solo flujo distinto de cero, el valor nominal al vencimiento: $(c_0, c_1, \ldots, c_N) = (-v_0,\ 0,\ \ldots,\ 0,\ v_N)$. Su precio es exactamente la fórmula de valor presente de un flujo único de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md#5-valor-futuro-y-valor-presente-de-un-flujo-único), sección 5, con un solo periodo ($N=1$):

$$v_0 = v_N \cdot (1+r)^{-1}$$

El mercado mexicano de dinero no cotiza $r$ como una tasa por periodo cualquiera: cotiza una tasa de rendimiento anual $i$ y prorratea el año usando la convención día/360 (el estándar del mercado de dinero, no de calendario). Sustituyendo $r$ por esa tasa prorrateada:

$$v_0 = \dfrac{v_N}{1+i \cdot \frac{n}{360}}$$

- **$i$**: tasa de rendimiento anual cotizada en la subasta o el mercado secundario.
- **$n$**: número de días por vencer.
- **$v_N$**: valor nominal (\$10 en un CETE, el monto del pagaré en papel comercial).

> **Ejemplo resuelto.** Un CETE a 28 días, valor nominal \$10, se subastó el 1 de septiembre de 2026 a una tasa de rendimiento de 6.49% anual.
> $v_0 = 10 / (1+0.0649 \times \frac{28}{360}) = 10/1.005049 \approx \$9.9498$
>
> La ganancia del inversionista que lo conserva a vencimiento es $10 - 9.9498 = \$0.0502$ por cada CETE de \$10, exactamente el descuento que fija la tasa de la subasta.

### 2. Valuación con cupón fijo

Un instrumento con cupón fijo (Bono M, UDIBONO, bono corporativo a tasa fija) paga el mismo cupón $c$ cada periodo más el valor nominal al vencimiento: $(c_0, c_1, \ldots, c_N) = (-v_0,\ c,\ c,\ \ldots,\ c,\ c+v_N)$. Ese vector es la suma de dos flujos superpuestos: una anualidad de $c$ por periodo ([`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md#7-valor-presente-de-una-serie-de-flujos-anualidad), sección 7) y un flujo único de $v_N$ al final (sección 5, arriba). El valor presente de una suma de flujos es la suma de sus valores presentes:

$$v_0 = c \cdot \dfrac{1-(1+r)^{-N}}{r} + v_N \cdot (1+r)^{-N} \qquad (r \neq 0)$$

- **$c$**: cupón fijo por periodo.
- **$r$**: tasa de descuento (rendimiento de mercado) por periodo.
- **$N$**: número de periodos por vencer.
- **$v_N$**: valor nominal.

Tres casos se siguen directamente de comparar $c$ contra $r$: si $c = r$, $v_0 = v_N$ (el bono se valúa exactamente **a la par**); si $c < r$, $v_0 < v_N$ (**a descuento**, el mercado exige más de lo que paga el cupón); si $c > r$, $v_0 > v_N$ (**con premio**, sobre par).

> **Ejemplo resuelto.** Un Bono M con cupón fijo de 8% anual (simplificando a un solo pago anual en vez de los dos pagos semestrales reales, para no complicar el ejemplo), valor nominal \$100 y 10 años por vencer, se descuenta hoy a la tasa de mercado vigente en 2026 para ese plazo, aproximadamente 9%.
> $v_0 = 8 \cdot \dfrac{1-(1.09)^{-10}}{0.09} + 100 \cdot (1.09)^{-10} \approx 8(6.4177) + 100(0.42241) \approx 51.34 + 42.24 = \$93.58$
>
> Como el cupón (8%) es menor que la tasa de mercado (9%), el bono se valúa a descuento: por debajo de su valor nominal de \$100.

### 3. Valuación con cupón variable

Un instrumento con cupón variable (certificado bursátil referenciado a TIIE) no tiene un vector de flujos completamente determinístico: $(c_0, C_1, C_2, \ldots, C_{N-1}, C_N+v_N)$, con cada $C_t$ dependiendo de la tasa de referencia vigente ese periodo. Sin un patrón constante ni flujos determinísticos no hay fórmula cerrada como la de la sección 2: valuar este instrumento significa proyectar o cubrir cada $C_t$ por separado.

Sí se puede afirmar algo del precio sin proyectar cada flujo. El cupón se recalcula en cada fecha de reseteo para igualar (aproximadamente) la tasa de mercado vigente, así que justo después de cada reseteo el instrumento vuelve a valuarse cerca de su valor nominal, por el mismo argumento de la sección 2 con $c \approx r$: un cupón que siempre se ajusta a la tasa de mercado no se aleja de la par por el nivel general de tasas. Entre reseteos, el precio sí puede desviarse un poco de la par, pero por otras razones (cambio en el riesgo de crédito del emisor, o en la sobretasa que el mercado exigiría para esa misma emisión hoy), no por el nivel general de tasas.

> **Ejemplo resuelto.** El certificado bursátil del BCIE de [`1_instrumentos_deuda.md`](1_instrumentos_deuda.md#3-certificado-bursátil-el-instrumento-híbrido) paga TIIE de fondeo a 28 días (cercana a la tasa de referencia de Banxico, 6.50% en septiembre de 2026) más una sobretasa. En cada fecha de reseteo (cada 28 días), ese cupón vuelve a igualar la tasa de mercado vigente más la sobretasa pactada, así que el precio del certificado se mantiene cerca de su valor nominal durante toda su vida, a diferencia de un Bono M a 10 años, cuyo cupón queda fijo desde la emisión y por eso su precio sí se aleja de la par cuando cambian las tasas (sección 2).

### 4. Amortización de capital

Ningún instrumento mexicano de esta unidad amortiza capital antes del vencimiento (todos son bullet, sección 2 de [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#2-qué-es-un-instrumento-de-deuda)), pero un crédito hipotecario, un préstamo de auto o una emisión corporativa con retiro programado sí lo hacen, y Fabozzi documenta las tres formas como otra característica más de los bonos. Todas comparten la misma estructura de saldo insoluto:

$$s_t = v_0 - \sum_{i=1}^{t} k_i \qquad (s_0 = v_0)$$

donde $k_t$ es el abono a capital del periodo $t$, con $\sum_{t=1}^{N} k_t = v_0$ (el capital completo se termina de pagar en $N$ periodos).

**Sistema francés (pago total constante):** cada pago $c$ es igual, resultado de aplicar la misma fórmula de anualidad de la sección 2 (con $v_N = 0$, porque no hay valor nominal residual al final: todo el capital ya se pagó en abonos):

$$c = v_0 \cdot \dfrac{r}{1-(1+r)^{-N}} \qquad (r \neq 0)$$

El abono a capital de cada periodo se obtiene restando el interés del periodo ($r \cdot s_{t-1}$) al pago total: $k_t = c - r \cdot s_{t-1}$. Como el saldo insoluto baja con el tiempo, el interés baja y el abono implícito sube, aunque el pago total se mantenga fijo.

> **Ejemplo resuelto.** Un crédito hipotecario de \$500,000 a 20 años, tasa fija de 10% anual, sistema francés.
> $c = 500{,}000 \cdot \dfrac{0.10}{1-(1.10)^{-20}} \approx 500{,}000 \times 0.117459 \approx \$58{,}730$ cada año.
> Primer año: interés $= 0.10 \times 500{,}000 = \$50{,}000$; abono a capital $k_1 = 58{,}730 - 50{,}000 = \$8{,}730$; saldo insoluto $s_1 = 500{,}000-8{,}730=\$491{,}270$.

**Sistema alemán (abono a capital constante):** el abono $k_t = v_0/N$ es igual cada periodo, así que el pago total decrece porque el interés se cobra sobre un saldo insoluto cada vez menor:

$$\text{pago}_t = \dfrac{v_0}{N} + r \cdot s_{t-1}$$

> **Ejemplo resuelto.** Mismo crédito (\$500,000, 20 años, 10% anual), sistema alemán.
> $k = 500{,}000/20 = \$25{,}000$ cada año.
> Primer pago $= 25{,}000 + 0.10 \times 500{,}000 = \$75{,}000$; segundo pago $= 25{,}000 + 0.10 \times 475{,}000 = \$72{,}500$: el pago baja \$2,500 cada año, siempre por el mismo abono constante multiplicado por la tasa.

**Fondo de amortización (sinking fund):** el emisor retira una fracción $k_t$ de la emisión cada periodo según un calendario pactado, no necesariamente uniforme (a diferencia del sistema alemán, donde $k_t$ sí es constante), y paga cupón solo sobre el saldo insoluto restante. La fórmula de precio es la misma idea que las dos anteriores, sumando cada pago descontado a su propio periodo:

$$v_0 = \sum_{t=1}^{N} \big(k_t + r \cdot s_{t-1}\big) \cdot (1+r)^{-t}$$

Es el mecanismo típico de una emisión corporativa que retira, por ejemplo, 10% del principal cada año durante los primeros años y el resto al vencimiento, en vez de repartirlo en partes exactamente iguales como el sistema alemán.

*Fuente: Fabozzi, F. J. (2009). Capital Markets, Financial Management, and Investment Management. Wiley. Cap. 19, "Bond Portfolio Management", "Provisions for Paying off Bonds", pp. 683-685.*

### 5. Ejemplo integrador con datos de mercado

Con las fórmulas de las secciones 1 y 2, y las tasas reales citadas en [`0_caracteristicas_mercado_deuda.md`](0_caracteristicas_mercado_deuda.md#1-introducción-institucional-y-funcional-al-mercado-de-deuda) y [`1_instrumentos_deuda.md`](1_instrumentos_deuda.md#1-instrumentos-gubernamentales-cetes-bono-m-y-udibono), se valúan los tres instrumentos gubernamentales a inicios de septiembre de 2026:

| Instrumento     | Fórmula que aplica                                            | Datos                                                         | Precio                          |
| --------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------- |
| CETE 28 días    | Sección 1 (descuento)                                         | $v_N =$ \$10, $i = 6.49\%$, $n = 28$                          | ≈ \$9.9498                      |
| Bono M 10 años  | Sección 2 (cupón fijo), simplificado a un pago anual          | $c =$ \$8, $v_N =$ \$100, $r \approx 9\%$, $N = 10$           | ≈ \$93.58 (a descuento)         |
| UDIBONO 10 años | Sección 2 (cupón fijo), en UDIs, simplificado a un pago anual | $c = r = 4.60\%$ (a la par en UDIs), $v_N = 100$ UDIs, $N=10$ | 100 UDIs × \$8.81 ≈ \$881 pesos |

El UDIBONO del ejemplo se valuó exactamente a la par (100 UDIs) porque su cupón real coincide con la tasa de mercado real vigente para ese plazo; convertirlo a pesos requiere multiplicar por el valor de la UDI del día (\$8.81 al 3 de septiembre de 2026), un paso adicional que ningún instrumento denominado en pesos necesita.

---

## Fuentes y referencias recomendadas

- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press. Cap. 3, "Fixed-Income Securities", pp. 46-58: valuación de bonos a descuento y con cupón a partir del valor presente de sus flujos.
- Fabozzi, F. J. (2009). *Capital Markets, Financial Management, and Investment Management*. Wiley. Cap. 19, "Bond Portfolio Management", "Provisions for Paying off Bonds", pp. 683-685: fórmulas y ejemplos de amortización (sistema francés, sistema alemán, sinking fund).
- Banco de México: convención día/360 para la tasa de rendimiento de CETES; ficha técnica de UDIBONOS (valor de la UDI); resultados de subasta consultados el 3 de septiembre de 2026 para las tasas usadas en los ejemplos.
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson. Cap. 12, "The Bond Market": relación entre cupón, tasa de mercado y precio (a la par, a descuento, con premio).

---

## Cierre de la unidad — Lo esencial para recordar

- El precio de cualquier instrumento de deuda es el **valor presente de su vector de flujos**, la misma idea de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md) aplicada a instrumentos de deuda: **flujo único** para un instrumento a descuento (CETE, papel comercial), **anualidad más flujo único** para un instrumento con cupón fijo (Bono M, UDIBONO, bono corporativo).
- Comparar el cupón contra la tasa de mercado predice el precio sin calcularlo: $c=r$ da un bono **a la par**, $c<r$ da un bono **a descuento**, $c>r$ da un bono **con premio**.
- Un instrumento con **cupón variable** no tiene fórmula cerrada de precio (cada flujo es estocástico), pero como el cupón se reajusta a la tasa de mercado en cada reseteo, su precio se mantiene cerca de la par por esa razón, aunque sí puede desviarse por riesgo de crédito o cambios en la sobretasa.
- La **amortización de capital** (sistema francés, sistema alemán, sinking fund) reparte el capital antes del vencimiento en vez de pagarlo todo de golpe (bullet); ninguno de los seis instrumentos mexicanos de esta unidad la usa, pero es la mecánica de un crédito hipotecario o de auto.
- Con tasas reales de mercado, un CETE a 28 días (6.49%) valúa cerca de su valor nominal (descuento pequeño, por el plazo corto); un Bono M a 10 años con cupón menor a la tasa de mercado valúa por debajo de la par; un UDIBONO a la par en UDIs todavía necesita convertirse a pesos con el valor del día de la UDI.

**Próxima sesión:** los riesgos a los que queda expuesto quien compra un instrumento de deuda (tasa de interés, crédito, inflación, liquidez), más allá del precio que se calculó aquí.
