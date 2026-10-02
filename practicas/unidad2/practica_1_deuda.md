# Unidad 2 · Práctica: Mercado, Instrumentos y Valuación de Deuda

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Ejercicios aplicando los conceptos de [`0_mercado_e_instrumentos_deuda.md`](../../notas_unidades/unidad2/0_mercado_e_instrumentos_deuda.md) y [`1_valuacion_instrumentos_deuda.md`](../../notas_unidades/unidad2/1_valuacion_instrumentos_deuda.md). Las dos notas se practican en conjunto: el vector de flujos que se construye en la primera es el que se descuenta en la segunda. Los ejercicios sobre el bono rescatable, la tasa de descuento, las causas del cambio de precio y el precio limpio y sucio se adaptan de Fabozzi, F. J. (Ed.). (2021). *The Handbook of Fixed Income Securities* (9ª ed.). McGraw Hill. Las respuestas están en [`practica_1_deuda_respuestas.md`](practica_1_deuda_respuestas.md).

---

## Mercado e Instrumentos de Deuda

### Ejercicio: clasifica el instrumento

Para cada instrumento, contesta las tres preguntas de la sección 7 (quién emite, a qué plazo, cómo paga) y decide si es deuda o participación de capital. Si alguno no pertenece a esta unidad, explica por qué.

| Instrumento                                                                        | ¿Quién emite? | ¿A qué plazo? | ¿Cómo paga? | ¿Deuda o participación? |
| ---------------------------------------------------------------------------------- | ------------- | ------------- | ----------- | ----------------------- |
| CETE a 182 días                                                                    |               |               |             |                         |
| UDIBONO a 30 años                                                                  |               |               |             |                         |
| Papel comercial a 28 días de una cadena de autoservicio                            |               |               |             |                         |
| Certificado bursátil de un gobierno estatal a 7 años, cupón TIIE + sobretasa       |               |               |             |                         |
| Acción de Walmart de México                                                        |               |               |             |                         |
| Certificado de una FIBRA                                                           |               |               |             |                         |
| Depósito a plazo fijo de 90 días en un banco                                       |               |               |             |                         |
| Bonde F a 3 años (cupón cada 28 días referenciado a la TIIE de fondeo)             |               |               |             |                         |
| Bono corporativo a 10 años con cupón fijo, rescatable por el emisor desde el año 5 |               |               |             |                         |

### Ejercicio: construye el vector de flujos

Escribe el vector $(c_0, c_1, \ldots, c_N)$ de cada instrumento y describe cómo se vería su diagrama de flujo (cuántas flechas, hacia dónde, cuál es la más alta). No calcules precios todavía: $a$ se deja como símbolo.

1. Un CETE a 91 días con valor nominal de \$10.
2. Un bono con valor nominal de \$100, cupón fijo de \$4.50 por periodo y 3 periodos por vencer.
3. Un certificado bursátil a 3 periodos con valor nominal de \$100, cuyo cupón es la TIIE de fondeo más una sobretasa. El cupón del primer periodo ya se fijó en \$0.60; los demás dependen de la TIIE que rija en cada fecha de revisión.
4. Un crédito de \$90 a 3 periodos al 10% por periodo, en sistema alemán. Escribe también el saldo insoluto $s_t$ de cada periodo.
5. Un bono corporativo con valor nominal de \$100, cupón fijo de \$9 por periodo y 4 periodos por vencer, que el emisor puede rescatar al final del periodo 2 pagando \$102 además del cupón de ese periodo. Escribe los dos vectores posibles. Si las tasas de mercado bajan mucho, ¿cuál de los dos esperarías ver? ¿Por qué el vector de este bono no se conoce hoy aunque su cupón sea fijo?
6. Un Bonde F a 3 periodos de 28 días con valor nominal de \$100, cuyo cupón es la TIIE de fondeo a un día capitalizada día con día durante cada periodo. Compara su vector con el del inciso 3: ¿qué flujo que ahí ya se conocía aquí no se conoce?

### Mini-caso: lo que pagó Laura y lo que vale hoy

Laura compró el día de la emisión un Bono M a 10 años con valor nominal de \$100 y cupón de 8%, cuando la tasa de mercado de ese plazo también era 8%. Dos años después, la tasa de mercado a 8 años es de 10%.

1. El día de la compra, ¿cuánto valían $a$, $v_0$ y $v_N$? ¿Por qué coinciden los tres?
2. Hoy, ¿cuál de las tres cantidades cambió, y en qué dirección? Justifica sin hacer cuentas.
3. Laura necesita el dinero y vende hoy. ¿Recupera los \$100 que pagó? ¿Y si en vez de vender lo conserva hasta el vencimiento (suponiendo que el gobierno paga)?

---

## Valuación de Instrumentos de Deuda

### Ejercicio: ¿qué incógnita se despeja?

La relación $v_0 = \sum_{t=1}^{N} c_t(1+r)^{-t}$ liga el vector de flujos, la tasa y el precio. Para cada situación, di cuál es la incógnita y a qué problema de inversión corresponde (fijación de precio, pago, inversión pura o cobertura).

1. Un fondo de deuda debe registrar hoy, a precio de mercado, el valor de su posición en Bonos M.
2. Un banco calcula la mensualidad fija de un crédito hipotecario a 20 años.
3. Un inversionista compra un bono corporativo a \$95 y quiere saber qué rendimiento obtiene si lo conserva al vencimiento.
4. Una aseguradora necesita saber cuánto valdrá dentro de 5 años lo que hoy invierte, para asegurarse de cubrir una póliza que vence en esa fecha.

### Ejercicio numérico: a descuento

1. El 21 de septiembre de 2026, cetesdirecto publicaba el CETE a 3 meses (91 días) con una tasa de 6.66%. Calcula su precio con valor nominal de \$10, y compáralo con el precio publicado de \$9.83.
2. Con la misma tasa de 6.66%, calcula el precio de un CETE a 182 días. ¿El descuento se duplica al duplicar el plazo?
3. Una empresa emite papel comercial por \$2,000,000 a 90 días con un rendimiento de 7.50% anual (cifras ilustrativas). ¿Cuánto recibe hoy y cuánto le cuesta el financiamiento en pesos?
4. En Estados Unidos, las letras del Tesoro y el papel comercial no se cotizan con la tasa de rendimiento $r_{nom}$ de la nota sino con una **tasa de descuento** $r_{desc}$, que divide la ganancia entre el valor nominal en vez de entre el precio:

   $$r_{desc} = \dfrac{v_N - v_0}{v_N}\dfrac{360}{n_{dias}}$$

   - **(a)** Despeja $r_{nom}$ de $v_0 = \dfrac{v_N}{1+r_{nom}\frac{n_{dias}}{360}}$ y compárala con $r_{desc}$. ¿En qué difieren las dos fórmulas?
   - **(b)** Calcula $r_{desc}$ del CETE a 91 días del inciso 1. ¿Es mayor o menor que 6.66%? ¿Cuál de las dos tasas mide lo que gana el inversionista sobre lo que pagó?
   - **(c)** ¿Con qué tasa de descuento se cotizaría el papel comercial del inciso 3?

### Ejercicio numérico: cupón fijo

Un bono paga un cupón fijo de 7% anual (un pago al año), con valor nominal de \$100 y 5 años por vencer.

1. **Antes de calcular:** di si el bono se valúa a la par, a descuento o con premio cuando la tasa de mercado es 6%, 7% y 9%. Justifica comparando $c$ con $rv_N$.
2. Calcula $v_0$ en los tres casos, paso a paso (factor de descuento, factor de anualidad, valor presente de los cupones, valor presente del valor nominal, suma).
3. Con la tasa de 9% fija, calcula el precio cuando le quedan 4, 3, 2 y 1 años. Repite con la tasa de 6%. ¿Hacia dónde va cada precio, y por qué?
4. Desde el caso a la par (7%), calcula también el precio a 5% y a 8%. ¿El precio sube lo mismo cuando la tasa baja 1 o 2 puntos que lo que baja cuando la tasa sube 1 o 2 puntos? ¿Cuánto valdría el bono con una tasa de 0%?

### Ejercicio: ¿por qué cambió el precio?

Para cada escenario, di qué causó el cambio de precio y en qué dirección se movió.

1. Banxico sube su tasa objetivo y el rendimiento del Bono M a 10 años pasa de 9.16% a 9.66%. ¿Qué le pasa al precio de un Bono M a 10 años ya emitido?
2. Pasa un año sin que cambie ninguna tasa. ¿Qué le pasa al precio del bono con cupón de 7% del ejercicio anterior si el mercado exige 6%? ¿Y si exige 9%?
3. El rendimiento del Bono M no cambia, pero el mercado pasa a exigir a todos los bonos corporativos de una industria 1.50 puntos sobre el Bono M del mismo plazo, en vez de 1.00.
4. Ni el Bono M ni la sobretasa de la industria cambian, pero una calificadora baja la calificación de un emisor en particular.
5. Las tasas bajan 2 puntos. Hay dos bonos corporativos idénticos, salvo que uno es rescatable por el emisor a \$102. ¿Cuál sube más?

Para cerrar: ¿cuáles de los cinco escenarios moverían el precio de un certificado bursátil a TIIE de fondeo más sobretasa justo después de su revisión de tasa?

### Ejercicio numérico: precio limpio y precio sucio

Un Bono M con cupón de 8% anual y valor nominal de \$100 paga cada 182 días con base 360, como describe el apartado "En la práctica" de la sección 3 de la nota de valuación. Le quedan 4 cupones por cobrar, ya corrieron 52 días del cupón vigente y el rendimiento de mercado es 9% anual.

1. Calcula el cupón por periodo, $c = v_N r_{cup}\frac{182}{360}$, y la tasa por periodo, $r_{per} = r_{nom}\frac{182}{360}$.
2. Valúa el bono en la próxima fecha de cupón: el cupón vigente, más los 3 cupones siguientes como anualidad, más el valor nominal descontado 3 periodos.
3. Lleva ese valor a hoy con el factor $(1+r_{per})^{-(182-52)/182}$ de la fracción de periodo que falta: es el precio sucio. Resta el interés devengado, $v_N r_{cup}\frac{52}{360}$, para obtener el precio limpio.
4. Un día antes del pago del cupón (181 días devengados), el precio sucio es \$102.63 y el limpio \$98.61; el día del pago, ya cobrado el cupón, los dos valen \$98.61. ¿Cuál de los dos precios brinca, y por qué? ¿Por qué el mercado cotiza el precio limpio aunque el comprador pague el sucio?

### Ejercicio numérico: ¿qué sistema de amortización paga más interés?

Una empresa pide un crédito de \$200,000 a 3 años, con tasa fija de 12% anual y pagos anuales. Determina cuál sistema de amortización, francés o alemán, le hace pagar más interés en total.

1. Calcula el pago constante del sistema francés y el abono constante del sistema alemán.
2. Llena el saldo insoluto y el interés de cada periodo en los dos sistemas, y suma el interés total:

   | Periodo | Saldo francés $s_{t-1}$ | Interés francés $rs_{t-1}$ | Saldo alemán $s_{t-1}$ | Interés alemán $rs_{t-1}$ |
   | ------- | ----------------------- | -------------------------- | ---------------------- | ------------------------- |
   | 1       |                         |                            |                        |                           |
   | 2       |                         |                            |                        |                           |
   | 3       |                         |                            |                        |                           |
   | Total   |                         |                            |                        |                           |

3. ¿Cuál sistema paga más interés, y por qué? Explícalo con el saldo insoluto.
4. ¿Pagar más interés total significa que ese sistema es más caro? ¿Cuánto valen los pagos de cada sistema descontados al 12%?

---

## Ejercicio integrador

Cetesdirecto publicó el 21 de septiembre de 2026 las tasas y precios siguientes (valor de la UDI ese día: \$8.818843):

| Instrumento     | Tasa         | Precio publicado |
| --------------- | ------------ | ---------------- |
| CETE a 1 mes    | 6.25%        | \$9.95           |
| Bono M a 3 años | 8.24%        | \$100.94         |
| UDIBONO 10 años | 4.75% (real) | \$838.79         |

Para cada instrumento:

- **(a)** Clasifícalo con las tres preguntas: quién emite, a qué plazo, cómo paga.
- **(b)** Escribe su vector de flujos.
- **(c)** Calcula su precio con la fórmula que le corresponde. Usa 28 días para el CETE; para el Bono M, un cupón de 8.60% anual; para el UDIBONO, un cupón real de 4.14% anual sobre 100 UDIs, y convierte el resultado a pesos. En ambos bonos simplifica a un pago anual, como en la sección 6 de la nota de valuación.
- **(d)** Compara con el precio publicado. ¿Qué explica la diferencia que queda? ¿Por qué el UDIBONO requiere un paso que los otros dos no?
- **(e)** Repite (c) para los dos bonos con el pago real cada 182 días: $c = v_N r_{cup}\frac{182}{360}$, $r_{per} = r_{nom}\frac{182}{360}$ y dos periodos por año. El valor nominal se descuenta los mismos $N$ periodos semestrales que el último cupón, no 3 o 10 años. ¿Cuánto de la diferencia de (d) se cierra?

Para cerrar: en la sección 6 de la nota de valuación, el Bono M a 10 años con cupón de 8% daba \$93.58 contra \$96.40 publicado. ¿Qué cambió en este ejercicio para que el Bono M a 3 años quedara tan cerca de su precio publicado?
