import streamlit as st
from dotenv import load_dotenv

from services.knowledgehub_service import KnowledgeHubService

load_dotenv()

st.set_page_config(
    page_title="KnowledgeHub AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 KnowledgeHub AI")

st.caption(
    "RAG | Cohere | FAISS | Gemini"
)

if "service" not in st.session_state:
    with st.spinner("Inicializando KnowledgeHub..."):
        st.session_state.service = KnowledgeHubService()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input(
    "Pregunta sobre los documentos..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Buscando información..."):

        result = st.session_state.service.ask(
            question
        )

    answer = result["answer"]

    sources = "\n".join(
        [
            f"- {doc.metadata['filename']} (Página {doc.metadata['page'] + 1})"
            for doc in result["documents"]
        ]
    )
    if answer == 'No encontré información suficiente en los documentos.':
        final_answer = (
            f"{answer}\n\n"
        )
    else:
        final_answer = (
            f"{answer}\n\n"
            f"### 📄 Fuentes\n"
            f"{sources}"
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(final_answer)
