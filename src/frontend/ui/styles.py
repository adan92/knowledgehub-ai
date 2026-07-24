"""
Estilos globales de la aplicación.
"""

import streamlit as st


def load_styles():

    st.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        width:320px;
    }

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
    }

    div[data-testid="stChatMessage"]{
        border-radius:12px;
    }
    
    div[data-testid="stVerticalBlock"] > div:has(div.stButton){
        margin-top:.4rem;
    }
    div[data-testid="stChatMessage"]{
        padding:1rem;
    }
    </style>
    """,
    unsafe_allow_html=True)
