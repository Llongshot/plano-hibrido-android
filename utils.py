# utils.py
import streamlit as st
import time

def iniciar_timer(segundos, nome_exercicio):
    placeholder = st.empty()
    progress = st.progress(0)
    for t in range(segundos):
        time.sleep(1)
        placeholder.text(f"⏱️ Tempo restante: {segundos - t}s")
        progress.progress((t+1)/segundos)
    st.success(f"{nome_exercicio} concluído! ✅")
