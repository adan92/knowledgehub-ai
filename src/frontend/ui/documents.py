import streamlit as st
import requests


def render_documents(document_client):

    st.title("📚 Base de conocimiento")

    st.caption(
        "Administra los documentos utilizados por la IA para responder preguntas."
    )

    st.divider()

    # ----------------------------------------------------
    # Subir documentos
    # ----------------------------------------------------

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

        if st.button(
            "Subir documentos",
            type="primary",
            use_container_width=True
        ):

            try:

                with st.spinner("Subiendo documentos..."):

                    for file in uploaded_files:
                        document_client.upload(file)

                st.success(
                    "Documentos cargados correctamente."
                )

                st.rerun()

            except requests.RequestException:

                st.error(
                    "No fue posible subir los documentos."
                )

    st.divider()

    # ----------------------------------------------------
    # Documentos
    # ----------------------------------------------------

    st.subheader("📄 Documentos indexados")

    try:

        documents = document_client.list_documents()

    except requests.RequestException:

        st.error(
            "No fue posible obtener la lista de documentos."
        )

        return

    if not documents:

        st.info(
            "No hay documentos cargados."
        )

    else:

        for filename in documents:

            col1, col2 = st.columns(
                [9, 1]
            )

            with col1:

                st.markdown(
                    f"📄 **{filename}**"
                )

            with col2:

                if st.button(
                    "🗑",
                    key=f"delete_{filename}"
                ):

                    try:

                        document_client.delete(
                            filename
                        )

                        st.success(
                            "Documento eliminado."
                        )

                        st.rerun()

                    except requests.RequestException:

                        st.error(
                            "No fue posible eliminar el documento."
                        )

    st.divider()

    # ----------------------------------------------------
    # Índice
    # ----------------------------------------------------

    st.subheader("🔄 Índice vectorial")

    if st.button(
        "Reconstruir índice",
        use_container_width=True
    ):

        try:

            with st.spinner(
                "Reconstruyendo índice..."
            ):

                document_client.rebuild()

            st.success(
                "Índice reconstruido correctamente."
            )

            st.rerun()

        except requests.RequestException:

            st.error(
                "No fue posible reconstruir el índice."
            )
