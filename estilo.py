import streamlit as st

def aplicar_estilo():
    st.markdown("""
    <style>
    body {background-color: #1e1e1e; color: #f5f5f5; font-family: 'Segoe UI', sans-serif;}
    h1,h2,h3,h4 { color:#f5f5f5; text-align:center; }

    .stButton>button {
        width: 200px;
        height: 60px;
        font-size: 18px;
        background-color: #60a5fa;
        color: #111111;
        border-radius: 12px;
        margin: 5px;
    }

    .exercicio-mobilidade {background-color: #2d2d2d; color: #f5f5f5; padding: 10px; border-radius: 8px; margin-bottom:5px;}
    .exercicio-forca {background-color: #1e3a8a; color: #f5f5f5; padding: 10px; border-radius: 8px; margin-bottom:5px;}
    .exercicio-postura {background-color: #4c1d95; color: #f5f5f5; padding: 10px; border-radius: 8px; margin-bottom:5px;}
    </style>
    """, unsafe_allow_html=True)
