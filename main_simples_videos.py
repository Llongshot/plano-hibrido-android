from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line, Ellipse
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import json
import os
import webbrowser

# Cores do tema
CORES = {
    'primaria': get_color_from_hex('#2563EB'),
    'secundaria': get_color_from_hex('#7C3AED'),
    'sucesso': get_color_from_hex('#10B981'),
    'aviso': get_color_from_hex('#F59E0B'),
    'erro': get_color_from_hex('#EF4444'),
    'fundo': get_color_from_hex('#1F2937'),
    'fundo_claro': get_color_from_hex('#374151'),
    'texto': get_color_from_hex('#F9FAFB'),
    'texto_secundario': get_color_from_hex('#D1D5DB')
}

# Dados dos exercícios com vídeos
EXERCICIOS_DATA = [
    {
        "nome": "Ponte de Glúteos",
        "objetivo": "Ativar glúteos e estabilizar a pelve; protege lombar.",
        "execucao": "Deitado de costas, joelhos dobrados, pés à largura da anca. Pressiona os calcanhares e eleva a bacia.",
        "series": "3x10–15",
        "erros": "Não exagerar na extensão da lombar.",
        "video": "https://www.youtube.com/watch?v=Pplko_LUxDI",
        "tipo": "ponte"
    },
    {
        "nome": "Gato-Vaca",
        "objetivo": "Melhorar mobilidade torácica e lombar.",
        "execucao": "Quatro apoios, mãos alinhadas com ombros e joelhos com ancas. Inspira arqueando costas, expira curvando.",
        "series": "3x8–12 ciclos",
        "erros": "Movimentos bruscos ou forçar amplitude.",
        "video": "https://www.youtube.com/watch?v=BZrfw5H5vmk",
        "tipo": "gato_vaca"
    },
    {
        "nome": "Prancha Modificada",
        "objetivo": "Fortalecer core sem sobrecarga lombar.",
        "execucao": "De barriga para baixo, apoia cotovelos sob ombros e joelhos. Levanta corpo mantendo linha reta.",
        "series": "3x20–30s",
        "erros": "Não deixar bacia cair nem elevar demasiado quadril.",
        "video": "https://www.youtube.com/watch?v=iFpHYVOhfMU",
        "tipo": "prancha"
    },
    {
        "nome": "Superman Alternado",
        "objetivo": "Fortalecer extensores da coluna.",
        "execucao": "Deitado de barriga para baixo, braços estendidos à frente. Eleva braço direito e perna esquerda simultaneamente.",
        "series": "2–3x8–12 por lado",
        "erros": "Não esticar demais; evitar rodar o tronco.",
        "video": "https://www.youtube.com/watch?v=ep3yBt7KAA0",
        "tipo": "superman"
    },
    {
        "nome": "Bird-Dog",
        "objetivo": "Coordenação, equilíbrio e estabilidade do core.",
        "execucao": "Quatro apoios, coluna neutra. Estende braço direito e perna esquerda até alinharem com o tronco.",
        "series": "3x8–12 por lado",
        "erros": "Não arquear a lombar; manter olhar para o chão.",
        "video": "https://www.youtube.com/watch?v=vzU5xrs1gMQ",
        "tipo": "bird_dog"
    },
    {
        "nome": "Retração Escapular na Parede",
        "objetivo": "Fortalecer parte superior das costas e corrigir postura dos ombros.",
        "execucao": "Encostado à parede, pés à frente, braços em 'goal post'. Puxa omoplatas para trás e para baixo.",
        "series": "3x10–15",
        "erros": "Não levantar os ombros; evitar inclinar o tronco.",
        "video": "https://www.youtube.com/watch?v=i90y_1kuWtk",
        "tipo": "retracao"
    }
]

class AnimatedButton(Button):
    def __init__(self, cor=None, **kwargs):
        super().__init__(**kwargs)
        self.cor = cor or CORES['primaria']
        self.background_color = self.cor
        self.color = CORES['texto']
        self.font_size = '16sp'
        self.bold = True
        
        self.bind(on_press=self._on_press)
        self.bind(on_release=self._on_release)
    
    def _on_press(self, instance):
        anim = Animation(size=(self.size[0] * 0.95, self.size[1] * 0.95), duration=0.1)
        anim.start(self)
    
    def _on_release(self, instance):
        anim = Animation(size=(self.size[0] / 0.95, self.size[1] / 0.95), duration=0.1)
        anim.start(self)

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'menu'
        
        with self.canvas.before:
            Color(*CORES['fundo'])
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_bg, pos=self._update_bg)
        
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        
        # Título
        title = Label(
            text='🏋️ PLANO HÍBRIDO\n8 Semanas • Escoliose, Peso e Tonificação\n🎥 Com Vídeos do YouTube',
            font_size='28sp',
            color=CORES['texto'],
            bold=True,
            halign='center',
            size_hint_y=0.4
        )
        title.bind(size=title.setter('text_size'))
        
        # Botões
        buttons_container = BoxLayout(orientation='vertical', spacing=20, size_hint_y=0.6)
        
        btn_semana = AnimatedButton(
            text='📆 PLANO SEMANAL',
            size_hint_y=None,
            height='80dp',
            cor=CORES['primaria']
        )
        btn_semana.bind(on_press=self.go_to_semana)
        
        btn_exercicios = AnimatedButton(
            text='🎥 EXERCÍCIOS COM VÍDEOS',
            size_hint_y=None,
            height='80dp',
            cor=CORES['secundaria']
        )
        btn_exercicios.bind(on_press=self.go_to_exercicios)
        
        btn_progresso = AnimatedButton(
            text='📊 PROGRESSO & NOTAS',
            size_hint_y=None,
            height='80dp',
            cor=CORES['sucesso']
        )
        btn_progresso.bind(on_press=self.go_to_progresso)
        
        buttons_container.add_widget(btn_semana)
        buttons_container.add_widget(btn_exercicios)
        buttons_container.add_widget(btn_progresso)
        
        layout.add_widget(title)
        layout.add_widget(buttons_container)
        self.add_widget(layout)
    
    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def go_to_semana(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'semana'
    
    def go_to_exercicios(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'exercicios'
    
    def go_to_progresso(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'progresso'

class SemanaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'semana'
        self.semana_atual = 1
        self.timer_ativo = False
        self.tempo_restante = 0
        
        with self.canvas.before:
            Color(*CORES['fundo'])
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_bg, pos=self._update_bg)
        
        self.semana_base = {
            "Segunda-feira": [
                {"exercicio": "Ponte de Glúteos", "tempo": 30},
                {"exercicio": "Bird-Dog", "tempo": 30},
                {"exercicio": "Prancha Modificada", "tempo": 20}
            ],
            "Quarta-feira": [
                {"exercicio": "Gato-Vaca", "tempo": 40},
                {"exercicio": "Superman Alternado", "tempo": 30}
            ],
            "Quinta-feira": [
                {"exercicio": "Retração Escapular na Parede", "tempo": 30},
                {"exercicio": "Prancha Modificada", "tempo": 20}
            ],
            "Sexta-feira": [
                {"exercicio": "Ponte de Glúteos", "tempo": 30},
                {"exercicio": "Superman Alternado", "tempo": 30},
                {"exercicio": "Retração Escapular na Parede", "tempo": 20}
            ],
            "Sábado": [],
            "Domingo": []
        }
        
        self.progressao = {1:0.8, 2:0.9, 3:1.0, 4:1.1, 5:1.15, 6:1.2, 7:1.25, 8:1.3}
        
        self.build_layout()
    
    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def build_layout(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=15)
        
        btn_voltar = AnimatedButton(
            text='← VOLTAR',
            size_hint_x=0.2,
            cor=CORES['erro']
        )
        btn_voltar.bind(on_press=self.voltar)
        
        # Controles da semana
        semana_controls = BoxLayout(orientation='horizontal', size_hint_x=0.6, spacing=10)
        
        btn_menos = AnimatedButton(text='◀', size_hint_x=0.2, cor=CORES['secundaria'])
        btn_menos.bind(on_press=self.diminuir_semana)
        
        self.label_semana = Label(
            text=f'SEMANA {self.semana_atual}\nIntensidade: {int(self.progressao[self.semana_atual]*100)}%',
            size_hint_x=0.6,
            font_size='20sp',
            color=CORES['texto'],
            bold=True,
            halign='center'
        )
        self.label_semana.bind(size=self.label_semana.setter('text_size'))
        
        btn_mais = AnimatedButton(text='▶', size_hint_x=0.2, cor=CORES['secundaria'])
        btn_mais.bind(on_press=self.aumentar_semana)
        
        semana_controls.add_widget(btn_menos)
        semana_controls.add_widget(self.label_semana)
        semana_controls.add_widget(btn_mais)
        
        header.add_widget(btn_voltar)
        header.add_widget(semana_controls)
        header.add_widget(Label(size_hint_x=0.2))
        
        # Área de exercícios
        scroll = ScrollView()
        self.exercicios_layout = BoxLayout(orientation='vertical', spacing=15, size_hint_y=None)
        self.exercicios_layout.bind(minimum_height=self.exercicios_layout.setter('height'))
        
        self.atualizar_exercicios()
        
        scroll.add_widget(self.exercicios_layout)
        
        main_layout.add_widget(header)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
    
    def atualizar_exercicios(self):
        self.exercicios_layout.clear_widgets()
        
        for dia, exercicios in self.semana_base.items():
            # Container do dia
            dia_container = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                spacing=10,
                padding=15
            )
            
            with dia_container.canvas.before:
                Color(*CORES['fundo_claro'])
                dia_container.bg_rect = Rectangle(size=dia_container.size, pos=dia_container.pos)
            
            dia_container.bind(
                size=lambda instance, value: setattr(instance.bg_rect, 'size', instance.size),
                pos=lambda instance, value: setattr(instance.bg_rect, 'pos', instance.pos)
            )
            
            # Título do dia
            dia_label = Label(
                text=f'📆 {dia}',
                font_size='18sp',
                size_hint_y=None,
                height='40dp',
                color=CORES['texto'],
                bold=True,
                halign='left'
            )
            dia_label.bind(size=dia_label.setter('text_size'))
            dia_container.add_widget(dia_label)
            
            if exercicios:
                for ex in exercicios:
                    tempo_ajustado = int(ex["tempo"] * self.progressao[self.semana_atual])
                    
                    # Container do exercício
                    ex_container = BoxLayout(
                        orientation='horizontal',
                        size_hint_y=None,
                        height='80dp',
                        spacing=10
                    )
                    
                    # Informações do exercício
                    info_label = Label(
                        text=f'{ex["exercicio"]}\n⏱️ {tempo_ajustado} segundos',
                        font_size='14sp',
                        color=CORES['texto'],
                        halign='left',
                        size_hint_x=0.5
                    )
                    info_label.bind(size=info_label.setter('text_size'))
                    
                    # Botão do vídeo
                    ex_data = next((e for e in EXERCICIOS_DATA if e["nome"] == ex["exercicio"]), None)
                    if ex_data:
                        btn_video = AnimatedButton(
                            text=f'🎥 VER VÍDEO\n{ex_data["nome"]}',
                            size_hint_x=0.3,
                            cor=CORES['aviso']
                        )
                        btn_video.bind(on_press=lambda x, url=ex_data["video"]: self.abrir_video(url))
                    else:
                        btn_video = Label(text='Sem vídeo', size_hint_x=0.3)
                    
                    # Botão iniciar
                    btn_iniciar = AnimatedButton(
                        text='▶ INICIAR',
                        size_hint_x=0.2,
                        cor=CORES['sucesso']
                    )
                    btn_iniciar.bind(on_press=lambda x, nome=ex["exercicio"], tempo=tempo_ajustado: self.iniciar_timer(nome, tempo))
                    
                    ex_container.add_widget(info_label)
                    ex_container.add_widget(btn_video)
                    ex_container.add_widget(btn_iniciar)
                    
                    dia_container.add_widget(ex_container)
            else:
                # Descanso
                descanso_label = Label(
                    text='🚶‍♀️ Descanso ativo (caminhada leve)',
                    font_size='16sp',
                    color=CORES['texto_secundario'],
                    size_hint_y=None,
                    height='40dp'
                )
                dia_container.add_widget(descanso_label)
            
            # Calcular altura
            altura = 60 + (len(exercicios) * 90 if exercicios else 50)
            dia_container.height = altura
            
            self.exercicios_layout.add_widget(dia_container)
    
    def abrir_video(self, url):
        # Mostrar popup com opções
        content = BoxLayout(orientation='vertical', spacing=20, padding=30)
        
        title_label = Label(
            text='🎥 Vídeo do Exercício',
            font_size='20sp',
            color=CORES['texto'],
            bold=True,
            size_hint_y=0.2
        )
        
        url_label = Label(
            text=f'Link: {url}',
            font_size='14sp',
            color=CORES['texto_secundario'],
            size_hint_y=0.2
        )
        
        buttons_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.6)
        
        btn_abrir = AnimatedButton(
            text='🌐 ABRIR NO NAVEGADOR',
            size_hint_y=None,
            height='50dp',
            cor=CORES['primaria']
        )
        btn_abrir.bind(on_press=lambda x: [webbrowser.open(url), popup.dismiss()])
        
        btn_copiar = AnimatedButton(
            text='📋 MOSTRAR LINK PARA COPIAR',
            size_hint_y=None,
            height='50dp',
            cor=CORES['secundaria']
        )
        btn_copiar.bind(on_press=lambda x: [self.mostrar_link(url), popup.dismiss()])
        
        btn_fechar = AnimatedButton(
            text='❌ FECHAR',
            size_hint_y=None,
            height='50dp',
            cor=CORES['erro']
        )
        
        buttons_layout.add_widget(btn_abrir)
        buttons_layout.add_widget(btn_copiar)
        buttons_layout.add_widget(btn_fechar)
        
        content.add_widget(title_label)
        content.add_widget(url_label)
        content.add_widget(buttons_layout)
        
        popup = Popup(
            title='',
            content=content,
            size_hint=(0.8, 0.6),
            separator_height=0
        )
        
        btn_fechar.bind(on_press=popup.dismiss)
        popup.open()
    
    def mostrar_link(self, url):
        content = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        info_label = Label(
            text='Copie este link e cole no seu navegador ou app do YouTube:',
            font_size='16sp',
            color=CORES['texto'],
            size_hint_y=0.3
        )
        
        url_input = TextInput(
            text=url,
            multiline=False,
            readonly=True,
            size_hint_y=0.4,
            font_size='14sp'
        )
        
        btn_fechar = AnimatedButton(
            text='Fechar',
            size_hint_y=0.3,
            cor=CORES['primaria']
        )
        
        content.add_widget(info_label)
        content.add_widget(url_input)
        content.add_widget(btn_fechar)
        
        popup = Popup(
            title='Link do Vídeo',
            content=content,
            size_hint=(0.9, 0.4)
        )
        
        btn_fechar.bind(on_press=popup.dismiss)
        popup.open()
    
    def diminuir_semana(self, instance):
        if self.semana_atual > 1:
            self.semana_atual -= 1
            self.atualizar_labels_semana()
            self.atualizar_exercicios()
    
    def aumentar_semana(self, instance):
        if self.semana_atual < 8:
            self.semana_atual += 1
            self.atualizar_labels_semana()
            self.atualizar_exercicios()
    
    def atualizar_labels_semana(self):
        self.label_semana.text = f'SEMANA {self.semana_atual}\nIntensidade: {int(self.progressao[self.semana_atual]*100)}%'
    
    def iniciar_timer(self, nome_exercicio, tempo):
        if self.timer_ativo:
            return
        
        self.timer_ativo = True
        self.tempo_restante = tempo
        
        # Timer popup simples
        content = BoxLayout(orientation='vertical', spacing=20, padding=30)
        
        self.timer_label = Label(
            text=nome_exercicio,
            font_size='24sp',
            color=CORES['texto'],
            bold=True,
            size_hint_y=0.2
        )
        
        self.tempo_label = Label(
            text=f'{self.tempo_restante}s',
            font_size='48sp',
            color=CORES['primaria'],
            bold=True,
            size_hint_y=0.4
        )
        
        self.progress_bar = ProgressBar(
            max=tempo,
            value=0,
            size_hint_y=0.2
        )
        
        btn_parar = AnimatedButton(
            text='⏹ PARAR',
            size_hint_y=0.2,
            cor=CORES['erro']
        )
        btn_parar.bind(on_press=self.parar_timer)
        
        content.add_widget(self.timer_label)
        content.add_widget(self.tempo_label)
        content.add_widget(self.progress_bar)
        content.add_widget(btn_parar)
        
        self.timer_popup = Popup(
            title='Timer do Exercício',
            content=content,
            size_hint=(0.6, 0.7),
            auto_dismiss=False
        )
        
        self.timer_popup.open()
        
        # Iniciar contagem
        self.timer_event = Clock.schedule_interval(lambda dt: self.atualizar_timer(nome_exercicio, tempo), 1)
    
    def atualizar_timer(self, nome_exercicio, tempo_total):
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.tempo_label.text = f'{self.tempo_restante}s'
            self.progress_bar.value = tempo_total - self.tempo_restante
            
            # Mudar cor conforme tempo
            if self.tempo_restante <= 5:
                self.tempo_label.color = CORES['erro']
            elif self.tempo_restante <= 10:
                self.tempo_label.color = CORES['aviso']
            else:
                self.tempo_label.color = CORES['primaria']
            
            return True
        else:
            # Concluído
            self.tempo_label.text = 'CONCLUÍDO!'
            self.tempo_label.color = CORES['sucesso']
            Clock.schedule_once(lambda dt: self.fechar_timer(), 2)
            return False
    
    def parar_timer(self, instance):
        self.fechar_timer()
    
    def fechar_timer(self):
        if hasattr(self, 'timer_event'):
            self.timer_event.cancel()
        self.timer_ativo = False
        if hasattr(self, 'timer_popup'):
            self.timer_popup.dismiss()
    
    def voltar(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'