# Unidad 2 · Valuación de Instrumentos de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante calcule el precio de un instrumento de deuda a partir de sus flujos y su valor nominal.

## Contenido

|     | Tema                                                   | Qué cubre                                                               |
| --- | ------------------------------------------------------ | ----------------------------------------------------------------------- |
| I   | Los flujos de un bono y las incógnitas que se despejan | El vector de flujos, y qué despejan el valor presente y el valor futuro |
| II  | Valuación a descuento                                  | CETE y papel comercial: la convención de mercado día/360                |
| III | Valuación con cupón fijo                               | Bono M, UDIBONO y bono corporativo: anualidad más flujo único           |
| IV  | Valuación con cupón variable                           | Por qué no hay fórmula cerrada, y qué sí se puede decir del precio      |
| V   | Amortización de capital                                | Sistema francés, sistema alemán y fondo de amortización (sinking fund)  |
| VI  | Ejemplo integrador con datos de mercado                | Precio de un CETE, un Bono M y un UDIBONO con tasas de mercado de 2026  |

> La práctica de este tema está en [`practica_unidad2.md`](../../practicas/unidad2/practica_unidad2.md).

---

### 1. Los flujos de un bono y las incógnitas que se despejan

Suponemos un instrumento de deuda que se compra en $t=0$ y vence en $t=N$, donde $t$ cuenta periodos (el intervalo entre un pago y el siguiente). Su vector de flujos $(c_0, c_1, \ldots, c_N)$, el que se construyó en [`0_mercado_e_instrumentos_deuda.md`](0_mercado_e_instrumentos_deuda.md#2-cómo-paga-un-instrumento-mecánicas-y-vector-de-flujos), lista lo que sale o entra de nuestro bolsillo en cada fecha: $c_0=-a$ es el capital pagado al comprar (negativo, porque sale) y cada $c_t$, con $t \geq 1$, es lo que el instrumento paga al final del periodo $t$ (positivo, porque entra), sea cupón, valor nominal o ambos. Dos instrumentos reales lo ilustran:

- **CETE a 28 días.** El 21 de septiembre de 2026, cetesdirecto ofrecía el CETE de un mes a \$9.95, con valor nominal de \$10 pagado al vencimiento. Es un solo periodo ($N=1$, de 28 días): $(c_0, c_1) = (-9.95,\ 10)$.
- **Bono M con cupón de 18%.** Es el ejemplo oficial de la descripción técnica de Banxico (con fechas del año 2000): valor nominal de \$100, cupón de \$9.10 cada 182 días y seis cupones por cobrar, el primero a los 161 días porque ya corrieron 21 del cupón vigente. Sus flujos son $(c_0, c_1, \ldots, c_6) = (-a,\ 9.10,\ 9.10,\ 9.10,\ 9.10,\ 9.10,\ 109.10)$, con el valor nominal sumado al último cupón. El capital $a$ que Banxico obtiene para ese bono, \$98.81269, se calcula en la sección 3.

Ambos vectores tienen la misma forma general y solo cambian en cuántos flujos hay entre $c_0$ y $c_N$: el CETE no tiene ninguno intermedio, y el Bono M tiene cinco cupones antes del último pago.

El vector, por sí solo, no dice cuánto vale el instrumento: \$10 dentro de 28 días y \$109.10 dentro de casi tres años no se pueden sumar, porque no están en la misma fecha. La fórmula de valor presente de un flujo único de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md#6-valor-futuro-y-valor-presente-de-un-flujo-único) lleva cada $c_t$ a hoy como $c_t(1+r)^{-t}$, y como el valor de una suma de flujos es la suma de sus valores, el vector completo vale hoy

$$v_0 = \sum_{t=1}^{N} c_t(1+r)^{-t}$$

que es la suma de la anualidad de esa misma nota (sección 7), con un $c_t$ distinto en cada periodo en vez de un $c$ constante. Esta relación liga el vector, la tasa $r$ y el precio $a$, y cuando se conocen todas las piezas menos una, la fórmula la despeja. Cada incógnita corresponde a una de las categorías de problemas típicos de inversión de la misma nota (sección 3):

- **El precio $a$, dados los flujos y la tasa: fijación de precio (pricing).** La pregunta es qué precio es consistente con lo que ofrece el resto del mercado, y la tasa $r$ con que se descuenta es justo esa referencia del mercado. Se calcula $v_0$ y ese es el precio.
- **El pago $c$, dados el capital, la tasa y el plazo: también fijación de precio, del lado de quien pide prestado.** Qué pago periódico es consistente con la tasa que exige el mercado. Se despeja $c$ de la fórmula de anualidad con $v_0=a$; así se calcula la mensualidad de un crédito (sección 5) y el cupón implícito del apéndice.
- **La tasa $r$, dados el precio y los flujos: inversión pura.** Para decidir dónde colocar el capital hay que comparar lo que rinde cada alternativa. Se busca la $r$ que hace $v_0=a$, la misma idea de la TIR de la unidad 1 aplicada a un bono; es el tema de [`2_rendimiento_y_curva_de_rendimientos.md`](2_rendimiento_y_curva_de_rendimientos.md).
- **El valor en una fecha futura, dado el valor de hoy: cobertura (hedging).** Cubrir una obligación que vence más adelante exige saber cuánto valdrá cada flujo en esa fecha. La fórmula de valor futuro, $v_t=v_0(1+r)^t$, lleva el resultado hacia adelante; es lo que hay detrás del riesgo de reinversión de [`3_riesgos_mercado_deuda.md`](3_riesgos_mercado_deuda.md) y de las estrategias de [`5_estrategias_renta_fija.md`](5_estrategias_renta_fija.md).

Importa por tres razones. El mercado cotiza tasas, no precios (el CETE se anuncia a 6.25%, y quien lo compra necesita saber cuántos pesos pagar). La fórmula pone en la misma fecha flujos que llegan en fechas distintas, así que permite comparar un CETE que paga una sola vez contra un Bono M que paga seis. Y es una sola relación entre precio, tasa y flujos: saber despejar cualquiera de las tres es lo que sostiene el resto de la unidad (rendimiento, riesgos, duración).

Esta nota resuelve la primera incógnita, el precio, recorriendo los tres vectores en el orden en que la suma se vuelve más difícil: un solo término (sección 2, a descuento), una anualidad más un término (sección 3, cupón fijo) y términos que todavía no se conocen (sección 4, cupón variable). La sección 5 resuelve la segunda, el pago, y la sección 6 aplica el precio con datos reales.

### 2. Valuación a descuento

El caso más simple de la suma de la sección 1 es el del CETE: un solo término. Resolverlo es el problema de fijación de precio en su forma mínima (cuántos pesos vale hoy el pago del vencimiento), y el dato que lo determina es la tasa que cotiza el mercado. En septiembre de 2026, el CETE a 28 días rindió 6.13% en la subasta del 1 de septiembre y 6.25% en la del 15; el 21 de septiembre, el Bono M a 10 años rendía 9.16%. Hablar de "la" tasa de interés como si fuera un solo número deja de tener sentido en cuanto se pregunta a qué plazo: cada plazo trae su propio precio, y esta nota calcula ese precio a partir de la tasa que le corresponde a cada instrumento, empezando por el más simple.

Un instrumento a descuento (CETE, papel comercial) tiene un solo flujo distinto de cero, el valor nominal al vencimiento: así que basta un solo periodo, del día de compra al vencimiento ($N=1$), y el vector es $(c_0, c_1) = (-a,\ v_N)$, como el del CETE de la sección 1. Su precio, lo que se paga al comprarlo ($a$), es su valor presente $v_0$: la suma de la sección 1 se reduce a un término, exactamente la fórmula de valor presente de un flujo único de la sección 6 de la unidad 1:

$$v_0 = v_N(1+r)^{-1}$$

El mercado mexicano de dinero no cotiza $r$ como una tasa por periodo cualquiera: cotiza una tasa nominal anual $r_{nom}$ y la prorratea al plazo exacto del instrumento con la convención día/360: los días de vida se cuentan en el calendario, pero el año se toma de 360 días en vez de 365 (el estándar del mercado de dinero). Es la misma idea de $r_{per} = r_{nom}\times \Delta t$ de la sección 10 de la nota de la unidad 1, aquí con $\Delta t = n_{dias}/360$. Esta $n_{dias}$ no es la $n$ de esa sección, que contaba los subperiodos de capitalización en que se divide el año ($r_{per}=r_{nom}/n$, con $\Delta t=1/n$): $n_{dias}$ cuenta los días de vida que le quedan al instrumento, y $\Delta t$ es esa fracción de un año de 360 días. Sustituyendo $r$ por esa tasa periódica prorrateada, $r_{per}=r_{nom}\frac{n_{dias}}{360}$:

$$v_0 = \dfrac{v_N}{1+r_{nom}\frac{n_{dias}}{360}}$$

- **$r_{nom}$**: tasa de rendimiento anual cotizada en la subasta o el mercado secundario.
- **$n_{dias}$**: número de días por vencer del instrumento (no confundir con la $n$ de subperiodos de capitalización de la unidad 1).
- **$v_N$**: valor nominal (\$10 en un CETE, el monto del pagaré en papel comercial).

> **Ejemplo resuelto.** Un CETE a 28 días, valor nominal \$10, se colocó en la subasta del 15 de septiembre de 2026 a una tasa de rendimiento de 6.25% anual.
>
> - **Fórmula general:** $v_0 = \dfrac{v_N}{1+r_{nom}\frac{n_{dias}}{360}}$
> - **Datos:** $v_N = 10$, $r_{nom} = 0.0625$, $n_{dias} = 28$
> - **Paso 1, tasa del periodo:** $r_{per} = r_{nom}\frac{n_{dias}}{360} = 0.0625 \times \frac{28}{360} = 0.004861$
> - **Paso 2, valor presente:** $v_0 = \dfrac{v_N}{1+r_{per}} = \dfrac{10}{1.004861} \approx \$9.9516$
>
> La ganancia del inversionista que lo conserva a vencimiento es $10 - 9.9516 = \$0.0484$ por cada CETE de \$10, exactamente el descuento que fija la tasa de la subasta.
>
> **Ejemplo resuelto: el plazo con la misma tasa.** El mismo CETE de \$10 con $r_{nom}=0.0625$ y distinto plazo (ilustrativo: el mercado cotiza una tasa distinta por plazo, pero aquí se fija para aislar el efecto de $n_{dias}$). En cada fila se aplica la misma fórmula general, el paso 1 para $r_{per}$ y el paso 2 para $v_0$:
>
> | $n_{dias}$ | $r_{per} = 0.0625\frac{n_{dias}}{360}$ | $1+r_{per}$ | $v_0 = 10/(1+r_{per})$ | Descuento $10-v_0$ |
> | ---------- | -------------------------------------- | ----------- | ---------------------- | ------------------ |
> | 28         | 0.004861                               | 1.004861    | \$9.9516               | \$0.0484           |
> | 91         | 0.015799                               | 1.015799    | \$9.8445               | \$0.1555           |
> | 182        | 0.031597                               | 1.031597    | \$9.6937               | \$0.3063           |
> | 364        | 0.063194                               | 1.063194    | \$9.4056               | \$0.5944           |
>
> El descuento crece casi en proporción al plazo, así que el precio por sí solo no compara instrumentos de plazos distintos: para eso se compara la tasa.
>
> **Ejemplo resuelto: papel comercial (ilustrativo).** Una empresa emite un pagaré de \$1,000,000 a 60 días con un rendimiento de 7.00% anual. Las cifras están inventadas para ilustrar y no corresponden a una emisión real.
>
> - **Fórmula general:** $v_0 = \dfrac{v_N}{1+r_{nom}\frac{n_{dias}}{360}}$
> - **Datos:** $v_N = 1,000,000$, $r_{nom} = 0.07$, $n_{dias} = 60$
> - **Paso 1, tasa del periodo:** $r_{per} = 0.07 \times \frac{60}{360} = 0.011667$
> - **Paso 2, valor presente:** $v_0 = \dfrac{1,000,000}{1.011667} \approx \$988,468$
>
> La empresa recibe \$988,468 hoy y paga \$1,000,000 en 60 días; los \$11,532 de diferencia son su costo de financiamiento por ese plazo. Es la misma fórmula del CETE: solo cambian el emisor y el valor nominal.
>
> **En la práctica.** El resultado de la subasta se difunde como tasa de rendimiento, no como precio; el precio se deriva con esta fórmula. El 21 de septiembre de 2026, la tabla de CETES de cetesdirecto mostraba el plazo de un mes a 6.25% con precio de \$9.95, y el de tres meses (91 días) a 6.66% con precio de \$9.83: $10/(1+0.0666\frac{91}{360}) \approx \$9.8344$. La plataforma solo convierte la tasa en el precio que ve el inversionista.

### 3. Valuación con cupón fijo

Un instrumento con cupón fijo (Bono M, UDIBONO, bono corporativo a tasa fija) es el segundo vector de la sección 1: paga el mismo cupón $c$ cada periodo más el valor nominal al vencimiento, $(c_0, c_1, \ldots, c_N) = (-a,\ c,\ c,\ \ldots,\ c,\ c+v_N)$. Con $c_t=c$ en cada periodo y $c_N=c+v_N$, la suma de la sección 1 se parte en dos flujos superpuestos: una anualidad de $c$ por periodo (sección 7 de la unidad 1) y un flujo único de $v_N$ al final, el de la sección 2. Como el valor presente de una suma de flujos es la suma de sus valores presentes:

$$v_0 = c\dfrac{1-(1+r)^{-N}}{r} + v_N(1+r)^{-N} \qquad (r \neq 0)$$

- **$c$**: cupón fijo por periodo.
- **$r$**: tasa de descuento (rendimiento de mercado) por periodo.
- **$N$**: número de periodos por vencer.
- **$v_N$**: valor nominal.

Tres casos se siguen directamente de comparar el cupón $c$ contra lo que el mercado paga por el mismo capital en un periodo, $rv_N$ (es decir, la tasa cupón $c/v_N$ contra la tasa de mercado $r$): si $c = rv_N$, $v_0 = v_N$ (el bono se valúa exactamente **a la par**); si $c < rv_N$, $v_0 < v_N$ (**a descuento**, el mercado exige más de lo que paga el cupón); si $c > rv_N$, $v_0 > v_N$ (**con premio**, sobre par).

![Precio de tres bonos a 10 años con cupón de 12%, 9% y 6% y tasa de mercado de 9% constante: el de 12% baja de 119 a 100, el de 9% se queda en 100 y el de 6% sube de 81 a 100](img/precio_hacia_la_par.png)

Si la tasa de mercado no cambia, los tres bonos llegan al valor nominal en el vencimiento (convergencia a la par, o *pull to par*): el premio o el descuento es el valor presente de la diferencia entre el cupón y lo que exige el mercado, y esa diferencia tiene cada año menos periodos por cobrar.

> **Ejemplo resuelto.** Un Bono M con cupón fijo de 8% anual (simplificando a un solo pago anual en vez de los dos pagos semestrales reales, para no complicar el ejemplo), valor nominal \$100 y 10 años por vencer, se descuenta hoy a la tasa de mercado de ese plazo, aproximadamente 9% (el Bono M a 10 años rendía 9.16% el 21 de septiembre de 2026, según cetesdirecto).
>
> - **Fórmula general:** $v_0 = c\dfrac{1-(1+r)^{-N}}{r} + v_N(1+r)^{-N}$
> - **Datos:** $c = 8$, $r = 0.09$, $N = 10$, $v_N = 100$
> - **Paso 1, factor de descuento:** $(1+r)^{-N} = (1.09)^{-10} = 0.42241$
> - **Paso 2, factor de anualidad:** $\dfrac{1-(1+r)^{-N}}{r} = \dfrac{1-0.42241}{0.09} = 6.4177$
> - **Paso 3, valor presente de los cupones:** $c \times 6.4177 = 8 \times 6.4177 = 51.34$
> - **Paso 4, valor presente del valor nominal:** $v_N(1+r)^{-N} = 100 \times 0.42241 = 42.24$
> - **Paso 5, suma:** $v_0 = 51.34 + 42.24 = \$93.58$
>
> Como el cupón (8%) es menor que la tasa de mercado (9%), el bono se valúa a descuento: por debajo de su valor nominal de \$100.
>
> **Ejemplo resuelto: el mismo cupón a dos plazos.** Un Bono M con el mismo cupón ilustrativo de 8% anual (un pago anual, valor nominal \$100), valuado con las tasas del 21 de septiembre de 2026 que publicó cetesdirecto: 8.24% a 3 años y 9.87% a 30 años. Los pasos 1 a 5 son los del ejemplo anterior, con $c = 8$ y $v_N = 100$ en ambos casos:
>
> | Paso                                  | 3 años                | 30 años                |
> | ------------------------------------- | --------------------- | ---------------------- |
> | Datos $r$ y $N$                       | $r = 0.0824$, $N = 3$ | $r = 0.0987$, $N = 30$ |
> | 1. Factor $(1+r)^{-N}$                | 0.78856               | 0.05938                |
> | 2. Anualidad $\frac{1-(1+r)^{-N}}{r}$ | 2.5660                | 9.5301                 |
> | 3. Cupones $8 \times$ anualidad       | 20.528                | 76.241                 |
> | 4. Nominal $100 \times$ factor        | 78.856                | 5.938                  |
> | 5. Suma $v_0$                         | \$99.384              | \$82.179               |
> | Diferencia con la par                 | -\$0.62               | -\$17.82               |
>
> Los dos están a descuento porque el cupón (8%) es menor que la tasa, pero el de 3 años cae solo \$0.62 bajo la par y el de 30 años \$17.82 por dos razones que se suman: a 30 años la diferencia entre cupón y tasa es mayor (1.87 puntos contra 0.24) y además se acumula durante diez veces más periodos. Los precios publicados (\$100.94 y \$84.22) difieren porque las series reales tienen su propio cupón; el apéndice lo despeja.
>
> **Ejemplo resuelto: bono corporativo con premio (ilustrativo).** Un bono corporativo a tasa fija con cupón de 10% anual, valor nominal \$100 y 5 años por vencer, cuando el mercado exige 8% a ese plazo. Las cifras están inventadas para ilustrar.
>
> - **Fórmula general:** $v_0 = c\dfrac{1-(1+r)^{-N}}{r} + v_N(1+r)^{-N}$
> - **Datos:** $c = 10$, $r = 0.08$, $N = 5$, $v_N = 100$
> - **Paso 1, factor de descuento:** $(1.08)^{-5} = 0.68058$
> - **Paso 2, factor de anualidad:** $\dfrac{1-0.68058}{0.08} = 3.9927$
> - **Paso 3, valor presente de los cupones:** $10 \times 3.9927 = 39.93$
> - **Paso 4, valor presente del valor nominal:** $100 \times 0.68058 = 68.06$
> - **Paso 5, suma:** $v_0 = 39.93 + 68.06 = \$107.99$
> - **Paso 6, de dónde viene el premio:** como $v_N\left(1-(1+r)^{-N}\right) = rv_N\dfrac{1-(1+r)^{-N}}{r}$, restar $v_N$ a la fórmula general da $v_0 - v_N = (c - rv_N)\dfrac{1-(1+r)^{-N}}{r}$, el valor presente de la diferencia entre el cupón y lo que el mercado paga por el mismo capital. Aquí $(10 - 0.08 \times 100) \times 3.9927 = 2 \times 3.9927 \approx \$7.99$, igual que $107.99 - 100$.
>
> Como el cupón (10%) es mayor que la tasa (8%), el bono se valúa con premio, y ese premio se irá extinguiendo hasta el vencimiento.
>
> **En la práctica.** El mercado real no simplifica tres cosas que este ejemplo sí. Primero, según la descripción técnica de Banxico, el Bono M tiene valor nominal de \$100 y paga cupón cada 182 días, con intereses calculados sobre los días efectivos y base de 360: $c = v_N r_{cup}\dfrac{182}{360}$, con $r_{cup}$ la tasa cupón anual. Segundo, se cotiza el rendimiento al vencimiento, no el precio; el precio sale de descontar todos los flujos con el mismo factor por periodo, $1+r_{per}$, con $r_{per}=r_{nom}\dfrac{182}{360}$ y $r_{nom}$ el rendimiento anual cotizado. Tercero, cuando ya corre un cupón, lo que se cotiza es el **precio limpio**, sin los intereses devengados de los $d$ días transcurridos, $v_N r_{cup}\dfrac{d}{360}$; al liquidar se suman y resulta el **precio sucio**.
>
> Banxico documenta el cálculo con un ejemplo oficial (con fechas del año 2000): un Bono M con cupón de 18% ($c = \$9.10$ por periodo), seis cupones por cobrar, 21 días transcurridos del cupón vigente y un rendimiento de 19%, es decir $r_{per} = 0.19\times\frac{182}{360} \approx 0.0961$ por periodo. Se suman el primer cupón, los cinco siguientes como anualidad y el valor nominal descontado cinco periodos: $9.10 + 34.8466 + 63.2175 = 107.1641$. Ese valor corresponde a la próxima fecha de cupón; se descuentan los $161/182$ de periodo que faltan (el mismo factor $(1+r)^{-t}$ con $t$ fraccionario) y resulta el precio sucio, \$98.81269. Restar el interés devengado, $9.10 \times 21/182 = \$1.05$, da el precio limpio, \$97.76269.

### 4. Valuación con cupón variable

La suma de la sección 1 supone que los $c_t$ se conocen hoy. Un instrumento con cupón variable (certificado bursátil referenciado a TIIE) no lo cumple, porque no tiene un vector de flujos completamente determinístico: $(c_0, C_1, C_2, \ldots, C_{N-1}, C_N+v_N)$, con cada $C_t$ dependiendo de la tasa de referencia vigente ese periodo. Sin un patrón constante ni flujos determinísticos no hay fórmula cerrada como la de la sección 3: la suma sigue valiendo, pero sus términos $C_t$ todavía no existen, así que valuar este instrumento significa proyectar o cubrir cada $C_t$ por separado.

Sí se puede afirmar algo del precio sin proyectar cada flujo. El cupón se recalcula en cada fecha de revisión de tasa (reseteo, *reset*) para igualar la tasa de referencia vigente más la sobretasa pactada. Si el mercado sigue exigiendo esa misma sobretasa, justo después de cada revisión el instrumento vuelve a valer su valor nominal, por el mismo argumento de la sección 3 con $c = rv_N$: un cupón que se ajusta a la tasa de mercado no se aleja de la par por el nivel general de tasas. Entre dos revisiones el nivel de tasas sí mueve un poco el precio, pero solo durante la fracción de periodo que falta para la siguiente. Lo que puede alejarlo de la par de forma duradera es otra cosa: un cambio en la sobretasa que el mercado exigiría hoy a esa misma emisión (por ejemplo, porque empeoró el riesgo de crédito del emisor), y ese cambio pesa en cualquier fecha, incluso justo después de una revisión. El apéndice lo comprueba con una simulación de 10,000 escenarios de tasas.

> **Ejemplo resuelto.** El certificado bursátil del BCIE de la sección 6 de la nota anterior paga TIIE de fondeo a 28 días (cercana a la tasa objetivo de Banxico, que se mantuvo en 6.50% en la decisión del 6 de agosto de 2026) más una sobretasa. El cupón de cada periodo de 28 días se calcula con la TIIE de fondeo de ese periodo más la sobretasa pactada, que no cambia. Como el cupón sigue así a la tasa de mercado, el certificado siempre paga lo que el mercado exige (más su sobretasa) y su precio se mantiene cerca del valor nominal durante toda su vida, a diferencia de un Bono M a 10 años, cuyo cupón queda fijo desde la emisión y por eso su precio sí se aleja de la par cuando cambian las tasas (sección 3).
>
> **Ejemplo resuelto: certificado cuya sobretasa se encarece (ilustrativo).** Un certificado bursátil corporativo a 2 años (26 cupones de 28 días) paga la TIIE de fondeo más una sobretasa pactada de 0.50%. Las cifras están inventadas para ilustrar.
>
> ¿Por qué exigiría el mercado más? La TIIE de fondeo paga el uso del dinero sin riesgo de impago; la sobretasa paga el riesgo de que el emisor no cumpla. El 0.50% se pactó con lo que se sabía del emisor al emitir. Si después su situación empeora (sus ventas caen, se endeuda más o una calificadora le baja la calificación), la probabilidad de que no pague sube, y quien vaya a prestarle hoy pide más compensación por ese riesgo: aquí, 0.90%. Es la sobretasa que el emisor tendría que ofrecer si emitiera hoy un certificado nuevo, y la que exige cualquier comprador del certificado viejo. Para aislar el efecto, la TIIE de fondeo se supone constante en 6.50%; así todos los cupones son iguales y aplica la fórmula de la sección 3.
>
> - **Fórmula general:** $v_0 = c\dfrac{1-(1+r)^{-N}}{r} + v_N(1+r)^{-N}$
> - **Datos:** $v_N = 100$, $N = 26$, TIIE de fondeo $r_{fond} = 0.065$, sobretasa pactada $m_{pac} = 0.005$, sobretasa exigida $m_{mer} = 0.009$, periodos de 28 días
> - **Paso 1, cupón por periodo:** $c = v_N(r_{fond}+m_{pac})\frac{28}{360} = 100 \times 0.07 \times \frac{28}{360} = 0.5444$
> - **Paso 2, tasa de descuento por periodo:** $r = (r_{fond}+m_{mer})\frac{28}{360} = 0.074 \times \frac{28}{360} = 0.005756$
> - **Paso 3, factores:** $(1+r)^{-26} = 0.86138$ y $\dfrac{1-0.86138}{0.005756} = 24.0839$
> - **Paso 4, valores presentes:** cupones $0.5444 \times 24.0839 = 13.112$; valor nominal $100 \times 0.86138 = 86.138$
> - **Paso 5, suma:** $v_0 = 13.112 + 86.138 = \$99.25$
>
> Si el mercado siguiera exigiendo solo 0.50%, el paso 2 daría $r = 0.07 \times \frac{28}{360}$, igual a $c/v_N$, el caso $c = rv_N$ de la sección 3, y el certificado valdría exactamente \$100. El resultado de \$99.25 se puede ver también con la diferencia de la sección 3: $(c - rv_N)\dfrac{1-(1+r)^{-N}}{r} = (0.5444 - 0.5756) \times 24.0839 = -\$0.75$. El certificado deja de pagar \$0.0311 por periodo respecto a lo que el mercado exige, durante 26 periodos, y ese es todo el ajuste: cae por el crédito del emisor, no por el nivel de la TIIE de fondeo.
>
> ¿Qué implica en la práctica? Depende de quién se mire:
>
> - **Quien ya tiene el certificado y vende hoy** recibe \$99.25 por cada \$100: pierde \$0.75. Un fondo de inversión, que valúa sus posiciones a precio de mercado todos los días, registra esa pérdida aunque no venda.
> - **Quien lo conserva hasta el vencimiento** cobra los \$100 si el emisor paga, así que no pierde capital; pero durante dos años recibe 0.50% de sobretasa por un riesgo que el mercado ya cobra a 0.90%. La pérdida es de oportunidad, y además carga un riesgo mayor que el que aceptó al comprar.
> - **Quien lo compra hoy a \$99.25** cobra los mismos cupones y además los \$0.75 de diferencia al vencimiento, y con eso gana TIIE de fondeo más 0.90%, justo lo que el mercado exige por ese emisor.
> - **El emisor** no paga más por este certificado, cuyo cupón ya está pactado, pero cualquier deuda nueva le costará 0.90% sobre la TIIE en vez de 0.50%.
>
> **En la práctica.** Banxico documenta cómo se valúa el Bonde F, el bono gubernamental de cupón variable: valor nominal de \$100 y cupón cada 28 días igual a la TIIE de Fondeo a un día capitalizada día con día, de modo que el monto se conoce hasta el final del periodo. A diferencia del certificado del BCIE, su cupón no lleva sobretasa pactada; la sobretasa (margen de descuento, *discount margin*) $m$ aparece solo al valuar. Tampoco se pronostica cada $C_t$: se proyectan los cupones con la última tasa conocida, constante, y se descuentan con esa tasa más $m$, que es lo que se cotiza. Otros participantes proyectan con las tasas forward de la curva, las que el mercado ya trae implícitas, pero ninguno necesita adivinar hacia dónde irá la tasa. Con $m=0$ en una fecha de revisión de tasa el instrumento vale exactamente la par, y en cualquier otro caso se aparta de ella según $m$ y los periodos que le quedan, no según el nivel general de tasas.
>
> **Ejemplo resuelto: el Bonde F de Banxico.** Caso oficial (con fechas del año 2021): TIIE de Fondeo conocida $r_{fond}=0.0403$, sobretasa $m=0.0010$, $N=13$ cupones por cobrar (357 días por vencer, incluido el vigente) y $d=7$ días devengados del cupón vigente, cuya tasa anual capitalizada fue $r_{dev}=0.04049938$ (con dos decimales en porcentaje, 4.05%, para el interés devengado).
>
> ¿De dónde sale la fórmula? Es la del Bono M oficial de la sección 3 con periodos de 28 días: el cupón vigente $c_1$, los $N-1$ siguientes como anualidad y el valor nominal, todo valuado a la próxima fecha de cupón y descontado la fracción de periodo $1-d/28$ que falta. Cambian dos cosas: el cupón se capitaliza día con día, y la tasa de descuento incluye la sobretasa.
>
> - **Fórmula general:** $v_{sucio} = \left[c_1 + c\dfrac{1-(1+r_{per})^{-(N-1)}}{r_{per}} + v_N(1+r_{per})^{-(N-1)}\right](1+r_{per})^{-(1-d/28)}$ y $v_{limpio} = v_{sucio} - v_N r_{dev}\dfrac{d}{360}$
> - **Tasa de descuento por periodo:** $r_{per} = \left(1+\dfrac{r_{fond}+m}{360}\right)^{28} - 1$, la tasa diaria más la sobretasa, capitalizada 28 días
> - **Cupón de los periodos siguientes:** $c = v_N\left[\left(1+\dfrac{r_{fond}}{360}\right)^{28} - 1\right]$, proyectado con la última tasa conocida constante
> - **Cupón vigente:** $c_1 = v_N\left[\left(1+r_{dev}\dfrac{d}{360}\right)\left(1+\dfrac{r_{fond}}{360}\right)^{28-d} - 1\right]$, con los $d$ días ya observados y los $28-d$ restantes a la última tasa
>
> Con $v_N = 100$, la sustitución paso a paso es:
>
> - **Paso 1, tasa de descuento:** $r_{per} = (1 + 0.0413/360)^{28} - 1 = 0.0032172$
> - **Paso 2, cupón siguiente:** $c = 100 \times \left[(1 + 0.0403/360)^{28} - 1\right] = 0.313919$
> - **Paso 3, cupón vigente:** $c_1 = 100 \times \left[(1 + 0.04049938 \times 7/360)(1 + 0.0403/360)^{21} - 1\right] = 0.314281$
> - **Paso 4, factores:** $(1+r_{per})^{-12} = 0.962189$ y $\dfrac{1-0.962189}{0.0032172} = 11.7528$
> - **Paso 5, valor en la próxima fecha de cupón:** $c_1 + c \times 11.7528 + v_N \times 0.962189 = 0.314281 + 3.68942 + 96.2189 = 100.2226$
> - **Paso 6, fracción de periodo:** $(1.0032172)^{-0.75} = 0.997594$, así que $v_{sucio} = 100.2226 \times 0.997594 = \$99.98144$
> - **Paso 7, interés devengado y precio limpio:** $100 \times 0.0405 \times 7/360 = \$0.07875$, y $v_{limpio} = 99.98144 - 0.07875 = \$99.90269$
>
> El resultado coincide con el de Banxico, unos diez centavos bajo la par por 0.10% de sobretasa. Cambiando solo $m$ en el paso 1 y repitiendo los pasos 4 a 7 se obtiene la tabla siguiente. El renglón de 0.10% es el oficial; los otros dos son cálculo propio con el mismo método, no cifras publicadas.
>
> | $m$   | $r_{per}$ | Valor en la próxima fecha de cupón | $v_{sucio}$ | $v_{limpio}$ | $100 - v_{limpio}$ |
> | ----- | --------- | ---------------------------------- | ----------- | ------------ | ------------------ |
> | 0.00% | 0.0031392 | 100.3143                           | 100.0788    | \$100.0000   | \$0.0000           |
> | 0.10% | 0.0032172 | 100.2226                           | 99.9814     | \$99.9027    | \$0.0973           |
> | 0.30% | 0.0033733 | 100.0395                           | 99.7871     | \$99.7084    | \$0.2916           |
>
> Sin sobretasa el Bonde F vale la par, y cada 0.10% de sobretasa le quita cerca de \$0.10, por casi un año de vida restante: la relación es casi lineal, porque un margen chico multiplica casi la misma anualidad.

### 5. Amortización de capital

La sección 1 dejó abierta una segunda incógnita, el pago $c$: aquí el capital, la tasa y el plazo son datos, y lo que se busca es el pago. Ningún instrumento mexicano de esta unidad amortiza capital antes del vencimiento (todos devuelven el capital en un solo pago al vencimiento, o *bullet*, como vimos en la sección 2 de la nota anterior), pero un crédito hipotecario, un préstamo de auto o una emisión corporativa con retiro programado sí lo hacen, y Fabozzi documenta las tres formas como otra característica más de los bonos. Todas comparten la misma estructura de saldo insoluto:

$$s_t = a - \sum_{i=1}^{t} k_i \qquad (s_0 = a)$$

donde $a$ es el capital prestado y $k_t$ el abono a capital del periodo $t$, con $\sum_{t=1}^{N} k_t = a$ (el capital completo se termina de pagar en $N$ periodos).

**Sistema francés (pago total constante):** cada pago $c$ es igual, resultado de despejar $c$ en la misma fórmula de anualidad de la sección 3 (con $v_N = 0$, porque no hay valor nominal residual al final: todo el capital ya se pagó en abonos; y con $v_0 = a$, porque el capital prestado es el valor presente de los pagos):

$$c = a\dfrac{r}{1-(1+r)^{-N}} \qquad (r \neq 0)$$

El abono a capital de cada periodo se obtiene restando el interés del periodo ($rs_{t-1}$) al pago total: $k_t = c - rs_{t-1}$. Como el saldo insoluto baja con el tiempo, el interés baja y el abono implícito sube, aunque el pago total se mantenga fijo.

> **Ejemplo resuelto.** Un crédito hipotecario de \$500,000 a 20 años, tasa fija de 10% anual, sistema francés.
> $c = 500,000\dfrac{0.10}{1-(1.10)^{-20}} \approx 500,000 \times 0.117459 \approx \$58,730$ cada año.
> Primer año: interés $= 0.10 \times 500,000 = \$50,000$; abono a capital $k_1 = 58,730 - 50,000 = \$8,730$; saldo insoluto $s_1 = 500,000-8,730=\$491,270$.
>
> **En la práctica.** Los bancos ofrecen este esquema con mensualidades fijas. A junio de 2026, BBVA México publicaba una hipoteca de tasa fija desde 9.15% a 5, 10, 15 o 20 años. Con los mismos \$500,000 a 20 años y periodos mensuales ($r_{per}=0.0915/12$, $N=240$): $c = 500,000\dfrac{0.0915/12}{1-(1+0.0915/12)^{-240}} \approx \$4,547$ al mes. El banco anuncia además el Costo Anual Total (CAT), que en su ejemplo era 13.3% sin IVA, calculado con una tasa de 11.20%. El CAT es la tasa interna de retorno de los flujos del crédito con todas sus comisiones y seguros, el mismo cálculo del rendimiento al vencimiento de la nota siguiente aplicado a un préstamo; por eso supera a la tasa: lo que realmente se paga por el dinero recibido es más que el interés.

**Sistema alemán (abono a capital constante):** el abono $k_t = a/N$ es igual cada periodo, así que el pago total decrece porque el interés se cobra sobre un saldo insoluto cada vez menor:

$$c_t = \dfrac{a}{N} + rs_{t-1}$$

> **Ejemplo resuelto.** Mismo crédito (\$500,000, 20 años, 10% anual), sistema alemán.
> $k = 500,000/20 = \$25,000$ cada año.
> Primer pago $= 25,000 + 0.10 \times 500,000 = \$75,000$; segundo pago $= 25,000 + 0.10 \times 475,000 = \$72,500$: el pago baja \$2,500 cada año, siempre por el mismo abono constante multiplicado por la tasa.

![Interés y abono a capital de cada pago anual de un crédito de $500,000 a 20 años y 10%: en el sistema francés el pago es de $58,730 cada año y el interés domina los primeros años; en el alemán el abono es de $25,000 y el pago baja de $75,000 a $27,500](img/amortizacion_interes_capital.png)

En el sistema francés el pago es parejo y el interés pesa más que el abono durante los primeros 13 años; en el alemán el abono es parejo, así que el pago arranca más alto y cae con el saldo.

**Fondo de amortización (sinking fund):** el emisor retira una fracción $k_t$ de la emisión cada periodo según un calendario pactado, no necesariamente uniforme (a diferencia del sistema alemán, donde $k_t$ sí es constante), y paga cupón solo sobre el saldo insoluto restante, a la tasa cupón pactada $r_{cup}$. El pago de cada periodo es $c_t = k_t + r_{cup}s_{t-1}$, y su precio es la suma de la sección 1 con esos flujos, cada uno descontado a su propio periodo con la tasa de mercado $r$:

$$v_0 = \sum_{t=1}^{N} \left(k_t + r_{cup}s_{t-1}\right)(1+r)^{-t}$$

Si el mercado exige lo mismo que paga el cupón ($r = r_{cup}$), la suma vale exactamente $a$, igual que en los dos sistemas anteriores; si $r > r_{cup}$ vale menos, a descuento, como en la sección 3. Es el mecanismo típico de una emisión corporativa que retira, por ejemplo, 10% del principal cada año durante los primeros años y el resto al vencimiento, en vez de repartirlo en partes exactamente iguales como el sistema alemán.

### 6. Ejemplo integrador con datos de mercado

Con las fórmulas de las secciones 2 y 3, se resuelve el problema de precio de la sección 1 para los tres instrumentos gubernamentales con las tasas publicadas el 21 de septiembre de 2026 y se comparan con el precio que publica cetesdirecto ese mismo día:

| Instrumento     | Fórmula que aplica                                            | Datos                                                       | Precio calculado                | Precio publicado (21 sep 2026)   |
| --------------- | ------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------- | -------------------------------- |
| CETE 28 días    | Sección 2 (descuento)                                         | $v_N =$ \$10, $r_{nom} = 6.25\%$, $n_{dias} = 28$           | ≈ \$9.9516                      | \$9.95 (tasa 6.25%)              |
| Bono M 10 años  | Sección 3 (cupón fijo), simplificado a un pago anual          | $c =$ \$8, $v_N =$ \$100, $r \approx 9\%$, $N = 10$         | ≈ \$93.58 (a descuento)         | \$96.40 (tasa 9.16%)             |
| UDIBONO 10 años | Sección 3 (cupón fijo), en UDIs, simplificado a un pago anual | $c = rv_N = 4.75$ UDIs (a la par), $v_N = 100$ UDIs, $N=10$ | 100 UDIs × \$8.82 ≈ \$882 pesos | \$838.79 pesos (tasa real 4.75%) |

El CETE coincide con el precio publicado porque la fórmula es exactamente la que usa la plataforma. Los otros dos no coinciden, y la diferencia enseña algo: los dos ejemplos simplificados suponen un cupón elegido por nosotros (8% en el Bono M, igual a la tasa en el UDIBONO) pagado una vez al año, pero cada serie real tiene el suyo, fijado en la emisión, y lo paga cada 182 días. El UDIBONO del ejemplo se valuó a la par por suposición ($c=rv_N$); el mercado publicó \$838.79, que dividido entre el valor de la UDI de ese día (\$8.818843) da 95.11 UDIs por cada 100 de valor nominal: por debajo de la par, porque el cupón real de esa serie es menor que el rendimiento real de 4.75% (sección 3). Convertirlo a pesos requiere multiplicar por el valor de la UDI del día, un paso adicional que ningún instrumento denominado en pesos necesita. El apéndice cuantifica cuánto de la diferencia se debe al cupón y cuánto a la frecuencia de pago.

---

## Apéndice: Verificación numérica con código y datos

Esta sección amplía el núcleo; no forma parte del objetivo ni se evalúa. Somete las fórmulas de la nota a pruebas en Python ([`codigo/`](codigo/)) y las contrasta con los precios publicados el 21 de septiembre de 2026 ([`datos/`](datos/)).

**Las fórmulas cumplen lo que la nota afirma.** `test_valuacion.py` reúne 43 pruebas, de las cuales las últimas diez fijan el comportamiento del modelo de tasas de la simulación. Las que importan para las fórmulas de esta nota son siete:

- La fórmula cerrada de la sección 3 da lo mismo que descontar los flujos uno por uno.
- Un bono con $c=rv_N$ vale $v_N$ a cualquier plazo, y con $c<rv_N$ o $c>rv_N$ vale menos o más que $v_N$.
- La función de precio de un Bono M reproduce el ejemplo oficial de Banxico de la sección 3: precio sucio de 98.81269 y limpio de 97.76269.
- La función de precio de un Bonde F reproduce el ejemplo oficial de Banxico de la sección 4: precio sucio de 99.98144 y limpio de 99.90269, y vale exactamente la par con $m=0$ en una fecha de revisión de tasa.
- Las tres tablas de amortización cierran el saldo en cero, suman $a$ en abonos y, descontados sus pagos a la tasa del crédito, valen exactamente $a$.
- El precio de un CETE a 28 y a 91 días coincide con el de la sección 2.
- Las cifras de los ejemplos adicionales de las secciones 2 a 4 (CETE a cuatro plazos, papel comercial, Bono M a 3 y 30 años, bono corporativo con premio, Bonde F con tres sobretasas y certificado con sobretasa que se encarece) coinciden con su cálculo.

La sección 3 excluye $r=0$ porque divide entre $r$. ¿De dónde sale el límite? Para $r$ pequeña, $(1+r)^{-N}\approx 1-Nr$, así que $\frac{1-(1+r)^{-N}}{r}\approx N$ y

$$v_0 \to Nc + v_N \qquad (r \to 0)$$

es decir, sin descuento el bono vale la suma de sus flujos. La prueba lo verifica con $r=10^{-7}$ y comprueba que la función rechaza $r=0$. Las pruebas se corren desde la raíz del repositorio con `python -m pytest notas_unidades/unidad2/codigo -q`.

**Conciliación con el precio publicado.** Cetesdirecto publica la tasa y el precio de cada plazo. Para los CETES, la fórmula de la sección 2 reproduce el precio al centavo (\$9.9516 contra \$9.95 a un mes, \$9.8344 contra \$9.83 a tres meses). Para Bonos M y UDIBONOS no se conoce el cupón de la serie que la plataforma valúa, pero el precio es lineal en el cupón, así que se despeja el cupón que haría coincidir la fórmula con el precio publicado. ¿De dónde sale la fórmula? De despejar $c$ en la fórmula de precio de la sección 3, con $r_{per}=r_{nom}\frac{182}{360}$ la tasa de cada periodo de 182 días:

$$c = \dfrac{v_0 - v_N(1+r_{per})^{-N}}{\dfrac{1-(1+r_{per})^{-N}}{r_{per}}} \qquad (r_{per} \neq 0)$$

- **$c$**: cupón por periodo que se despeja, el que haría coincidir la fórmula con el precio publicado.
- **$v_0$**: precio publicado por la plataforma, en pesos para un Bono M y en UDIs para un UDIBONO.
- **$v_N$**: valor nominal (\$100 o 100 UDIs).
- **$r_{per}$**: tasa por periodo de 182 días, $r_{nom}\frac{182}{360}$.
- **$N$**: número de periodos de 182 días por vencer, dos por cada año del plazo.

La tasa de cupón anual es $\frac{c}{v_N}\times\frac{360}{182}$. El cálculo supone que el plazo por vencer es el plazo nominal ($N$ periodos de 182 días, dos por año) y que la liquidación cae en fecha de cupón, de modo que el precio limpio es el sucio. Cualquier otra diferencia con la serie real (su cupón exacto, su plazo por vencer, los días devengados) queda dentro del resultado, así que el cupón implícito es un diagnóstico y no el cupón de la emisión.

| Instrumento     | Rendimiento | Precio publicado | Cupón implícito |
| --------------- | ----------- | ---------------- | --------------- |
| Bono M 3 años   | 8.24%       | \$100.94         | 8.60%           |
| Bono M 5 años   | 9.00%       | \$98.90          | 8.72%           |
| Bono M 10 años  | 9.16%       | \$96.40          | 8.61%           |
| Bono M 20 años  | 9.64%       | \$86.34          | 8.09%           |
| Bono M 30 años  | 9.87%       | \$84.22          | 8.22%           |
| UDIBONO 3 años  | 3.99%       | 99.95 UDIs       | 3.97%           |
| UDIBONO 10 años | 4.75%       | 95.11 UDIs       | 4.14%           |
| UDIBONO 30 años | 4.90%       | 86.95 UDIs       | 4.07%           |

Los cupones implícitos de los Bonos M quedan entre 8.1% y 8.7%, cerca del 8% del ejemplo de la sección 3, y los de los UDIBONOS rondan 4%. Coincide con lo visto en la sección 6: el UDIBONO a 10 años vale menos de 100 UDIs porque su cupón implícito (4.14%) es menor que su rendimiento real (4.75%), mientras que el de 3 años, con cupón implícito de 3.97% y rendimiento de 3.99%, vale casi la par.

Para el Bono M a 10 años, la diferencia entre el \$93.58 del ejemplo y el \$96.40 publicado se descompone cambiando un supuesto a la vez, en este orden:

| Paso                                                        | Precio  | Cambio |
| ----------------------------------------------------------- | ------- | ------ |
| Ejemplo de la sección 3 (cupón 8%, tasa 9%, pago anual)     | \$93.58 |        |
| Tasa publicada de 9.16%, todavía con pago anual             | \$92.61 | -0.97  |
| Pagos cada 182 días con base 360, todavía con cupón de 8%   | \$92.46 | -0.15  |
| Cupón implícito de 8.61%, que reproduce el precio publicado | \$96.40 | +3.94  |

El cupón explica más que toda la brecha; la tasa y la frecuencia de pago mueven el precio en sentido contrario y por mucho menos. El orden de los pasos cambia cuánto se atribuye a cada uno, no el total.

**Costo de las simplificaciones.** Las secciones 2 y 3 simplifican dos cosas que el mercado no: la base de días y la frecuencia del cupón. Cuánto pesa cada una:

| Simplificación                                                     | Precio simplificado | Precio con la convención | Diferencia |
| ------------------------------------------------------------------ | ------------------- | ------------------------ | ---------- |
| CETE a 28 días al 6.25%: base 365 en vez de 360                    | \$9.9523            | \$9.9516                 | \$0.0007   |
| CETE a 91 días al 6.66%: base 365 en vez de 360                    | \$9.8367            | \$9.8344                 | \$0.0022   |
| Bono M a 10 años, cupón 8%, tasa 9%: pago anual en vez de 182 días | \$93.58             | \$93.45                  | \$0.13     |

La base de días cambia el precio menos de un centavo por cada \$10, pero a 91 días redondea a \$9.84 con base 365 y a \$9.83 con base 360, y cetesdirecto publica \$9.83: los datos confirman la convención día/360. El pago anual en vez de cada 182 días mueve el precio de un bono de \$100 unos 13 centavos.

**Sistemas de amortización.** Para el crédito de la sección 5 (\$500,000, 20 años, 10% anual) y un fondo de amortización que retira 10% del capital cada año durante los años 1 a 5 y el 50% restante en el año 20:

| Sistema               | Primer pago | Último pago | Interés total | Pago total  |
| --------------------- | ----------- | ----------- | ------------- | ----------- |
| Francés               | \$58,730    | \$58,730    | \$674,596     | \$1,174,596 |
| Alemán                | \$75,000    | \$27,500    | \$525,000     | \$1,025,000 |
| Fondo de amortización | \$100,000   | \$275,000   | \$575,000     | \$1,075,000 |

El sistema alemán paga menos interés porque devuelve el capital antes, a cambio de un primer pago 28% mayor que el francés; el fondo de amortización termina con un pago final de \$275,000. Pagar más interés total no significa que el francés sea más caro: descontados al 10%, los tres esquemas valen exactamente \$500,000, y la diferencia está solo en cuándo se paga.

**Simulación: cupón fijo contra cupón variable.** La sección 4 argumenta con palabras que el precio de un instrumento con cupón variable se mantiene cerca de la par. Una simulación de Monte Carlo lo pone a prueba con 10,000 escenarios de tasas.

Las tasas se generan con el modelo de **Vasicek**, en el que la tasa corta no vaga sin rumbo sino que es atraída hacia un nivel de largo plazo $r_{lp}$ con una velocidad $\kappa$.

¿De dónde sale la fórmula? Es la misma idea de un valor que se acerca a otro por un factor fijo cada periodo, la de $(1+r)^{-t}$ de la sección 1, aplicada a la distancia que separa a la tasa de su nivel de largo plazo: esa distancia se encoge en $e^{-\kappa\Delta t}$ cada paso, y lo que queda es lo que la lleva de vuelta. A eso se suma un empujón aleatorio, escalado para que la varianza acumulada deje de crecer y se estacione en $\sigma^2/(2\kappa)$, en vez de dispararse como lo haría si cada periodo sumara su ruido al anterior sin nada que lo contuviera:

$$R_{t+1} = r_{lp} + (R_t - r_{lp})e^{-\kappa\Delta t} + \sigma\sqrt{\dfrac{1-e^{-2\kappa\Delta t}}{2\kappa}}\,Z_{t+1} \qquad (\kappa > 0)$$

- **$R_t$**: tasa corta vigente en la fecha de cupón $t$. Va en mayúscula porque es incierta: depende de todos los empujones aleatorios hasta esa fecha.
- **$r_{lp}$**: nivel de largo plazo, la tasa hacia la que el proceso es atraído.
- **$\kappa$**: velocidad de reversión, en unidades de 1/año. Entre más grande, más rápido vuelve la tasa a $r_{lp}$.
- **$\sigma$**: volatilidad de la tasa, en puntos porcentuales anuales.
- **$\Delta t$**: fracción de año entre una fecha de cupón y la siguiente, $182/360$ aquí.
- **$Z_{t+1}$**: variable aleatoria normal estándar (media 0, varianza 1), independiente de un periodo a otro. Es la única fuente de azar de la tasa; $\kappa$, $\sigma$ y $r_{lp}$ son parámetros fijos.

Los parámetros no son supuestos: se estiman por mínimos cuadrados con la tasa interbancaria mexicana a 3 meses, mensual de julio de 2001 a agosto de 2026. Salen $\kappa = 0.217$, que equivale a cerrar la mitad de la distancia en 3.2 años, $\sigma = 1.24$ puntos porcentuales al año y $r_{lp} = 6.11\%$. La simulación arranca en la última tasa observada, 6.79% en agosto de 2026. El laboratorio [`laboratorio_calibracion.md`](../../practicas/unidad2/laboratorio_calibracion.md) explica cómo se estiman y, sobre todo, qué tan bien predicen.

El Bono M se valúa descontando los flujos que le quedan con la curva que el propio modelo implica, no aplicando la tasa corta a todos los plazos. Eso importa: bajo Vasicek, un movimiento de 100 puntos base en la tasa corta mueve el rendimiento a 10 años solo 41, porque el mercado sabe que el brinco de hoy se va a deshacer. Un modelo que moviera las dos por igual exageraría el riesgo de los plazos largos.

Para descontar, sin embargo, no se usa el nivel de 6.11%: con él la curva del modelo quedaría muy por debajo de la del mercado. Se usa otro nivel, 10.91%, elegido para que la curva del modelo reproduzca el 9.16% que rendía el Bono M a 10 años el 21 de septiembre (la curva queda **anclada** a ese plazo). Son dos niveles con dos papeles: 6.11% dice hacia dónde se mueven las tasas en los escenarios, y 10.91% cómo las descuenta el mercado de ese día. El cupón del bono se fija en 9.13%, el que lo deja exactamente a la par con esa curva, para que los dos instrumentos arranquen en el mismo punto.

Para el certificado, justo después de una revisión de tasa el cupón ya iguala la TIIE de fondeo más la sobretasa pactada, así que lo único que lo separa de la par es el margen acumulado $M_t$, el cambio de la sobretasa que hoy exigiría el mercado a esa emisión respecto a la pactada: un flujo de $M_t\Delta t\,v_N$ por periodo que el certificado deja de pagar durante los $N-t$ periodos restantes. Ese flujo es la anualidad de la sección 3, sin valor nominal aparte, y se resta de $v_N$:

$$V_t = v_N\left(1 - M_t\Delta t\sum_{j=1}^{N-t} P_j\right)$$

- **$V_t$**: precio del certificado en la fecha de cupón $t$. En mayúscula porque depende de $M_t$ y de $R_t$, que son inciertos.
- **$v_N$**: valor nominal.
- **$M_t$**: margen acumulado en la fecha $t$, la diferencia entre la sobretasa que el mercado exigiría hoy a esa emisión y la que quedó pactada. Arranca en cero y va en mayúscula porque es aleatorio.
- **$N$**: número total de cupones de la emisión; **$t$**: cupones ya transcurridos, así que quedan $N-t$.
- **$P_j$**: factor de descuento del modelo al plazo $j\Delta t$, evaluado en la tasa corta $R_t$ de ese escenario; en mayúscula porque $R_t$ es incierta. Es el equivalente de $(1+r)^{-j}$ de la sección 3, pero con una tasa distinta para cada plazo en vez de una sola.
- **$\Delta t$**: la misma fracción de año de arriba.

El margen sigue su propio proceso aleatorio, con volatilidad anual de 0.3 puntos porcentuales, y esa sí es un supuesto de orden de magnitud, no una estimación.

![Diez mil trayectorias simuladas del precio de un Bono M a 10 años con cupón fijo, con una banda de 5% a 95% que se abre hasta unos 96 y 112 puntos y una mediana que sube a 104, y de un certificado a tasa variable, con una banda que se mantiene entre 95 y 105 y una mediana plana en 100](img/fijo_vs_variable_simulacion.png)

| Horizonte | Bono M: desviación | Bono M: 5% a 95% | Certificado: desviación | Certificado: 5% a 95% |
| --------- | ------------------ | ---------------- | ----------------------- | --------------------- |
| 1 año     | 3.55               | 95.16 a 106.92   | 1.89                    | 96.93 a 103.13        |
| 3 años    | 4.85               | 94.98 a 110.94   | 2.78                    | 95.39 a 104.59        |
| 5 años    | 4.86               | 95.34 a 112.31   | 2.80                    | 95.34 a 104.50        |

El Bono M se mueve casi el doble que el certificado a cualquier horizonte, que es lo que la sección 4 anticipaba. Hay dos detalles más. El primero es que la dispersión del Bono M deja de crecer después del tercer año, por dos razones que se suman: las tasas revierten a su nivel en vez de alejarse sin límite, y al bono le quedan cada vez menos años por vencer, la convergencia a la par de la sección 3. El segundo es que la mediana del Bono M sube a 104 en cinco años en vez de quedarse en 100. No es un error del cálculo: es la distancia entre los dos niveles de arriba. La curva del mercado del 21 de septiembre (el nivel de 10.91%) descontaba tasas más altas que las que el modelo estimado con 25 años de historia realmente entrega (el de 6.11%), y esa diferencia es la prima que paga un bono largo por el riesgo de tasa que carga, la preferencia por la liquidez que explica la sección 4 de la nota siguiente. El certificado no la cobra, y por eso su mediana se queda plana.

Esa diferencia muestra por qué el modelo no es un pronóstico. En la práctica nadie predice el nivel de las tasas desde cero: se leen las que el mercado ya descuenta (tasas forward, futuros y swaps de tasas de un día), se modela la reacción del banco central y se apuesta donde se cree que el mercado se equivoca. Las tasas forward tampoco son pronósticos puros porque incluyen la prima por plazo, y hay modelos, como los de Adrian, Crump y Moench y de Kim y Wright, que la separan de la tasa esperada. El Vasicek de esta simulación mide cuánto se dispersa el precio si las tasas se comportan como en la historia, no dónde estarán.

La reversión a la media pesa en el resultado. Si la tasa vagara sin rumbo (una caminata aleatoria con la misma $\sigma$), la desviación del Bono M a cinco años sería de 7.54 puntos en vez de 4.86: más de un tercio de ese riesgo aparente vendría del supuesto sobre las tasas, no del instrumento.

**Hasta dónde llega este modelo.** Vasicek tiene un solo factor, la tasa corta, así que toda la curva se mueve a partir de un solo número. Eso le alcanza para lo que hace aquí (comparar la dispersión de dos instrumentos) pero no para reproducir la curva completa de un día. Con el nivel anclado al plazo de 10 años, el resto de la curva queda así:

| Plazo   | Observado | Modelo | Error    |
| ------- | --------- | ------ | -------- |
| 3 años  | 8.24%     | 7.87%  | -0.37 pp |
| 5 años  | 9.00%     | 8.37%  | -0.63 pp |
| 10 años | 9.16%     | 9.16%  | 0.00 pp  |
| 20 años | 9.64%     | 9.87%  | +0.23 pp |
| 30 años | 9.87%     | 10.15% | +0.28 pp |

Acierta a 10 años porque ahí se ancló, y en los demás plazos se queda corto hasta 63 puntos base: la curva que produce es más plana que la del mercado. Un solo factor da una sola forma de curva, y esa forma la fija $\kappa$. Hay una familia de modelos construidos justamente para levantar esa restricción, empezando por el de Hull y White, que convierte $r_{lp}$ en una función del tiempo elegida para reproducir la curva observada entera en vez de un punto. Brigo y Mercurio los recorren todos y advierten, sobre los de un solo factor, que suponer que toda la curva se mueve a partir de su punto inicial es un supuesto peligroso cuando lo que se valúa depende de cómo se mueven unos plazos respecto a otros. El laboratorio tiene el mapa de esa familia.

**Datos y reproducibilidad.** [`cetesdirecto_2026-09-21.csv`](datos/cetesdirecto_2026-09-21.csv) guarda las tasas y los precios publicados de la conciliación, y [`fred_tasas_mensual.csv`](datos/fred_tasas_mensual.csv) las series mensuales con las que se calibró el modelo, ambos con su fecha, para que las cifras de la nota no dependan de una consulta que cambia cada día. `analisis_valuacion.py` imprime las tablas de este apéndice, `calibracion.py` las del laboratorio y `generar_figuras.py` produce las figuras, todos con semilla fija y corridos desde la raíz del repositorio.

---

## Fuentes y referencias recomendadas

- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press: valuación de bonos a descuento y con cupón a partir del valor presente de sus flujos.
- Fabozzi, F. J. y Drake, P. P. (2009). *Capital Markets, Financial Management, and Investment Management*. Wiley: fórmulas y ejemplos de amortización (sistema francés, sistema alemán, sinking fund).
- Banco de México. (s. f.). *Descripción técnica de los Bonos de Desarrollo del Gobierno Federal con tasa de interés fija*. Consultado el 21 de septiembre de 2026: valor nominal, cupón cada 182 días, intereses sobre días efectivos con base de 360, cotización por rendimiento, precio limpio y sucio, y el ejemplo oficial de valuación.
- Banco de México. (s. f.). *Descripción técnica de los Bonos de Desarrollo del Gobierno Federal BONDES F*. Consultado el 26 de septiembre de 2026: cupón de TIIE de Fondeo capitalizada cada 28 días, colocación por precio, valuación con sobretasa y el ejemplo oficial de precio limpio y sucio.
- Banco de México. (2026). Convención día/360 de los CETES, valor de la UDI, decisión de política monetaria del 6 de agosto de 2026 (tasa objetivo de 6.50%) y documento de apoyo para el cálculo del Costo Anual Total (CAT). Los resultados de las subastas del 1 y del 15 de septiembre de 2026 (CETE a 28 días: 6.13% y 6.25%) se consultaron en la prensa financiera y en cetes.app, porque el portal de subastas de Banxico carga sus tablas con JavaScript.
- Cetesdirecto. (2026, 21 de septiembre). *Tablas de valores gubernamentales (CETES, Bonos y UDIBONOS)*: precio y tasa publicados de cada plazo y valor de la UDI (\$8.818843).
- BBVA México. (2026, 30 de junio). *Hipoteca de tasa fija*: tasa desde 9.15%, CAT de 13.3% sin IVA, plazos de 5 a 20 años y mensualidades fijas.
- Mishkin, F. S. y Eakins, S. G. (2014). *Financial Markets and Institutions* (8ª ed.). Pearson: relación entre cupón, tasa de mercado y precio (a la par, a descuento, con premio).
- Vasicek, O. (1977). An equilibrium characterization of the term structure. *Journal of Financial Economics*, 5(2), 177-188: el modelo de tasa corta con reversión a la media que usa la simulación del apéndice, y la fórmula del precio del cupón cero que se deriva de él.
- Brigo, D. y Mercurio, F. (2006). *Interest Rate Models: Theory and Practice. With Smile, Inflation and Credit* (2ª ed.). Springer: la referencia estándar de modelación de tasas, de Vasicek a los modelos de mercado. De ahí salen la limitación de los modelos de un solo factor y la familia de extensiones que la corrigen.
- Adrian, T., Crump, R. K. y Moench, E. (2013). Pricing the term structure with linear regressions. *Journal of Financial Economics*, 110(1), 110-138: modelo que separa la tasa esperada de la prima por plazo en la curva de rendimientos.
- Kim, D. H. y Wright, J. H. (2005). An arbitrage-free three-factor term structure model and the recent behavior of long-term yields and distant-horizon forward rates. *Finance and Economics Discussion Series*, 2005-33, Federal Reserve Board: el otro modelo de prima por plazo de uso común.
- Federal Reserve Bank of St. Louis (FRED): series mensuales con las que se calibró el modelo, consultadas el 21 de septiembre de 2026. La tasa interbancaria mexicana a 3 meses y el rendimiento del bono mexicano a 10 años son el espejo que la OCDE publica en FRED, no la fuente primaria; el último dato de la serie de 10 años, 9.16%, coincide con el que cetesdirecto publicó ese mismo día.

---

## Cierre de la unidad — Lo esencial para recordar

- El precio de cualquier instrumento de deuda es el **valor presente de su vector de flujos**: **flujo único** para un instrumento a descuento (CETE, papel comercial), **anualidad más flujo único** para uno con cupón fijo (Bono M, UDIBONO, bono corporativo). Comparar el cupón contra lo que paga el mercado predice el precio sin calcularlo: $c=rv_N$ da un bono **a la par**, $c<rv_N$ **a descuento** y $c>rv_N$ **con premio**.
- Un instrumento con **cupón variable** no tiene fórmula cerrada de precio (cada flujo es incierto), pero como el cupón se reajusta a la tasa de mercado en cada revisión, el nivel de tasas casi no lo aleja de la par; lo que sí lo mueve es un cambio en la sobretasa exigida, que es justo lo que se cotiza en un Bonde F (margen de descuento).
- La **amortización de capital** (sistema francés, sistema alemán, fondo de amortización) devuelve el capital en abonos antes del vencimiento en vez de en un solo pago final; ninguno de los seis instrumentos mexicanos de esta unidad la usa, pero es la mecánica de un crédito hipotecario o de auto.
- En el mercado real se cotiza la tasa y el precio se deriva: con datos de septiembre de 2026 la fórmula reproduce el precio de un CETE (\$9.95), un Bono M con cupón menor a la tasa vale menos que la par y un UDIBONO se convierte a pesos con la UDI del día. Cada precio se calculó con la tasa de un solo plazo, pero esas tasas son puntos de una misma curva.

**Próxima sesión:** el camino inverso: dado el precio de mercado de un bono, qué rendimiento gana quien lo compra a ese precio.
