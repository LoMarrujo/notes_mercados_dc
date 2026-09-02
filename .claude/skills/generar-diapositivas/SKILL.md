---
name: generar-diapositivas
description: Genera (o regenera) el .pptx y el .pdf de una nota de teoría de unidad a partir de su .md, con fidelidad total al contenido. Úsalo siempre que un .md en notas_unidades/**/*.md cambie y su .pptx/.pdf deba reflejar ese cambio, o para crear el .pptx/.pdf de una nota nueva. No edites un .pptx a mano: los .pptx/.pdf de este repo se consideran generados, no fuente.
---

# Generar diapositivas desde las notas

## Por qué existe esta skill

Antes, el `.pptx` de cada unidad se editaba a mano después de escribir el
`.md`, adaptando y resumiendo el contenido a mano en cada diapositiva. Con el
tiempo eso genera drift: el `.md` cambia, alguien olvida (o interpreta
distinto) actualizar el `.pptx`, y el `.pdf` que reciben los alumnos deja de
coincidir con la nota. Esta skill elimina esa categoría de bug: el `.pptx` y
el `.pdf` se generan por completo a partir del `.md`, siguiendo la estructura
que ya exige el skill `notas-unidad` (Objetivo, Contenido, secciones `### N.
...`, Fuentes, Cierre). No hay edición manual intermedia, así que no hay
drift posible entre lo que dice la nota y lo que muestra la diapositiva.

**Regla dura: nunca edites un `.pptx` de `notas_unidades/` directamente (ni a
mano en PowerPoint, ni con python-pptx ad-hoc).** Si el contenido de una
diapositiva está mal, corrige el `.md` y vuelve a correr esta skill. Si el
*diseño* de las diapositivas necesita cambiar (colores, tipografía, cómo se
parte una tabla), el cambio va en `scripts/md_to_pptx.py`, no en un `.pptx`
individual — así el arreglo aplica a todas las unidades a la vez.

## Cuándo usar esta skill

- El usuario edita o pide editar un `.md` de `notas_unidades/unidadN/` y
  también quiere el `.pptx`/`.pdf` actualizado ("actualiza los pptx",
  "regenera las diapositivas", "crea el pptx de la unidad X").
- Se crea una nota de teoría nueva y hace falta su `.pptx`/`.pdf`.
- Se sospecha drift entre una nota y su diapositiva ("siento que el pptx no
  dice lo mismo que el md"): regenerar es la forma de eliminarlo, no
  parchear el pptx existente.

## Cómo usarla

```bash
python .claude/skills/generar-diapositivas/scripts/md_to_pptx.py <ruta/al/archivo.md>
```

Esto escribe `<archivo>.pptx` y `<archivo>.pdf` junto al `.md` (mismo
directorio, mismo nombre base). Requiere Windows con PowerPoint instalado
(usa automatización COM para exportar el PDF); si solo hace falta el
`.pptx`, agrega `--no-pdf`.

Para regenerar una unidad completa, corre el script sobre cada archivo de
teoría de esa unidad (no sobre `practica_unidadN.md`, que no lleva
diapositivas):

```bash
for f in notas_unidades/unidad1/[0-9]_*.md; do
  python .claude/skills/generar-diapositivas/scripts/md_to_pptx.py "$f"
done
```

Después de generar, **verifica visualmente el resultado** (no asumas que
"corrió sin errores" equivale a "se ve bien"): convierte el PDF a imágenes o
ábrelo página por página y revisa que las tablas, fórmulas y diagramas no se
corten ni se encimen. El motor pagina automáticamente por altura estimada;
un bloque inusualmente largo (una tabla de muchas columnas, una nota muy
extensa) puede necesitar ajuste en el script si algo se ve apretado.

## Qué espera del `.md`

El input debe seguir la convención de `notas-unidad`: un `#` con el título,
la línea en negritas del curso, `## Objetivo de la unidad`, `## Contenido`
(tabla con numeral romano/tema/qué cubre), secciones `### 1. ...`, `### 2.
...` en orden, `## Fuentes y referencias recomendadas`, `## Cierre de la
unidad`. Un `## Apéndice: ...` opcional entre las secciones numeradas y
Fuentes también se soporta (se convierte en su propia sección, sin entrada
en la tabla de contenido, igual que en el `.md`).

Dentro de una sección, el generador entiende: párrafos, listas con `-`,
listas numeradas `1.`, tablas, `> blockquotes` (incluyendo uno con una lista
`> - ...` anidada, para los "Ejemplo resuelto"), fórmulas `$inline$` y
`$$display$$` en LaTeX simple, bloques ` ```mermaid ` con `graph TD`, texto
en `**negrita**`/`*cursiva*`/`` `code` ``, y enlaces `[texto](url)` (el
texto se conserva, el URL se descarta porque una diapositiva no es
clickeable). Una citación de fórmula en su propia línea (`*Fuente: ...*`) se
distingue de una cita bibliográfica normal y se dibuja como pie de nota.

También entiende una imagen en su propia línea, `![alt](ruta/relativa.png)`:
inserta el archivo tal cual (PNG/JPG), escalado para llenar el ancho de
contenido sin deformarse. La ruta es relativa al `.md`. A diferencia de
`mermaid` (que se genera desde texto en cada corrida), la imagen es un
archivo real que debe existir y versionarse junto al `.md`; si se generó con
un script (p. ej. una figura de matplotlib/seaborn), ese script también se
versiona junto a la imagen para que sea reproducible, no un PNG suelto sin
origen.

Todo el contenido de cada sección se dibuja; si no cabe en una diapositiva,
el motor pagina automáticamente creando una diapositiva "(cont.)" — nunca
recorta o resume contenido para que quepa.

**Límite conocido del math inline (`$...$`) y su excepción.** El math en
línea no es LaTeX real: convierte sub/superíndices a caracteres Unicode
(`SUB_MAP`/`SUPER_MAP` en `md_to_pptx.py`). Unicode no tiene ningún carácter
de subíndice para letras mayúsculas (solo dígitos y un puñado de minúsculas
como t, n), así que `$v_N$` en texto corrido siempre pierde el subíndice
("vN"), sin importar la notación elegida. **Excepción:** en un bullet que
empieza con un símbolo así, `- **$v_N$**: definición...`, el generador
detecta el subíndice mayúscula y rasteriza *solo ese símbolo* como una
imagen (vía `render_formula_png`), preservando el subíndice real; el resto
del texto del bullet sigue siendo texto normal. Esto no aplica dentro de
prosa corrida (Definición, Justificación): ahí PowerPoint no soporta
imágenes ancladas dentro de un párrafo que hace wrap, así que el símbolo se
queda como "vN" sin subíndice — limitación aceptada, no un bug a repetir
arreglando cada vez que aparezca.

## Estructura del deck generado

Portada → Objetivo de la unidad → Tabla de contenido (con números de página
reales, calculados después de generar el contenido) → una o más
diapositivas por cada sección `### N. ...` (y por el `## Apéndice`, si
existe) → Cierre de la unidad (una diapositiva por cada ~4-5 puntos de
cierre) → Fuentes y referencias recomendadas.

## Diseño

La paleta y tipografía (`Cambria` para títulos, `Calibri` para cuerpo, azul
marino `#1E2761`, dorado `#C9A227`) viven como constantes al inicio de
`scripts/md_to_pptx.py`. Las fórmulas se renderizan con matplotlib
(`render_formula_png`) y los diagramas `mermaid` con un layout por capas
sobre networkx + matplotlib (`render_mermaid_png`) — ninguno de los dos
depende de un binario externo (no hace falta LaTeX ni Graphviz instalados).
