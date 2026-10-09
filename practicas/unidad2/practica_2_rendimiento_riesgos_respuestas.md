# Unidad 2 · Práctica 2: Respuestas

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Respuestas de [`practica_2_rendimiento_riesgos.md`](practica_2_rendimiento_riesgos.md). Las cifras se calcularon con las funciones de [`valuacion.py`](../../notas_unidades/unidad2/codigo/valuacion.py) y se redondean a dos decimales; un resultado a mano puede diferir en el último dígito.

---

## Ejercicio 1: Calcula el rendimiento

El vector es $(-98.90,\ 4.41,\ \ldots,\ 4.41,\ 104.41)$, con 10 pagos. La TIR da $r_{per}\approx4.55\%$, y $r_{nom}=0.0455\times360/182\approx9.00\%$, el rendimiento que publicaba cetesdirecto.

---

## Ejercicio 2: Laura vende su Bono M

1. Lo emite el Gobierno Federal; por plazo es mercado de capitales (más de un año); paga un cupón fijo y el valor nominal al vencer. Su vector al comprar era $(-100,\ 8,\ 8,\ \ldots,\ 8,\ 108)$, con 10 pagos.
2. Con 8 años por vencer al 10%: $8\dfrac{1-1.10^{-8}}{0.10}+100(1.10)^{-8}\approx$ \$89.33. El comprador obtiene un YTM de 10%: ese precio es justo el que hace que el vector restante rinda la tasa de mercado.
3. $(-100,\ 8,\ 97.33)$: el segundo flujo junta el cupón del año 2 y el precio de venta. Su TIR es 2.74% anual, muy por debajo del 8% prometido. No se cumplió el supuesto de conservar el bono hasta el vencimiento: vendió después de que la tasa subió y realizó la pérdida de precio. Es el riesgo de tasa de interés.
4. Al bono a 3 años le queda un año: $108/1.10\approx$ \$98.18, y $(-100,\ 8,\ 106.18)$ rinde 7.12%. Pierde \$1.82 contra \$10.67 del bono a 10 años: a más plazo, más sensibilidad del precio a la tasa.
5. No habría realizado ninguna pérdida: cobraría los mismos cupones y los \$100 al vencer. Queda expuesta al riesgo de reinversión, que con la tasa al alza le juega a favor, porque reinvierte cada cupón al 10% en vez de al 8%.

---

## Ejercicio 3: La tesorera y el millón de pesos

1. El vector de B es $(-98.45,\ 4.85,\ \ldots,\ 4.85,\ 104.85)$, con 10 pagos. La TIR da $r_{per}\approx5.05\%$, y $r_{nom}\approx9.99\%$. Rinde 99 pb (casi un punto) más que A: es la **sobretasa**, que paga el riesgo de crédito de la empresa y la menor liquidez de su bono.
2. A: tasa de interés, si tuviera que vender antes (y reinversión de los cupones). B: crédito, además de los de A. C: reinversión, porque todo el dinero se reinvierte cada mes a una tasa que hoy no se conoce; casi no tiene riesgo de precio ni de crédito.
3. Respuesta abierta. Un argumento razonable: A, porque vence cuando se paga la máquina y no tiene riesgo de crédito; B si la empresa acepta ese riesgo por 100 pb más; C solo si espera que las tasas suban mucho, renunciando hoy a casi 3 puntos de rendimiento. La nota de estrategias retoma esta pregunta.
