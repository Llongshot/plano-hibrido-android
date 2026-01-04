# 🏋️ Plano Híbrido 8 Semanas - Android App

Aplicação Android para plano de exercícios híbrido de 8 semanas, focado em escoliose, perda de peso e tonificação.

## 📱 Funcionalidades

- ✅ **Timer Visual**: Cronômetro integrado para cada exercício
- ✅ **Vídeos do YouTube**: Links diretos para vídeos demonstrativos
- ✅ **Progresso Pessoal**: Registo de peso e notas por dia
- ✅ **8 Semanas Progressivas**: Intensidade ajustada automaticamente
- ✅ **Interface Android TV**: Otimizada para controlo remoto
- ✅ **Offline**: Funciona sem internet (exceto vídeos)

## 🎯 Exercícios Incluídos

1. **Ponte de Glúteos** - Ativação dos glúteos
2. **Bird-Dog** - Coordenação e equilíbrio
3. **Prancha Modificada** - Fortalecimento do core
4. **Gato-Vaca** - Mobilidade da coluna
5. **Superman Alternado** - Extensores da coluna
6. **Retração Escapular** - Postura dos ombros

## 📥 Download

### Opção 1: Download Direto (Recomendado)
[![Download APK](https://img.shields.io/badge/Download-APK-green?style=for-the-badge&logo=android)](../../releases/latest)

### Opção 2: Compilação Automática
O APK é compilado automaticamente via GitHub Actions a cada commit.

## 📲 Instalação

1. **Baixe o APK** da seção [Releases](../../releases)
2. **Ative fontes desconhecidas** no Android:
   - Configurações → Segurança → Fontes desconhecidas
3. **Instale o APK** tocando no arquivo baixado
4. **Abra a aplicação** e comece a treinar!

## 🔧 Compilação Local

Se quiser compilar localmente:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/plano-hibrido-android.git
cd plano-hibrido-android

# Instale dependências (Linux/WSL)
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Instale Buildozer
pip install buildozer

# Compile o APK
buildozer android debug
```

## 🎮 Como Usar

### Menu Principal
- **📆 Plano Semanal**: Exercícios organizados por dia
- **🎥 Exercícios com Vídeos**: Descrições detalhadas + vídeos
- **📊 Progresso & Notas**: Registo de peso e observações

### Plano Semanal
- Use **◀ ▶** para navegar entre semanas (1-8)
- Clique **🎥 VÍDEO** para ver demonstração
- Clique **▶ INICIAR** para começar o timer
- Intensidade aumenta automaticamente por semana

### Timer
- Contagem regressiva visual
- Barra de progresso
- Mudança de cor nos últimos segundos
- Botão **⏹ PARAR** para cancelar

## 📱 Compatibilidade

- **Android 5.0+** (API 21+)
- **Android TV** suportado
- **Smartphones** e **tablets**
- **Orientação landscape** recomendada para TV

## 🎥 Vídeos

Os vídeos são abertos no:
1. **App do YouTube** (se instalado)
2. **Navegador padrão** (fallback)
3. **Link copiável** (manual)

## 💾 Dados

- **Progresso salvo localmente** no dispositivo
- **Arquivo JSON** para backup/restauro
- **Sem coleta de dados** pessoais
- **Funciona offline** (exceto vídeos)

## 🔄 Atualizações

As atualizações são disponibilizadas via:
- **GitHub Releases** (manual)
- **Compilação automática** (CI/CD)

## 🐛 Problemas Conhecidos

- Vídeos requerem conexão à internet
- Primeira instalação pode pedir permissões
- Em alguns dispositivos, pode ser necessário permitir "Apps desconhecidas"

## 📞 Suporte

Para problemas ou sugestões:
1. Abra uma [Issue](../../issues)
2. Descreva o problema detalhadamente
3. Inclua modelo do dispositivo e versão Android

## 📄 Licença

Este projeto é de código aberto. Veja o arquivo LICENSE para detalhes.

---

**Desenvolvido com ❤️ usando Kivy + Buildozer**