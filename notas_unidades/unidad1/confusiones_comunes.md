# Confusiones comunes

**Mercados de Deuda y Capitales**, Licenciatura en Comercio y Finanzas Internacionales, Universidad Autónoma de Zacatecas

Este documento reúne confusiones frecuentes de la Unidad 1, puntos donde la intuición cotidiana (o una explicación genérica) no calza con la forma precisa en que este curso define los conceptos. Cada sección responde una pregunta puntual y remite a la nota de teoría correspondiente para el desarrollo completo.

## ¿Cuál es la diferencia entre deuda y participación de capital como activos financieros?

La distinción ya se desarrolla a fondo en [`1_intermediacion_financiera.md`](1_intermediacion_financiera.md#2-deuda-directa-indirecta-y-capital): depende de qué promete el emisor, no de qué tan bien le vaya al negocio. Con deuda, el emisor promete un monto fijo (capital más interés) en fechas determinadas, sin importar su desempeño; el inversionista actúa como acreedor. Con participación de capital, el inversionista se vuelve copropietario de una parte de la empresa y su pago depende de las utilidades y del precio de mercado, sin monto ni fecha garantizados.

La confusión más común es tratar "riesgo de la deuda = bajo" como una regla general. No lo es: lo que sí es consistentemente más bajo en la deuda es el riesgo del rendimiento (si el emisor paga, el monto ya se conoce desde la emisión), no el riesgo de crédito (si el emisor va a pagar), que depende de qué tan solvente sea ese emisor en particular. Un bono corporativo de una empresa muy endeudada puede tener más riesgo de crédito que una acción de una empresa sólida, aunque la deuda siga siendo, por diseño, la que promete un monto fijo.

| Característica                          | Deuda (renta fija)                                                                       | Participación de capital (renta variable)                                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Rol del inversionista                   | Acreedor (prestamista)                                                                   | Copropietario (accionista)                                                                                                               |
| Qué promete el emisor                   | Monto fijo: interés periódico más principal al vencimiento                               | Nada garantizado: dividendos (si los hay) y el precio de reventa                                                                         |
| Riesgo del rendimiento                  | Bajo: el monto se conoce desde la emisión (no estocástico)                               | Alto: ni el dividendo ni el precio futuro se conocen de antemano (estocástico)                                                           |
| Riesgo de crédito                       | Depende del emisor: puede ser bajo (CETE) o alto (bono corporativo de empresa endeudada) | No aplica de la misma forma: el accionista no tiene una promesa de pago que incumplir, asume el riesgo del negocio directamente          |
| Prioridad de cobro si el emisor quiebra | Alta: los acreedores cobran antes que los accionistas                                    | Baja: cobra el residual, después de pagar a todos los acreedores                                                                         |
| Derechos corporativos                   | Ninguno                                                                                  | Derecho a voto en asambleas (acciones ordinarias); las preferentes normalmente lo ceden a cambio de preferencia en el pago de dividendos |
| Ejemplos en México                      | CETES, Bonos M, papel comercial, certificados bursátiles                                 | Acciones, FIBRAs, CKD, CERPI                                                                                                             |

Dos ideas más que ayudan a fijar la distinción:

- **Sin fecha de vencimiento.** Un instrumento de deuda tiene una fecha pactada de devolución del capital; la participación de capital no vence nunca, el inversionista solo recupera su dinero si vende el título en el mercado.
- **Riesgo asimétrico de la participación de capital.** Como accionista, lo máximo que puedes perder es el 100% de lo que invertiste (si la empresa quiebra y no queda nada para los accionistas), pero no hay techo a lo que puedes ganar si el negocio crece. Con deuda ocurre lo contrario: tu ganancia está topada a la tasa pactada desde el inicio, aunque a la empresa le vaya excepcionalmente bien. Esta asimetría es la razón última por la que, en promedio y a largo plazo, la participación de capital exige (y históricamente ha pagado) un rendimiento mayor al de la deuda: es la prima por riesgo del principio de aversión al riesgo (ver [`4_ciencia_inversion.md`](4_ciencia_inversion.md#2-principios-del-análisis-de-inversión)).

---

## Fuentes y referencias recomendadas

- Fabozzi, F. J. y Peterson Drake, P. (2009). *Finance*. Wiley.
