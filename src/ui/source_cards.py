"""
Componentes para mostrar las fuentes utilizadas por el modelo.
"""

import streamlit as st


def render_sources(sources: list[dict]) -> None:
    """
    Renderiza las fuentes utilizadas para generar la respuesta.

    Args:
        sources:
            Lista de fuentes utilizadas por el modelo.
    """

    if not sources:
        return

    st.divider()
    st.subheader("📚 Fuentes consultadas")

    for source in sources:

        with st.container(border=True):

            st.markdown(f"#### 📄 {source.filename}")

            col1, col2 = st.columns([3, 1])

            with col1:
                st.caption(
                    f"Página {source.page}"
                )

            with col2:
                if st.button(
                        "👁",
                        key=f"{source.document_id}_{source.page}",
                        use_container_width=True
                ):
                    st.info(
                        "Próximamente"
                    )