---
name: revisor-estilo
description: Revisa y corrige el estilo de prosa (em dashes, referencias por libro en vez de por capítulo, verbosidad de LLM, términos en inglés sin su equivalente en español antes) y la notación matemática (mayúscula solo para variables aleatorias, minúscula para todo lo demás) en archivos de notas_unidades/**/*.md o practicas/**/*.md ya escritos, según las reglas de "Estilo de prosa" y "Notación matemática" del skill notas-unidad. Úsalo cuando el usuario pida revisar, limpiar o pulir el estilo de una nota existente, no para redactar contenido nuevo (para eso usa notas-unidad).
---

# Revisor de estilo de notas

Aplica las reglas de "Estilo de prosa" y "Notación matemática" del skill `notas-unidad` a un archivo (o archivos) ya escritos. Es un pase de limpieza, no de contenido: no agrega ni quita información, no cambia definiciones ni ejemplos, no reestructura secciones a menos que se pida aparte.

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

3. **Referencias por libro, no por capítulo.** Busca líneas `*Fuente: ...*` sueltas después de fórmulas o subsecciones, y cualquier referencia con capítulo, sección, número de ecuación o página específica (`Cap. X`, `Sec. Y`, `pp. Z`), o un paréntesis `(sección #)` dentro de la prosa. Si las hay:
   - Simplifica cada referencia a una cita de libro completo en formato APA (Autor, A. A. (Año). *Título*. Editorial), sin capítulo, sección ni página.
   - Verifica que esa cita ya esté (o agrégala) en `## Fuentes y referencias recomendadas`, al final del archivo, una sola vez por libro.
   - Borra las líneas `*Fuente: ...*` sueltas del cuerpo: no hay excepción para la cita puntual de una fórmula. Si de verdad hace falta apuntar a un lugar preciso del libro, va a pie de página, nunca como paréntesis `(sección #)` en la prosa.
   - Confirma que `## Fuentes y referencias recomendadas` **no** tenga fila propia en la tabla `## Contenido` (no es un tema de la unidad).

4. **Verbosidad de LLM.** Busca:
   - Frases de relleno: "cabe destacar que", "es importante notar que", "conviene mencionar/notar/señalar que", "hay que tener en cuenta que".
   - Oraciones (a menudo una cita textual con atribución de autor) que solo repiten con otras palabras la oración inmediatamente anterior sin agregar información nueva.
   - Bullets o cláusulas que prueban lo mismo que otro bullet de la misma lista (ver también la regla 4 de "Objetivos de aprendizaje" en `notas-unidad`, que ya prohíbe esto para los objetivos).
   Corta lo que se pueda cortar sin perder información. Si una frase es dudosa (podría ser matiz real y no relleno), déjala y no la fuerces.

5. **Mayúsculas/minúsculas en notación matemática.** Busca símbolos algebraicos de una letra (o letra con subíndice, ej. `$c_t$`, `$v_t$`, `$C_t$`) y verifica que sigan la regla "mayúscula solo para variables aleatorias (inciertas); todo lo demás en minúscula": un símbolo determinista, aunque sea calculado por la fórmula (un dato de entrada como $c$ o $c_t$, o un valor calculado a partir de ellos como $v_t$, con $v_0$ el valor presente y $v_N$ el valor futuro), va en minúscula. Solo lo genuinamente incierto, un flujo estocástico, una variable aleatoria (ej. $C_t$, el valor futuro incierto de una acción), va en mayúscula. "Se calculó con una fórmula" no es lo mismo que "es incierto": no subas de caso un símbolo solo porque la fórmula lo produce. Esta regla aplica donde ya hay notación algebraica (fórmulas, definiciones formales); no la introduzcas en secciones puramente intuitivas o de motivación (ej. una introducción conceptual con ejemplos en palabras y números, sin fórmulas) — ahí el símbolo sería ruido, no precisión. Ver la regla en "Notación matemática" de `notas-unidad`. No toques las siglas multiletra ya establecidas (TNA, TEA, TIR, VPN): esas siempre van en mayúscula, sean dato, resultado o variable aleatoria, y no las cubre esta regla.

6. **Español primero, inglés entre paréntesis.** Busca menciones de un término en inglés (o su sigla) que no vayan precedidas del término en español. Si el término en español no aparece en absoluto (solo el inglés), agrégalo antes: "fijación de precio (pricing)", no solo "pricing"; "valor presente (present value, PV)", no "esto es lo que en inglés se llama *present value*". Ver la regla en "Estilo de prosa" de `notas-unidad`.

7. **Formato Markdown y tablas.** Si el proyecto tiene `markdownlint`/`prettier` instalados, córrelos y aplica sus fixes. Si no (como en este repo, sin `node_modules`), revisa a mano: encabezados con salto de nivel correcto y una línea en blanco antes/después, listas rodeadas de línea en blanco, sin tabs ni espacios al final de línea, el archivo termina en un solo salto de línea, y cada tabla tiene sus columnas alineadas (ancho de la celda más larga, `|` alineados entre filas, al menos un espacio de margen a cada lado del texto). No aplica `MD013` (longitud de línea): las tablas y párrafos largos son parte del estilo de estas notas.

## Qué reportar al usuario

Al terminar, resume en pocas líneas: cuántos em dashes se cambiaron y a qué, si se movieron citas a la sección de Fuentes, qué oraciones se recortaron por redundantes, y qué símbolos cambiaron de mayúscula a minúscula (o viceversa) y por qué (con un ejemplo breve de antes/después si el cambio no es obvio). No hace falta un reporte exhaustivo línea por línea.

## Qué NO hacer

- No reordenar ni renumerar secciones, no mover contenido a apéndices, no agregar ejemplos ni tablas nuevas — eso es edición de contenido, no de estilo.
- No aplicar estas reglas fuera de `notas_unidades/**/*.md` y `practicas/**/*.md` (por ejemplo, no tocar `README.md` ni archivos en `data/`) a menos que el usuario lo pida explícitamente.
