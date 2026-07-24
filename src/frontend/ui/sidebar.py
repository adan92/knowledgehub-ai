"""
Componentes de la barra lateral.
"""

from typing import Literal, cast

import streamlit as st


def render_sidebar(document_service):

    with st.sidebar:

        st.title("🧠 KnowledgeHub AI")

        st.divider()

        st.subheader("Navegación")

        if st.button(
            "💬 Chat",
            use_container_width=True,
            type=cast(
                Literal["primary", "secondary"],
                "primary" if st.session_state.view == "chat" else "secondary"
            ),
        ):
            st.session_state.view = "chat"
            st.rerun()

        if st.button(
            "📚 Base de conocimiento",
            use_container_width=True,
            type=cast(
                Literal["primary", "secondary"],
                "primary" if st.session_state.view == "knowledge" else "secondary"
            ),
        ):
            st.session_state.view = "knowledge"
            st.rerun()

        st.button(
            "ℹ️ Acerca",
            use_container_width=True,
            disabled=True
        )

        st.divider()

        st.subheader("Documentos")

        documents = document_service.list_documents()

        if not documents:

            st.caption("No hay documentos cargados.")

        else:

            for document in documents:
                st.markdown(f"📄 {document.stem}")

        st.divider()

        st.caption(f"{len(documents)} documento(s)")