"""
Componentes de la barra lateral.
"""

import streamlit as st


def render_sidebar(document_service):

    with st.sidebar:

        st.title("🧠 KnowledgeHub AI")

        st.divider()

        st.subheader("Navegación")

        st.button(
            "💬 Chat",
            use_container_width=True
        )

        st.button(
            "📂 Documentos",
            use_container_width=True
        )

        st.button(
            "⚙️ Configuración",
            use_container_width=True
        )

        st.button(
            "ℹ️ Acerca",
            use_container_width=True
        )

        st.divider()

        st.subheader("Documentos")

        documents = document_service.list_documents()

        if not documents:
            st.caption("No hay documentos.")

            return

        for document in documents:

            st.markdown(f"📄 {document.stem}")