---
name: notas-unidad
description: Convenciones de este curso (Mercados de Deuda y Capitales) para escribir o editar objetivos de unidad, fórmulas de finanzas, la estructura de archivos (teoría/práctica separadas), el estilo de prosa (sin em dashes, fuentes consolidadas, sin relleno de LLM) y el formato Markdown (lint limpio, tablas prettified) en notas_unidades/**/*.md y en el README. Úsalo antes de redactar un objetivo de aprendizaje, presentar una fórmula matemática nueva, crear/reorganizar archivos de una unidad, o escribir prosa nueva en una nota.
---

# Convenciones de notas de unidad

Aplica a cualquier archivo en `notas_unidades/**/*.md` y a los bloques `**Objetivo:**` del `README.md`.

## Objetivos de aprendizaje

Una clase es útil cuando el estudiante puede hacer algo nuevo al salir, no cuando "vio" más contenido. El objetivo se define primero; el contenido y la actividad bajan de ahí — nunca al revés (elegir temas y ponerles un objetivo encima después).

Reglas:

1. **Un objetivo, un verbo de acción observable.** Nada de "entender" o "conocer" — no son observables. Usar verbos como *clasificar, distinguir, calcular, ubicar, justificar, aplicar, trazar*.
2. **Si el objetivo tiene "y" uniendo dos habilidades distintas, son dos objetivos** — a menos que se puedan encadenar en una sola acción. Ejemplo de encadenado válido: "clasificar un activo financiero según quién lo emite, y ubicar qué autoridad lo regularía" (en vez de "entender los activos... y cómo está organizado el sistema").
3. **Todo objetivo debe ser comprobable con algo que ya está en la sesión** — normalmente la actividad práctica o los casos de la Parte II. Si no hay actividad que exponga si el estudiante lo logró: o sobra el objetivo, o falta la actividad (agrégala, no dejes el objetivo suelto).
4. **No dupliques cobertura entre objetivos de la misma unidad.** Si dos bullets prueban esencialmente lo mismo, fusiónalos.

Checklist antes de dar por bueno un objetivo:
- ¿Tiene un solo verbo de acción observable?
- ¿Hay una actividad concreta (ejercicio, taller, caso, dinámica) que lo compruebe?
- ¿Se solapa con otro objetivo de la misma unidad?

Reglas de diseño de la sesión que sostienen a los objetivos (aplican al redactar o reordenar contenido, no solo el bullet del objetivo):

- **Puente narrativo:** cada concepto nuevo responde una pregunta que dejó abierta el anterior, no aparece de la nada.
- **Teoría y práctica cercanas en el tiempo:** no amontonar todo el bloque teórico al inicio y la práctica hasta el final.
- **Participación de bajo riesgo:** voluntaria + puntos extra, en vez de examinar en frío.
- **Cierre = síntesis, no relleno:** 3–4 puntos que cubran todo el arco de la sesión (inicio y final), en el lenguaje del estudiante — sirve también como autochequeo de si sobraron ideas.

## Estructura de archivos: teoría y práctica separadas

Cada archivo de nota tiene una sola responsabilidad: teoría, o práctica, nunca ambas — y dentro de teoría, un solo objetivo de aprendizaje por archivo.

- **Teoría, un archivo por objetivo de aprendizaje**, en `notas_unidades/unidadN/`, numerado secuencialmente (`0_...`, `1_...`, `2_...`, ...) en el orden en que aparecen los objetivos en el README. Si un tema del temario cubre varios objetivos observables distintos (ej. "activo financiero" prueba un objetivo y "estructura del SFM" prueba otro), son archivos separados aunque vengan del mismo tema o de las mismas diapositivas — no lo decidas por tema del temario, decídelo por objetivo. Cada archivo contiene: `## Objetivo de la unidad` (el objetivo exacto del README que prueba), `## Contenido`, las secciones de teoría numeradas desde 1 (`### 1. ...`, `### 2. ...`) directamente después de la tabla de Contenido, sin encabezado "Parte I" que las agrupe (no hay una "Parte II" en el mismo archivo con la que contrastarlo, la práctica vive aparte), `## Fuentes y referencias recomendadas` y `## Cierre de la unidad` (3-4 puntos, solo del contenido de ese archivo).
- **Práctica, un solo archivo por unidad**, en `practicas/unidadN/practica_unidadN.md` (carpeta `practicas/` en la raíz del repo, espejo de `notas_unidades/`, no dentro de `notas_unidades/unidadN/`). Junta los ejercicios/talleres/casos de *todos* los archivos de teoría de esa unidad, agrupados con un `##` por archivo de teoría (mismo título que el `#` del archivo de teoría correspondiente, en el mismo orden). No lleva Objetivo, Contenido ni Cierre propios — esos viven en los archivos de teoría.
- La tabla `## Contenido` de cada archivo de teoría **no incluye una fila de "Taller práctico"**; en su lugar lleva, justo debajo de la tabla, una nota `> La práctica de este tema está en [\`practica_unidadN.md\`](../../practicas/unidadN/practica_unidadN.md).` (ruta relativa desde `notas_unidades/unidadN/`).
- Al crear una unidad nueva (2, 3, 4...), sigue este mismo patrón desde el inicio: primero fija los objetivos del README, luego un archivo de teoría por objetivo, luego un solo `practica_unidadN.md` — no mezcles teoría y práctica en el mismo archivo, y no juntes dos objetivos en un mismo archivo de teoría aunque el tema tenga solo una sesión.

## Notación matemática

Las fuentes del curso (Fabozzi et al.) usan notación en inglés. En las notas del curso se traduce siempre a esta notación:

| En vez de... | Usar | Significado |
|---|---|---|
| `PV` | `VP` | Valor presente |
| `FV` | `VF` | Valor futuro |
| `i` | `r` | Tasa de interés por periodo |
| `APR` | `TNA` | Tasa nominal anual |
| `EAR` | `TEA` | Tasa efectiva anual |
| `CF` | `FC` | Flujo (pago) constante |
| "principal" | "capital" | Monto invertido o prestado |

Reglas adicionales:

- **Toda fórmula nueva lleva, antes de presentarse, un bloque "¿De dónde sale la fórmula?"** que la derive a partir de una fórmula ya vista antes en la misma unidad — nunca postularla sin mostrar de dónde sale. Encadena la derivación con lo inmediato anterior (ej. la TEA se deriva aplicando la fórmula de VF a un periodo con tasa `r = TNA/n`; la anualidad se deriva como suma de flujos únicos descontados con la fórmula de VP de la sección anterior).
- **Anota restricciones de dominio explícitas en la fórmula misma** cuando existan (ej. `r ≠ 0` al dividir entre `r`), no solo en el texto que la rodea.
- **Conserva las citas del libro de texto original** (autor, capítulo, número de ecuación en inglés) aunque el símbolo en el cuerpo del texto esté en español — la cita apunta a la fuente tal cual está publicada.

## Estilo de prosa

Aplica a toda prosa nueva o editada en `notas_unidades/**/*.md` (y a `practicas/**/*.md`).

- **Sin em dashes ("—").** Nunca los uses para unir cláusulas. Según el caso: aposición breve → coma o paréntesis; explicación o consecuencia → dos puntos; dos oraciones relacionadas → punto y coma o punto separado. Excepción: el encabezado de plantilla ya establecido en los archivos de teoría de esta unidad (`## Cierre de la unidad — Lo esencial para recordar`) se mantiene tal cual por consistencia entre archivos; si se cambia, se cambia en todos los archivos de la unidad a la vez, no en uno solo.
- **Sin encabezado "Parte I" vestigial.** No agrupes las secciones de teoría bajo un `## Parte I: Teoría` (o `— Teoría`). No hay una "Parte II" en el mismo archivo con la que contrastarlo (la práctica vive en `practica_unidadN.md`), así que ese encabezado no distingue nada. Las secciones `### 1. ...` van directamente después del separador de la tabla de Contenido.
- **Fuentes consolidadas, no repartidas.** No pongas una línea `*Fuente: ...*` después de cada subsección. Todas las citas bibliográficas de un archivo de teoría van juntas en `## Fuentes y referencias recomendadas`, al final, y esa sección **no** aparece como fila en la tabla `## Contenido` (no es un tema de la unidad, es material de referencia). Esto no aplica a la cita puntual de una fórmula (ver "Notación matemática" arriba), que sí se mantiene junto a la fórmula misma.
- **Sin verbosidad de LLM.** Evita frases de relleno ("cabe destacar que", "es importante notar que", "conviene mencionar antes de continuar") y evita repetir con otras palabras algo que la oración anterior ya dijo, incluida una cita textual con atribución que no aporta nada nuevo. Si una oración se puede borrar sin perder información, bórrala.
- **El archivo debe pasar markdown lint sin errores.** Reglas por defecto de `markdownlint` (encabezados con salto de nivel correcto y una línea en blanco antes/después, listas rodeadas de línea en blanco, sin tabs, sin espacios al final de línea, el archivo termina en un solo salto de línea), excepto `MD013` (longitud de línea), desactivada porque las tablas y los párrafos largos son parte del estilo de estas notas. Si el proyecto no tiene `markdownlint`/`prettier` instalados, revisa estas reglas a mano.
- **Las tablas van "prettified".** Columnas alineadas: cada columna tiene el ancho de su celda más larga, con al menos un espacio de margen a cada lado del texto y los `|` alineados verticalmente entre filas, igual que produce un formateador de Markdown (p. ej. Prettier) al guardar. No dejes una tabla con columnas sin alinear.
