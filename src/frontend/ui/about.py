"""
Página "Acerca de".
"""

import streamlit as st


def render_about() -> None:

    st.title("ℹ️ Acerca de KnowledgeHub AI")

    st.markdown("""
KnowledgeHub AI es un asistente conversacional diseñado para facilitar la consulta de documentación mediante Inteligencia Artificial.

En lugar de buscar manualmente entre múltiples documentos, el usuario puede realizar preguntas en lenguaje natural y obtener respuestas fundamentadas en la información disponible dentro de su repositorio documental.
""")

    st.divider()

    st.header("🎯 Problema que busca resolver")

    st.markdown("""
En muchas organizaciones el conocimiento se encuentra distribuido en manuales, procedimientos, documentación técnica, políticas internas y otros archivos PDF.

Encontrar una respuesta específica suele implicar revisar varios documentos, utilizar buscadores poco precisos o depender del conocimiento de otras personas.

KnowledgeHub AI busca reducir ese tiempo permitiendo consultar toda la documentación mediante una interfaz conversacional.
""")

    st.divider()

    st.header("⚙️ ¿Cómo funciona?")

    st.markdown("""
El sistema utiliza una arquitectura **Retrieval-Augmented Generation (RAG)**.

De forma simplificada:

1. Los documentos se procesan y dividen en fragmentos.
2. Cada fragmento se convierte en una representación vectorial.
3. Ante una pregunta, se recuperan únicamente los fragmentos más relevantes.
4. El modelo de lenguaje genera una respuesta utilizando únicamente esa información.
5. Se muestran las fuentes utilizadas para que el usuario pueda verificar la respuesta.
""")

    st.info(
        "Las respuestas siempre incluyen las fuentes utilizadas para facilitar su validación."
    )

    st.divider()

    st.header("🔒 Privacidad y confidencialidad")

    st.markdown("""
KnowledgeHub AI fue concebido pensando en escenarios donde la documentación contiene información privada o confidencial.

Aunque esta versión utiliza un modelo de lenguaje mediante API, la arquitectura fue diseñada desde el inicio para permitir la integración de modelos locales (self-hosted), reduciendo la necesidad de enviar información sensible a servicios externos.

Esto permite que la solución pueda evolucionar hacia implementaciones completamente privadas dentro de la infraestructura de una organización.
""")

    st.divider()

    st.header("🏢 Casos de uso")

    st.markdown("""
KnowledgeHub AI puede utilizarse como repositorio inteligente de conocimiento para diferentes áreas, por ejemplo:

- 📚 Manuales internos.
- 🏭 Procedimientos operativos.
- ⚖️ Normativas y políticas.
- 💻 Documentación técnica.
- 📖 Base de conocimiento corporativa.
- 🛠️ Documentación de proyectos.
- 📑 Guías de soporte.
- 🎓 Material de capacitación.
""")

    st.divider()

    st.header("🚀 Tecnologías utilizadas")

    st.markdown("""
- Python
- Streamlit
- FastAPI
- LangChain
- FAISS
- Google Gemini
- Arquitectura RAG (Retrieval-Augmented Generation)
""")

    st.divider()

    st.caption(
        "KnowledgeHub AI es un proyecto demostrativo orientado a mostrar una arquitectura moderna para asistentes conversacionales sobre documentación privada."
    )