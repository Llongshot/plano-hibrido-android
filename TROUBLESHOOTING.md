# 🔧 Resolução de Problemas - Compilação APK

## ❌ Exit Code 100 (Buildozer)

### Causas Comuns:
1. **Versões incompatíveis** de Android SDK/NDK
2. **Dependências em falta** no sistema
3. **Problemas de memória** durante compilação
4. **Configuração incorreta** do buildozer.spec

### Soluções:

#### 1. Usar Workflow Simples
Use o arquivo `.github/workflows/build-simple.yml` que tem configurações mais estáveis:
- Java 8 (mais compatível)
- Android API 31 (testado)
- NDK 23b (estável)

#### 2. Testar Localmente Primeiro
```bash
python test_local_build.py
```

#### 3. Limpar Cache do Buildozer
```bash
buildozer android clean
rm -rf .buildozer
```

#### 4. Verificar Logs Detalhados
No GitHub Actions, procure por:
- `Error:` ou `FAILED:`
- Problemas de download do SDK/NDK
- Erros de compilação C/C++

---

## 🐛 Problemas Comuns e Soluções

### 1. **"No module named 'kivy'"**
```bash
pip install kivy
```

### 2. **"Java not found"**
- Instale Java 8: `sudo apt install openjdk-8-jdk`
- Configure JAVA_HOME: `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64`

### 3. **"Android SDK not found"**
- Buildozer baixa automaticamente
- Se falhar, delete `.buildozer` e tente novamente

### 4. **"NDK build failed"**
- Use NDK 23b (mais estável)
- Verifique se há espaço suficiente (~5GB)

### 5. **"Permission denied"**
- No Android: ative "Fontes desconhecidas"
- No Linux: `chmod +x buildozer`

---

## 📱 Problemas de Instalação APK

### 1. **"App não instalada"**
**Soluções:**
- Ative "Instalar apps desconhecidas" nas configurações
- Desinstale versão anterior primeiro
- Verifique se APK não está corrompido

### 2. **"Aplicação não abre"**
**Soluções:**
- Verifique compatibilidade (Android 5.0+)
- Veja logs: `adb logcat | grep python`
- Reinstale o APK

### 3. **"Vídeos não abrem"**
**Soluções:**
- Instale app do YouTube
- Use navegador alternativo
- Verifique conexão à internet

---

## 🔄 Workflows Alternativos

### Opção 1: Build Simples (Recomendado)
Use `build-simple.yml`:
- Configuração minimalista
- Java 8 + Android API 31
- Retry automático se falhar

### Opção 2: Build Avançado
Use `build-apk-alternative.yml`:
- Cache para acelerar builds
- Mais informações de debug
- Java 17 + Android API 34

### Opção 3: Build Local
```bash
# Ubuntu/WSL
sudo apt update
sudo apt install openjdk-8-jdk python3-pip
pip install buildozer
buildozer android debug
```

---

## 📊 Monitoramento da Compilação

### GitHub Actions:
1. Vá em **Actions** no repositório
2. Clique no workflow em execução
3. Expanda cada step para ver logs
4. Procure por erros em vermelho

### Logs Importantes:
- **Setup Python**: Instalação do Python
- **Install dependencies**: Dependências do sistema
- **Build APK**: Compilação principal
- **Upload APK**: Upload do arquivo final

---

## 💡 Dicas de Otimização

### 1. **Acelerar Compilação**
- Use cache no workflow
- Compile apenas arquiteturas necessárias
- Use NDK/SDK versions estáveis

### 2. **Reduzir Tamanho do APK**
- Remova dependências desnecessárias
- Use `android.archs = arm64-v8a` (apenas 64-bit)
- Ative ProGuard (avançado)

### 3. **Melhorar Compatibilidade**
- Use Android API 21+ (Android 5.0+)
- Teste em diferentes dispositivos
- Evite recursos muito novos

---

## 🆘 Quando Pedir Ajuda

Se nada funcionar, abra uma **Issue** com:

1. **Logs completos** do erro
2. **Sistema operacional** usado
3. **Versões** de Python/Java/Buildozer
4. **Passos** que levaram ao erro
5. **Arquivos** buildozer.spec e workflow

### Template de Issue:
```
**Problema:** [Descreva o erro]

**Ambiente:**
- OS: [Windows/Linux/macOS]
- Python: [versão]
- Buildozer: [versão]

**Logs:**
```
[Cole os logs aqui]
```

**Já tentei:**
- [ ] Limpar cache buildozer
- [ ] Usar workflow simples
- [ ] Testar localmente
```

---

## ✅ Checklist de Verificação

Antes de compilar, verifique:

- [ ] `main.py` existe e funciona
- [ ] `buildozer.spec` está configurado
- [ ] Workflow do GitHub Actions está correto
- [ ] Repositório é público
- [ ] Não há erros de sintaxe no código
- [ ] Dependências estão listadas corretamente

**🎯 Com essas soluções, 95% dos problemas são resolvidos!**