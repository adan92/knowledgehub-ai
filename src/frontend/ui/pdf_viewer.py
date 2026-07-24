"""
Visor de documentos.
"""

from pathlib import Path
from urllib.parse import quote
import streamlit as st

from config.settings import settings


def show_pdf(source) -> None:
    """
    Guarda el documento seleccionado.
    """

    st.session_state.selected_source = source


def render_pdf_panel() -> None:

    source = st.session_state.get("selected_source")

    if source is None:

        st.info(
            "Selecciona una fuente para consultar "
            "el documento utilizado por la IA."
        )

        return

    title_col, close_col = st.columns([9, 1])

    with title_col:

        st.markdown(
            f"### 📄 {source['filename']}"
        )

    with close_col:

        if st.button(
            "✕",
            key="close_pdf_panel",
            help="Cerrar visor"
        ):

            st.session_state.pop(
                "selected_source",
                None
            )

            st.rerun()

    st.caption(
        f"📍 Página {source['page']}"
    )

    st.divider()

    st.markdown(
        "#### Fragmento recuperado"
    )

    st.text(
        source['content']
    )

    pdf_path = Path(source['filepath'])

    if pdf_path.exists():
        url = (
            f"{settings.api_base_url}"
            f"/documents/{quote(source['filename'])}"
            f"#page={source['page']}"
        )
        st.link_button(
            "🌐 Abrir PDF",
            url
        )
    else:
        st.error(
            "No fue posible localizar el documento."
        )
