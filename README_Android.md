# Plano Híbrido 8 Semanas - Android TV

Aplicação Android convertida do projeto Streamlit original para funcionar em Android TV.

## Funcionalidades

- ✅ **Menu Principal**: Navegação entre seções
- ✅ **Plano Semanal**: Visualização e execução de exercícios por semana
- ✅ **Timer Integrado**: Cronômetro para cada exercício
- ✅ **Exercícios Detalhados**: Descrições completas de cada exercício
- ✅ **Progresso**: Registo de peso e notas por dia
- ✅ **Interface TV-Friendly**: Otimizada para controlo remoto

## Estrutura da App

### Telas Principais:
1. **MenuScreen**: Tela inicial com navegação
2. **SemanaScreen**: Plano semanal com timer
3. **ExerciciosScreen**: Detalhes dos exercícios
4. **ProgressoScreen**: Registo de progresso

### Funcionalidades Especiais:
- **Timer Visual**: Popup com contagem regressiva e barra de progresso
- **Navegação por Semanas**: Botões +/- para alterar semana (1-8)
- **Progressão Automática**: Intensidade ajustada por semana
- **Persistência**: Dados salvos em JSON local

## Como Compilar para Android

### Pré-requisitos:
```bash
# Instalar Python e pip
# Instalar buildozer
pip install buildozer

# Instalar dependências do sistema (Ubuntu/Debian)
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Instalar Android SDK e NDK (buildozer fará automaticamente)
```

### Compilação:
```bash
# Primeira compilação (demora mais tempo)
buildozer android debug

# Compilações subsequentes
buildozer android debug --private

# Para release (APK assinado)
buildozer android release
```

### Instalação no Android TV:
```bash
# Via ADB
adb install bin/planohibrido-1.0-arm64-v8a-debug.apk

# Ou copiar APK para dispositivo e instalar manualmente
```

## Controlo Remoto Android TV

### Navegação:
- **Setas**: Navegar entre botões
- **OK/Enter**: Selecionar
- **Voltar**: Retornar ao menu anterior
- **Home**: Sair da aplicação

### Atalhos:
- **Menu**: Ir para tela principal
- **Play/Pause**: Pausar/retomar timer (quando ativo)

## Diferenças da Versão Streamlit

### Removido:
- ❌ Vídeos do YouTube (limitações Android TV)
- ❌ Interface web
- ❌ Dependência de browser

### Adicionado:
- ✅ Interface nativa Android
- ✅ Controlo remoto suportado
- ✅ Timer visual melhorado
- ✅ Navegação otimizada para TV
- ✅ Armazenamento local

## Estrutura de Ficheiros

```
├── main.py              # Aplicação principal Kivy
├── buildozer.spec       # Configuração de compilação
├── requirements.txt     # Dependências Python
├── progresso.json       # Dados de progresso (criado automaticamente)
└── README_Android.md    # Este ficheiro
```

## Personalização

### Alterar Cores/Tema:
Editar as propriedades dos widgets em `main.py`:
```python
Button(
    text='Texto',
    background_color=(0.2, 0.6, 1, 1),  # RGBA
    font_size='20sp'
)
```

### Adicionar Exercícios:
Modificar a lista `self.exercicios` em `ExerciciosScreen` e `self.semana_base` em `SemanaScreen`.

### Alterar Progressão:
Modificar o dicionário `self.progressao` em `SemanaScreen`.

## Resolução de Problemas

### Erro de Compilação:
```bash
# Limpar cache
buildozer android clean

# Recompilar
buildozer android debug
```

### App não inicia:
- Verificar logs: `adb logcat | grep python`
- Verificar permissões no Android
- Reinstalar APK

### Timer não funciona:
- Verificar se Clock está importado
- Verificar se popup não está bloqueado

## Suporte

Para problemas específicos do Android TV:
1. Verificar compatibilidade do dispositivo
2. Testar em modo desenvolvedor
3. Verificar logs via ADB

## Próximas Melhorias

- [ ] Adicionar sons de notificação
- [ ] Melhorar animações
- [ ] Adicionar estatísticas
- [ ] Suporte a múltiplos utilizadores
- [ ] Backup na nuvem