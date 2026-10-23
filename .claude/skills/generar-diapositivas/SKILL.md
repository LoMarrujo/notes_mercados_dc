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

Con `--conciso` el deck lleva el mínimo de texto: se conservan definiciones
(primera cláusula), fórmulas, tablas, figuras, el arranque de cada "Ejemplo
resuelto" con sus fórmulas/tablas/listas, y de cada lista o párrafo con
encabezado en negritas solo el encabezado y su primera cláusula. La prosa
explicativa, los "¿De dónde sale la fórmula?", los comentarios en
blockquote y el `## Apéndice` se quedan solo en el `.md`; las fuentes se
reducen a la referencia bibliográfica. Sigue siendo generado desde el `.md`
(los recortes son reglas mecánicas en `condense_doc`), así que no hay drift.

De la prosa de un "Ejemplo resuelto", el modo conciso conserva además la
oración que lleva algo en **negritas**: en el `.md`, la cifra clave de la
conclusión (el punto de equilibrio, lo que se gana o se pierde) va en
negritas para que la diapositiva no pierda el resultado del ejemplo. Una
figura que sigue inmediatamente a un ejemplo viaja con él y se reduce (hasta
`SHRINK_MIN`, la mitad de su tamaño) para caber en la misma diapositiva, y
reemplaza a la tabla del ejemplo: la diapositiva muestra la figura y no la
tabla, que se queda solo en el `.md`. Las tablas sin figura (fuera de un
ejemplo, o de un ejemplo sin figura) se conservan.

Las mismas reglas aplican a un ejemplo escrito como párrafo,
`**Ejemplo (...).** ...`, en vez de blockquote: el segmento que abre (hasta
el siguiente párrafo con encabezado en negritas o subtítulo) conserva la
oración en negritas de su prosa, y la figura con que termina se pega al
ejemplo, se reduce y reemplaza a su tabla. Así una nota escrita con
ejemplos en párrafo no necesita marcas `conservar` para mostrar sus
resultados ni deja figuras solas en una diapositiva.

Si una diapositiva conciso queda demasiado escueta, se marca en el `.md` el
bloque que debe salir completo con `<!-- diapositivas: conservar -->` en la
línea anterior (un párrafo, una lista o un blockquote entero). El comentario
no se ve en la nota renderizada y no afecta el modo normal.

Para que una figura se vea grande, `<!-- diapositivas: figura sola -->` en
la línea anterior a la imagen la pone sola en su diapositiva, escalada al
alto y ancho disponibles, en ambos modos. En modo conciso no se pega a su
ejemplo ni le quita la tabla. Es una excepción deliberada al presupuesto
de diapositivas: cada figura marcada cuesta una diapositiva propia. Si el
texto que precede a la figura queda suelto en una diapositiva, conviene
reordenar el `.md` para que la figura vaya después de sus fórmulas (como
en 4.3 de `unidad3/1_probabilidad_y_riesgo.md`).

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
recorta o resume contenido para que quepa (salvo con `--conciso`, ver
arriba).

La paginación respeta segmentos de conocimiento (`starts_segment`): un
subtítulo `#### N.M ...` abre su propia diapositiva y se vuelve su título;
un párrafo con encabezado en negritas (`**Definición:**`, `**Cómo se
mitiga.**`), un "Ejemplo resuelto" o una figura empiezan un segmento, que
pasa completo a la siguiente diapositiva si no cabe en lo que queda. Un
encabezado sin cuerpo propio (un párrafo en negritas corto o que termina en
":") viaja con el segmento que le sigue; uno con contenido propio ("**Cuándo
conviene.** El Bono M conviene si...") se queda donde cabe. Solo un
segmento más alto que una diapositiva entera se parte bloque por bloque.

**Math en línea (`$...$`).** No es LaTeX real: `_latex_frag_to_text` lo
convierte a texto. Los sub/superíndices se dibujan como runs con baseline
real (`_split_subscript`), así que `$F_X$` o `$v_N$` conservan su subíndice
también en prosa corrida. Entiende griegas, fracciones simples, `\sqrt`,
relaciones y la notación de conjuntos y probabilidad (`\mathcal{F}` → ℱ,
`\mathbb{R}` → ℝ, `\cup`, `\cap`, `\emptyset`, `\subseteq`, `\in`, `\mid`,
`\sim`, `\cdots`, `\int`, `\sum`, `\mathbf{}`/`\operatorname{}` sin
estilo). Un comando que no esté en la tabla sale sin la diagonal
("mathfrak{X}"): se agrega a `_latex_frag_to_text`, nunca se parchea el
`.pptx`. En un bullet que empieza con `- **$v_N$**: ...`, ese símbolo
todavía se rasteriza como imagen (`bullet_leading_symbol`).

**Fórmulas en bloque (`$$...$$`).** Se dibujan con el mathtext de
matplotlib, que no tiene entornos. Por eso `\begin{cases}` y
`\begin{pmatrix}` se maquetan aparte (`_render_env_formula`: cada celda en
una rejilla, con la llave o los paréntesis escalados), y `\big(`/`\Big(` se
traducen a `\left(`/`\right)` (`_mathtext_compat`). Otros entornos
(`aligned`, `array`, `bmatrix`) no están soportados: o se agrega su caso
ahí, o la fórmula se reescribe.

## Estructura del deck generado

Portada → Objetivo de la unidad → Tabla de contenido (con números de página
reales, calculados después de generar el contenido; con más de 6 temas el
"qué cubre" va a la derecha de cada tema, en letra chica, para que quepan
todos; con 6 o menos va debajo, y si alguno es largo el renglón crece para
que su segunda línea no se encime) → una o más
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
