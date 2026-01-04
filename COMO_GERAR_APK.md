# 📱 Como Gerar o APK da Aplicação

## 🚀 Método Automático (Recomendado)

### Passo 1: Criar Repositório no GitHub
1. Acesse [GitHub.com](https://github.com)
2. Clique em "New repository"
3. Nome: `plano-hibrido-android` (ou outro nome)
4. Marque "Public" 
5. Clique "Create repository"
6. **Copie a URL** do repositório (ex: `https://github.com/usuario/plano-hibrido-android.git`)

### Passo 2: Executar Script de Configuração
1. Execute `setup_github.bat`
2. Cole a URL do repositório quando solicitado
3. Aguarde o upload dos arquivos

### Passo 3: Aguardar Compilação
1. Acesse seu repositório no GitHub
2. Vá na aba "Actions"
3. Aguarde a compilação terminar (~15-20 minutos)
4. ✅ Quando aparecer um ✓ verde, está pronto!

### Passo 4: Baixar APK
1. Vá na aba "Releases" do repositório
2. Baixe o arquivo `.apk`
3. Instale no seu Android/Android TV

---

## 🔧 Método Manual (Avançado)

### Pré-requisitos
- Linux ou WSL2 no Windows
- Python 3.8+
- Java 8

### Comandos
```bash
# Instalar dependências
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Instalar Buildozer
pip install buildozer

# Compilar APK
buildozer android debug
```

O APK será gerado em `bin/planohibrido-1.0-arm64-v8a-debug.apk`

---

## 📲 Instalação no Android

### Android TV
1. Ative "Opções de desenvolvedor"
2. Ative "Depuração USB" e "Apps de fontes desconhecidas"
3. Transfira o APK via USB ou rede
4. Instale tocando no arquivo

### Smartphone/Tablet
1. Configurações → Segurança → "Fontes desconhecidas" (ativar)
2. Baixe o APK
3. Toque no arquivo para instalar
4. Confirme a instalação

---

## ❓ Resolução de Problemas

### Erro "App não instalada"
- Verifique se "Fontes desconhecidas" está ativado
- Tente desinstalar versão anterior primeiro

### Erro de compilação no GitHub
- Verifique se todos os arquivos foram enviados
- Aguarde alguns minutos e tente novamente

### APK muito grande
- Normal, primeira compilação pode ser ~50MB
- Inclui todas as dependências necessárias

---

## 🎯 Resultado Final

Após seguir estes passos, terá:
- ✅ APK funcional para Android
- ✅ Timer visual para exercícios  
- ✅ Vídeos do YouTube integrados
- ✅ Interface otimizada para TV
- ✅ Progresso salvo localmente

**Tempo total: ~20-30 minutos (incluindo compilação)**