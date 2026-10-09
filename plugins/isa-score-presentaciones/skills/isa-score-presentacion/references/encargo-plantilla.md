# Plantilla de encargo

Copia este bloque, rellénalo y pégalo en la conversación (en español o inglés). Las diapositivas saldrán siempre en inglés.

```
Presentación ISA · SCORE

1. Tema y contexto (2–10 líneas)            [IMPRESCINDIBLE]
   Qué se presenta, de qué trabajo/proyecto sale y qué tiene que entender el público.

2. Evento, público y duración               [IMPRESCINDIBLE]
   p. ej. "CAiSE'27, sesión de research papers, 20 min + 5 preguntas" /
          "reunión interna del proyecto SPARK, informal, 30 min".

3. Ponente y coautores                       [IMPRESCINDIBLE]
   Ponente (se subraya en la portada) y coautores en orden. Afiliación si no es
   "SCORE Lab, I3US, Universidad de Sevilla, Seville, Spain".

4. Congreso/reunión y fecha                  [IMPRESCINDIBLE]
   Tal como debe salir en la portada, p. ej. "CAiSE'27 · 10th June 2027".

5. Fuentes                                   [RECOMENDADO]
   Paper (PDF o enlace), repositorio, documentación, URLs, capturas, datos.

6. Estructura o secciones deseadas           [RECOMENDADO]
   p. ej. Motivation · Proposal · Evaluation · Conclusions.

7. Mensajes clave (3–5)                      [RECOMENDADO]
   Lo que el público debe recordar.

8. Cautelas                                  [RECOMENDADO]
   Lo que NO se puede afirmar, valores ilustrativos, cosas no confirmadas.

9. Extras                                    [OPCIONAL]
   Correo y QR para el cierre, financiación (sí/no), componentes de la biblioteca
   que quieras reutilizar, capturas a enseñar, fecha de entrega.
```

## Valores por defecto (si falta un dato y nadie puede contestar)

| Dato | Por defecto |
| --- | --- |
| Duración | 20 min → ≈ 15–20 ideas, 45–60 diapositivas físicas |
| Afiliación | SCORE Lab, I3US, Universidad de Sevilla, Seville, Spain |
| Secciones | Motivation · Proposal · Evaluation · Conclusions (o las que salgan del contenido) |
| Cierre | «Thank You» + correo del ponente; sin QR si no hay enlace; logos de financiación sí |
| Idioma | Diapositivas en inglés; notas del orador en el idioma del encargo |

Tema/contexto, ponente y evento **no** tienen valor por defecto: sin ellos se pregunta.

## Ejemplo (resumen del encargo de SPARK, oct. 2026)

```
1. Tema: cómo encajan las piezas del grupo, desde elegir servicios para una composición
   hasta operar un servicio con un pricing publicado. Parte 1: QACO con un ejemplo
   continuo de gestión de flotas; variantes (colocación Cloud–Edge/IoT con CLASP-FaaS,
   selección de recursos cuánticos, reparto de shots); el paso a asignación (qué, dónde,
   cuánto, cuándo); OpenBinding y BIM v1; QACOBench/QACOForge. Parte 2: pricings e
   iPricing, costes en CLASP, pricing-renderer en Delivera (con capturas), SPHERE/SPACE
   y la demo TomatoMeter.
2. Reunión SPARK, informal, ~40 min.
3. Francisco Javier Cavero.
4. SPARK Meeting · October 2026.
5. Documentación de OpenBinding (https://open-binding-docs.vercel.app), capturas de Delivera.
6. QACO · Towards allocation · OpenBinding & BIM · Pricings in operation.
8. No sobredimensionar resultados; los valores del ejemplo son ilustrativos; el mecanismo
   de sincronización no está confirmado.
```

Resultado: `examples/spark/` (64 diapositivas físicas, portada y cierre reales, `agenda-arc` ×4, `pricing-table-build` y `curse-of-customization` reutilizados, arquitectura de OpenBinding con spotlight).
