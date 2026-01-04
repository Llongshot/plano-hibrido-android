@echo off
echo 🔧 Atualizando repositório com correções para licenças Android
echo ============================================================

echo.
echo 📋 Correções aplicadas:
echo.
echo ✅ Workflow robusto com aceitação automática de licenças
echo ✅ Buildozer.spec simplificado (Android API 30, NDK 21b)
echo ✅ Múltiplas estratégias de build (expect, yes, manual)
echo ✅ Verificação detalhada de APK gerado
echo ✅ Release automático com informações completas
echo.

echo 📁 Adicionando arquivos atualizados...
git add .

echo 💬 Fazendo commit das correções...
git commit -m "🔧 Fix: Correção automática de licenças Android SDK

✨ Melhorias aplicadas:
- 🤖 Aceitação automática de licenças Android SDK
- 📋 Pré-população de arquivos de licença conhecidos
- 🔄 Múltiplas estratégias de build (expect + yes + manual)
- 🛠️ Buildozer.spec otimizado (API 30, NDK 21b)
- 📊 Verificação detalhada de APK gerado
- 🎯 Workflow robusto com fallbacks

🔧 Problemas resolvidos:
- ❌ Exit code 100 (buildozer)
- ❌ Android SDK license not accepted
- ❌ Build-tools não encontrado
- ❌ AIDL não encontrado

📱 Resultado esperado:
- ✅ APK gerado automaticamente
- ✅ Compatível com Android 5.0+
- ✅ Interface Android TV otimizada
- ✅ Timer + vídeos + progresso funcionais"

echo 🚀 Enviando correções para GitHub...
git push

if %errorlevel% equ 0 (
    echo.
    echo ✅ Correções enviadas com sucesso!
    echo.
    echo 📋 O que acontecerá agora:
    echo.
    echo 1️⃣  GitHub Actions iniciará automaticamente
    echo 2️⃣  Licenças Android serão aceitas automaticamente
    echo 3️⃣  APK será compilado com múltiplas estratégias
    echo 4️⃣  Se bem-sucedido, APK estará em "Releases"
    echo.
    echo 🎯 Acompanhe o progresso:
    echo    - Vá ao repositório no GitHub
    echo    - Clique em "Actions"
    echo    - Veja o workflow "Build APK Robust" em execução
    echo.
    echo ⏱️  Tempo estimado: 25-35 minutos
    echo 📱 APK final: ~15-25MB
    echo.
    echo 🔍 Se ainda falhar, verifique os logs detalhados no Actions
) else (
    echo.
    echo ❌ Erro ao enviar correções.
    echo 🔧 Tente executar manualmente:
    echo    git add .
    echo    git commit -m "Fix Android licenses"
    echo    git push
)

echo.
pause