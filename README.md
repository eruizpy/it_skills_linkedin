# it_skills_linkedin — Skill para Claude: `linkedin-perfil-tech`

> **Skill para Claude (Anthropic).** Este repositorio contiene una *Agent Skill* diseñada para ser ejecutada por los modelos **Claude** (claude.ai, Claude Code y la Claude API). No es una app ni un script independiente: es un conjunto de instrucciones que Claude carga cuando detecta que la tarea encaja con su descripción.

`linkedin-perfil-tech` audita y reescribe perfiles de LinkedIn de profesionales tech (desarrollo, ingeniería de software, QA/testing, DevOps/cloud, IA) para que:

1. aparezcan en las búsquedas de **LinkedIn Recruiter** (titular, título actual, Skills y Acerca de alineados con las keywords reales de las vacantes);
2. convenzan a un **reclutador humano** en los primeros segundos (hook con números, logros con fórmula XYZ, prueba social);
3. queden listos para procesos **remotos/híbridos** en **español e inglés** (perfil secundario en otro idioma, Open to Work bien configurado, zona horaria, nivel de idioma);
4. muestren un posicionamiento **creíble en IA** y en **buenas prácticas de ingeniería y QA** (evidencia y métricas, nunca autodeclaraciones).

La skill entrega un documento con scorecard de 12 dimensiones (0–100), mapa de keywords EN/ES, secciones reescritas antes → después con conteo de caracteres, plan de actividad 30/60/90 y checklist de implementación. Está basada en fuentes verificadas (LinkedIn Help, LinkedIn Skills/Jobs on the Rise 2026, Stack Overflow Developer Survey 2026, análisis de vacantes de QA 2026); la lista completa está al final de `linkedin-perfil-tech/SKILL.md`.

## Estructura

```
it_skills_linkedin/
├── linkedin-perfil-tech/
│   └── SKILL.md        # la skill (frontmatter name/description + instrucciones)
├── README.md
└── LICENSE             # GPL-3.0
```

## Instalación

### claude.ai (web / desktop / móvil)

1. Descarga o clona este repo y comprime **la carpeta** de la skill (el `.zip` debe contener `linkedin-perfil-tech/SKILL.md`):
   ```bash
   zip -r linkedin-perfil-tech.zip linkedin-perfil-tech
   ```
2. En Claude: **Personalizar → Habilidades → + → Crear habilidad → Subir una habilidad** y selecciona el `.zip`.
3. Actívala en la lista. Requiere tener habilitada la **ejecución de código y creación de archivos** (planes Pro, Max, Team y Enterprise; en Enterprise el propietario debe habilitar *Skills* en la configuración de la organización).

**Compartir con colegas (planes Team/Enterprise):** en *Personalizar → Habilidades*, menú `…` de la skill → **Compartir** (personas o grupos) o **Publicar en la organización** para que cualquiera la instale desde el directorio. En planes individuales cada colega sube el `.zip` a su propia cuenta.

### Claude Code

Copia la carpeta en el proyecto (compartida con el equipo vía git) o en tu usuario:

```bash
# por proyecto
mkdir -p .claude/skills && cp -r linkedin-perfil-tech .claude/skills/
# o personal
mkdir -p ~/.claude/skills && cp -r linkedin-perfil-tech ~/.claude/skills/
```

Claude Code la detecta automáticamente; también puedes invocarla con `/linkedin-perfil-tech`.

### Claude API

Sube el `.zip` con la Skills API (`/v1/skills`) y referéncialo en el `container.skills` de tus mensajes. Documentación: https://docs.claude.com/en/api/skills-guide

## Cómo usarla

Pega tu perfil (o el PDF que LinkedIn genera con *Más → Guardar como PDF*) y pide, por ejemplo:

- «Audita mi perfil de LinkedIn para roles remotos de Backend Node.js/AWS en EE. UU. y LatAm, en inglés y español.»
- «Reescribe mi titular y mi Acerca de como QA Automation Engineer; aquí van 4 vacantes que me interesan.»
- «Quiero posicionarme en IA sin inflar: esto es lo que realmente he construido.»

Cuanto más aportes (2–3 roles objetivo, 3–5 vacantes reales, logros con números, certificaciones, modalidad y zona horaria), mejor será el resultado. La skill nunca inventa métricas ni credenciales: lo que falte queda marcado como `[DATO]` para que lo completes.

## Versionado

- **1.0.0** (2026-11-07) — primera versión. Límites de LinkedIn y tendencias de mercado verificados a esa fecha; revísalos si LinkedIn cambia sus reglas.

## Atribución y licencia

Skill redactada con **Claude** (Anthropic) para ser aplicada por modelos Claude. Código y texto bajo licencia **GPL-3.0** (ver `LICENSE`). Las marcas LinkedIn, GitHub y otras citadas pertenecen a sus respectivos dueños; este proyecto no está afiliado a ellas.
