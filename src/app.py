"""Interfaz web de Streamlit para consultar la base documental de KnowledgeHub."""

import streamlit as st
from dotenv import load_dotenv

from services.knowledgehub_service import KnowledgeHubService

NO_ANSWER = "No encontré información suficiente en los documentos."

load_dotenv()

st.set_page_config(page_title="KnowledgeHub AI", page_icon="📚", layout="wide")
st.title("📚 KnowledgeHub AI")
st.caption("RAG | Cohere | FAISS | Gemini")

if "service" not in st.session_state:
    try:
        with st.spinner("Inicializando KnowledgeHub..."):
            st.session_state.service = KnowledgeHubService()
    except Exception as error:
        st.error("No se pudo inicializar la base de conocimiento.")
        st.exception(error)
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Pregunta sobre los documentos...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    try:
        with st.spinner("Buscando información..."):
            result = st.session_state.service.ask(question)
    except Exception as error:
        st.error("No se pudo procesar la consulta. Inténtalo de nuevo.")
        st.exception(error)
        st.stop()

    answer = result["answer"]
    sources = "\n".join(
        f"- {document.metadata.get('filename', 'Documento sin nombre')} "
        f"(Página {document.metadata.get('page', 0) + 1})"
        for document in result["documents"]
    )
    final_answer = answer
    if answer != NO_ANSWER and sources:
        final_answer = f"{answer}\n\n### 📄 Fuentes\n{sources}"

    st.session_state.messages.append({"role": "assistant", "content": final_answer})
    with st.chat_message("assistant"):
        st.markdown(final_answer)
