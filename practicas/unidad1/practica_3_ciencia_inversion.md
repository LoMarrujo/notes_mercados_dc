# Unidad 1 · Práctica: Ciencia de la Inversión

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Ejercicios aplicando los conceptos de [`4_ciencia_inversion.md`](../../notas_unidades/unidad1/4_ciencia_inversion.md).

---

## Ciencia de la Inversión

### Ejercicio conceptual

1. Para cada situación, indica si el flujo es determinístico o estocástico y qué tipo de diagrama usarías. (a) Comprar un Bono M por \$50,000 con cupón semestral fijo de 4%, a vencer en 2 años. (b) El precio de cierre diario de una acción de Grupo México durante el próximo trimestre. (c) Una arrendadora financiera proyecta su cartera vencida a 1, 2 y 3 años, con un rango que se abre cuanto más lejano el horizonte.
   *Respuesta: (a) Determinístico, línea de tiempo. (b) Estocástico, trayectorias simuladas (random walk). (c) Estocástico, fan chart.*
2. Identifica qué principio del análisis de inversión aplica en cada caso. (a) Un asesor ofrece un pagaré privado a 8% anual cuando el CETE a plazo similar rinde 9%. (b) Dos ETFs que replican el mismo índice (mismo riesgo) cotizan a precios distintos en dos casas de bolsa. (c) Un portafolio armado hace 6 meses con 60% acciones y 40% bonos ya no es el óptimo hoy porque el precio de las acciones subió mucho.
   *Respuesta: (a) Comparación. (b) No arbitraje. (c) Dinámica.*
3. Clasifica cada problema como fijación de precio, cobertura o inversión pura. (a) Una empresa que importa insumos en dólares compra hoy un forward para fijar el tipo de cambio a 90 días, sin buscar ganar con el movimiento del dólar. (b) Dado que un Bono M paga cupones semestrales fijos y el mercado exige una tasa de descuento de 9%, ¿cuánto debería costar hoy? (c) Un ahorrador con \$100,000 decide qué porcentaje destinar a CETES, Bonos M y un fondo de acciones para maximizar su rendimiento esperado dado el riesgo que tolera.
   *Respuesta: (a) Cobertura. (b) Fijación de precio. (c) Inversión pura (selección de portafolio).*

### Ejercicio numérico

1. Un banco ofrece una tasa nominal anual del 18%, capitalizable trimestralmente. Calcula la tasa efectiva anual.
   *Respuesta: TEA = (1 + 0.18/4)⁴ − 1 ≈ 19.25%*
2. ¿Cuál es el valor presente de \$50,000 que recibirás en 4 años, si la tasa de descuento es 10% anual?
   *Respuesta: VP = 50,000 / (1.10)⁴ ≈ \$34,151*
3. Un instrumento paga \$2,000 anuales durante 3 años. Con una tasa de descuento de 7%, ¿cuál es su valor presente?
   *Respuesta: VP = 2,000 × [1 − (1.07)⁻³] / 0.07 ≈ \$5,249*
4. Un CETE se compra hoy en \$970 y paga \$1,000 de valor nominal al vencimiento en 91 días. ¿Cuál es la TIR del periodo?
   *Respuesta: TIR = 1,000/970 − 1 ≈ 3.09% (91 días)*
5. Dos proyectos requieren un desembolso inicial de \$10,000 hoy. El proyecto A paga \$15,000 en 1 año; el proyecto B paga \$20,000 en 3 años. La tasa de mercado es 12% anual. (a) Calcula la TIR de cada proyecto. (b) Calcula el VPN de cada proyecto a la tasa de mercado. (c) ¿Coinciden los dos criterios en cuál proyecto conviene?
   *Respuesta: TIR_A = 50%, TIR_B ≈ 26%: por TIR conviene A. VPN_A ≈ \$3,393, VPN_B ≈ \$4,236 (a 12%): por VPN conviene B. Los criterios no coinciden.*
6. Isabel invierte \$25,000 en un instrumento que rinde 10% anual. Calcula el valor de la inversión a 3 años y a 15 años, bajo interés simple y bajo interés compuesto. ¿Qué tanto más gana bajo interés compuesto en cada caso?
   *Respuesta: Simple: \$32,500 (3 años), \$62,500 (15 años). Compuesto: ≈\$33,275 (3 años), ≈\$104,431 (15 años). La diferencia crece de \$775 a ≈\$41,931.*
7. Una empresa evalúa un proyecto que requiere una inversión inicial de \$1,000,000 y que generará flujos de \$600,000 al final del año 1 y \$720,000 al final del año 2 (sin flujos adicionales). Calcula la TIR del proyecto.
   *Respuesta: r\* = 20% (18x² + 15x − 25 = 0 con x = (1+r\*)⁻¹ da x = 5/6).*
8. Un banco ofrece un CEDE con capitalización continua sobre una TNA de 15%. (a) ¿Cuál es la tasa efectiva anual equivalente (r_cont)? (b) Si inviertes \$80,000 hoy, ¿cuánto tendrás en 2 años?
   *Respuesta: (a) r_cont = e^0.15 − 1 ≈ 16.18%. (b) ≈ \$80,000 × e^(0.15×2) ≈ \$107,989.*
9. Un fondo de deuda ofrece una TEA de 8.2%. Al momento de invertir, la inflación esperada para el año es 4.5% (r̂_inf); al terminar el año, la inflación observada fue 5.6% (r_inf). Calcula (a) la tasa efectiva real predicha y (b) la tasa efectiva real (realizada). (c) ¿El inversionista ganó más o menos poder de compra del que esperaba?
   *Respuesta: (a) r̂_real = 1.082/1.045 − 1 ≈ 3.54%. (b) r_real = 1.082/1.056 − 1 ≈ 2.46%. (c) Ganó menos poder de compra del esperado, porque la inflación observada superó a la esperada.*
