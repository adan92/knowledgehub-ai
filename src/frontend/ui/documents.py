import streamlit as st


def render_documents():

    st.title("📚 Base de conocimiento")

    st.caption(
        "Administra los documentos utilizados por la IA para responder preguntas."
    )

    st.divider()

    st.subheader("➕ Agregar documentos")

    uploaded_files = st.file_uploader(
        "Selecciona uno o varios archivos PDF",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    if uploaded_files:

        st.info(
            f"{len(uploaded_files)} documento(s) listo(s) para subir."
        )

        st.button(
            "Subir documentos",
            type="primary",
            use_container_width=True
        )

    st.divider()

    st.subheader("📄 Documentos indexados")

    st.info(
        "La integración con el backend se agregará en el siguiente paso."
    )

    st.dataframe(
        data=[
            {
                "Documento": "Frontend.pdf",
                "Tamaño": "2.3 MB",
                "Fecha": "20/07/2026"
            },
            {
                "Documento": "Docker.pdf",
                "Tamaño": "1.4 MB",
                "Fecha": "19/07/2026"
            }
        ],
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🔄 Índice vectorial")

    st.button(
        "Reconstruir índice",
        use_container_width=True
    )