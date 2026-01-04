#!/bin/bash

echo "🏋️ Instalador Plano Híbrido 8 Semanas - Android TV"
echo "=================================================="

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Por favor instale Python3 primeiro."
    exit 1
fi

echo "✅ Python3 encontrado"

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Instalando..."
    sudo apt update
    sudo apt install python3-pip -y
fi

echo "✅ pip3 encontrado"

# Instalar buildozer
echo "📦 Instalando buildozer..."
pip3 install --user buildozer

# Instalar dependências do sistema (Ubuntu/Debian)
echo "📦 Instalando dependências do sistema..."
sudo apt update
sudo apt install -y \
    git \
    zip \
    unzip \
    openjdk-8-jdk \
    python3-pip \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev \
    build-essential \
    ccache \
    libffi6

# Adicionar buildozer ao PATH se necessário
if ! command -v buildozer &> /dev/null; then
    echo "export PATH=\$PATH:\$HOME/.local/bin" >> ~/.bashrc
    export PATH=$PATH:$HOME/.local/bin
fi

echo "✅ Dependências instaladas"

# Verificar se estamos no diretório correto
if [ ! -f "main.py" ]; then
    echo "❌ Arquivo main.py não encontrado. Execute este script no diretório do projeto."
    exit 1
fi

echo "✅ Projeto encontrado"

# Compilar para Android (primeira vez demora mais)
echo "🔨 Compilando aplicação Android..."
echo "⚠️  Primeira compilação pode demorar 30-60 minutos"
echo "⚠️  Buildozer irá baixar Android SDK/NDK automaticamente"

buildozer android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Compilação concluída com sucesso!"
    echo ""
    echo "📱 APK criado em: bin/planohibrido-1.0-arm64-v8a-debug.apk"
    echo ""
    echo "📋 Para instalar no Android TV:"
    echo "   1. Ative 'Opções de desenvolvedor' no Android TV"
    echo "   2. Ative 'Depuração USB' e 'Instalar apps desconhecidas'"
    echo "   3. Conecte via ADB ou copie APK para dispositivo"
    echo "   4. Execute: adb install bin/planohibrido-1.0-arm64-v8a-debug.apk"
    echo ""
    echo "🎯 Ou copie o APK para um pendrive e instale diretamente no Android TV"
else
    echo ""
    echo "❌ Erro na compilação. Verifique os logs acima."
    echo ""
    echo "🔧 Soluções comuns:"
    echo "   - Execute: buildozer android clean"
    echo "   - Verifique conexão à internet"
    echo "   - Verifique espaço em disco (precisa ~5GB)"
fi