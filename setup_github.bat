@echo off
echo 🚀 Configurando repositório GitHub para compilação automática do APK
echo ================================================================

echo.
echo 📋 Passos necessários:
echo.
echo 1️⃣  Criar repositório no GitHub
echo 2️⃣  Executar este script
echo 3️⃣  Aguardar compilação automática
echo 4️⃣  Baixar APK da seção Releases
echo.

set /p repo_url="🔗 Cole a URL do repositório GitHub (ex: https://github.com/usuario/repo.git): "

if "%repo_url%"=="" (
    echo ❌ URL não fornecida. Saindo...
    pause
    exit /b 1
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

✨ Funcionalidades:
- Timer visual para exercícios
- Vídeos do YouTube integrados  
- Progresso e notas persistentes
- Interface otimizada para Android TV
- 8 semanas de progressão automática

🔧 Tecnologias:
- Kivy + Buildozer
- GitHub Actions (CI/CD)
- Android API 21+

📱 Compilação automática via GitHub Actions"

echo.
echo 🔗 Conectando ao repositório remoto...
git branch -M main
git remote add origin %repo_url%

echo.
echo 🚀 Enviando código para GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Sucesso! Repositório configurado.
    echo.
    echo 📋 Próximos passos:
    echo.
    echo 1️⃣  Acesse: %repo_url%
    echo 2️⃣  Vá em "Actions" para ver a compilação
    echo 3️⃣  Aguarde ~15-20 minutos para o APK ficar pronto
    echo 4️⃣  Baixe o APK em "Releases" quando concluído
    echo.
    echo 🎯 O APK será criado automaticamente e estará disponível para download!
) else (
    echo.
    echo ❌ Erro ao enviar para GitHub.
    echo 🔧 Verifique se:
    echo    - A URL está correta
    echo    - Você tem permissão no repositório
    echo    - Git está configurado (git config user.name/email)
)

echo.
pause