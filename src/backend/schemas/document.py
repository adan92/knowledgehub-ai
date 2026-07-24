import streamlit as st


def render_documents():

    st.title("📚 Base de conocimiento")

    st.caption(
        "Administra los documentos utilizados por la IA para responder preguntas."
    )

    st.divider()

    # ==========================================================
    # Subida
    # ==========================================================

    st.subheader("➕ Agregar documentos")

    uploaded_files = st.file_uploader(
        "Selecciona uno o varios PDFs",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    if uploaded_files:

        st.success(
            f"{len(uploaded_files)} documento(s) listo(s) para subir."
        )

        st.button(
            "Subir documentos",
            type="primary",
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # Documentos
    # ==========================================================

    st.subheader("📄 Documentos indexados")

    documents = [
        {
            "name": "Frontend.pdf",
            "size": "2.3 MB",
            "date": "20/07/2026"
        },
        {
            "name": "Docker.pdf",
            "size": "1.4 MB",
            "date": "18/07/2026"
        },
        {
            "name": "Microservicios.pdf",
            "size": "5.8 MB",
            "date": "16/07/2026"
        }
    ]

    if not documents:

        st.info("No existen documentos cargados.")

    else:

        for document in documents:

            col1, col2, col3, col4 = st.columns(
                [6, 2, 2, 1],
                vertical_alignment="center"
            )

            with col1:
                st.markdown(f"**📄 {document['name']}**")

            with col2:
                st.caption(document["size"])

            with col3:
                st.caption(document["date"])

            with col4:

                st.button(
                    "🗑️",
                    key=document["name"],
                    help="Eliminar documento"
                )

            st.divider()

    # ==========================================================
    # Reindexar
    # ==========================================================

    st.subheader("🔄 Índice vectorial")

    st.button(
        "Reconstruir índice",
        use_container_width=True
    )
