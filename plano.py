import streamlit as st
import pandas as pd
import time

# ==============================
# CONFIGURAÇÃO INICIAL
# ==============================
st.set_page_config(page_title="Plano Híbrido 8 Semanas", layout="wide")
st.title("🏋️ Plano Híbrido 8 Semanas – Escoliose, Peso e Tonificação")

tab = st.sidebar.radio("Navegação", ["Semana", "Exercícios", "Alimentação & Notas"])

# ==============================
# DICIONÁRIO DE VÍDEOS
# ==============================
videos_exercicios = {
    "Ponte de Glúteos": "https://www.youtube.com/watch?v=Pplko_LUxDI",
    "Bird-Dog": "https://www.youtube.com/watch?v=vzU5xrs1gMQ",
    "Prancha Modificada": "https://www.youtube.com/watch?v=iFpHYVOhfMU",
    "Gato-Vaca": "https://www.youtube.com/watch?v=BZrfw5H5vmk",
    "Superman Alternado": "https://www.youtube.com/watch?v=ep3yBt7KAA0",
    "Retração Escapular na Parede": "https://www.youtube.com/watch?v=i90y_1kuWtk"
}

# ==============================
# 1️⃣ SEMANA – PLANO PRINCIPAL
# ==============================
if tab == "Semana":
    st.header("📅 Plano Híbrido 8 Semanas – Adaptado (sem terça-feira)")
    st.info("""
    Plano desenvolvido para pessoa de 40 anos, sedentária e fumadora, com escoliose leve a moderada.  
    ➜ Foco em mobilidade, força postural e reeducação corporal.  
    ➜ Sem impacto, sem carga externa, progressivo e seguro.
    """)

    # Estrutura semanal base (sem terça-feira)
    semana_base = {
        "Segunda-feira": [
            {"exercicio": "Ponte de Glúteos", "tempo": 30},
            {"exercicio": "Bird-Dog", "tempo": 30},
            {"exercicio": "Prancha Modificada", "tempo": 20}
        ],
        "Quarta-feira": [
            {"exercicio": "Gato-Vaca", "tempo": 40},
            {"exercicio": "Superman Alternado", "tempo": 30}
        ],
        "Quinta-feira": [
            {"exercicio": "Retração Escapular na Parede", "tempo": 30},
            {"exercicio": "Prancha Modificada", "tempo": 20}
        ],
        "Sexta-feira": [
            {"exercicio": "Ponte de Glúteos", "tempo": 30},
            {"exercicio": "Superman Alternado", "tempo": 30},
            {"exercicio": "Retração Escapular na Parede", "tempo": 20}
        ],
        "Sábado": [],
        "Domingo": []
    }

    # Progressão semanal (% sobre tempo base)
    progressao = {1:0.8,2:0.9,3:1.0,4:1.1,5:1.15,6:1.2,7:1.25,8:1.3}

    semana_atual = st.slider("Seleciona a semana", 1, 8, 1)
    st.write(f"📈 Intensidade ajustada: **{int(progressao[semana_atual]*100)}%**")

    # Loop diário
    for dia, exercicios in semana_base.items():
        st.subheader(f"📆 {dia}")
        if exercicios:
            for i, ex in enumerate(exercicios):
                tempo_ajustado = int(ex["tempo"] * progressao[semana_atual])
                
                # Colunas: nome, tempo, botão timer
                col1, col2, col3 = st.columns([2,1,1])
                with col1:
                    st.markdown(f"**{ex['exercicio']}**")
                with col2:
                    st.markdown(f"⏱️ {tempo_ajustado}s")
                with col3:
                    if st.button(f"Iniciar {ex['exercicio']}", key=f"{dia}_{i}_sem{semana_atual}"):
                        placeholder = st.empty()
                        progress = st.progress(0)
                        for t in range(tempo_ajustado):
                            time.sleep(1)
                            placeholder.text(f"Tempo restante: {tempo_ajustado - t}s")
                            progress.progress((t+1)/tempo_ajustado)
                        st.success(f"{ex['exercicio']} concluído! ✅")
                
                # Expander com vídeo embebido
                with st.expander(f"▶️ Ver vídeo: {ex['exercicio']}"):
                    st.video(videos_exercicios[ex['exercicio']])
        else:
            st.info("Descanso ativo opcional 🚶‍♀️ (caminhada leve ou alongamentos suaves).")

# ==============================
# 2️⃣ EXERCÍCIOS – DESCRIÇÕES DETALHADAS
# ==============================
elif tab == "Exercícios":
    st.header("🏋️ Exercícios Detalhados")

    exercicios = [
        {"nome":"Ponte de Glúteos","objetivo":"Ativar glúteos e estabilizar a pelve; protege lombar.","execucao":"Deitado de costas, joelhos dobrados, pés à largura da anca. Pressiona calcanhares e eleva a bacia.","series":"3x10–15","erros":"Evitar arquear a lombar ou forçar extensão.","video":videos_exercicios["Ponte de Glúteos"]},
        {"nome":"Bird-Dog","objetivo":"Melhorar coordenação e estabilidade lombar.","execucao":"Em quatro apoios, estende braço direito e perna esquerda até alinharem com o tronco. Mantém 2s e troca.","series":"3x8–12 por lado","erros":"Evitar arquear lombar; olhar sempre para o chão.","video":videos_exercicios["Bird-Dog"]},
        {"nome":"Prancha Modificada","objetivo":"Fortalecer core sem sobrecarregar a lombar.","execucao":"De barriga para baixo, apoia cotovelos e joelhos, mantendo corpo alinhado.","series":"3x20–30s","erros":"Não deixar bacia cair nem elevar demasiado quadril.","video":videos_exercicios["Prancha Modificada"]},
        {"nome":"Gato-Vaca","objetivo":"Melhorar mobilidade torácica e lombar.","execucao":"Em quatro apoios, inspira arqueando costas e expira curvando.","series":"3x8–12 ciclos","erros":"Evitar movimentos bruscos.","video":videos_exercicios["Gato-Vaca"]},
        {"nome":"Superman Alternado","objetivo":"Fortalecer extensores da coluna.","execucao":"Deitado de barriga para baixo, eleva braço direito e perna esquerda simultaneamente.","series":"2–3x8–12 por lado","erros":"Evitar rodar tronco ou esticar demais.","video":videos_exercicios["Superman Alternado"]},
        {"nome":"Retração Escapular na Parede","objetivo":"Fortalecer parte superior das costas e melhorar postura.","execucao":"Encostado à parede, puxa omoplatas para trás e para baixo, mantendo 3–5s.","series":"3x10–15","erros":"Não levantar ombros nem inclinar o tronco.","video":videos_exercicios["Retração Escapular na Parede"]}
    ]

    for ex in exercicios:
        with st.expander(ex["nome"]):
            st.video(ex["video"])
            st.markdown(f"**🎯 Objetivo:** {ex['objetivo']}")
            st.markdown(f"**🧭 Execução:** {ex['execucao']}")
            st.markdown(f"**🔁 Séries/Repetições:** {ex['series']}")
            st.markdown(f"**⚠️ Erros a evitar:** {ex['erros']}")

# ==============================
# 3️⃣ ALIMENTAÇÃO E NOTAS
# ==============================
elif tab == "Alimentação & Notas":
    st.header("🥦 Orientações Alimentares")
    st.markdown("""
    - Evitar bebidas açucaradas e fritos.
    - Priorizar proteína magra (frango, peixe, ovos).
    - Aumentar consumo de vegetais e fibra.
    - Fazer pequenas refeições regulares.
    - Hidratar-se: **1,5–2 L/dia**.
    - Reduzir gradualmente o tabaco (ideal: não fumar antes do treino).
    """)

    st.subheader("📝 Notas Pessoais")
    st.text_area("Regista aqui observações, progresso ou sintomas sentidos durante os treinos...")
