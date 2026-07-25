# KnowledgeHub AI

> Asistente RAG para consultar documentos PDF privados mediante lenguaje natural, con respuestas fundamentadas en fragmentos recuperados de la base documental.

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](#tecnologías)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white)](#arquitectura)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit&logoColor=white)](#arquitectura)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C)](#tecnologías)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-6B4EFF)](#tecnologías)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](#docker)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green)](#licencia)

## Descripción

KnowledgeHub AI transforma una colección de documentos PDF en una base de conocimiento consultable. El usuario formula una pregunta desde una interfaz web y el sistema recupera fragmentos semánticamente relevantes antes de solicitar una respuesta al modelo de lenguaje.

La aplicación separa la experiencia de usuario, la API y el núcleo de negocio. En esta versión, los embeddings se generan con Cohere y la generación se realiza con Google Gemini. El diseño encapsula ambos proveedores para facilitar una evolución futura hacia modelos y embeddings autoalojados, con el objetivo de reducir la exposición de documentos empresariales a servicios externos. **La versión actual no funciona completamente offline**: Gemini y Cohere se consumen mediante API.

## ¿Qué problema resuelve?

El conocimiento operativo suele quedar repartido entre manuales, procedimientos, políticas, guías y documentación técnica. Localizar una respuesta puntual exige revisar archivos extensos, usar búsquedas por palabras poco precisas o depender de personas que ya conocen el contenido.

KnowledgeHub AI ofrece una capa conversacional sobre esos documentos: indexa su texto, recupera el contexto más pertinente para cada pregunta y devuelve una respuesta acompañada por sus fuentes y páginas. Así, el contenido documental sigue siendo el punto de referencia para validar la respuesta.

## Características

- Carga, listado, descarga y eliminación de documentos PDF desde la interfaz.
- Reconstrucción automática del índice al cargar o eliminar un PDF, y reconstrucción manual bajo demanda.
- Extracción de páginas con `PyPDFLoader` y fragmentación con `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=200`).
- Embeddings multilingües con `CohereEmbeddings` (`embed-multilingual-v3.0`).
- Índice vectorial FAISS persistido en `data/vectorstore`.
- Recuperación semántica mediante Max Marginal Relevance (hasta 12 fragmentos; 20 candidatos).
- Respuestas RAG generadas con `gemini-flash-latest` a temperatura 0.
- Fuentes por documento y página, con el fragmento recuperado y acceso al PDF desde la interfaz.
- API REST con FastAPI, interfaz desacoplada en Streamlit y ejecución definida con Docker Compose.

# 🎥 Demo

## 📹 Video demostrativo

> Pendiente de publicación

**YouTube**

https://youtube.com/...

---

## 🌐 Aplicación desplegada

> https://knowledgehub.world/

---
## Ejemplos de preguntas y respuestas

Con los documentos de ejemplo incluidos:

| Pregunta                                        | Respuesta |
|-------------------------------------------------|-----------|
| ¿Cuál es el stack tecnológico estándar?         | .         |
| ¿Qué tecnologías utiliza el proyecto Frontend?  | .         |
| ¿Qué frameworks se mencionan?                   | .         |
| ¿Cuál es la arquitectura del proyecto? | .         |
| ¿Qué responsabilidades tiene el Backend?            | .         |
| ¿Cómo está organizado el Frontend?            | .         |
| ¿Qué herramientas recomienda la guía?           | .         |


## Arquitectura

La aplicación se organiza en tres capas. Streamlit consume la API REST; FastAPI delega las consultas al `KnowledgeHubService`; y `src/core` contiene los servicios de indexación, recuperación y generación.

```text
Usuario
  |
  v
Streamlit (src/frontend)
  |
  | HTTP
  v
FastAPI (src/backend)
  |
  v
KnowledgeHubService
  |
  +--> RAGService --> RetrieverService --> FAISS
  |                                      ^
  |                                      |
  |                         CohereEmbeddings
  |
  +--> LLMService --> Google Gemini

Indexación de documentos
  Documentos PDF --> PDFLoaderService --> DocumentProcessor
                                             |
                                             v
                                      CohereEmbeddings --> FAISS
```

`KnowledgeHubService` actúa como fachada del flujo de consulta. Al iniciar, reutiliza el índice FAISS si existen `index.faiss` e `index.pkl`; de lo contrario, carga los PDF disponibles, los procesa y persiste un índice nuevo.

### Flujo de indexación

```text
PDF en data/documents
          |
          v
PyPDFLoader (una página por documento LangChain)
          |
          v
DocumentProcessor
  - fragmentos de 1000 caracteres
  - solapamiento de 200 caracteres
  - metadatos: archivo, página, id y fragmento
          |
          v
CohereEmbeddings (embed-multilingual-v3.0)
          |
          v
FAISS persistido en data/vectorstore
```

### Flujo de consulta

```text
Usuario
  |
  v
Streamlit --> POST /api/chat
  |
  v
KnowledgeHubService --> RAGService
  |
  v
RetrieverService --> búsqueda MMR en FAISS
  |
  v
Fragmentos relevantes + pregunta --> prompt con contexto
  |
  v
Google Gemini --> respuesta + fuentes (archivo, página y fragmento)
```

El prompt instruye al modelo a responder únicamente con el contexto recuperado y a indicar que no encontró información suficiente cuando el contenido no está disponible.

## Tecnologías

| Tecnología | Uso en el proyecto |
| --- | --- |
| Python 3.13 | Lenguaje y runtime de la aplicación |
| Streamlit | Interfaz web conversacional y administración documental |
| FastAPI | API REST para salud, chat y documentos |
| LangChain | Carga, fragmentación, embeddings, vector store y LLM |
| PyPDF / PyPDFLoader | Lectura de documentos PDF |
| Cohere | Embeddings multilingües |
| FAISS | Almacenamiento y búsqueda vectorial local en disco |
| Google Gemini | Generación de respuestas en el flujo RAG |
| Docker / Docker Compose | Contenerización de API e interfaz |

## Estructura del proyecto

```text
knowledgehub-ai/
├── config/
│   └── settings.py                 # Variables de configuración
├── data/
│   ├── documents/                  # PDFs de la base de conocimiento
│   └── vectorstore/                # Índice FAISS persistido
├── src/
│   ├── backend/
│   │   ├── api.py                  # Aplicación FastAPI
│   │   ├── routes/                 # Chat, documentos y health check
│   │   └── schemas/                # Contratos de la API
│   ├── core/
│   │   ├── embeddings/             # CohereEmbeddings
│   │   ├── llm/                    # Adaptador de Gemini
│   │   ├── loaders/                # Carga de PDF
│   │   ├── models/                 # Metadatos y fuentes
│   │   ├── processing/             # Fragmentación y enriquecimiento
│   │   ├── rag/                    # Recuperación y generación RAG
│   │   ├── services/               # Fachada y servicios de índice/documentos
│   │   ├── utils/                  # Rutas del proyecto
│   │   └── vectorstore/            # Persistencia FAISS
│   └── frontend/
│       ├── api/                    # Clientes HTTP de la API
│       ├── ui/                     # Vistas y componentes Streamlit
│       └── app.py                  # Punto de entrada de la interfaz
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/adan92/knowledgehub-ai.git
cd knowledgehub-ai
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Cree un archivo `.env` en la raíz del proyecto:

```dotenv
GOOGLE_API_KEY=tu_clave_de_google
COHERE_API_KEY=tu_clave_de_cohere
API_BASE_URL=http://localhost:8000/api
```

> `API_BASE_URL` debe incluir el prefijo `/api`, ya que las rutas expuestas por FastAPI se registran bajo ese prefijo.

### 5. Ejecutar el backend

**Windows (PowerShell)**

```powershell
$env:PYTHONPATH = "src"
uvicorn backend.api:app --host 0.0.0.0 --port 8000 --app-dir src
```

La API queda disponible en `http://localhost:8000`; el endpoint de estado es `GET /api/health`.

### 6. Ejecutar el frontend

En otra terminal, con el entorno virtual activo:

```powershell
$env:PYTHONPATH = "src"
streamlit run src/frontend/app.py
```

Streamlit mostrará la URL local de la interfaz, normalmente `http://localhost:8501`.

## Docker

El repositorio incluye un `Dockerfile` común y un `docker-compose.yml` con dos servicios: `knowledgehub-api` y `knowledgehub-ui`. Ambos montan `./data` para conservar los PDF y el índice vectorial entre reinicios.

La intención de ejecución es:

```bash
docker compose up --build
```

### Estado de la configuración incluida

Antes de usar Docker Compose, hay tres valores que deben alinearse en la versión actual del repositorio:

- El comando del servicio `knowledgehub-ui` apunta a `src/app.py`, mientras que el punto de entrada existente es `src/frontend/app.py`.
- El frontend necesita `API_BASE_URL=http://knowledgehub-api:8000/api` dentro de Docker para alcanzar la API por su nombre de servicio y por el prefijo correcto.
- El servicio de API declara `"8000"`, que lo expone sólo para la red de Compose. Para acceder desde el host debe publicarse como `"8000:8000"`.

Con esos ajustes, ejecute el comando anterior y abra la interfaz en `http://localhost:8501`.

## Variables de entorno

| Variable | Requerida | Descripción |
| --- | --- | --- |
| `GOOGLE_API_KEY` | Sí | Clave utilizada por `ChatGoogleGenerativeAI` para invocar `models/gemini-flash-latest`. |
| `COHERE_API_KEY` | Sí | Clave utilizada por `CohereEmbeddings` con el modelo `embed-multilingual-v3.0`. |
| `API_BASE_URL` | Recomendada | URL base del cliente Streamlit. El valor por defecto en código es `http://localhost:8000`; para las rutas actuales debe configurarse con el sufijo `/api`. |

## Casos de uso

- Consulta de manuales internos y guías operativas.
- Búsqueda asistida sobre procedimientos y políticas organizacionales.
- Acceso conversacional a documentación técnica de proyectos.
- Centralización consultable de una base de conocimiento en PDF.
- Soporte a equipos que necesitan localizar el origen de una respuesta y revisar su página dentro del documento.

## Principios de diseño

- **Frontend y backend separados.** Streamlit no conoce la implementación RAG: utiliza clientes HTTP para consumir la API.
- **Núcleo modular.** Carga, procesamiento, índice vectorial, recuperación, LLM y administración documental viven en módulos independientes de `src/core`.
- **Bajo acoplamiento con proveedores.** `EmbeddingService`, `LLMService` y `FAISSStoreService` concentran la dependencia de Cohere, Gemini y FAISS.
- **Persistencia local del índice.** FAISS se guarda en `data/vectorstore` y se reutiliza al iniciar cuando sus archivos existen.
- **Trazabilidad de respuestas.** Cada fragmento conserva archivo, página e identificadores; la interfaz los presenta como fuentes seleccionables.
- **Evolución prevista.** La separación de adaptadores facilita sustituir el LLM o los embeddings y ampliar los cargadores documentales. Estas extensiones no están implementadas todavía.

## Limitaciones actuales

- Sólo se aceptan y procesan documentos PDF; no hay cargadores para otros formatos ni OCR.
- Se usa un único directorio documental y un único índice FAISS compartido; no existen colecciones, espacios de trabajo ni aislamiento por usuario.
- No hay autenticación ni autorización en la API; además, CORS permite cualquier origen en esta versión.
- La conversación se conserva únicamente en el estado de la sesión de Streamlit; no existe persistencia de historial.
- La generación y los embeddings dependen de las APIs de Google y Cohere, por lo que se requieren credenciales y conectividad.
- No hay pruebas automatizadas incluidas en la estructura del proyecto.
- La configuración de Docker Compose requiere los ajustes señalados en la sección anterior para iniciar la interfaz y exponer la API desde el host.

## Roadmap

### Versión actual

- [x] API REST para salud, chat y gestión de PDF.
- [x] Interfaz Streamlit para consultar y administrar documentos.
- [x] Pipeline RAG con fragmentación, Cohere, FAISS y Gemini.
- [x] Fuentes con documento, página y fragmento recuperado.
- [x] Definiciones de Docker y Docker Compose.

### Próximas versiones

- [ ] Modelos LLM y embeddings autoalojados (por ejemplo, Ollama o vLLM) para escenarios con mayores requisitos de privacidad.
- [ ] Nuevas fuentes documentales además de PDF.
- [ ] Autenticación, autorización y aislamiento de colecciones.
- [ ] OCR para documentos escaneados.
- [ ] Persistencia de conversaciones y observabilidad del flujo RAG.
- [ ] Pruebas automatizadas y validación de la configuración de despliegue.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

## Agradecimientos

KnowledgeHub AI inició como parte de **Oracle Next Education AI Tech Builder** y ha evolucionado como un proyecto independiente.
