---
name: notas-unidad
description: Convenciones de este curso (Mercados de Deuda y Capitales) para escribir o editar objetivos de unidad, fórmulas de finanzas y la estructura de archivos (teoría/práctica separadas) en notas_unidades/**/*.md y en el README. Úsalo antes de redactar un objetivo de aprendizaje, presentar una fórmula matemática nueva, o crear/reorganizar archivos de una unidad.
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

- **Teoría, un archivo por objetivo de aprendizaje**, en `notas_unidades/unidadN/`, numerado secuencialmente (`0_...`, `1_...`, `2_...`, ...) en el orden en que aparecen los objetivos en el README. Si un tema del temario cubre varios objetivos observables distintos (ej. "activo financiero" prueba un objetivo y "estructura del SFM" prueba otro), son archivos separados aunque vengan del mismo tema o de las mismas diapositivas — no lo decidas por tema del temario, decídelo por objetivo. Cada archivo contiene: `## Objetivo de la unidad` (el objetivo exacto del README que prueba), `## Contenido`, `## Parte I — Teoría` (secciones numeradas desde 1 dentro del archivo), `## Fuentes y referencias recomendadas` y `## Cierre de la unidad` (3-4 puntos, solo del contenido de ese archivo).
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
