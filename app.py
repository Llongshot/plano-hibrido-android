import streamlit as st
from exercicios import exercicios
from render_semana import render_semana
from estilo import aplicar_estilo
from progresso import carregar_progresso, salvar_progresso
from utils import iniciar_timer

# ------------------- Estilo -------------------
aplicar_estilo()
st.set_page_config(page_title="Plano Híbrido 8 Semanas", layout="wide")

# ------------------- Título -------------------
st.markdown("<h1 style='text-align: center;'>🏋️ Plano Híbrido 8 Semanas – Escoliose, Peso e Tonificação</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Escolhe a aba</h3>", unsafe_allow_html=True)

# ------------------- Navegação -------------------
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
with col2:
    if st.button("📆 Semana", key="btn_semana"):
        st.session_state['tab'] = 'Semana'
with col3:
    if st.button("🏋️ Exercícios", key="btn_exercicios"):
        st.session_state['tab'] = 'Exercícios'
with col4:
    if st.button("🥦 Alimentação & Notas", key="btn_alimentacao"):
        st.session_state['tab'] = 'Alimentação & Notas'

tab = st.session_state.get('tab', 'Semana')

# ------------------- Dados base -------------------
semana_base = {
    "Segunda-feira": [{"exercicio":"Ponte de Glúteos","tempo":30},
                      {"exercicio":"Bird-Dog","tempo":30},
                      {"exercicio":"Prancha Modificada","tempo":20}],
    "Quarta-feira": [{"exercicio":"Gato-Vaca","tempo":40},
                      {"exercicio":"Superman Alternado","tempo":30}],
    "Quinta-feira": [{"exercicio":"Retração Escapular na Parede","tempo":30},
                     {"exercicio":"Prancha Modificada","tempo":20}],
    "Sexta-feira": [{"exercicio":"Ponte de Glúteos","tempo":30},
                     {"exercicio":"Superman Alternado","tempo":30},
                     {"exercicio":"Retração Escapular na Parede","tempo":20}],
    "Sábado": [], "Domingo": []
}
progressao = {1:0.8,2:0.9,3:1.0,4:1.1,5:1.15,6:1.2,7:1.25,8:1.3}

# ------------------- Carregar progresso -------------------
progresso = carregar_progresso()

# ------------------- Renderizar abas -------------------
if tab == "Semana":
    semana_atual = st.slider("Semana", 1, 8, 1)
    render_semana(semana_base, progressao, semana_atual)

    # ------------------- Progresso e notas -------------------
    st.header("📋 Progresso do Dia")
    for dia, dados in progresso["Dias"].items():
        st.subheader(dia)
        peso = st.text_input(f"Peso (kg) - {dia}", value=dados["Peso"], key=f"peso_{dia}")
        notas = st.text_area(f"Notas - {dia}", value=dados["Notas"], key=f"notas_{dia}")

        progresso["Dias"][dia]["Peso"] = peso
        progresso["Dias"][dia]["Notas"] = notas

    salvar_progresso(progresso)

elif tab == "Exercícios":
    st.header("🏋️ Exercícios Detalhados")
    for ex in exercicios:
        with st.expander(ex["nome"]):
            st.video(ex["video"])
            st.markdown(f"**🎯 Objetivo:** {ex['objetivo']}")
            st.markdown(f"**🧭 Execução:** {ex['execucao']}")
            st.markdown(f"**🔁 Séries/Repetições:** {ex['series']}")
            st.markdown(f"**⚠️ Erros a evitar:** {ex['erros']}")

elif tab == "Alimentação & Notas":
    st.header("🥦 Orientações Alimentares")
    st.markdown("""
    - Reduzir bebidas açucaradas e fritos.
    - Priorizar proteína magra, legumes e fibra.
    - Pequenas refeições regulares.
    - Hidratação: 1,5–2 L/dia.
    """)
    st.subheader("Notas Pessoais")
    for dia, dados in progresso["Dias"].items():
        st.text_area(f"Notas - {dia}", value=dados["Notas"], key=f"notas_pessoal_{dia}")
        progresso["Dias"][dia]["Notas"] = st.session_state[f"notas_pessoal_{dia}"]
    salvar_progresso(progresso)
