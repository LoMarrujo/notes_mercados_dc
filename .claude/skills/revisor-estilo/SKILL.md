---
name: revisor-estilo
description: Revisa y corrige el estilo de prosa (em dashes, fuentes repartidas, verbosidad de LLM) en archivos de notas_unidades/**/*.md o practicas/**/*.md ya escritos, según las reglas de "Estilo de prosa" del skill notas-unidad. Úsalo cuando el usuario pida revisar, limpiar o pulir el estilo de una nota existente, no para redactar contenido nuevo (para eso usa notas-unidad).
---

# Revisor de estilo de notas

Aplica las reglas de "Estilo de prosa" del skill `notas-unidad` a un archivo (o archivos) ya escritos. Es un pase de limpieza, no de contenido: no agrega ni quita información, no cambia definiciones ni ejemplos, no reestructura secciones a menos que se pida aparte.

## Alcance

Antes de tocar nada, determina qué archivo(s) revisar:
- Si el usuario nombró un archivo, revisa solo ese.
- Si no, revisa los archivos de `notas_unidades/**/*.md` o `practicas/**/*.md` modificados en la sesión actual o en el último commit (`git diff --name-only`, `git diff --name-only HEAD~1`).

## Checklist (en este orden)

1. **Encabezado "Parte I" vestigial.** Si el archivo tiene un `## Parte I: Teoría` (o `## Parte I — Teoría`) seguido de una oración que solo resume lo que ya dice la tabla `## Contenido`, bórralo (el encabezado y esa oración). No aporta nada: no hay un "Parte II" en el mismo archivo (la práctica vive aparte, en `practica_unidadN.md`), así que numerar "Parte I" no distingue nada. Las secciones `### 1. ...`, `### 2. ...` quedan directamente después del separador `---` de la tabla de Contenido.

2. **Em dashes ("—").** Busca cada instancia con Grep. Para cada una, decide el reemplazo según el caso:
   - Aposición breve → coma o paréntesis.
   - Explicación o consecuencia → dos puntos.
   - Dos oraciones relacionadas → punto y coma, o córtalas en dos oraciones con punto.
   - **Excepción, no la toques:** `## Cierre de la unidad — Lo esencial para recordar`, encabezado de plantilla compartido entre los cuatro archivos de teoría de una unidad. Si el usuario pide quitarlo, avísale que es compartido entre archivos antes de hacerlo solo en uno.

3. **Fuentes repartidas.** Busca líneas `*Fuente: ...*` sueltas después de subsecciones. Si las hay:
   - Verifica que cada referencia ya esté (o agrégala) en `## Fuentes y referencias recomendadas`, al final del archivo.
   - Borra las líneas `*Fuente: ...*` sueltas del cuerpo.
   - No toques la cita puntual de una fórmula (número de ecuación, autor, capítulo pegado a la fórmula misma) — esa se queda donde está.
   - Confirma que `## Fuentes y referencias recomendadas` **no** tenga fila propia en la tabla `## Contenido` (no es un tema de la unidad).

4. **Verbosidad de LLM.** Busca:
   - Frases de relleno: "cabe destacar que", "es importante notar que", "conviene mencionar/notar/señalar que", "hay que tener en cuenta que".
   - Oraciones (a menudo una cita textual con atribución de autor) que solo repiten con otras palabras la oración inmediatamente anterior sin agregar información nueva.
   - Bullets o cláusulas que prueban lo mismo que otro bullet de la misma lista (ver también la regla 4 de "Objetivos de aprendizaje" en `notas-unidad`, que ya prohíbe esto para los objetivos).
   Corta lo que se pueda cortar sin perder información. Si una frase es dudosa (podría ser matiz real y no relleno), déjala y no la fuerces.

5. **Formato Markdown y tablas.** Si el proyecto tiene `markdownlint`/`prettier` instalados, córrelos y aplica sus fixes. Si no (como en este repo, sin `node_modules`), revisa a mano: encabezados con salto de nivel correcto y una línea en blanco antes/después, listas rodeadas de línea en blanco, sin tabs ni espacios al final de línea, el archivo termina en un solo salto de línea, y cada tabla tiene sus columnas alineadas (ancho de la celda más larga, `|` alineados entre filas, al menos un espacio de margen a cada lado del texto). No aplica `MD013` (longitud de línea): las tablas y párrafos largos son parte del estilo de estas notas.

## Qué reportar al usuario

Al terminar, resume en pocas líneas: cuántos em dashes se cambiaron y a qué, si se movieron citas a la sección de Fuentes, y qué oraciones se recortaron por redundantes (con un ejemplo breve de antes/después si el cambio no es obvio). No hace falta un reporte exhaustivo línea por línea.

## Qué NO hacer

- No reordenar ni renumerar secciones, no mover contenido a apéndices, no agregar ejemplos ni tablas nuevas — eso es edición de contenido, no de estilo.
- No aplicar estas reglas fuera de `notas_unidades/**/*.md` y `practicas/**/*.md` (por ejemplo, no tocar `README.md` ni archivos en `data/`) a menos que el usuario lo pida explícitamente.
