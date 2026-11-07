---
name: linkedin-perfil-tech
description: Audita y reescribe perfiles de LinkedIn de profesionales tech (desarrollo, ingeniería de software, QA/testing, DevOps/cloud, IA) para rankear en LinkedIn Recruiter y atraer reclutadores de roles remotos/híbridos, en español e inglés. Úsala siempre que el usuario pegue o adjunte su perfil/CV y pida mejorar titular, Acerca de, experiencia, skills, recomendaciones, keywords, SEO de LinkedIn, Open to Work, perfil bilingüe o posicionamiento en IA, aunque no diga LinkedIn si habla de que lo encuentren reclutadores. Also for LinkedIn profile optimization, headline/About rewrites, recruiter visibility and keyword strategy for software, QA and AI roles.
---

# LinkedIn Perfil Tech — auditoría y reescritura orientada a reclutadores (ES/EN)

Esta skill convierte el perfil de LinkedIn de un profesional tech (desarrollo, ingeniería de software, QA/testing, DevOps/cloud, datos/IA) en un perfil que: (1) aparece en las búsquedas de LinkedIn Recruiter, (2) convence a un reclutador humano en los primeros segundos de lectura, y (3) está listo para procesos remotos/híbridos en español e inglés, con un posicionamiento creíble en IA y en buenas prácticas de ingeniería.

Responde siempre en el idioma en que te habla el usuario; produce las piezas del perfil en los idiomas que pidió (por defecto EN + ES).

## 1. Cómo funciona realmente la visibilidad en LinkedIn

Trabaja con tres "audiencias" distintas y no las confundas: lo que rankea en el buscador no es lo mismo que lo que convence a una persona ni lo que el feed amplifica.

**A. El buscador de LinkedIn Recruiter (filtros + ranking).** Los reclutadores no navegan: escriben un título, 2–3 skills, una ubicación y operadores booleanos, y reciben una lista rankeada según la coincidencia en titular, título del puesto actual, sección Skills y Acerca de. Consecuencias:
- El **titular** es el campo de mayor peso y el único texto que acompaña al nombre y la foto en los resultados. Debe contener el título estándar del rol y las skills más buscadas, no un eslogan.
- La sección **Skills** actúa como filtro discreto en Recruiter: si la skill no está en la lista, en una búsqueda filtrada por esa skill el perfil queda excluido, no "más abajo". Por eso importan los nombres exactos (LinkedIn solo acepta skills de su catálogo estandarizado).
- El **título del puesto actual** se filtra explícitamente: usa títulos estándar de mercado ("Senior Software Engineer", "QA Automation Engineer"), nunca títulos creativos. Una prueba de un consultor sobre ~2.500 perfiles encontró que abreviaturas como "Sr." rankean peor que "Senior" escrito completo.
- LinkedIn publica que los miembros con 5+ skills son encontrados hasta 27x más en búsquedas de reclutadores, con puesto actual hasta 16x más, con ciudad hasta 23x más, y que los perfiles con foto reciben 21x más visitas. Son cifras promocionales (no estudios controlados), pero señalan qué campos alimentan el índice.
- Recruiter permite filtrar por años de experiencia con una skill y rankea mejor a candidatos conectados con empleados de la empresa que busca: la red del usuario también cuenta.

**B. El reclutador humano.** Escanea en este orden: foto → titular → ubicación → puesto actual → primeras líneas de Acerca de → números. Cada sección debe sostenerse sola, y lo que se ve antes del "ver más" (≈300 caracteres en Acerca de, ≈70 del titular en móvil) debe contener la propuesta de valor completa.

**C. El algoritmo del feed** (solo si el usuario quiere publicar). Según análisis independientes 2025–2026 (LinkedIn no publica pesos), prioriza tiempo de lectura (dwell time), comentarios sustantivos y guardados por encima de likes; penaliza engagement bait, pods y exceso de hashtags; degrada enlaces externos en el cuerpo (magnitud discutida, de ~10% a ~60%); y favorece documentos/carruseles y video nativo. Trátalo como orientación, no como ciencia exacta, y dilo así al usuario.

### Límites técnicos vigentes (si el usuario reporta algo distinto, verifica en LinkedIn Help)

| Campo | Límite | Nota práctica |
|---|---|---|
| Titular | 220 caracteres | ~70 visibles en móvil y resultados: lo importante primero |
| Acerca de | 2.600 caracteres | ~300 visibles antes de "ver más"; apuntar a 1.800–2.200 |
| Descripción por experiencia | 2.000 caracteres | Título del puesto: 100 caracteres |
| Skills (sección) | 100 según LinkedIn Help (muchas guías aún dicen 50) | Las skills asociadas a puestos no cuentan en el límite |
| Top skills en Acerca de | 5 | Deben ser las 5 keywords más buscadas para el rol objetivo |
| Skills por puesto (Experiencia) | hasta 5 | Solo 2 se muestran sin desplegar |
| Perfil en otro idioma | 1 secundario, solo desde desktop | Sin traducción automática; ambos se mantienen a mano |
| Post / comentario | 3.000 / 1.250 caracteres | Para el plan de actividad |

## 2. Flujo de trabajo

### Paso 0 — Reúne insumos antes de escribir

Pide (o localiza en lo que el usuario ya adjuntó):
1. **Perfil actual completo**: texto pegado o el PDF que LinkedIn genera con "Más → Guardar como PDF". No intentes abrir la URL del perfil: LinkedIn bloquea el acceso sin sesión.
2. **2–3 títulos de rol objetivo** y, si es posible, **3–5 vacantes reales** (texto o enlaces). Son la fuente de verdad de las keywords; sin ellas, usa la biblioteca de la sección 4 y dilo.
3. **Seniority, años de experiencia y stack real** (lo que puede defender en entrevista).
4. **3–5 logros con números** o los datos crudos para calcularlos (usuarios, requests/día, tiempos de despliegue, costos, incidentes, cobertura, bugs en producción, releases). Si no hay números, pide el antes/después y ayúdalo a estimar de forma honesta y defendible.
5. **Certificaciones, educación, idiomas con nivel MCER** (B2/C1) — los reclutadores de roles remotos filtran por nivel de inglés.
6. **Modalidad y mercados objetivo** (LatAm, EE. UU., España/UE), zona horaria, disponibilidad.
7. **Restricciones**: ¿está empleado? (Open to Work "solo reclutadores"), NDA, proyectos no publicables.

Si el usuario solo pegó el perfil y quiere avanzar, haz una primera pasada completa y marca cada hueco con `[DATO: …]` y cada suposición con `[SUPUESTO: …]`. Nunca inventes un número, un título, una fecha ni una certificación: un dato falso en LinkedIn se detecta en la primera entrevista y destruye la credibilidad del resto del perfil.

### Paso 1 — Fija el objetivo en una línea

"[Rol objetivo] [seniority] para [tipo de empresa/mercado], [modalidad], idioma primario [EN/ES]". Toda decisión posterior se evalúa contra esta línea. Si el usuario quiere apuntar a dos roles muy distintos (p. ej., QA Lead y AI Engineer), explícale que un perfil dividido rankea peor para ambos y propón un rol principal más uno adyacente coherente (p. ej., "QA Automation Engineer" + "AI-assisted testing").

### Paso 2 — Construye el mapa de keywords

1. Extrae de las vacantes los términos que aparecen en 3 o más anuncios: títulos, tecnologías, prácticas, certificaciones, soft skills, requisitos de modalidad e idioma.
2. Completa con la biblioteca de keywords (sección 4) del dominio del usuario.
3. Clasifica cada término: **Título** (titular + puesto actual), **Core** (titular + top 5 skills + Acerca de), **Soporte** (sección Skills + descripciones de experiencia), **Modalidad/idioma**.
4. Define el par EN/ES de cada término y dónde se usa cada versión (ver Paso 5). Los nombres de tecnologías, frameworks y certificaciones no se traducen.
5. Regla de oro: una keyword solo entra si el usuario puede sostenerla en entrevista. Lo que esté aprendiendo se marca como "aspiracional" y no va en titular ni en top 5.

### Paso 3 — Audita con el scorecard (0–100)

Puntúa cada dimensión, explica el hallazgo en una línea y la acción concreta. El total sirve para medir antes/después.

| # | Dimensión | Pts | Qué evaluar |
|---|---|---|---|
| 1 | Encontrabilidad | 15 | Título estándar + keywords Core presentes en titular, puesto actual y Skills; ubicación e industria completas |
| 2 | Titular | 10 | Fórmula completa, ≤220, lo esencial en los primeros 70 caracteres, sin frases vacías |
| 3 | Acerca de | 10 | Hook con número en las primeras 2 líneas, pruebas, stack, forma de trabajar, IA, modalidad, CTA |
| 4 | Experiencia | 15 | Bullets de impacto cuantificado (fórmula XYZ), títulos estándar, hasta 5 skills por puesto, sin huecos inexplicados |
| 5 | Skills | 10 | 30–60 relevantes, top 5 = keywords Core, obsoletas eliminadas, endorsements en las top |
| 6 | Prueba social | 10 | Recomendaciones recientes y específicas, Destacados con repos/demos/artículos, Proyectos, Licencias y certificaciones |
| 7 | Básicos | 5 | Foto profesional, banner con propuesta de valor, URL personalizada, info de contacto, idiomas, pronunciación del nombre |
| 8 | Señales de IA | 5 | Evidencia concreta (qué construyó o cómo lo usa con métricas), no autodeclaraciones |
| 9 | Prácticas de ingeniería / calidad | 5 | Vocabulario SDLC y de calidad respaldado por ejemplos (CI/CD, testing, arquitectura, métricas DORA) |
| 10 | Preparación remoto/híbrido | 5 | Open to Work configurado, zona horaria y solapamiento, nivel de inglés, trabajo asíncrono, tooling |
| 11 | Bilingüe | 5 | Perfil secundario creado, coherente y actualizado; títulos estándar en ambos idiomas |
| 12 | Actividad | 5 | Cadencia, formato, tema consistente, comentarios sustantivos en su nicho |

Añade la **prueba del reclutador**: pide al usuario que busque en el buscador de personas de LinkedIn "título objetivo + 2 skills" (idealmente desde otra cuenta) y anote en qué página aparece. Se repite 2–3 semanas después de los cambios; la indexación no es inmediata.

### Paso 4 — Reescribe sección por sección

Entrega siempre **antes → después** y el conteo de caracteres de cada pieza.

**Foto y banner.** Foto actual, rostro visible, fondo neutro. Banner con una frase de valor + stack (ej.: "Backend Node.js & AWS · Rescato sistemas legacy y los llevo a producción con CI/CD"). Sin foto, el perfil pierde la mayor parte de las visitas.

**Titular (≤220).** Fórmula:
`[Título estándar del rol] | [2–3 skills Core] | [Resultado con número o especialidad] | [Ángulo IA concreto] | [Modalidad · idiomas]`
- Entrega 3 opciones por idioma: una conservadora (máxima densidad de keywords), una con resultado, una con especialidad de nicho.
- Prohibido: "apasionado", "ninja", "rockstar", "buscando nuevas oportunidades", "| Open to Work" (para eso está la función).
- Si el usuario es junior, sustituye el resultado por formación + proyecto demostrable.

Ejemplos (verifica el conteo antes de entregar):
- EN: `Senior Backend Engineer | Node.js · TypeScript · AWS | APIs serving 50M req/day · Legacy rescue & modernization | LLM/RAG integrations | Remote · EN/ES`
- ES: `Ingeniero de Software Senior (Backend) | Node.js · TypeScript · AWS | Rescate y modernización de sistemas legacy | Integraciones con LLM/RAG | Remoto · ES/EN`
- QA EN: `QA Automation Engineer (SDET) | Playwright · TypeScript · API Testing · CI/CD | Cut regression time 70% | AI-assisted testing · ISTQB CTFL | Remote · EN/ES`

**Acerca de (1.800–2.200).** Estructura:
1. **Hook (≤300 caracteres, visible sin desplegar)**: rol + problema que resuelve + un número. Sin "Hola, soy…".
2. **Pruebas**: 3 logros con métricas, uno por línea.
3. **Stack**: una línea con las keywords Core y Soporte, separadas por "·".
4. **Cómo trabajo**: 2–3 prácticas de ingeniería/calidad con ejemplo concreto (no una lista de buzzwords).
5. **IA**: qué construyó o cómo la usa, con evidencia y criterio (ver sección 3).
6. **Modalidad**: remoto/híbrido, zona horaria ("UTC-3, solapamiento completo con EST y 4h con CET"), idiomas con nivel.
7. **CTA**: cómo contactar y para qué tipo de conversación.
Escribe en primera persona, frases cortas, párrafos de 1–3 líneas; nada de formato Unicode "negrita" que rompe lectores de pantalla y búsquedas.

**Experiencia.** Por puesto: título estándar (si el título interno era raro, usa el estándar y aclara el interno entre paréntesis), empresa, fechas, modalidad (LinkedIn permite indicar remoto/híbrido/presencial), 1 línea de contexto (producto, escala, equipo) y 3–5 bullets con la fórmula XYZ de Google: *Logré [X], medido por [Y], haciendo [Z]*.
- Antes: "Responsable del backend y de los despliegues".
- Después: "Reduje el tiempo de despliegue de 2 h a 12 min (−90 %) migrando un monolito PHP a servicios Node.js con pipelines de CI/CD en GitHub Actions y despliegue a VPS".
- Añade hasta 5 skills por puesto, coherentes con la sección Skills: dan contexto a los filtros del reclutador.
- Huecos laborales: una entrada honesta ("Formación en…", "Proyecto independiente…") supera a un hueco inexplicado.

**Skills.** Top 5 en Acerca de = las 5 keywords Core exactas de las vacantes. Sección Skills: 30–60 relevantes ordenadas por prioridad; elimina obsoletas y genéricas ("Microsoft Office"); pide endorsements a colegas reales ofreciendo reciprocidad (nunca comprados). Usa los nombres del catálogo de LinkedIn (p. ej., "Node.js", no "NodeJS").

**Destacados y Proyectos.** 3–6 piezas: repositorio con README sólido, demo, artículo técnico, charla, caso de estudio en PDF. Etiqueta skills en cada proyecto. Para QA: framework de automatización público, reporte de estrategia de pruebas anonimizado.

**Licencias y certificaciones.** Nombre oficial exacto, emisor, fecha, ID/URL de verificación. Prioriza las que aparecen en vacantes (AWS, ISTQB, Kubernetes, Scrum, etc.).

**Recomendaciones.** Objetivo: 3–6 recientes de perfiles distintos (jefe, par, cliente, QA↔Dev). Entrega un mensaje de solicitud por idioma que indique en qué proyecto trabajaron y qué 2 puntos agradecería que mencione (facilita la respuesta y orienta las keywords). Ofrece escribir una recomendación a cambio.

**Configuración.** Open to Work: 3–5 títulos estándar, tipos de ubicación (remoto + híbrido si aplica), ubicaciones (ciudad + "Remoto" en los países objetivo), tipo de empleo, fecha de inicio, visibilidad "solo reclutadores" si está empleado (LinkedIn dice aplicar "esfuerzos razonables" para ocultarlo al empleador actual, sin garantía). Ubicación: área metropolitana real, no un país genérico. URL personalizada con nombre y apellido. Sección Idiomas con nivel. Si ofrece servicios freelance, activar la página de servicios.

### Paso 5 — Versión bilingüe (perfil en otro idioma)

- El perfil secundario se crea solo desde desktop ("Añadir perfil en otro idioma"); LinkedIn no traduce nada y los cambios del perfil primario **no** se propagan: cada actualización se hace dos veces. Los visitantes ven la versión que coincide con su idioma de interfaz, con un selector manual.
- **Idioma primario**: para roles remotos internacionales, inglés (la mayoría de búsquedas de reclutadores globales se hacen en inglés); español como secundario para LatAm y España. Si el mercado principal es local, al revés. Advierte que cambiar el idioma primario después es engorroso.
- **Títulos de rol**: en el perfil en español, usa el título que usan las vacantes locales; en tech latinoamericano suelen convivir "Ingeniero/a de Software" y "Backend Developer". Cuando el mercado use el término inglés, mantenlo también en el perfil en español.
- **Qué traducir**: titular, Acerca de, títulos y descripciones de experiencia, recomendaciones (resumen), educación. **Qué no traducir**: tecnologías, certificaciones, nombres de productos, métricas.
- **Registro**: el inglés profesional de LinkedIn es más directo y cuantitativo; el español tolera más contexto. No hagas traducción literal; reescribe con las keywords del mercado de cada idioma.
- Entrega las dos versiones lado a lado con los conteos de caracteres.

### Paso 6 — Plan de actividad 30/60/90 (opcional, si el usuario publicará)

- **Semanas 1–4**: implementar el perfil; comentar con sustancia (3+ líneas con una idea propia) en 5–10 publicaciones semanales de su nicho; conectar con reclutadores y personas de 10 empresas objetivo con nota personalizada (≤300 caracteres).
- **Semanas 5–8**: 2 publicaciones por semana sobre un tema estable (p. ej., "rescate de proyectos legacy", "automatización de pruebas con IA"): casos reales, antes/después, lecciones. Formatos que generan lectura: documento/carrusel PDF, texto + imagen, video nativo corto. Enlaces externos en el primer comentario. Responder cada comentario en la primera hora.
- **Semanas 9–12**: pedir 2–3 recomendaciones, publicar 1 caso de estudio en Destacados, repetir la prueba del reclutador y recalcular el scorecard.

### Paso 7 — Verificación final antes de entregar

- Conteo de caracteres de cada pieza dentro del límite y lo esencial dentro de la zona visible.
- Cada número, título, fecha y certificación proviene del usuario; los huecos están marcados `[DATO]`.
- Las keywords Core aparecen en titular, puesto actual, top 5 skills y Acerca de (coherencia que el ranking premia); ninguna keyword aparece de forma forzada o repetida sin sentido (los lectores humanos y los filtros de calidad penalizan el stuffing).
- Nada de claims de IA sin evidencia; nada de superlativos; sin datos personales sensibles (dirección, documento, teléfono personal en texto público).
- Versiones EN y ES dicen lo mismo con las keywords de cada mercado.

## 3. Posicionamiento en IA y en ingeniería (sin inflar)

La "alfabetización en IA" ya es piso, no diferenciador: LinkedIn (Skills on the Rise 2025) la puso como la skill de mayor crecimiento y en 2026 el crecimiento se movió a skills técnicas concretas (prompt engineering, anotación de datos, MLOps/LLMOps, fine-tuning, APIs de modelos, RAG, bases vectoriales, automatización de flujos) y a estrategia (gobernanza de datos, IA responsable). El Stack Overflow Developer Survey 2026 muestra que dos tercios de los desarrolladores usan asistentes o agentes de código y que la confianza depende de poder verificar el resultado: el perfil debe mostrar **criterio**, no entusiasmo.

Tres niveles de evidencia; usa el más alto que el usuario pueda demostrar:
1. **Ingeniería asistida por IA**: qué herramientas usa (Claude Code, GitHub Copilot, Cursor…), con qué disciplina (revisión de código, tests, evaluación del output) y qué resultado medible (tiempo de entrega, cobertura, defectos). Ej.: "Reduje 35 % el tiempo de implementación de features integrando asistentes de código con revisión obligatoria y pruebas de contrato".
2. **Construcción de features con IA**: integraciones con APIs de LLM, RAG, bases vectoriales, agentes, evaluaciones (evals), guardrails, control de costo y latencia, observabilidad de prompts. Ej.: "Diseñé un asistente RAG sobre 40k documentos con 92 % de precisión en evals internos y costo por consulta < USD 0,01".
3. **Calidad y testing de sistemas con IA**: pruebas de aplicaciones LLM (no determinismo, evals, red-teaming, sesgos), generación de pruebas asistida por IA, pruebas autorreparables, certificaciones ISTQB CT-AI / Testing with Generative AI.

Prácticas de ingeniería que los reclutadores técnicos reconocen (menciónalas solo con ejemplo): SDLC y Agile/Scrum, TDD/BDD, Clean Code y SOLID, arquitectura limpia/hexagonal, DDD, microservicios y event-driven, REST/GraphQL/gRPC, CI/CD, infraestructura como código, contenedores y Kubernetes, observabilidad (OpenTelemetry, Grafana), métricas DORA (frecuencia de despliegue, lead time, tasa de fallos, MTTR), code review, trunk-based development, feature flags, seguridad (OWASP, SAST/DAST), gestión de deuda técnica y ADRs.

## 4. Biblioteca de keywords por dominio (EN primero; ES cuando difiere)

**Títulos (EN ↔ ES)**: Software Engineer ↔ Ingeniero/a de Software · Backend Developer ↔ Desarrollador/a Backend · Full Stack Developer ↔ Desarrollador/a Full Stack · Frontend Developer ↔ Desarrollador/a Frontend · Tech Lead ↔ Líder Técnico · Solutions/Software Architect ↔ Arquitecto/a de Soluciones/Software · DevOps / Platform / Cloud Engineer ↔ Ingeniero/a DevOps/Cloud · Site Reliability Engineer (SRE) · QA Engineer ↔ Ingeniero/a de QA · QA Automation Engineer / SDET ↔ Ingeniero/a de Automatización de Pruebas · Test Lead / QA Manager ↔ Líder de QA · AI Engineer ↔ Ingeniero/a de IA · Machine Learning Engineer · Data Engineer ↔ Ingeniero/a de Datos.

**Backend / APIs**: Node.js, TypeScript, NestJS, Express, Go (Golang), Python, FastAPI, Java, Spring Boot, PHP, Laravel, .NET, REST APIs, GraphQL, gRPC, Microservices, Event-Driven Architecture, Domain-Driven Design, PostgreSQL, MySQL, MongoDB, Redis, Kafka, RabbitMQ, Software Architecture, System Design, Performance Optimization, Legacy Modernization.

**Frontend / Mobile**: React, Next.js, Angular, Vue.js, React Native, Flutter, Web Performance, Accessibility (WCAG), Design Systems, Testing Library.

**Cloud / DevOps**: AWS (Lambda, ECS/EKS, RDS, S3, API Gateway), Azure, Google Cloud, Docker, Kubernetes, Terraform, AWS CDK, GitHub Actions, GitLab CI, Jenkins, Infrastructure as Code, CI/CD, Linux, Observability, OpenTelemetry, Grafana, Prometheus, Cost Optimization, Cloud Security.

**QA / Testing**: Test Automation, Playwright, Cypress, Selenium, Appium, API Testing (Postman, REST Assured, Playwright API), Contract Testing (Pact), Performance Testing (k6, JMeter, Gatling), Test Strategy, Test Planning, Test Pyramid, Shift-Left Testing, BDD (Cucumber/Gherkin), Quality Gates (SonarQube), Exploratory Testing, Risk-Based Testing, Regression Testing, Mobile Testing, Accessibility Testing (axe), Security Testing (OWASP ZAP), Test Data Management, Flaky Test Management, CI/CD Integration, ISTQB CTFL v4.0, ISTQB CT-TAE, ISTQB CT-AI, AI-Assisted Testing, Self-Healing Tests, Testing LLM Applications. (ES: Automatización de Pruebas, Pruebas de API, Pruebas de Rendimiento, Estrategia de Pruebas, Aseguramiento de Calidad.)

**IA / Datos**: Large Language Models (LLM), Prompt Engineering, Retrieval-Augmented Generation (RAG), Vector Databases (pgvector, Pinecone), LangChain, LangGraph, AI Agents, Model Context Protocol (MCP), OpenAI API, Anthropic API, Google Gemini, Model Fine-Tuning, LLMOps, MLOps, AI Evaluation (Evals), Responsible AI, AI Governance, Workflow Automation, API Integration, Python, PyTorch, Data Pipelines.

**Remoto / colaboración**: Remote Work, Distributed Teams, Asynchronous Communication, Documentation, Cross-functional Collaboration, Stakeholder Management, Mentoring, Technical Communication, Agile, Scrum, Jira, English (C1) — en ES: Trabajo Remoto, Equipos Distribuidos, Comunicación Asíncrona, Colaboración Interfuncional.

Dato de mercado útil para QA: en análisis de ~3.000 vacantes de QA (2026), el modo presencial sigue siendo mayoritario (~53 %); para competir por las vacantes remotas, el perfil de QA debe demostrar automatización, API testing e integración en CI/CD, no solo pruebas manuales.

## 5. Casos particulares

- **Junior / sin experiencia**: titular con rol objetivo + stack + proyecto demostrable; Acerca de centrado en proyectos, formación y cómo aprende; Destacados con 2–3 repos con README y tests; Open to Work público.
- **Cambio a QA o de QA manual a automatización**: destaca pruebas automatizadas ya escritas (aunque sean propias), lenguaje (TypeScript/Python), CI, y una certificación en curso marcada como tal.
- **Liderazgo (Tech Lead / QA Lead)**: métricas de equipo y de entrega (DORA, tiempo de ciclo, escapes a producción), decisiones de arquitectura, mentoría; sin perder las keywords técnicas que filtran los reclutadores.
- **Freelance / consultoría / software factory**: página de servicios, casos de estudio con resultados de negocio, titular que mezcle rol + oferta ("Rescate de proyectos con deuda técnica").

## 6. Formato de entrega

Entrega el resultado como documento (artifact de documento si está disponible; si no, Markdown) con esta estructura:

```
# Auditoría y optimización de perfil LinkedIn — [Nombre]
## 1. Resumen ejecutivo (score actual → estimado; los 3 cambios de mayor impacto)
## 2. Objetivo y mercado (roles, modalidad, idiomas, mercados, idioma primario)
## 3. Mapa de keywords (tabla: categoría | término EN | término ES | dónde va | fuente)
## 4. Scorecard (tabla de 12 dimensiones: puntos, hallazgo, acción)
## 5. Secciones reescritas (antes → después, conteo de caracteres)
   5.1 Titular — 3 opciones EN y 3 ES
   5.2 Acerca de — EN y ES
   5.3 Experiencia — bullets XYZ por puesto + skills por puesto
   5.4 Skills — top 5, lista priorizada, a eliminar
   5.5 Destacados, Proyectos, Licencias y certificaciones
   5.6 Recomendaciones — a quién pedir + mensaje modelo ES/EN
   5.7 Configuración — Open to Work, ubicación, URL, idiomas, perfil secundario
## 6. Plan de actividad 30/60/90 (si aplica)
## 7. Checklist de implementación (orden y tiempo estimado por tarea)
## 8. Datos pendientes [DATO] y supuestos [SUPUESTO]
```

Si el usuario pide solo una pieza (p. ej., "mejórame el titular"), haz el Paso 2 en versión corta (keywords de 2–3 vacantes o de la biblioteca) y entrega esa pieza con 3 opciones y conteo; ofrece el resto en una línea.

## 7. Guardarraíles

- Veracidad primero: ningún número, título, fecha o credencial que el usuario no haya dado. Marca lo pendiente; no "redondees hacia arriba".
- Ninguna autodeclaración de experto en IA sin evidencia; prefiere "construí/integré/evalué" con métricas a "apasionado por la IA".
- Sin keyword stuffing ni listas de 50 tecnologías en el titular: dañan la lectura humana y pueden activar filtros de calidad.
- No prometas posiciones en el ranking ni tiempos de resultado; LinkedIn no publica el algoritmo y las cifras de terceros son estimaciones que cambian cada año (fecha esta skill: noviembre 2026; si tienes búsqueda web y el usuario pregunta por un límite o una regla concreta, verifícala en LinkedIn Help antes de afirmarla).
- Respeta la privacidad: no sugieras publicar datos sensibles ni información confidencial de empleadores (usa cifras relativas si hay NDA: "−40 % de costo" en lugar del monto).
- Trata los cambios de perfil como un sistema: titular, puesto actual, top 5 skills y Acerca de deben contar la misma historia.

## 8. Fuentes consultadas al construir esta skill

- LinkedIn Help: "Create or delete a profile in another language" (https://www.linkedin.com/help/linkedin/answer/1717); "Edit your secondary language profile" (https://www.linkedin.com/help/linkedin/answer/a570288); "Skill endorsements" — límite de 100 skills (https://www.linkedin.com/help/linkedin/answer/31888); "Manage your profile Experience section" (https://www.linkedin.com/help/learning/answer/a593695).
- LinkedIn Official Blog, "5 Steps to Improve your LinkedIn Profile in Minutes" (2016): cifras de foto, skills y ubicación (https://blog.linkedin.com/2016/08/03/5-steps-to-improve-your-linkedin-profile-in-minutes-).
- LinkedIn News, "LinkedIn Skills on the Rise 2026: The fastest-growing skills in the U.S." (https://www.linkedin.com/pulse/linkedin-skills-rise-2026-fastest-growing-us-linkedin-news-nujwe) y cobertura de CNBC (2026-02-24) y Quartz.
- LinkedIn "Jobs on the Rise 2026" (EE. UU.): AI Engineer como rol de mayor crecimiento; cobertura de Social Media Today y NewsNation.
- Stack Overflow, "The results of the 2026 Developer Survey are here" (https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/).
- Social Media Today (2023): top 5 skills en la sección Acerca de y skills por proyecto.
- Coursera, "How to Let Recruiters Know You're Open to Work on LinkedIn"; LoopCV y Resume.co sobre preferencias y visibilidad de Open to Work.
- InterviewStack.io, análisis de 2.983 vacantes de QA Engineer (mayo 2026); TestDino, "Playwright Job Market in 2026".
- Análisis independientes del algoritmo del feed 2026 (eClincher, Expandi, Webtures, Socialync): orientativos, no oficiales.
- Auditorías de practicantes sobre búsqueda en Recruiter (DEV Community, ATS Verification, Slategit): comportamiento de filtros por skills y peso del titular; evidencia anecdótica pero consistente.
