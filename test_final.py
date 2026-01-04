#!/usr/bin/env python3
"""
Script de teste para a versão final da aplicação com vídeos do YouTube
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main_final import ExercicioApp
    print("✅ Importação bem-sucedida")
    
    print("🚀 Iniciando aplicação FINAL com vídeos...")
    print("📱 Simulando Android TV (1280x720)")
    print("🎥 Vídeos do YouTube integrados!")
    print("🎨 Interface visual melhorada!")
    print("⌨️  Use mouse/teclado para navegar")
    print("🔄 Feche a janela para sair")
    print()
    print("🎯 Funcionalidades:")
    print("   • Timer visual com animações")
    print("   • Exercícios com animações 2D")
    print("   • Vídeos do YouTube (clique nos thumbnails)")
    print("   • Progresso e notas persistentes")
    print("   • Interface otimizada para TV")
    
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
    print("   pip install kivy")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erro na aplicação: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)