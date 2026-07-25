"""
Componente principal del chat.
"""
from uuid import uuid4

import streamlit as st

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


def render_chat(chat_client) -> None:

    st.title("💬 Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_column, viewer_column = st.columns(
        [7, 3],
        gap="large"
    )

    # ------------------------------------------------------------------
    # CHAT
    # ------------------------------------------------------------------

    with chat_column:

        if not st.session_state.messages:
            st.info(WELCOME_MESSAGE)

        # Historial
        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.markdown(message["content"])

                if message["role"] == "assistant":

                    render_sources(
                        message.get("sources", []),
                        message["id"]
                    )

        question = st.chat_input(
            "Pregunta sobre tus documentos..."
        )

        if question:

            st.session_state.pop(
                "selected_source",
                None
            )

            #
            # Mostrar inmediatamente la pregunta
            #
            with st.chat_message("user"):
                st.markdown(question)

            #
            # Placeholder para la respuesta
            #
            with st.chat_message("assistant"):

                response_placeholder = st.empty()

                with response_placeholder.container():

                    with st.spinner(
                        "🧠 Analizando documentos..."
                    ):
                        response = chat_client.ask(question)

                if response.success:

                    assistant_message = response.answer
                    sources = response.sources

                else:

                    assistant_message = response.message
                    sources = []

                #
                # Reemplaza el spinner por la respuesta
                #
                response_placeholder.empty()

                st.markdown(assistant_message)

                render_sources(
                    sources,
                    "current"
                )

            #
            # Persistir conversación
            #
            st.session_state.messages.append({
                "id": uuid4().hex,
                "role": "user",
                "content": question
            })

            st.session_state.messages.append({
                "id": uuid4().hex,
                "role": "assistant",
                "content": assistant_message,
                "sources": sources
            })

            st.rerun()

    # ------------------------------------------------------------------
    # VISOR
    # ------------------------------------------------------------------

    with viewer_column:

        st.subheader("📄 Documento")

        render_pdf_panel()