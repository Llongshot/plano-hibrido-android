import json
import os

FICHEIRO = "progresso.json"

def carregar_progresso():
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "Semana": 1,
        "Dias": {
            "Segunda-feira": {"Peso": "", "Notas": ""},
            "Quarta-feira": {"Peso": "", "Notas": ""},
            "Quinta-feira": {"Peso": "", "Notas": ""},
            "Sexta-feira": {"Peso": "", "Notas": ""}
        }
    }

def salvar_progresso(progresso):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(progresso, f, indent=4, ensure_ascii=False)
