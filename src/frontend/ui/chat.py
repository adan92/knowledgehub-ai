"""
Componente principal del chat.
"""
import requests
import streamlit as st

from config.settings import settings
from frontend.ui.pdf_viewer import render_pdf_panel
from frontend.ui.source_cards import render_sources

WELCOME_MESSAGE = """
# 🧠 KnowledgeHub AI

Bienvenido.

Consulta tus documentos utilizando Inteligencia Artificial.

Este asistente responde exclusivamente con información encontrada en los documentos cargados.

### ¿Qué puedes hacer?

- 📚 Buscar información en varios documentos.
- 💬 Hacer preguntas en lenguaje natural.
- 📄 Consultar las fuentes utilizadas.
- 🔎 Revisar el fragmento exacto utilizado para responder.
"""


def render_chat() -> None:
    st.title("💬 Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_column, viewer_column = st.columns(
        [7, 3],
        gap="large"
    )

    #
    # CHAT
    #
    with chat_column:

        if not st.session_state.messages:
            st.info(WELCOME_MESSAGE)

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.markdown(
                    message["content"]
                )

                if message["role"] == "assistant":
                    render_sources(
                        message.get("sources", [])
                    )

        question = st.chat_input(
            "Pregunta sobre tus documentos..."
        )

        if question:
            # Limpiar el visor para la nueva consulta
            st.session_state.pop("selected_source", None)

            st.session_state.messages.append({
                "role": "user",
                "content": question
            })

            with st.chat_message("user"):
                st.markdown(question)

            with st.chat_message("assistant"):
                with st.spinner(
                        "🧠 Analizando documentos..."
                ):
                    response = requests.post(
                        f"{settings.api_base_url}/chat",
                        json={
                            "question": question
                        }
                    )
                    data = response.json()

                st.markdown(
                    data["answer"]
                )

                render_sources(
                    data["sources"]
                )

            st.session_state.messages.append({
                "role": "assistant",
                "content": data["answer"],
                "sources": data["sources"]
            })

    #
    # VISOR
    #
    with viewer_column:

        st.subheader("📄 Documento")

        render_pdf_panel()
