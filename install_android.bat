@echo off
echo 🏋️ Instalador Plano Híbrido 8 Semanas - Android TV
echo ==================================================

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Por favor instale Python primeiro.
    echo 📥 Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python encontrado

REM Verificar se pip está instalado
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip não encontrado. Reinstale Python com pip incluído.
    pause
    exit /b 1
)

echo ✅ pip encontrado

REM Instalar buildozer
echo 📦 Instalando buildozer...
pip install buildozer

REM Verificar se estamos no diretório correto
if not exist "main.py" (
    echo ❌ Arquivo main.py não encontrado. Execute este script no diretório do projeto.
    pause
    exit /b 1
)

echo ✅ Projeto encontrado

echo.
echo ⚠️  ATENÇÃO: Compilação Android no Windows requer WSL ou Docker
echo.
echo 📋 Opções para compilar:
echo.
echo 1️⃣  WSL (Windows Subsystem for Linux):
echo    - Instale WSL2 com Ubuntu
echo    - Execute o script install_android.sh dentro do WSL
echo.
echo 2️⃣  Docker:
echo    - Use uma imagem Docker com buildozer
echo.
echo 3️⃣  Máquina Virtual Linux:
echo    - Use VirtualBox/VMware com Ubuntu
echo.
echo 4️⃣  Serviço Online:
echo    - Use GitHub Actions ou similar
echo.
echo 💡 Recomendação: Use WSL2 para melhor performance
echo.
echo 📖 Guia WSL: https://docs.microsoft.com/en-us/windows/wsl/install
echo.

pause