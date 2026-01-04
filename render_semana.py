import streamlit as st
from exercicios import videos_exercicios
from utils import iniciar_timer

TIPO_EXERCICIO = {
    "Ponte de Glúteos": "forca",
    "Bird-Dog": "forca",
    "Prancha Modificada": "forca",
    "Superman Alternado": "forca",
    "Gato-Vaca": "mobilidade",
    "Retração Escapular na Parede": "postura"
}

def render_semana(semana_base, progressao, semana_atual):
    st.write(f"📈 Intensidade ajustada: **{int(progressao[semana_atual]*100)}%**")

    for dia, exercicios in semana_base.items():
        st.subheader(f"📆 {dia}")
        if exercicios:
            for ex in exercicios:
                tempo_ajustado = int(ex["tempo"] * progressao[semana_atual])
                tipo = TIPO_EXERCICIO.get(ex['exercicio'], "mobilidade")
                classe = f"exercicio-{tipo}"

                st.markdown(f"""
                <div class="{classe}">
                    <b>{ex['exercicio']}</b> ⏱️ {tempo_ajustado}s
                </div>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns([1,1])
                with col1:
                    if st.button(f"Iniciar {ex['exercicio']}", key=f"{dia}_{ex['exercicio']}_{semana_atual}"):
                        iniciar_timer(tempo_ajustado, ex['exercicio'])
                with col2:
                    with st.expander(f"▶️ Ver vídeo: {ex['exercicio']}"):
                        st.video(videos_exercicios[ex['exercicio']])
        else:
            st.info("Descanso ativo 🚶‍♀️ (caminhada leve ou alongamentos suaves).")
