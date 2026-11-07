# IT Skills LinkedIn — ChatGPT / Codex y Claude

**Edición: `ChatGPT` · Español / English · Software Engineering · QA / SDET · AI**

Colección de skills para mejorar perfiles de LinkedIn de profesionales de tecnología. La variante **LinkedIn Profile Optimizer — ChatGPT / Codex** convierte experiencia real en contenido ES/EN para oportunidades remotas e híbridas, contrastando competencias con vacantes actuales cuando dispone de navegación.

## Catálogo de skills

| Skill | Entorno objetivo | Ubicación | Documentación |
| --- | --- | --- | --- |
| **linkedin-profile-optimizer** | **OpenAI ChatGPT / Codex**; identificador **ChatGPT** | [Carpeta completa](skills/linkedin-profile-optimizer/) | Guía detallada y know-how en este README |
| **linkedin-perfil-tech** | Claude / Anthropic, según su documentación | [Skill existente](linkedin-perfil-tech/SKILL.md) | [Guía de Claude conservada](docs/claude-guide.md) |

Cada variante tiene su propio procedimiento. La guía operativa, las plantillas, el helper y las verificaciones descritas a continuación corresponden a **ChatGPT/Codex**. La variante Claude incorporada al repositorio se conserva; su documentación incluye sus propias instrucciones de instalación y uso.

[English guide](#english-guide) · [Skill](skills/linkedin-profile-optimizer/SKILL.md) · [Know-how](#know-how-cómo-realizar-un-buen-análisis) · [Colaborar](#cómo-colaborar-y-construir-mejores-versiones) · [Formulario de entrada](skills/linkedin-profile-optimizer/assets/intake.md) · [Fuentes](skills/linkedin-profile-optimizer/references/sources.md) · [Edición ChatGPT](skills/linkedin-profile-optimizer/)

## Qué entrega

| Entregable | Utilidad |
| --- | --- |
| Diagnóstico priorizado | Identifica problemas de enfoque, evidencia, claridad e idiomas |
| Registro de evidencia | Vincula cada logro con su fuente y contribución individual |
| Contraste de vacantes | Compara requisitos del rol, mercado y modalidad elegidos |
| Mapa ES/EN de términos | Selecciona palabras pertinentes sin atribuir competencias inexistentes |
| Titular, About y experiencia ES/EN | Proporciona bloques coherentes listos para revisar y copiar |
| Skills y Featured | Ordena capacidades y propone pruebas de trabajo relevantes |
| Solicitudes de recomendación ES/EN | Prepara borradores para colaboradores reales |
| Plan de 30 días | Define acciones, evidencia pendiente y seguimiento de contactos cualificados |

Se adapta a Software Engineers, Developers, Software/Systems Analysts, QA Analysts, QA Automation Engineers, SDET y profesionales de productos o calidad de IA. Selecciona un posicionamiento principal; no combina todos estos cargos en un titular.

## Enfoque técnico

Distingue **IA asistiendo el desarrollo**, **construcción de productos con IA** y **evaluación de sistemas de IA**. Explora análisis de requisitos, arquitectura, APIs, datos, pruebas, CI/CD, observabilidad, seguridad y colaboración distribuida según evidencia real.

TDD, BDD, DDD, CQRS o arquitectura hexagonal se presentan como decisiones que deben poder explicarse. La skill pregunta qué problema resolvieron y qué coste o alternativa se evaluó. El [mapa técnico](skills/linkedin-profile-optimizer/references/technical-evidence.md) contiene las referencias profesionales.

Para tecnologías “actuales”, investiga el mercado de cada persona en el momento de uso. No mantiene una lista universal de stacks de moda ni convierte anuncios en experiencia adquirida.

## Empezar

1. Preparar el [formulario](skills/linkedin-profile-optimizer/assets/intake.md): perfil/CV, rol, mercado, modalidad y contribuciones verificables. Las vacantes y artefactos técnicos ayudan, pero no son obligatorios para comenzar.
2. Instalar o proporcionar la carpeta completa de la skill en el entorno elegido.
3. Usar el prompt siguiente y adjuntar el material en un espacio privado.
4. Revisar hechos y las dos versiones antes de aplicar cambios en LinkedIn.

```text
Usa $linkedin-profile-optimizer para auditar mi LinkedIn.
Objetivo: [rol principal] en [mercados], modalidad [remota/híbrida].
Adjunto mi perfil/CV, contribuciones y vacantes de interés.
Entrega diagnóstico, mapa de términos, titular, About y experiencia ES/EN,
skills priorizadas, propuestas de Featured, solicitudes de recomendación
y un plan de 30 días. Distingue experiencia, proyectos y aprendizaje.
Si falta evidencia, indícalo. Conserva los mismos hechos en ambos idiomas.
```

Los corchetes del prompt son campos a completar, no contenido para publicar. En ChatGPT con Skills, seleccionar la skill con `@`; en Codex, usar `$linkedin-profile-optimizer` o el selector de skills. [Documentación oficial](https://learn.chatgpt.com/docs/build-skills).

## Instalación en Codex

La carpeta a copiar es **`skills/linkedin-profile-optimizer` completa**, incluidos `references`, `assets`, `agents` y `scripts`. Para uso personal, Codex descubre skills en `~/.agents/skills`; para un proyecto, en `.agents/skills`. [Referencia](https://learn.chatgpt.com/docs/build-skills).

### macOS / Linux

```bash
git clone --branch main --depth 1 https://github.com/eruizpy/it_skills_linkedin.git
mkdir -p "$HOME/.agents/skills"
cp -R it_skills_linkedin/skills/linkedin-profile-optimizer "$HOME/.agents/skills/"
```

Si ya existe una skill con ese nombre, revisar diferencias antes de reemplazarla. La instalación usa `main`, que puede contener actualizaciones posteriores. Para reproducir una edición, utilizar un tag publicado o un commit concreto.

### Windows PowerShell

```powershell
git clone --branch main --depth 1 https://github.com/eruizpy/it_skills_linkedin.git
$skillDestination = Join-Path $HOME '.agents/skills/linkedin-profile-optimizer'
if (Test-Path $skillDestination) { throw 'La skill ya existe; revisa las diferencias antes de reemplazarla.' }
New-Item -ItemType Directory -Path (Split-Path $skillDestination) -Force | Out-Null
Copy-Item -Recurse 'it_skills_linkedin/skills/linkedin-profile-optimizer' $skillDestination
```

## Uso en ChatGPT

Si el entorno permite instalar Skills, importar la carpeta completa mediante su flujo de instalación. En un chat sin instalación de Skills, adjuntar `SKILL.md`, los archivos de `references` y el formulario, y pedir que siga ese procedimiento. Esto permite uso manual y no constituye una instalación persistente.

La navegación habilita la revisión de fuentes y vacantes actuales. Sin ella, la skill trabaja con el material aportado y señala esa limitación. No necesita API keys ni acceso automático a LinkedIn. Python es opcional y solo se usa para el helper local.

## Sobre el algoritmo y la credibilidad

La ayuda de [LinkedIn Recruiter](https://www.linkedin.com/help/recruiter/answer/a414428) documenta filtros por cargos, aptitudes, ubicación e idiomas. La skill aprovecha esos campos para mejorar pertinencia y claridad. **No promete ranking, entrevistas ni una fórmula del algoritmo.**

Mantiene fechas, títulos, métricas y responsabilidades reales. Un curso no se convierte en experiencia; usar ChatGPT no convierte automáticamente a alguien en AI Engineer. “Remoto” se contrasta con las restricciones de cada oferta.

Las recomendaciones de texto son borradores. Publicar cambios, modificar preferencias o enviar mensajes requiere una instrucción explícita. Los datos de candidatos se trabajan en privado y no se agregan a este repositorio.

## Helper y verificaciones

El helper revisa únicamente los campos `headline` y `about` en los objetos `es` y `en` de un JSON UTF-8. Cuenta puntos de código Unicode y detecta algunos marcadores pendientes. No evalúa la verdad del perfil ni la calidad de la traducción.

```bash
python3 skills/linkedin-profile-optimizer/scripts/check_profile.py skills/linkedin-profile-optimizer/assets/profile.example.json
python3 -m unittest discover -s tests -v
```

Los objetivos por defecto son **editoriales**: 180 caracteres de titular y 2.000 de About. No se presentan como límites oficiales. Se pueden ajustar con `--headline-target` y `--about-target` después de verificar la interfaz.

El ejemplo JSON es completamente ficticio. Los [casos de comportamiento](tests/behavior-cases.md) permiten revisar calidad y veracidad al modificar la skill. Las pruebas locales no miden recomendaciones reales de LinkedIn.

En esta entrega se ejecutaron **17 tests del helper** y **un escenario compuesto en una conversación independiente** que revisó transición QA, paridad ES/EN, vacantes duplicadas, restricciones geográficas e instrucciones maliciosas dentro de una oferta. Los resultados y límites están descritos en los casos de comportamiento.

## Know-how: cómo realizar un buen análisis

La mejor entrada combina **lo que la persona hizo**, **las oportunidades que busca** y **evidencia que permita conectar ambos**. “Mejorá mi LinkedIn” permite comenzar, pero obliga a completar más vacíos. Un perfil atractivo debe poder sostenerse después en una entrevista técnica.

### 1. Definir una hipótesis profesional

Elegir un rol principal y un mercado concreto. Ejemplos: Backend Engineer para equipos que contratan en LATAM; QA Automation Engineer para un mercado específico; Software Analyst híbrido en una ciudad viable. Explicar qué especialidad se quiere destacar y por qué existe evidencia para hacerlo.

Si una persona considera dos carreras diferentes, pedir **dos variantes separadas**, compararlas y elegir. No usar un titular que intente ser simultáneamente Backend Engineer, QA Lead, AI Architect y Project Manager.

**Condición para avanzar:** tener un rol principal, una modalidad y restricciones geográficas conocidas o explícitamente pendientes.

### 2. Reunir una pequeña carpeta de evidencia

Preparar el perfil actual, CV y dos o tres contribuciones relevantes. Para cada una, explicar problema, participación individual, decisión, artefacto y resultado. Un repositorio público es útil cuando corresponde, pero puede reemplazarse por una explicación técnica anonimizada y autorizada.

Incluir pruebas, reportes, criterios de aceptación, diagramas existentes, decisiones de arquitectura o documentación cuando demuestren el trabajo. No compartir secretos ni información de clientes sin permiso. Separar empleo, proyecto personal, curso e interés de aprendizaje.

**Condición para avanzar:** poder distinguir lo demostrado, lo declarado y lo desconocido. Si falta una cifra, el análisis puede continuar con un resultado cualitativo confirmado.

### 3. Comparar vacantes compatibles

Proporcionar enlaces o texto de ofertas reales, o permitir que la skill investigue. El procedimiento intenta reunir 5–8 anuncios pertinentes y registra las limitaciones si obtiene menos. Conviene incluir más de una empresa y excluir republicaciones del mismo anuncio.

Revisar rol, nivel, país, modalidad, idioma y condiciones de contratación antes de contar tecnologías. Un anuncio remoto limitado a residentes de otro país no pertenece a la misma comparación que uno compatible con la persona.

**Condición para avanzar:** conocer qué anuncios entran en la muestra y cuáles se excluyen. Sin navegación o fechas verificables, el resultado debe declarar su actualidad no verificada.

### 4. Transformar experiencia en posicionamiento

Cruzar cada término relevante con evidencia. Si una vacante pide automatización en producción y la persona tiene un proyecto personal, mostrar ese proyecto en su contexto y proponer la brecha siguiente. No convertir el requisito del anuncio en una experiencia del candidato.

Para IA, responder tres preguntas independientes: ¿usa asistentes en su trabajo?, ¿construye productos con modelos?, ¿prueba sistemas cuyo comportamiento incorpora IA? En arquitectura y QA, explicar decisiones y tradeoffs, no solo mencionar nombres de patrones.

**Condición para avanzar:** cada afirmación importante del borrador debe tener una fuente, una declaración identificada o una aspiración claramente expresada.

### 5. Revisar la versión bilingüe como si fuera una entrevista

Leer ambas versiones y comprobar: ¿son iguales las fechas, cargos, métricas y responsabilidades?, ¿se podría explicar cada herramienta mencionada?, ¿la versión inglesa aumenta el seniority?, ¿se presenta una aspiración como empleo actual?

Revisar también el tono. Preferir verbos específicos, contribuciones y contexto. El registro de evidencia acompaña el análisis, pero no se pega dentro de About ni de los bullets finales.

**Condición para avanzar:** disponer de texto sin marcadores pendientes, factual y coherente ES/EN. El helper verifica estructura y extensión; la revisión humana valida significado y veracidad.

### 6. Aplicar cambios y observar resultados

Revisar primero la propuesta y después aplicar las secciones y preferencias elegidas. Las solicitudes de recomendación se personalizan para personas que conocen el trabajo. La auditoría no envía mensajes ni modifica LinkedIn automáticamente.

Anotar una línea base y revisar a los 14 y 30 días. Priorizar contactos compatibles con el objetivo y entrevistas pertinentes. Las apariciones o visitas, cuando estén disponibles, son señales complementarias. Registrar postulaciones, networking y otros cambios para evitar atribuir todo al perfil.

**Condición para iterar:** contar con observaciones concretas. Ajustar una hipótesis —por ejemplo, especialidad o claridad del titular— y conservar un registro de qué se cambió.

### Ejemplo de una solicitud bien preparada

El siguiente caso es ficticio y solo demuestra cómo aportar contexto:

```text
Usa $linkedin-profile-optimizer.
Soy QA Analyst y busco QA Automation en equipos que contraten desde LATAM.
Trabajo con pruebas exploratorias, SQL y Postman. Tengo un proyecto personal
con Playwright, todavía sin uso en producción. Uso IA para proponer casos
que reviso manualmente; no he desarrollado productos con IA.
Adjunto mi perfil, dos contribuciones y cinco ofertas.
Primero define qué posicionamiento puedo sostener hoy y qué requiere
evidencia adicional. Después entrega el perfil ES/EN y el siguiente paso
práctico para fortalecer mi candidatura sin aumentar mi experiencia real.
```

Para una segunda iteración, compartir el borrador anterior y observaciones concretas: “estas frases no representan mi aporte”, “esta oferta restringe el país”, “ya documenté este proyecto” o “recibí contactos para un rol distinto al buscado”. Pedir que actualice la propuesta y explique qué cambió.

## Skills y capacidades incluidas

La variante ChatGPT/Codex contiene **una skill instalable**, `linkedin-profile-optimizer`, organizada en capacidades complementarias. El catálogo incluye además la variante existente para Claude. Los módulos siguientes pertenecen a ChatGPT/Codex y no son instalaciones independientes:

| Capacidad | Saber práctico que aporta | Resultado revisable |
| --- | --- | --- |
| Diagnóstico profesional | Elegir foco y reconocer brechas | Propuesta de valor y prioridades |
| Investigación del mercado | Comparar oportunidades compatibles y fechar evidencia | Muestra y matriz de requisitos |
| Ingeniería de software | Relacionar requisitos, diseño, implementación y operación | Contribuciones técnicas explicables |
| QA y testing | Diferenciar análisis, exploración, automatización y calidad | Evidencia de estrategia y pruebas |
| Ingeniería y calidad de IA | Separar asistencia, construcción y evaluación | Posicionamiento de IA proporcional a la experiencia |
| Redacción y localización | Comunicar sin aumentar alcance al traducir | Texto ES/EN coherente |
| Visibilidad y credibilidad | Revisar campos pertinentes y referencias de colaboradores | Ajustes y borradores de recomendaciones |
| Mejora continua | Evaluar señales observables y revisar hipótesis | Plan de 30 días y siguiente iteración |

## Cómo colaborar y construir mejores versiones

### Aportes que resultan útiles

- **Reclutamiento:** casos de perfiles difíciles de interpretar, vocabulario de roles y restricciones habituales, acompañados de fuentes o ejemplos anonimizados.
- **Ingeniería y arquitectura:** preguntas que distingan experiencia aplicada de una lista de patrones, y ejemplos de decisiones con tradeoffs.
- **QA:** escenarios que detecten exageraciones de experiencia, fallos de localización, resultados sin evidencia o comportamiento incorrecto del helper.
- **IA:** criterios para evaluar contribuciones, seguridad, evaluación y operación de sistemas, manteniendo separadas las tres dimensiones de IA.
- **ES/EN:** mejoras de naturalidad y terminología que conserven hechos y seniority.
- **Documentación:** fuentes oficiales actualizadas, instrucciones más claras y casos de uso reproducibles.

### Abrir una propuesta o reportar un problema

Usar [Issues](https://github.com/eruizpy/it_skills_linkedin/issues) con esta estructura:

```text
Problema u oportunidad:
Versión/tag/commit utilizado:
Entorno: ChatGPT / Codex; con o sin navegación; Python si corresponde:
Caso mínimo ficticio o anonimizado:
Resultado observado:
Resultado esperado y por qué:
Fuente primaria, si se cambia una afirmación de plataforma o tecnología:
Impacto para quien usa la skill:
```

No pegar CVs ni mensajes privados. Si el fallo depende de una historia real, crear un caso sintético que conserve el problema. Una captura puede ayudar, pero debe estar libre de datos personales o secretos.

### Proponer un cambio mediante pull request

1. Crear un fork o una rama de trabajo, según los permisos disponibles.
2. Describir un problema concreto y proponer el cambio más pequeño que lo resuelva.
3. Modificar la fuente correspondiente: procedimiento en `SKILL.md`, conocimiento en `references`, plantillas en `assets` o helper en `scripts`.
4. Ejecutar los tests si se modifica código. Si cambia el comportamiento, ejecutar un caso pertinente en una conversación nueva y registrar el resultado con datos sintéticos.
5. Comprobar enlaces relativos, lenguaje ES/EN, ausencia de datos privados y vigencia de fuentes.
6. Abrir la PR explicando problema, solución, cambio de comportamiento, validación y limitaciones.

No hace falta ampliar todos los archivos para una corrección pequeña. Si una contribución agrega capacidades distintas —por ejemplo, preparación de entrevistas—, justificar primero si pertenece aquí o a otra skill.

### Criterios para aceptar una mejor versión

| Criterio | Evidencia de que mejora |
| --- | --- |
| Utilidad | Resuelve un problema reproducible de análisis o uso |
| Veracidad | Conserva trazabilidad y no agrega experiencia ficticia |
| Actualidad | Las afirmaciones temporales tienen fuentes consultadas |
| Coherencia | ES/EN conserva alcance y seniority |
| Generalización | Funciona con distintos perfiles y no sobreajusta un único ejemplo |
| Mantenimiento | Reglas claras, referencias localizables y cambios acotados |
| Privacidad | No depende de publicar información personal |

Las pruebas automáticas comprueban el helper. Los casos de comportamiento comprueban el flujo del LLM. La efectividad de contratación exige observación posterior; ninguno de los dos tipos de prueba garantiza entrevistas.

### Versionado

Usar versiones semánticas para futuras publicaciones: `PATCH` para correcciones compatibles, `MINOR` para capacidades compatibles y `MAJOR` para cambios que requieran adaptar el uso. Registrar qué cambió y qué se probó en la descripción de la publicación.

La edición se identifica con `ChatGPT` para ChatGPT/Codex. Los comandos de instalación usan `main`. Para compartir versiones reproducibles, utilizar un tag publicado o el SHA de un commit. Preservar los tags ya publicados y crear nuevos tags de versión para las siguientes entregas.


## Estructura y mantenimiento

| Ruta | Contenido |
| --- | --- |
| `skills/linkedin-profile-optimizer/SKILL.md` | Procedimiento y criterios de entrega |
| `linkedin-perfil-tech/SKILL.md` | Variante existente para Claude |
| `docs/claude-guide.md` | Documentación de Claude conservada |
| `agents/openai.yaml` dentro de la skill | Nombre, descripción e invocación para OpenAI |
| `references/` dentro de la skill | LinkedIn, evidencia técnica y fuentes |
| `assets/` dentro de la skill | Entrada, contrato de reporte y ejemplo ficticio |
| `scripts/` dentro de la skill | Helper sin dependencias externas |
| `tests/` | Pruebas del helper y escenarios de comportamiento |

Fuentes revisadas el **7 de noviembre de 2026**. Verificar nuevamente funcionalidades, herramientas y vacantes en cada análisis. Para contribuir, conservar ejemplos sintéticos, actualizar fuentes y ejecutar las verificaciones pertinentes. La etiqueta **ChatGPT** identifica ChatGPT/Codex como entornos objetivo; no implica respaldo oficial de OpenAI o LinkedIn.

## English guide

**LinkedIn Profile Optimizer** is a reusable ChatGPT/Codex skill for evidence-based professional profiles in Spanish and English. It supports software engineering, software analysis, QA, test automation and AI-related roles, with attention to remote and hybrid hiring constraints.

The repository also preserves the separate **linkedin-perfil-tech** Claude variant. See its [existing guide](docs/claude-guide.md). The workflow, helper and validation results below describe the ChatGPT/Codex variant.

It delivers a prioritized review, an evidence ledger, a relevant job-posting comparison, a bilingual keyword map, profile copy, skills/Featured recommendations and a 30-day measurement plan. It separates professional experience, personal projects and learning, and preserves the same facts in both languages.

Use the installation commands above to copy the whole skill folder. For ChatGPT environments without skill installation, attach the instructions, references and intake form for manual use. Live market research requires browsing; without it, the output explicitly limits claims to supplied material.

```text
Use $linkedin-profile-optimizer to review my LinkedIn profile.
Target role: [role]. Markets: [locations]. Work mode: [remote/hybrid].
I have attached my profile, supported contributions and target job postings.
Create an evidence-based review and Spanish/English profile copy,
prioritized skills, Featured suggestions, recommendation request drafts,
and a 30-day improvement plan. Separate experience from projects and learning.
```

AI-assisted coding, building AI products and testing AI systems are treated as different capabilities. Architecture patterns and testing practices require concrete examples and tradeoffs. The skill does not invent achievements, language proficiency, credentials or metrics; it does not guarantee search ranking or job offers.

Keep candidate files private. The repository contains reusable instructions and synthetic examples only. The optional Python helper checks field structure, character counts and unresolved markers—not truth, translation quality or employability.

### Practical know-how

Start with one target role and realistic locations. Supply the current profile, two or three supported contributions and relevant job postings. Keep professional work, personal projects and learning separate. Compare only compatible jobs and remove duplicates. Map each proposed claim to evidence, then check factual parity between the Spanish and English copy before applying it.

Review observable results after 14 and 30 days. Track qualified opportunities, not just activity counts. Record other job-search actions and avoid treating correlation as proof that a profile edit caused a hiring outcome.

### Contributing

Open an issue with the version, environment, minimal synthetic input, observed behavior and expected outcome. Include primary sources when changing platform or technology claims. For a pull request, make a focused change, run applicable tests, exercise changed behavior in a fresh conversation, and describe limitations. Contributions from recruiters, engineers, QA specialists and bilingual reviewers are welcome.

Do not include private candidate data. Preserve published tags and use new version tags for subsequent releases. See the detailed contribution criteria above and [AGENTS.md](AGENTS.md).

## Licencia / License

Se conserva la licencia **GNU GPL v3** existente en [LICENSE](LICENSE). La carpeta distribuible incluye una copia. Consultar el archivo para sus términos. Las fuentes enlazadas conservan sus propios términos y no se redistribuyen íntegramente.
