# Unidad 2 · Duración y Convexidad

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

> **Lectura complementaria, no evaluada.** Por calendario, este tema sale del examen de la unidad; se conserva como consulta.

## Objetivo de la unidad

Que el estudiante calcule la duración y la convexidad de un bono para cuantificar su sensibilidad a cambios en la tasa.

## Contenido

|     | Tema                       | Qué cubre                                                                              |
| --- | -------------------------- | -------------------------------------------------------------------------------------- |
| I   | Cuánto se mueve el precio  | El precio de un Bono M a 2 y a 10 años ante subidas de tasa de 1, 10 y 100 puntos base |
| II  | Duración de Macaulay       | El promedio del plazo de cada flujo, ponderado por cuánto del precio aporta cada uno   |
| III | Duración modificada y PVBP | La sensibilidad del precio a la tasa, en porcentaje y en pesos por punto base          |
| IV  | Convexidad                 | La corrección de curvatura cuando el cambio de tasa es grande                          |

---

### 1. Cuánto se mueve el precio

La sección 2 de [`4_riesgos_mercado_deuda.md`](4_riesgos_mercado_deuda.md#2-riesgo-de-tasa-de-interés) ya dijo que un bono de plazo más largo se mueve más que uno corto ante el mismo cambio de tasa. Eso responde en qué dirección y, a grandes rasgos, en qué instrumentos es peor; falta responder cuánto. Antes de nombrar nada, conviene verlo en una tabla: el precio de un Bono M a 10 años y el de uno a 2 años, ambos con cupón fijo de 8% y valor nominal \$100, ante subidas de la tasa de mercado de 1, 10 y 100 puntos base (pb) sobre una tasa inicial de 9%.

| Cambio en la tasa  | Precio, Bono M 2 años | Precio, Bono M 10 años |
| ------------------ | --------------------- | ---------------------- |
| Sin cambio (9.00%) | \$98.24               | \$93.58                |
| +1 pb (9.01%)      | \$98.22               | \$93.52                |
| +10 pb (9.10%)     | \$98.07               | \$92.97                |
| +100 pb (10.00%)   | \$96.53               | \$87.71                |

Graficando el precio contra la tasa para cada bono, las dos curvas descienden, y la del bono a 10 años cae con mayor pendiente que la del bono a 2 años en cualquier punto: esa pendiente, la razón de cambio del precio respecto a la tasa, es exactamente lo que la **duración** va a medir. Se llama así, y se mide en años, por una coincidencia algebraica de su fórmula (se ve abajo), no porque sea literalmente un tiempo: es una sensibilidad, y confundirla con un plazo es uno de los errores más comunes de esta unidad.

### 2. Duración de Macaulay

**Duración de Macaulay ($D$):** el promedio del plazo de cada flujo, ponderado por qué proporción del precio total aporta ese flujo:

$$D = \dfrac{\displaystyle\sum_{i=1}^{N} t_i\, c_i(1+r)^{-t_i}}{v_0} \qquad (v_0 \neq 0)$$

¿De dónde sale la fórmula? $v_0=\sum_i c_i(1+r)^{-t_i}$ es la fórmula de precio de [`1_valuacion_instrumentos_deuda.md`](1_valuacion_instrumentos_deuda.md#1-los-flujos-de-un-bono-y-las-incógnitas-que-se-despejan); cada término $c_i(1+r)^{-t_i}$ es el valor presente del flujo del periodo $t_i$, y dividirlo entre $v_0$ da qué fracción del precio total viene de ese flujo. $D$ es el promedio de los plazos $t_i$, ponderado por esas fracciones: un bono cupón cero (un solo flujo, todo el peso en $t_N$) tiene $D=t_N$, exactamente su plazo; un bono con cupones tiene $D<t_N$, porque parte del peso ya se cobró antes del vencimiento.

### 3. Duración modificada y PVBP

**Duración modificada ($D_{mod}$):** la sensibilidad real del precio ante un cambio en la tasa, la pendiente que se vio en la tabla:

$$D_{mod} = \dfrac{D}{1+r} \qquad\text{y}\qquad \dfrac{\Delta v_0}{v_0} \approx -D_{mod}\,\Delta r$$

¿De dónde sale la fórmula? Derivando $v_0(r)=\sum_i c_i(1+r)^{-t_i}$ respecto a $r$: $\dfrac{dv_0}{dr} = -\sum_i t_i c_i (1+r)^{-t_i-1} = -\dfrac{1}{1+r}\sum_i t_i c_i(1+r)^{-t_i} = -\dfrac{D\,v_0}{1+r}$. Despejando, $\dfrac{1}{v_0}\dfrac{dv_0}{dr} = -\dfrac{D}{1+r} = -D_{mod}$: la duración modificada es, por definición, el cambio porcentual del precio por cada punto que se mueve la tasa, la relación inversa entre precio y tasa convertida en número.

> **PVBP (price value of a basis point):** cuánto dinero, no porcentaje, cambia el precio si la tasa se mueve exactamente un punto base ($\Delta r = 0.0001$): $\text{PVBP} \approx D_{mod}\,v_0\,(0.0001)$. Es la misma aproximación de arriba, solo que en pesos por posición en vez de en porcentaje, útil para dimensionar una mesa de dinero que necesita saber cuánto arriesga un portafolio completo, no solo un bono.

### 4. Convexidad

**Convexidad ($C$):** la aproximación lineal de $D_{mod}$ se aleja del precio real mientras más grande es el cambio de tasa (la tabla de la sección 1 ya lo insinúa: el precio no cae proporcionalmente igual entre +1 pb y +100 pb). La convexidad corrige ese error usando la segunda derivada:

$$C = \dfrac{1}{v_0}\dfrac{d^2v_0}{dr^2} = \dfrac{\displaystyle\sum_{i=1}^N t_i(t_i+1)\,c_i(1+r)^{-t_i-2}}{v_0} \qquad\text{y}\qquad \dfrac{\Delta v_0}{v_0} \approx -D_{mod}\,\Delta r + \dfrac{1}{2}C(\Delta r)^2$$

¿De dónde sale la fórmula? Es la misma derivación de $D_{mod}$, un paso más: derivar $dv_0/dr$ una segunda vez respecto a $r$ da $d^2v_0/dr^2 = \sum_i t_i(t_i+1)c_i(1+r)^{-t_i-2}$; dividir entre $v_0$ dimensiona esa segunda derivada igual que se hizo con la primera. Sumar el término de convexidad a la aproximación de $D_{mod}$ es la misma idea que una expansión de Taylor de segundo orden: la recta tangente (duración) más la corrección de curvatura (convexidad).

> Un bono con más convexidad es, en igualdad de duración, mejor para su tenedor: gana más de lo que la duración predice cuando la tasa baja, y pierde menos de lo que predice cuando sube. Esa asimetría es justamente lo que la curvatura de la tabla de la sección 1 ya mostraba, antes de ponerle un nombre o una fórmula.

---

## Fuentes y referencias recomendadas

- Fabozzi, F. J., & Fabozzi, F. A. (2021). *Bond Markets, Analysis, and Strategies* (10ª ed.). MIT Press: duración de Macaulay, duración modificada, PVBP y convexidad como medidas de sensibilidad del precio ante cambios en la tasa.
- Luenberger, D. G. (2013). *Investment Science* (2ª ed.). Oxford University Press: duración de Macaulay y duración modificada como sensibilidad del precio a la tasa, y convexidad como corrección de segundo orden.

---

## Cierre de la unidad — Lo esencial para recordar

- La **duración de Macaulay** es el promedio del plazo de cada flujo, ponderado por cuánto del precio aporta cada uno; un cupón cero tiene una duración igual a su plazo, y un bono con cupones, menor.
- La **duración modificada** cuantifica el riesgo de tasa de interés: el cambio porcentual aproximado del precio ante un cambio en la tasa. Es una sensibilidad, no un plazo, aunque se mida en años; el **PVBP** la expresa en pesos por punto base en vez de en porcentaje.
- La **convexidad** corrige esa aproximación lineal para cambios de tasa grandes: en igualdad de duración, más convexidad es mejor para el tenedor.

**Dónde se usa:** la duración es la herramienta del apéndice de inmunización de [`3_estrategias_renta_fija.md`](3_estrategias_renta_fija.md#apéndice-inmunización).
