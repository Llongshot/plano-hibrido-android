@echo off
echo 🚀 Configurando repositório GitHub para compilação automática do APK
echo ================================================================

echo.
echo 📋 Passos necessários:
echo.
echo 1️⃣  Criar repositório no GitHub
echo 2️⃣  Executar este script
echo 3️⃣  Aguardar compilação automática (~20-30 min)
echo 4️⃣  Baixar APK da seção Releases
echo.

set /p repo_url="🔗 Cole a URL do repositório GitHub (ex: https://github.com/usuario/repo.git): "

if "%repo_url%"=="" (
    echo ❌ URL não fornecida. Saindo...
    pause
    exit /b 1
)

echo.
echo 🔧 Verificando se Git está configurado...
git config user.name >nul 2>&1
if %errorlevel% neq 0 (
    set /p git_name="👤 Digite seu nome para Git: "
    git config --global user.name "!git_name!"
)

git config user.email >nul 2>&1
if %errorlevel% neq 0 (
    set /p git_email="📧 Digite seu email para Git: "
    git config --global user.email "!git_email!"
)

echo.
echo 📦 Inicializando repositório Git...
git init

echo.
echo 📁 Adicionando arquivos...
git add .

echo.
echo 💬 Fazendo commit inicial...
git commit -m "🏋️ Plano Híbrido 8 Semanas - Aplicação Android

✨ Funcionalidades principais:
- ⏱️ Timer visual com contagem regressiva
- 🎥 Vídeos do YouTube integrados (6 exercícios)
- 📊 Progresso e notas persistentes
- 📺 Interface otimizada para Android TV
- 🔄 8 semanas de progressão automática
- 💾 Dados salvos localmente

🎯 Exercícios incluídos:
- Ponte de Glúteos
- Bird-Dog  
- Prancha Modificada
- Gato-Vaca
- Superman Alternado
- Retração Escapular na Parede

🔧 Tecnologias:
- Kivy + Buildozer
- GitHub Actions (CI/CD)
- Android API 21+ (Android 5.0+)
- Java 17 + Python 3.11

📱 Compilação automática via GitHub Actions
🚀 APK gerado automaticamente a cada commit"

echo.
echo 🔗 Conectando ao repositório remoto...
git branch -M main
git remote add origin %repo_url%

echo.
echo 🚀 Enviando código para GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Sucesso! Repositório configurado com GitHub Actions atualizadas.
    echo.
    echo 📋 Próximos passos:
    echo.
    echo 1️⃣  Acesse: %repo_url%
    echo 2️⃣  Vá em "Actions" para acompanhar a compilação
    echo 3️⃣  Aguarde ~20-30 minutos para o APK ficar pronto
    echo 4️⃣  Baixe o APK em "Releases" quando aparecer ✅ verde
    echo.
    echo 🎯 Funcionalidades do APK:
    echo    - Timer visual para exercícios
    echo    - Vídeos do YouTube (botões que abrem links)
    echo    - Progresso salvo localmente
    echo    - Interface Android TV
    echo    - 8 semanas progressivas
    echo.
    echo 📱 O APK será compatível com Android 5.0+ e Android TV!
) else (
    echo.
    echo ❌ Erro ao enviar para GitHub.
    echo 🔧 Verifique se:
    echo    - A URL está correta
    echo    - Você tem permissão no repositório
    echo    - Sua conexão à internet está funcionando
    echo    - Git está instalado corretamente
    echo.
    echo 💡 Tente executar manualmente:
    echo    git remote add origin %repo_url%
    echo    git push -u origin main
)

echo.
echo 🔍 Para acompanhar o progresso:
echo    1. Vá ao repositório no GitHub
echo    2. Clique na aba "Actions"
echo    3. Veja o status da compilação em tempo real
echo.
pause