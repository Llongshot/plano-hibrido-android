#!/usr/bin/env python3
"""
Script de teste para a aplicação Kivy
Execute este script para testar a app no desktop antes de compilar para Android
"""

import sys
import os

# Adicionar diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import ExercicioApp
    print("✅ Importação bem-sucedida")
    
    print("🚀 Iniciando aplicação de teste...")
    print("📱 Janela será aberta simulando Android TV")
    print("⌨️  Use mouse/teclado para navegar")
    print("🔄 Feche a janela para sair")
    
    # Configurar para simular Android TV
    from kivy.config import Config
    Config.set('graphics', 'width', '1280')
    Config.set('graphics', 'height', '720')
    Config.set('graphics', 'resizable', False)
    
    app = ExercicioApp()
    app.run()
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("📦 Instale as dependências:")
    print("   pip install kivy kivymd")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erro na aplicação: {e}")
    sys.exit(1)