#!/usr/bin/env python3
"""
Script para testar a aplicação localmente antes de compilar
"""

import sys
import os

def test_imports():
    """Testa se todas as importações funcionam"""
    print("🔍 Testando importações...")
    
    try:
        import kivy
        print(f"✅ Kivy {kivy.__version__} importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar Kivy: {e}")
        return False
    
    try:
        from main import ExercicioApp
        print("✅ Aplicação principal importada com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar aplicação: {e}")
        return False
    
    return True

def test_data_files():
    """Verifica se os arquivos necessários existem"""
    print("\n📁 Verificando arquivos...")
    
    required_files = [
        'main.py',
        'buildozer.spec'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} encontrado")
        else:
            print(f"❌ {file} não encontrado")
            return False
    
    return True

def run_app():
    """Executa a aplicação para teste"""
    print("\n🚀 Iniciando aplicação de teste...")
    
    try:
        from kivy.config import Config
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '600')
        Config.set('graphics', 'resizable', True)
        
        from main import ExercicioApp
        app = ExercicioApp()
        app.run()
        
        return True
    except Exception as e:
        print(f"❌ Erro ao executar aplicação: {e}")
        return False

def main():
    print("🏋️ Teste Local - Plano Híbrido 8 Semanas")
    print("=" * 50)
    
    # Teste 1: Importações
    if not test_imports():
        print("\n❌ Falha nos testes de importação")
        print("💡 Execute: pip install kivy")
        return False
    
    # Teste 2: Arquivos
    if not test_data_files():
        print("\n❌ Falha na verificação de arquivos")
        return False
    
    print("\n✅ Todos os testes passaram!")
    print("\n🎯 Opções:")
    print("1. Testar aplicação (t)")
    print("2. Sair (qualquer tecla)")
    
    choice = input("\nEscolha: ").lower()
    
    if choice == 't':
        run_app()
    
    print("\n🎉 Teste concluído!")
    return True

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Teste interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)