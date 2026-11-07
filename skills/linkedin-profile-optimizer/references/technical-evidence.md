# Competencias técnicas y evidencias para perfiles ES/EN

Fecha de revisión: 2026-11-07.

## Regla de uso

Usar este mapa para descubrir experiencia demostrable y redactar un posicionamiento coherente. Las fuentes documentan prácticas y conocimientos; no miden demanda laboral ni preferencias del algoritmo de LinkedIn. Determinar prioridades comerciales solamente con vacantes fechadas del mercado, nivel y modalidad objetivo. No convertir esta matriz en una lista obligatoria ni atribuir conocimientos, certificaciones o experiencia por asociación.

Clasificar cada competencia como **experiencia profesional**, **proyecto demostrable**, **formación** o **interés**. Pedir contexto, responsabilidad individual, decisión, artefacto y resultado. Aceptar descripciones anonimizadas cuando exista confidencialidad; un repositorio público no es requisito. Si faltan cifras, describir alcance y resultado cualitativo confirmado, sin inventar porcentajes.

## Matriz de exploración

| Rol objetivo / términos EN | Competencias que explorar | Evidencia que pedir | Decisiones y límites que aclarar |
| --- | --- | --- | --- |
| Desarrollo e ingeniería de software / Software Developer, Software Engineer | Programación, estructuras de datos, debugging, APIs, datos, pruebas, revisión de código y diseño mantenible. [1] | Funcionalidad entregada; PR o relato del cambio; fallo diagnosticado; prueba; decisión de diseño; contribución propia. | Elegir tecnologías y complejidad según restricciones. No usar el título Engineer como prueba automática de seniority. |
| Análisis de software / Software Analyst, Systems Analyst, Requirements Analyst | Elicitación, requisitos funcionales y de calidad, modelado, criterios de aceptación, trazabilidad, cambios e interfaces. [1] | Requisito ambiguo aclarado; modelo; ejemplos de aceptación; vínculo requisito–prueba; decisión acordada con stakeholders. | Separar necesidad de solución; explicar conflictos, restricciones y validación. Aclarar si el trabajo fue análisis funcional, técnico o ambos. |
| QA funcional / QA Analyst, Test Analyst | Riesgo de producto, diseño de pruebas, exploración, regresión, defectos y colaboración sobre requisitos. API y SQL cuando procedan. [1–2] | Carta de prueba exploratoria, matriz de riesgos, casos con oráculos, defecto reproducible, decisión de cobertura y resultado. | Justificar qué probar y qué excluir. No medir calidad únicamente por número de casos o defectos. |
| Automatización / QA Automation Engineer, SDET | Código de automatización mantenible, pruebas unitarias/API/contrato/UI según arquitectura, integración CI, datos y diagnóstico de inestabilidad. [2] | Suite ejecutable o explicación técnica; pipeline; fallo útil detectado; medición de duración o flakiness; mantenimiento realizado. | Equilibrar señal, coste, velocidad y fiabilidad. Automatizar una interfaz no demuestra por sí solo ingeniería de frameworks ni competencia SDET completa. |
| Productos con IA / AI Application Engineer, LLM Application Developer | Integración de modelos, datos, recuperación cuando aporte valor, herramientas, evaluaciones, seguridad y operación. [4–6] | Caso de uso; baseline; arquitectura; evaluación versionada; permisos; costes y latencia medidos; gestión de fallos. | Justificar modelo, RAG o agentes frente a alternativas más simples; distinguir prototipo, piloto y producción. |
| Calidad de IA / AI Quality Engineer, AI Test Engineer | Pruebas de datos, modelos y sistema; comportamiento probabilístico; métricas por tarea; sesgos, robustez y seguridad. [3–6] | Dataset y criterios; casos típicos, extremos y adversarios; resultados por segmentos; regresiones; revisión humana; límites conocidos. | No reducir calidad a una única accuracy ni generalizar desde una demo. Explicar el oráculo y la incertidumbre de la evaluación. |

## Distinguir tres relaciones con IA

**IA asistiendo el SDLC:** utilizar asistentes para código, análisis, documentación o generación de pruebas. Pedir cómo se revisó el resultado, cómo se verificó y qué datos se compartieron. Redactar “desarrollo asistido por IA / AI-assisted development” cuando corresponda; esto no acredita construcción de modelos o productos IA.

**Construcción de productos IA:** integrar capacidades de modelos en un sistema con usuarios, datos y operaciones. Preguntar por evaluación, acceso a herramientas, fallback y decisiones de calidad/coste/latencia.

**QA de IA:** evaluar el sistema cuyo comportamiento incluye IA. Distinguirlo de utilizar IA para apoyar pruebas convencionales. ISTQB separa expresamente ambos ámbitos en CT-AI y Testing with Generative AI. [3] No inferir que el candidato posea ninguna certificación.

## Buenas prácticas como decisiones demostradas

Aplicar estos criterios editoriales de entrevista, sin presentarlos como mandatos universales:

- **TDD:** pedir un ejemplo de prueba que guio comportamiento y diseño, con refactorización. Examinar feedback y mantenibilidad; una cifra de cobertura no demuestra TDD.
- **BDD:** pedir ejemplos acordados con negocio y su relación con aceptación. Escribir Gherkin, por sí solo, no prueba colaboración ni descubrimiento.
- **Clean / hexagonal architecture:** pedir límites, dependencias, puertos/adaptadores y motivo de aislamiento. Valorar el coste añadido frente a la variabilidad real del dominio.
- **CQRS:** nombrarlo cuando existan necesidades distintas de lectura/escritura y una decisión explicable. Preguntar por consistencia, diagnósticos y mantenimiento; no introducirlo para adornar el perfil.
- **CI/CD, observabilidad y seguridad:** describir integración, feedback, despliegue, recuperación, señales operativas y controles concretos. DORA distingue entrega continua de despliegue continuo. [2] Para IA, explorar inyección de instrucciones, exposición de datos, permisos excesivos y tratamiento de salidas. [5]

## Errores de posicionamiento

Evitar titulares que acumulen todos los roles; stacks extensos sin contexto; “experto” tras un curso; “AI Engineer” por usar un asistente; “producción” para una demo; apropiarse de resultados del equipo; métricas sin periodo, baseline o alcance; y garantías de seguridad o ausencia de alucinaciones. Conservar equivalencia factual ES/EN: traducir responsabilidades con verbos precisos sin aumentar seniority, alcance, fluidez lingüística ni certificaciones.

## Fuentes primarias

Revisadas el **2026-11-07**. Revalidar versiones y disponibilidad antes de recomendar formación o herramientas.

1. [IEEE Computer Society — SWEBOK V4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4), con [PDF oficial consultado](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf): base de conocimientos de requisitos, arquitectura, construcción, pruebas, calidad, operaciones y seguridad. El PDF permite consultar el contenido cuando la página de presentación restringe el acceso.
2. [DORA — Continuous delivery](https://dora.dev/capabilities/continuous-delivery/): integración, automatización, feedback, observabilidad, seguridad y distinción entre delivery y deployment.
3. [ISTQB — CT-AI v2.0](https://istqb.org/certifications/certified-tester-ai-testing-ct-ai/): pruebas de sistemas IA, datos, modelos y comportamiento probabilístico; diferencia respecto a probar con IA generativa.
4. [NIST — Generative AI Profile, AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): gestión contextual de riesgos a lo largo del ciclo de vida.
5. [OWASP — GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/): amenazas, escenarios y mitigaciones para aplicaciones LLM.
6. [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): evaluaciones específicas por tarea, datasets representativos, evaluación continua y calibración humana; usar los principios independientemente de una plataforma concreta.
