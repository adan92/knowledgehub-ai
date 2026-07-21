# 🧠 KnowledgeHub AI

> Motor de conocimiento impulsado por Inteligencia Artificial que permite consultar documentos privados mediante lenguaje natural utilizando Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.13-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Gemini](https://img.shields.io/badge/Gemini-LLM-orange)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-blueviolet)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED)
![OCI](https://img.shields.io/badge/Oracle%20Cloud-Deploy-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Descripción

KnowledgeHub AI es un asistente inteligente capaz de responder preguntas sobre documentos privados utilizando Inteligencia Artificial.

En lugar de buscar manualmente entre múltiples archivos PDF, el usuario simplemente realiza una pregunta en lenguaje natural y el sistema recupera la información más relevante mediante una arquitectura **Retrieval-Augmented Generation (RAG)**.

Aunque actualmente trabaja con documentos PDF, el proyecto fue diseñado desde su inicio para evolucionar hacia múltiples fuentes de información como hojas de cálculo, imágenes, bases de datos y APIs.

---

# 🎥 Demo

## 📹 Video demostrativo

> Pendiente de publicación

**YouTube**

https://youtube.com/...

---

## 🌐 Aplicación desplegada

> Pendiente de publicación

https://...

---

# ❓ ¿Por qué KnowledgeHub AI?

Las organizaciones almacenan gran parte de su conocimiento en documentos como:

- Manuales
- Políticas
- Documentación técnica
- Contratos
- Reportes
- Guías

Encontrar una respuesta específica suele requerir revisar cientos de páginas.
Además que garantiza una mayor privacidad de los documentos que son compartidos.

KnowledgeHub AI transforma esos documentos en una base de conocimiento inteligente capaz de responder preguntas mediante lenguaje natural.

---

# 💡 Solución

KnowledgeHub AI combina:

- Procesamiento de documentos
- Chunking
- Embeddings
- Búsqueda semántica
- Modelos de Lenguaje (LLM)

para responder preguntas utilizando únicamente la información contenida en los documentos del usuario.

Actualmente soporta:

- ✅ PDF

Arquitectura preparada para incorporar:

- Excel
- CSV
- Word
- OCR
- Bases de datos
- APIs
- WhatsApp

---

# 🚀 Características

## MVP

- Lectura automática de documentos PDF
- Extracción de texto
- Chunking
- Embeddings con Cohere
- Base vectorial FAISS
- Recuperación semántica
- Generación de respuestas mediante Gemini
- Interfaz web con Streamlit
- Despliegue en Oracle Cloud Infrastructure
- Arquitectura modular

---

# 🏗 Arquitectura

## Arquitectura general

```text
                     Usuario
                         │
                  Streamlit UI
                         │
                         ▼
              KnowledgeHubService
                         │
                         ▼
                   RAGService
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
      RetrieverService      Gemini LLM
              │
              ▼
            FAISS
              │
              ▼
      Cohere Embeddings
              │
              ▼
      DocumentProcessor
              │
              ▼
       PDFLoaderService
              │
              ▼
          PDF Documents
```

---

## Flujo de indexación

```text
PDF Documents
      │
      ▼
PDFLoaderService
      │
      ▼
DocumentProcessor
(Chunking)
      │
      ▼
Cohere Embeddings
      │
      ▼
FAISS
```

---

## Flujo de consulta

```text
Usuario
    │
Pregunta
    │
    ▼
Retriever (FAISS)
    │
Chunks relevantes
    │
    ▼
Prompt RAG
    │
    ▼
Gemini
    │
    ▼
Respuesta
```

---

# 🛠 Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python | Backend |
| LangChain | Orquestación del flujo RAG |
| Gemini | Modelo de lenguaje |
| Cohere | Embeddings |
| FAISS | Base de datos vectorial |
| PyPDF | Procesamiento de documentos |
| Streamlit | Interfaz web |
| Docker | Contenerización |
| Oracle Cloud Infrastructure | Despliegue |
| Git / GitHub | Control de versiones |

---

# 📂 Estructura

```text
knowledgehub-ai/

│
├── app.py
│
├── src/
│   ├── loaders/
│   ├── processing/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── rag/
│   ├── llm/
│   ├── services/
│   └── utils/
│
├── data/
├── docs/
├── tests/
├── requirements.txt
└── README.md
```

---

# ⚙ Instalación

## Clonar repositorio

```bash
git clone https://github.com/adan92/knowledgehub-ai.git
```

```bash
cd knowledgehub-ai
```

## Crear entorno virtual

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Variables de entorno

Crear un archivo `.env`

```text
GOOGLE_API_KEY=...
COHERE_API_KEY=...
```

## Ejecutar

```bash
streamlit run src/app.py
```

---

# 💬 Casos de prueba

## Preguntas generales

Estas preguntas validan el flujo completo del sistema.

- ¿Cuál es el stack tecnológico estándar?
- ¿Qué tecnologías utiliza el proyecto Frontend?
- ¿Qué frameworks se mencionan?
- ¿Cuál es la arquitectura del proyecto?
- ¿Qué responsabilidades tiene el Backend?
- ¿Cómo está organizado el Frontend?
- ¿Qué herramientas recomienda la guía?

---

## Preguntas específicas

Estas preguntas permiten validar que FAISS recupera correctamente el contexto adecuado.

- ¿Qué es React?
- ¿Qué es Angular?
- ¿Qué es Spring Boot?
- ¿Qué es Docker?
- ¿Qué es JWT?
- ¿Qué es TypeScript?
- ¿Qué es REST?

---

## Preguntas fuera del contexto

El asistente responde únicamente utilizando la información contenida en los documentos.

Ejemplos:

- ¿Quién ganó el Mundial 2022?
- ¿Cuál es la capital de Francia?
- ¿Qué es ChatGPT?

En estos casos el sistema indicará que no encontró información suficiente en los documentos disponibles.

---

# 📈 Resultados

KnowledgeHub AI permite:

- Consultar documentos mediante lenguaje natural.
- Recuperar información utilizando búsqueda semántica.
- Reducir significativamente el tiempo necesario para localizar información.
- Mantener las respuestas restringidas al conocimiento disponible en la base documental.

---

# 📸 Capturas

## Pantalla principal

> Imagen pendiente

---

## Respuesta del asistente

> Imagen pendiente

---


# ☁ Despliegue

El proyecto se encuentra preparado para desplegarse utilizando Docker sobre Oracle Cloud Infrastructure (OCI).

---

# 🧭 Principios de diseño

Durante el desarrollo del proyecto se siguieron los siguientes principios:

- Arquitectura modular
- Separación de responsabilidades
- Código mantenible
- Escalabilidad
- Bajo acoplamiento
- Preparado para incorporar nuevas fuentes de información

---

# ⚠ Limitaciones actuales

La versión MVP presenta las siguientes limitaciones:

- Solo soporta documentos PDF.
- No cuenta con autenticación.
- No soporta OCR.
- Trabaja con una única colección de documentos.
- No almacena historial de conversaciones.
- La recuperación de contexto utiliza búsqueda semántica simple.

---

# 🗺 Roadmap

## MVP

- [x] PDF Loader
- [x] Chunking
- [x] Embeddings
- [x] FAISS
- [x] Gemini
- [x] Streamlit
- [x] Docker
- [x] Oracle Cloud Infrastructure



---

# 🙌 Agradecimientos

Este proyecto fue iniciado como parte del programa **Oracle Next Education – AI Tech Builder**, pero está diseñado para evolucionar como un proyecto independiente y de código abierto.

---

# 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.