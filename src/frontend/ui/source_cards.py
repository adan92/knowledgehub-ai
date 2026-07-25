"""
Componentes para mostrar las fuentes utilizadas por el modelo.
"""

import streamlit as st

from frontend.ui.pdf_viewer import show_pdf


def render_sources(
        sources: list,
        message_id: str
) -> None:
    """
    Renderiza las fuentes utilizadas por el modelo.

    Cada mensaje del chat posee un identificador único (`message_id`)
    para evitar colisiones entre los botones de distintas respuestas.
    """

    if not sources:
        return

    with st.expander(
        f"📚 Ver {len(sources)} fuente(s) utilizada(s)",
        expanded=False
    ):

        selected = st.session_state.get(
            "selected_source"
        )

        for source in sources:

            is_selected = (
                selected is not None
                and selected["document_id"] == source["document_id"]
                and selected["page"] == source["page"]
            )

            label = (
                f"✅ 📄 {source['filename']} · Página {source['page']}"
                if is_selected
                else f"📄 {source['filename']} · Página {source['page']}"
            )

            st.button(
                label,
                key=(
                    f"{message_id}_"
                    f"{source['document_id']}_"
                    f"{source['page']}"
                ),
                use_container_width=True,
                on_click=show_pdf,
                args=(source,)
            )