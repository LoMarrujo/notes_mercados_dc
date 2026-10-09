# Unidad 2 · Práctica 2: Rendimiento, Curva de Rendimientos y Riesgos

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Tres ejercicios que recorren [`0_mercado_e_instrumentos_deuda.md`](../../notas_unidades/unidad2/0_mercado_e_instrumentos_deuda.md), [`1_valuacion_instrumentos_deuda.md`](../../notas_unidades/unidad2/1_valuacion_instrumentos_deuda.md), [`2_rendimiento_y_curva_de_rendimientos.md`](../../notas_unidades/unidad2/2_rendimiento_y_curva_de_rendimientos.md) y [`3_riesgos_mercado_deuda.md`](../../notas_unidades/unidad2/3_riesgos_mercado_deuda.md); el centro es el rendimiento (nota 2). Las preguntas de riesgos son lectura complementaria y no entran al examen.

Los datos de mercado son los de cetesdirecto del 21 de septiembre de 2026; el bono corporativo es ilustrativo. Usa la hoja de cálculo (función TIR) para los vectores con muchos periodos. Las respuestas están en [`practica_2_rendimiento_riesgos_respuestas.md`](practica_2_rendimiento_riesgos_respuestas.md).

---

## Ejercicio 1: Calcula el rendimiento

El 21 de septiembre de 2026, cetesdirecto publicaba el Bono M a 5 años en \$98.90. Paga un cupón de \$4.41 cada 182 días, le quedan 10 cupones por cobrar y su valor nominal es de \$100. Calcula su YTM: escribe el vector de flujos, obtén $r_{per}$ con la función TIR de la hoja de cálculo y anualízalo con $r_{nom}=r_{per}\frac{360}{182}$.

---

## Ejercicio 2: Laura vende su Bono M

Es la continuación del mini-caso de la práctica 1. Laura compró el día de la emisión un Bono M a 10 años con valor nominal de \$100 y cupón de 8%, a la par. Para simplificar, el bono paga un cupón al año. Dos años después, ya cobrados dos cupones, Laura necesita el dinero y vende.

1. Clasifica el Bono M con las tres preguntas (quién emite, a qué plazo, cómo paga) y escribe el vector de flujos que Laura esperaba al comprar.
2. El día que vende, la tasa de mercado a 8 años es de 10%. Calcula el precio de venta. Quien le compra conserva el bono hasta el vencimiento: ¿qué YTM obtiene? Contesta sin calcular.
3. Escribe el vector de Laura en sus dos años, $(-100,\ c_1,\ c_2)$, y calcula su rendimiento anual con la TIR. ¿Cuál de los dos supuestos del YTM no se cumplió? ¿Qué riesgo se materializó?
4. Si en vez del bono a 10 años hubiera comprado uno a 3 años con el mismo cupón, ¿a qué precio vendería con la tasa de 10%, y qué rendimiento habría obtenido? ¿Qué dice esto sobre el plazo y el riesgo de tasa?
5. Si Laura no hubiera vendido, ¿habría perdido algo cuando la tasa subió? ¿A qué otro riesgo queda expuesta quien conserva el bono, y le juega a favor o en contra cuando la tasa sube?

---

## Ejercicio 3: La tesorera y el millón de pesos

La tesorera de una empresa zacatecana tiene \$1,000,000 que necesitará dentro de 5 años para pagar una máquina. El 21 de septiembre de 2026 compara tres opciones:

| Opción | Instrumento                                            | Precio  | Pagos                               | YTM   |
| ------ | ------------------------------------------------------ | ------- | ----------------------------------- | ----- |
| A      | Bono M a 5 años del ejercicio 1                        | \$98.90 | \$4.41 cada 182 días                | 9.00% |
| B      | Bono corporativo a 5 años (ilustrativo)                | \$98.45 | \$4.85 cada 182 días                | ?     |
| C      | CETES a 28 días, renovados cada mes durante los 5 años | \$9.95  | Valor nominal de \$10 a los 28 días | 6.25% |

1. Calcula el YTM de B como en el ejercicio 1. ¿Cuántos puntos base rinde más que A, y qué paga esa diferencia?
2. ¿Qué riesgo pesa más en cada opción: tasa de interés, reinversión, crédito, inflación o liquidez?
3. ¿Qué opción elegirías? Justifícalo en tres renglones.
