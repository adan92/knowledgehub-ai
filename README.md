# 🧠 KnowledgeHub AI

> Un motor de conocimiento impulsado por Inteligencia Artificial que permite consultar información privada mediante lenguaje natural utilizando Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![OCI](https://img.shields.io/badge/Oracle%20Cloud-Deploy-orange)

---

# 📖 Descripción

KnowledgeHub AI es un asistente inteligente capaz de responder preguntas sobre documentos privados utilizando Inteligencia Artificial.

En lugar de abrir manualmente múltiples archivos PDF para buscar información, el usuario simplemente realiza preguntas en lenguaje natural y obtiene respuestas contextualizadas mediante una arquitectura basada en RAG (Retrieval-Augmented Generation).

La primera versión del proyecto trabaja con documentos PDF, pero desde su diseño fue concebido para evolucionar hacia múltiples fuentes de información como hojas de cálculo, imágenes, bases de datos y servicios externos.

---

# 🎯 Problema

Actualmente almacenamos información importante en múltiples documentos:

- Manuales
- Contratos
- Documentación técnica
- Políticas
- Reportes
- Guías

Buscar una respuesta específica normalmente implica abrir varios archivos y recorrer cientos de páginas manualmente.

KnowledgeHub AI transforma esos documentos en una base de conocimiento inteligente que puede consultarse mediante preguntas en lenguaje natural.

---

# 💡 Solución

KnowledgeHub AI combina procesamiento de documentos, embeddings, búsqueda semántica y Modelos de Lenguaje (LLM) para responder preguntas utilizando únicamente la información contenida en los documentos del usuario.

Actualmente soporta:

- ✅ Documentos PDF

Arquitectura preparada para soportar próximamente:

- Excel
- CSV
- Imágenes (OCR)
- Bases de datos
- APIs
- WhatsApp

---

# 🚀 Características

## Versión actual (MVP)

- Lectura de documentos PDF
- Extracción automática de texto
- División del documento en fragmentos (Chunking)
- Generación de Embeddings
- Almacenamiento en FAISS
- Búsqueda semántica
- Respuestas mediante IA
- Interfaz desarrollada con Streamlit
- Despliegue en Oracle Cloud Infrastructure (OCI)

---

# 🏗 Arquitectura

```
                     Usuario
                         │
                 Interfaz Streamlit
                         │
               KnowledgeHub Service
                         │
               Pipeline RAG (LangChain)
               ┌──────────┴──────────┐
               │                     │
         Retriever             Modelo LLM
               │
          Vector Store (FAISS)
               │
           Embeddings
               │
          Documentos PDF
```

---

# 🛠 Tecnologías utilizadas

## Backend

- Python

## Framework IA

- LangChain

## Modelo de Lenguaje

- OpenAI GPT

## Base de Datos Vectorial

- FAISS

## Procesamiento de documentos

- PyPDF

## Interfaz

- Streamlit

## Cloud

- Oracle Cloud Infrastructure (OCI)

## Control de versiones

- Git
- GitHub

---

# 📂 Estructura del proyecto

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
│
├── docs/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Instalación

Clonar el repositorio

```bash
git clone https://github.com/adan92/knowledgehub-ai.git
```

Entrar al proyecto

```bash
cd knowledgehub-ai
```

Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno virtual

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación

```bash
streamlit run main.py
```

---

# 💬 Ejemplos de preguntas

El asistente podrá responder preguntas como:

- ¿Qué tecnologías utiliza el backend?
- ¿Cómo funciona el proceso de onboarding?
- ¿Cuál es la arquitectura de microservicios?
- ¿Qué estándares de desarrollo recomienda la empresa?
- ¿Cómo se gestionan los incidentes?

---

# 📸 Capturas de pantalla

> Se agregarán una vez finalizada la implementación.

---

# ☁ Despliegue en Oracle Cloud

La documentación del despliegue será incorporada una vez publicada la aplicación en Oracle Cloud Infrastructure.

---

# 🧭 Principios de Diseño

Durante el desarrollo del proyecto se siguieron los siguientes principios:

- Arquitectura modular
- Separación de responsabilidades
- Fácil mantenimiento
- Escalabilidad
- Preparado para evolucionar hacia nuevas fuentes de información

---

# ⚠ Limitaciones actuales

La versión MVP presenta las siguientes limitaciones:

- Sólo soporta documentos PDF
- No cuenta con autenticación
- No soporta OCR
- Sólo permite una colección de documentos
- No almacena historial de conversaciones

---

# 🔮 Futuro del proyecto

KnowledgeHub AI nace como un motor de conocimiento.

El objetivo es evolucionar progresivamente para convertirse en un asistente capaz de consultar información distribuida en múltiples fuentes, como documentos, bases de datos, aplicaciones empresariales y plataformas de mensajería.

---

# 🙌 Agradecimientos

Este proyecto fue iniciado como parte del Challenge **Oracle Next Education – AI Tech Builder**, pero está diseñado para continuar evolucionando como un proyecto independiente de código abierto.

---

# 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.