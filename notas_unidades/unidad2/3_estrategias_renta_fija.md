# Unidad 2 · Estrategias de Inversión en Renta Fija

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

## Objetivo de la unidad

Que el estudiante justifique una estrategia de inversión en renta fija (calce de flujos o elección de plazo) para una obligación o un escenario de tasas dado.

## Contenido

|     | Tema                                        | Qué cubre                                                                                       |
| --- | ------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| I   | Calce de flujos                             | Comprar bonos cuyos pagos coincidan con las fechas de una obligación, sin depender de la tasa   |
| II  | Elegir el plazo según el escenario de tasas | Comparar, a un año, un CETE contra un Bono M largo si las tasas bajan, no cambian o suben       |
| III | Bala, barra y escalera                      | Tres formas de repartir el dinero entre plazos, y qué escenario de la curva favorece a cada una |

> La práctica de este tema está en [`practica_2_rendimiento_estrategias.md`](../../practicas/unidad2/practica_2_rendimiento_estrategias.md).

---

### 1. Calce de flujos

[`2_rendimiento_y_curva_de_rendimientos.md`](2_rendimiento_y_curva_de_rendimientos.md#3-qué-mide-y-qué-no-mide-el-rendimiento) cerró con dos advertencias: el precio de un bono se mueve en sentido contrario a la tasa, más mientras más largo el plazo, y el YTM solo se gana si el bono se conserva hasta el vencimiento y los cupones se reinvierten a esa misma tasa. Quien invierte en deuda casi siempre tiene un motivo concreto: un pago que hacer en una fecha conocida, o una opinión sobre hacia dónde van las tasas. ¿Qué conviene comprar en cada caso? Esta nota responde primero el caso de la fecha conocida.

**Definición:** el **calce de flujos** (*cash matching*) consiste en comprar bonos cuyos pagos cubran cada pago de una obligación en su fecha, y conservarlos hasta su vencimiento.

Como no se vende nada antes de tiempo, el precio de mercado de los bonos deja de importar después de comprarlos: no hay riesgo de tasa de interés. Como cada flujo se usa el mismo día que llega, tampoco hay que reinvertirlo: no hay riesgo de reinversión, salvo por lo que sobre.

El portafolio se arma **hacia atrás**, empezando por el último pago. Si la obligación paga $o_t$ en el periodo $t$, se cubre $o_N$ con un bono que vence en $N$; los cupones de ese bono llegan también en las fechas anteriores y reducen lo que falta ahí; se repite con el siguiente pago hacia atrás.

¿De dónde sale la fórmula? En el periodo $N$, cada título de un bono con cupón $c$ y valor nominal $v_N$ paga su último flujo, $c+v_N$ (el vector de [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#1-los-flujos-de-un-bono-y-las-incógnitas-que-se-despejan)). Para que $q_N$ títulos paguen exactamente $o_N$ hace falta $q_N(c+v_N)=o_N$, y en cada fecha anterior esos mismos títulos ya cubren $q_Nc$:

$$q_N = \dfrac{o_N}{c+v_N} \qquad\text{y}\qquad \text{falta en } t<N:\ o_t - q_Nc \qquad (c+v_N>0)$$

> **Ejemplo resuelto.** Un fondo de becas tiene que pagar \$100,000 dentro de un año y otros \$100,000 dentro de tres. Con los precios de cetesdirecto del 21 de septiembre de 2026:
>
> 1. **Año 3.** El Bono M a 3 años cuesta \$100.94 y su cupón implícito es \$8.61 (sección 1 de la nota de rendimiento; \$8.6063 sin redondear). Hacen falta $q_3 = 100{,}000/108.61 \approx 920.76$ títulos, que cuestan $920.76 \times 100.94 =$ \$92,941.17.
> 2. **Año 1.** Esos títulos ya pagan \$7,924.34 de cupón al año 1, así que solo falta cubrir $100{,}000 - 7{,}924.34 =$ \$92,075.66. Se cubre con CETES a 364 días al 7.24%: cada \$100 de valor nominal cuestan $100/(1+0.0724 \times 364/360) \approx$ \$93.18, y el total cuesta \$85,795.08.
> 3. **Año 2.** No hay pago, pero el Bono M paga otro cupón de \$7,924.34: es un **sobrante**.
>
> | Año | Obligación | Flujo del portafolio | Sobrante   |
> | --- | ---------- | -------------------- | ---------- |
> | 1   | \$100,000  | \$100,000.00         | \$0.00     |
> | 2   | \$0        | \$7,924.34           | \$7,924.34 |
> | 3   | \$100,000  | \$100,000.00         | \$0.00     |
>
> El portafolio cuesta \$178,736.26 hoy y paga exactamente lo que se debe, pase lo que pase con las tasas.

![Arriba, la obligación: dos pagos de 100,000 en los años 1 y 3. Abajo, el portafolio que la calza: una salida de 178,736.26 hoy, entradas de 100,000 en los años 1 y 3, y un cupón sobrante de 7,924.34 en el año 2](img/flujo_calce.png)

El calce tiene tres límites. No siempre existe un bono que venza en la fecha exacta del pago: el ejemplo funcionó porque había un Bono M a 3 años y un CETE a un año. Los sobrantes sí se reinvierten, y ahí reaparece un poco de riesgo de reinversión. Y suele salir más caro que una estrategia que acepta algo de riesgo de tasa: se paga por la certeza.

### 2. Elegir el plazo según el escenario de tasas

El segundo caso es el del inversionista que no tiene una fecha de pago, sino un horizonte y una opinión sobre las tasas. La tabla de la sección 2 de la nota de rendimiento ya mostró cuánto pesa el plazo: al pasar el rendimiento de 8% a 9%, el precio cae 2.53% a 3 años, 6.42% a 10 años y 10.27% a 30 años. Eso funciona en los dos sentidos: si las tasas bajan, el bono largo es el que más sube.

Para comparar dos estrategias a un mismo horizonte se usa el **rendimiento a horizonte**: lo que se gana en un año al comprar un bono hoy en $a$, cobrar su cupón $c$ y venderlo al cierre del año en $v_1$, el precio que tenga entonces.

¿De dónde sale la fórmula? Es la TIR de [`4_ciencia_inversion.md`](../unidad1/4_ciencia_inversion.md#8-tasa-interna-de-retorno-tir) para un vector de un solo periodo, $(-a,\ c+v_1)$: la tasa $r_h$ que resuelve $-a + (c+v_1)(1+r_h)^{-1}=0$. El precio de venta $v_1$ es el de un bono al que le quedan $N-1$ periodos, con la fórmula de precio de la nota de valuación y el YTM $r_1$ que tenga el mercado al cierre del año:

$$r_h = \dfrac{c+v_1-a}{a} \qquad\text{con}\qquad v_1 = c\dfrac{1-(1+r_1)^{-(N-1)}}{r_1} + v_N(1+r_1)^{-(N-1)} \qquad (a>0,\ r_1\neq 0)$$

El numerador separa las dos fuentes de retorno que importan en un año: el cupón $c$ y la ganancia o pérdida de precio $v_1-a$.

> **Ejemplo resuelto.** Un inversionista tiene \$1,000,000 y un horizonte de un año, y duda entre dos opciones con los precios del 21 de septiembre de 2026:
>
> - **A. CETE a 364 días al 7.24%.** Gana $0.0724 \times 364/360 \approx 7.32\%$ en el año, pase lo que pase.
> - **B. Bono M a 10 años**, comprado en \$96.40 (YTM 9.16%, cupón implícito \$8.5951) y vendido al cierre del año como un bono a 9 años.
>
> | Escenario para el YTM al cierre del año | $r_1$  | Precio de venta $v_1$ | Rendimiento a horizonte $r_h$ |
> | --------------------------------------- | ------ | --------------------- | ----------------------------- |
> | Baja 100 pb                             | 8.16%  | \$102.70              | 15.45%                        |
> | No cambia                               | 9.16%  | \$96.64               | 9.16%                         |
> | Sube 100 pb                             | 10.16% | \$91.04               | 3.36%                         |
>
> Si la tasa no se mueve, el Bono M rinde justo su YTM. Si baja, casi duplica al CETE; si sube, rinde menos de la mitad. El punto de equilibrio está en un YTM de 9.47% al cierre del año: si las tasas suben **más de 31 pb**, el CETE gana. La decisión se justifica con esa cifra. Si el inversionista espera que Banxico siga recortando, el Bono M es la apuesta; si espera un alza mayor a 31 pb, o simplemente no puede perder, el CETE.

![Rendimiento en un año del CETE a 364 días (7.32% en los tres escenarios) contra el Bono M a 10 años: 15.45% si las tasas bajan 100 pb, 9.16% si no cambian y 3.36% si suben 100 pb](img/estrategia_escenarios.png)

La regla general que deja el ejemplo es la siguiente:

| Si se espera que las tasas... | Conviene                   | Por qué                                                                               |
| ----------------------------- | -------------------------- | ------------------------------------------------------------------------------------- |
| Bajen                         | Alargar el plazo (Bonos M) | El precio del bono largo es el que más sube                                           |
| Suban                         | Acortar el plazo (CETES)   | El precio casi no se mueve y el dinero se reinvierte pronto a la tasa nueva, más alta |
| No hay opinión                | Repartir entre plazos      | Ningún escenario arruina el portafolio completo (sección 3)                           |

El mismo razonamiento aplica a la **sobretasa** de un bono corporativo de la sección 4 de la nota de rendimiento. Si se espera que el riesgo de crédito del emisor mejore, su sobretasa se cierra y su precio sube frente al de un Bono M del mismo plazo.

### 3. Bala, barra y escalera

Una opinión sobre el **nivel** de las tasas decide si alargar o acortar. Una opinión sobre la **pendiente** de la curva (el segundo movimiento de la [sección 4 de la nota de rendimiento](2_rendimiento_y_curva_de_rendimientos.md#4-la-curva-de-rendimientos-ubicar-un-bono)) decide cómo repartir el dinero entre plazos. Hay tres formas básicas:

| Estructura          | Cómo se arma                                                       | Conviene si                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Bala (*bullet*)     | Todo cerca de un solo plazo; por ejemplo, Bonos M a 5 años         | Hay una obligación en esa fecha, o se espera que la curva se empine (el tramo largo sube de tasa más que el medio)                             |
| Barra (*barbell*)   | Una parte en CETES y otra en Bonos M a 20 o 30 años, nada en medio | Se espera que la curva se aplane (las tasas largas bajan frente a las cortas): el extremo largo gana precio y el corto se reinvierte pronto    |
| Escalera (*ladder*) | Montos iguales que vencen cada año, de 1 a $N$ años                | No hay opinión: cada año vence un tramo que se reinvierte a la tasa de ese momento, así que el riesgo de tasa y el de reinversión se promedian |

La escalera es la versión de "repartir entre plazos" de la sección 2, y la estrategia de un inversionista que no quiere apostar. La barra y la bala son apuestas sobre la forma de la curva, y se justifican igual que en la sección 2: con el rendimiento a horizonte de cada estructura bajo el escenario que se espera.

---

## Apéndice: inmunización

> Este apéndice no se evalúa. Usa la duración de Macaulay de [`5_duracion_convexidad.md`](5_duracion_convexidad.md#2-duración-de-macaulay), que es lectura complementaria.

El calce de la sección 1 necesita un bono por cada fecha de pago. La **inmunización** relaja esa exigencia: en vez de igualar cada flujo, iguala dos números del portafolio con los de la obligación, su valor presente y su duración de Macaulay $D$. Si los dos coinciden, un cambio pequeño y parejo de la tasa mueve el valor del portafolio y el de la obligación casi lo mismo.

¿De dónde sale la regla? $D$ es un promedio ponderado de plazos, así que la duración de un portafolio de dos instrumentos es el promedio de sus duraciones, ponderado por la fracción $w$ del dinero que va a cada uno: $D_{port} = (1-w)D_A + wD_B$. Igualarla con la de la obligación y despejar $w$ da

$$w = \dfrac{D_{obl}-D_A}{D_B-D_A} \qquad (D_B\neq D_A)$$

> **Ejemplo resuelto.** La misma obligación de la sección 1 (\$100,000 en los años 1 y 3), con el supuesto de una curva plana al 9%, como en Luenberger. Su valor presente es \$168,961.47 y su duración, 1.91 años. Se cubre con un CETE a un año ($D_A=1$, un solo flujo) y el Bono M a 10 años con cupón de \$8.5951 ($D_B=7.05$ años). Entonces $w=(1.91-1)/(7.05-1)\approx 0.15$: \$143,451.07 en CETES y \$25,510.39 en Bonos M.
>
> | Choque de tasa | Valor del portafolio | Valor de la obligación | Diferencia |
> | -------------- | -------------------- | ---------------------- | ---------- |
> | Baja 100 pb    | \$172,016.14         | \$171,975.82           | +\$40.33   |
> | Sube 100 pb    | \$166,077.01         | \$166,040.57           | +\$36.43   |
>
> En los dos casos el portafolio sigue cubriendo la obligación, con unos \$40 de margen sobre más de \$166,000.

La protección tiene condiciones que el calce no necesita. Supone una curva plana que se mueve de forma pareja. Solo vale para cambios pequeños. Y se pierde con el tiempo, porque las duraciones cambian a ritmos distintos y hay que rebalancear el portafolio.

---

## Fuentes y referencias recomendadas

- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press: calce de flujos (cash matching) e inmunización con valor presente y duración.
- Fabozzi, F. J., & Fabozzi, F. A. (2021). *Bond Markets, Analysis, and Strategies* (10ª ed.). MIT Press: estrategias según el escenario de tasas, rendimiento a horizonte y estructuras de bala, barra y escalera.
- Cetesdirecto: tablas de CETES y Bonos M del 21 de septiembre de 2026 (precio y tasa por plazo). Los ejemplos de las secciones 1 y 2 y del apéndice se reproducen con `codigo/estrategias.py`, y sus números se comprueban en `codigo/test_estrategias.py`.

---

## Cierre de la unidad — Lo esencial para recordar

- El **calce de flujos** cubre cada pago de una obligación con un bono que vence en esa fecha, y se arma hacia atrás desde el último pago. No tiene riesgo de tasa ni de reinversión (salvo los sobrantes), pero exige un bono por fecha y se paga por esa certeza.
- Con un horizonte y una opinión sobre las tasas, se compara el **rendimiento a horizonte** de cada opción en cada escenario. Si se espera que las tasas bajen, conviene alargar el plazo; si se espera que suban, acortarlo.
- Una estrategia se justifica con un número: por ejemplo, el alza de tasa a partir de la cual el bono largo rinde menos que el CETE (31 pb en el ejemplo).
- La **bala**, la **barra** y la **escalera** reparten el dinero entre plazos según lo que se espere de la pendiente de la curva. La escalera es la opción cuando no hay opinión.

**Próxima sesión:** examen de la Unidad 2. Después, la Unidad 3: el mercado de participación (acciones, FIBRAs, CKD y CERPIs).
