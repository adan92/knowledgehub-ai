"""
Componente principal del chat.
"""

import streamlit as st

from ui.source_cards import render_sources


def render_chat(knowledgehub) -> None:
    """
    Renderiza la interfaz principal del chat.
    """

    st.title("💬 Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Historial de conversación
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message["role"] == "assistant":
                render_sources(
                    message.get("sources", [])
                )

    question = st.chat_input(
        "Pregunta sobre tus documentos..."
    )

    if not question:
        return

    # Mostrar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generar respuesta
    with st.chat_message("assistant"):

        with st.spinner("🧠 Analizando documentos..."):

            response = knowledgehub.ask(question)

        st.markdown(
            response["answer"]
        )

        render_sources(
            response["sources"]
        )

    # Guardar respuesta en el historial
    st.session_state.messages.append({
        "role": "assistant",
        "content": response["answer"],
        "sources": response["sources"]
    })