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
import platform

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
        "video_id": "Pplko_LUxDI",
        "tipo": "ponte"
    },
    {
        "nome": "Gato-Vaca",
        "objetivo": "Melhorar mobilidade torácica e lombar.",
        "execucao": "Quatro apoios, mãos alinhadas com ombros e joelhos com ancas. Inspira arqueando costas, expira curvando.",
        "series": "3x8–12 ciclos",
        "erros": "Movimentos bruscos ou forçar amplitude.",
        "video": "https://www.youtube.com/watch?v=BZrfw5H5vmk",
        "video_id": "BZrfw5H5vmk",
        "tipo": "gato_vaca"
    },
    {
        "nome": "Prancha Modificada",
        "objetivo": "Fortalecer core sem sobrecarga lombar.",
        "execucao": "De barriga para baixo, apoia cotovelos sob ombros e joelhos. Levanta corpo mantendo linha reta.",
        "series": "3x20–30s",
        "erros": "Não deixar bacia cair nem elevar demasiado quadril.",
        "video": "https://www.youtube.com/watch?v=iFpHYVOhfMU",
        "video_id": "iFpHYVOhfMU",
        "tipo": "prancha"
    },
    {
        "nome": "Superman Alternado",
        "objetivo": "Fortalecer extensores da coluna.",
        "execucao": "Deitado de barriga para baixo, braços estendidos à frente. Eleva braço direito e perna esquerda simultaneamente.",
        "series": "2–3x8–12 por lado",
        "erros": "Não esticar demais; evitar rodar o tronco.",
        "video": "https://www.youtube.com/watch?v=ep3yBt7KAA0",
        "video_id": "ep3yBt7KAA0",
        "tipo": "superman"
    },
    {
        "nome": "Bird-Dog",
        "objetivo": "Coordenação, equilíbrio e estabilidade do core.",
        "execucao": "Quatro apoios, coluna neutra. Estende braço direito e perna esquerda até alinharem com o tronco.",
        "series": "3x8–12 por lado",
        "erros": "Não arquear a lombar; manter olhar para o chão.",
        "video": "https://www.youtube.com/watch?v=vzU5xrs1gMQ",
        "video_id": "vzU5xrs1gMQ",
        "tipo": "bird_dog"
    },
    {
        "nome": "Retração Escapular na Parede",
        "objetivo": "Fortalecer parte superior das costas e corrigir postura dos ombros.",
        "execucao": "Encostado à parede, pés à frente, braços em 'goal post'. Puxa omoplatas para trás e para baixo.",
        "series": "3x10–15",
        "erros": "Não levantar os ombros; evitar inclinar o tronco.",
        "video": "https://www.youtube.com/watch?v=i90y_1kuWtk",
        "video_id": "i90y_1kuWtk",
        "tipo": "retracao"
    }
]
class AnimatedButton(Button):
    def __init__(self, cor=None, **kwargs):
        super().__init__(**kwargs)
        self.cor = cor or CORES['primaria']
        self.background_color = (0, 0, 0, 0)
        self.color = CORES['texto']
        self.font_size = '18sp'
        self.bold = True
        
        with self.canvas.before:
            Color(*self.cor)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
        
        self.bind(size=self._update_rect, pos=self._update_rect)
        self.bind(on_press=self._on_press)
        self.bind(on_release=self._on_release)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def _on_press(self, instance):
        anim = Animation(size=(self.size[0] * 0.95, self.size[1] * 0.95), duration=0.1)
        anim.start(self)
    
    def _on_release(self, instance):
        anim = Animation(size=(self.size[0] / 0.95, self.size[1] / 0.95), duration=0.1)
        anim.start(self)

class ExerciseAnimation(Widget):
    def __init__(self, exercise_type, **kwargs):
        super().__init__(**kwargs)
        self.exercise_type = exercise_type
        self.animation_step = 0
        self.animation_event = None
        
        with self.canvas:
            Color(*CORES['fundo_claro'])
            self.bg_rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        
        self.bind(size=self._update_bg, pos=self._update_bg)
        Clock.schedule_once(lambda dt: self.start_animation(), 0.5)
    
    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def start_animation(self):
        if self.animation_event:
            self.animation_event.cancel()
        self.animation_event = Clock.schedule_interval(self.animate, 1.0)
    
    def stop_animation(self):
        if self.animation_event:
            self.animation_event.cancel()
    
    def animate(self, dt):
        self.canvas.clear()
        
        with self.canvas:
            Color(*CORES['fundo_claro'])
            self.bg_rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
            
            if self.exercise_type == "ponte":
                self._draw_ponte_animation()
            elif self.exercise_type == "prancha":
                self._draw_prancha_animation()
            elif self.exercise_type == "bird_dog":
                self._draw_bird_dog_animation()
            elif self.exercise_type == "gato_vaca":
                self._draw_gato_vaca_animation()
            elif self.exercise_type == "superman":
                self._draw_superman_animation()
            elif self.exercise_type == "retracao":
                self._draw_retracao_animation()
        
        self.animation_step = (self.animation_step + 1) % 4
        return True
    
    def _draw_ponte_animation(self):
        center_x = self.center_x
        center_y = self.center_y
        
        Color(*CORES['primaria'])
        if self.animation_step < 2:
            Line(points=[center_x - 60, center_y - 10, center_x + 60, center_y - 10], width=4)
        else:
            Line(points=[center_x - 60, center_y - 10, center_x - 20, center_y + 20, 
                        center_x + 20, center_y + 20, center_x + 60, center_y - 10], width=4)
        
        Color(*CORES['secundaria'])
        Line(points=[center_x - 50, center_y - 10, center_x - 50, center_y - 30], width=3)
        Line(points=[center_x + 50, center_y - 10, center_x + 50, center_y - 30], width=3)
    
    def _draw_prancha_animation(self):
        center_x = self.center_x
        center_y = self.center_y
        
        Color(*CORES['primaria'])
        if self.animation_step < 2:
            Line(points=[center_x - 50, center_y, center_x + 50, center_y], width=4)
        else:
            Line(points=[center_x - 50, center_y + 2, center_x + 50, center_y - 2], width=4)
        
        Color(*CORES['secundaria'])
        Line(points=[center_x - 40, center_y, center_x - 40, center_y - 20], width=3)
        Line(points=[center_x + 40, center_y, center_x + 40, center_y - 20], width=3)
    
    def _draw_bird_dog_animation(self):
        center_x = self.center_x
        center_y = self.center_y
        
        Color(*CORES['primaria'])
        Line(points=[center_x - 30, center_y, center_x + 30, center_y], width=4)
        
        Color(*CORES['secundaria'])
        if self.animation_step < 2:
            Line(points=[center_x + 30, center_y, center_x + 60, center_y + 15], width=3)
            Line(points=[center_x - 30, center_y, center_x - 60, center_y - 15], width=3)
        else:
            Line(points=[center_x + 20, center_y, center_x + 20, center_y - 20], width=3)
            Line(points=[center_x - 20, center_y, center_x - 20, center_y - 20], width=3)
    
    def _draw_gato_vaca_animation(self):
        center_x = self.center_x
        center_y = self.center_y
        
        Color(*CORES['primaria'])
        if self.animation_step < 2:
            Line(points=[center_x - 40, center_y - 10, center_x - 10, center_y + 20, 
                        center_x + 10, center_y + 20, center_x + 40, center_y - 10], width=4)
        else:
            Line(points=[center_x - 40, center_y + 10, center_x - 10, center_y - 20, 
                        center_x + 10, center_y - 20, center_x + 40, center_y + 10], width=4)
        
        Color(*CORES['secundaria'])
        for x in [-30, -10, 10, 30]:
            Line(points=[center_x + x, center_y - 10, center_x + x, center_y - 30], width=2)
    
    def _draw_superman_animation(self):
        center_x = self.center_x
        center_y = self.center_y
        
        Color(*CORES['primaria'])
        Line(points=[center_x - 30, center_y, center_x + 30, center_y], width=4)
        
        Color(*CORES['secundaria'])
        if self.animation_step < 2:
            Line(points=[center_x - 30, center_y, center_x - 50, center_y + 20], width=3)
            Line(points=[center_x + 30, center_y, center_x + 50, center_y + 20], width=3)
        else:
            Line(points=[center_x - 30, center_y, center_x - 50, center_y - 5], width=3)
            Line(points=[center_x + 30, center_y, center_x + 50, center_y - 5], width=3)
    
    def _draw_retracao_animation(self):
        center_x = self.center_x
        center_y = self.center_y
        
        Color(*CORES['fundo'])
        Line(points=[center_x + 30, center_y - 40, center_x + 30, center_y + 40], width=6)
        
        Color(*CORES['primaria'])
        Line(points=[center_x - 20, center_y - 20, center_x - 20, center_y + 20], width=4)
        
        Color(*CORES['secundaria'])
        if self.animation_step < 2:
            Line(points=[center_x - 20, center_y + 10, center_x - 35, center_y + 5], width=3)
            Line(points=[center_x - 20, center_y - 10, center_x - 35, center_y - 5], width=3)
        else:
            Line(points=[center_x - 20, center_y + 10, center_x - 50, center_y + 15], width=3)
            Line(points=[center_x - 20, center_y - 10, center_x - 50, center_y - 15], width=3)

class VideoThumbnail(Widget):
    def __init__(self, video_url, video_id, exercise_name, **kwargs):
        super().__init__(**kwargs)
        self.video_url = video_url
        self.video_id = video_id
        self.exercise_name = exercise_name
        
        layout = BoxLayout(orientation='vertical', spacing=5)
        
        # Container do thumbnail
        thumb_container = FloatLayout(size_hint_y=0.8)
        
        with thumb_container.canvas.before:
            Color(*CORES['fundo_claro'])
            thumb_container.bg_rect = RoundedRectangle(
                size=thumb_container.size,
                pos=thumb_container.pos,
                radius=[10]
            )
        
        thumb_container.bind(
            size=lambda instance, value: setattr(instance.bg_rect, 'size', instance.size),
            pos=lambda instance, value: setattr(instance.bg_rect, 'pos', instance.pos)
        )
        
        # Ícone de play
        play_button = Button(
            text='▶',
            font_size='32sp',
            size_hint=(None, None),
            size=('80dp', '80dp'),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=CORES['primaria'],
            color=CORES['texto']
        )
        play_button.bind(on_press=self.open_video)
        
        # Label do YouTube
        youtube_label = Label(
            text='🎥 YouTube',
            font_size='12sp',
            color=CORES['texto_secundario'],
            pos_hint={'center_x': 0.5, 'y': 0.1},
            size_hint_y=None,
            height='20dp'
        )
        
        thumb_container.add_widget(play_button)
        thumb_container.add_widget(youtube_label)
        
        # Botões de ação
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=5)
        
        btn_youtube = Button(
            text='📱 App',
            font_size='10sp',
            background_color=CORES['erro']
        )
        btn_youtube.bind(on_press=self.open_youtube_app)
        
        btn_browser = Button(
            text='🌐 Web',
            font_size='10sp',
            background_color=CORES['secundaria']
        )
        btn_browser.bind(on_press=self.open_browser)
        
        buttons_layout.add_widget(btn_youtube)
        buttons_layout.add_widget(btn_browser)
        
        layout.add_widget(thumb_container)
        layout.add_widget(buttons_layout)
        
        self.add_widget(layout)
    
    def open_video(self, instance):
        self.show_video_options()
    
    def open_youtube_app(self, instance):
        try:
            if platform.system() == 'Linux':  # Android
                import subprocess
                subprocess.call(['am', 'start', '-a', 'android.intent.action.VIEW', 
                               '-d', f'vnd.youtube:{self.video_id}'])
            else:
                self.open_browser(instance)
        except:
            self.open_browser(instance)
    
    def open_browser(self, instance):
        try:
            webbrowser.open(self.video_url)
        except:
            self.show_url_popup()
    
    def show_video_options(self):
        content = BoxLayout(orientation='vertical', spacing=20, padding=30)
        
        title_label = Label(
            text=f'🎥 {self.exercise_name}',
            font_size='20sp',
            color=CORES['texto'],
            bold=True,
            size_hint_y=0.2
        )
        
        info_label = Label(
            text='Escolha como assistir ao vídeo:',
            font_size='16sp',
            color=CORES['texto_secundario'],
            size_hint_y=0.2
        )
        
        buttons_container = BoxLayout(orientation='vertical', spacing=15, size_hint_y=0.6)
        
        btn_youtube = AnimatedButton(
            text='📱 Abrir no YouTube App',
            cor=CORES['erro'],
            size_hint_y=None,
            height='50dp'
        )
        btn_youtube.bind(on_press=lambda x: [self.open_youtube_app(x), popup.dismiss()])
        
        btn_browser = AnimatedButton(
            text='🌐 Abrir no Navegador',
            cor=CORES['secundaria'],
            size_hint_y=None,
            height='50dp'
        )
        btn_browser.bind(on_press=lambda x: [self.open_browser(x), popup.dismiss()])
        
        btn_copy = AnimatedButton(
            text='📋 Copiar Link',
            cor=CORES['aviso'],
            size_hint_y=None,
            height='50dp'
        )
        btn_copy.bind(on_press=lambda x: [self.show_url_popup(), popup.dismiss()])
        
        btn_fechar = AnimatedButton(
            text='❌ Fechar',
            cor=CORES['fundo_claro'],
            size_hint_y=None,
            height='50dp'
        )
        
        buttons_container.add_widget(btn_youtube)
        buttons_container.add_widget(btn_browser)
        buttons_container.add_widget(btn_copy)
        buttons_container.add_widget(btn_fechar)
        
        content.add_widget(title_label)
        content.add_widget(info_label)
        content.add_widget(buttons_container)
        
        popup = Popup(
            title='',
            content=content,
            size_hint=(0.8, 0.7),
            separator_height=0
        )
        
        btn_fechar.bind(on_press=popup.dismiss)
        popup.open()
    
    def show_url_popup(self):
        content = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        url_label = Label(
            text='Link do vídeo:',
            font_size='16sp',
            color=CORES['texto'],
            size_hint_y=0.2
        )
        
        url_input = TextInput(
            text=self.video_url,
            multiline=False,
            readonly=True,
            size_hint_y=0.4,
            font_size='14sp',
            background_color=CORES['fundo'],
            foreground_color=CORES['texto']
        )
        
        info_label = Label(
            text='Copie este link e cole no seu navegador ou app do YouTube',
            font_size='12sp',
            color=CORES['texto_secundario'],
            size_hint_y=0.2
        )
        
        btn_fechar = AnimatedButton(
            text='Fechar',
            size_hint_y=0.2,
            cor=CORES['primaria']
        )
        
        content.add_widget(url_label)
        content.add_widget(url_input)
        content.add_widget(info_label)
        content.add_widget(btn_fechar)
        
        popup = Popup(
            title='Link do Vídeo',
            content=content,
            size_hint=(0.8, 0.5)
        )
        
        btn_fechar.bind(on_press=popup.dismiss)
        popup.open()
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'menu'
        
        with self.canvas.before:
            Color(*CORES['fundo'])
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_bg, pos=self._update_bg)
        
        layout = FloatLayout()
        
        main_container = BoxLayout(
            orientation='vertical', 
            padding=[40, 60, 40, 60], 
            spacing=30,
            size_hint=(0.8, 0.8),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        title_container = BoxLayout(orientation='vertical', size_hint_y=0.3, spacing=10)
        
        title = Label(
            text='🏋️ PLANO HÍBRIDO',
            font_size='36sp',
            color=CORES['texto'],
            bold=True,
            halign='center'
        )
        title.bind(size=title.setter('text_size'))
        
        subtitle = Label(
            text='8 Semanas • Escoliose, Peso e Tonificação\n🎥 Com Vídeos do YouTube',
            font_size='18sp',
            color=CORES['texto_secundario'],
            halign='center'
        )
        subtitle.bind(size=subtitle.setter('text_size'))
        
        title_container.add_widget(title)
        title_container.add_widget(subtitle)
        
        buttons_container = BoxLayout(orientation='vertical', spacing=20, size_hint_y=0.7)
        
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
        
        for i, btn in enumerate([btn_semana, btn_exercicios, btn_progresso]):
            btn.opacity = 0
            anim = Animation(opacity=1, duration=0.5)
            Clock.schedule_once(lambda dt, b=btn, a=anim: a.start(b), i * 0.2)
        
        buttons_container.add_widget(btn_semana)
        buttons_container.add_widget(btn_exercicios)
        buttons_container.add_widget(btn_progresso)
        
        main_container.add_widget(title_container)
        main_container.add_widget(buttons_container)
        
        layout.add_widget(main_container)
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
        
        header = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=15)
        
        btn_voltar = AnimatedButton(
            text='← VOLTAR',
            size_hint_x=0.2,
            cor=CORES['erro']
        )
        btn_voltar.bind(on_press=self.voltar)
        
        semana_container = BoxLayout(orientation='vertical', size_hint_x=0.6, spacing=5)
        
        semana_controls = BoxLayout(orientation='horizontal', spacing=10)
        
        btn_semana_menos = AnimatedButton(
            text='◀',
            size_hint_x=0.15,
            cor=CORES['secundaria']
        )
        btn_semana_menos.bind(on_press=self.diminuir_semana)
        
        self.label_semana = Label(
            text=f'SEMANA {self.semana_atual}',
            size_hint_x=0.7,
            font_size='24sp',
            color=CORES['texto'],
            bold=True,
            halign='center'
        )
        self.label_semana.bind(size=self.label_semana.setter('text_size'))
        
        btn_semana_mais = AnimatedButton(
            text='▶',
            size_hint_x=0.15,
            cor=CORES['secundaria']
        )
        btn_semana_mais.bind(on_press=self.aumentar_semana)
        
        self.label_intensidade = Label(
            text=f'Intensidade: {int(self.progressao[self.semana_atual]*100)}%',
            font_size='16sp',
            color=CORES['texto_secundario'],
            halign='center'
        )
        self.label_intensidade.bind(size=self.label_intensidade.setter('text_size'))
        
        semana_controls.add_widget(btn_semana_menos)
        semana_controls.add_widget(self.label_semana)
        semana_controls.add_widget(btn_semana_mais)
        
        semana_container.add_widget(semana_controls)
        semana_container.add_widget(self.label_intensidade)
        
        header.add_widget(btn_voltar)
        header.add_widget(semana_container)
        header.add_widget(Label(size_hint_x=0.2))
        
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
            dia_container = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                spacing=10,
                padding=15
            )
            
            with dia_container.canvas.before:
                Color(*CORES['fundo_claro'])
                dia_container.bg_rect = RoundedRectangle(
                    size=dia_container.size, 
                    pos=dia_container.pos, 
                    radius=[10]
                )
            
            dia_container.bind(
                size=lambda instance, value: setattr(instance.bg_rect, 'size', instance.size),
                pos=lambda instance, value: setattr(instance.bg_rect, 'pos', instance.pos)
            )
            
            dia_label = Label(
                text=f'📆 {dia}',
                font_size='20sp',
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
                    
                    ex_container = BoxLayout(
                        orientation='horizontal',
                        size_hint_y=None,
                        height='120dp',
                        spacing=15
                    )
                    
                    # Encontrar dados do exercício
                    ex_data = next((e for e in EXERCICIOS_DATA if e["nome"] == ex["exercicio"]), None)
                    
                    if ex_data:
                        # Animação do exercício
                        ex_animation = ExerciseAnimation(
                            ex_data["tipo"],
                            size_hint_x=0.2,
                            size_hint_y=1
                        )
                        
                        # Informações do exercício
                        info_layout = BoxLayout(orientation='vertical', size_hint_x=0.35, spacing=5)
                        
                        ex_nome = Label(
                            text=ex["exercicio"],
                            font_size='16sp',
                            color=CORES['texto'],
                            bold=True,
                            halign='left',
                            size_hint_y=0.6
                        )
                        ex_nome.bind(size=ex_nome.setter('text_size'))
                        
                        ex_tempo = Label(
                            text=f'⏱️ {tempo_ajustado} segundos',
                            font_size='14sp',
                            color=CORES['texto_secundario'],
                            halign='left',
                            size_hint_y=0.4
                        )
                        ex_tempo.bind(size=ex_tempo.setter('text_size'))
                        
                        info_layout.add_widget(ex_nome)
                        info_layout.add_widget(ex_tempo)
                        
                        # Thumbnail do vídeo
                        video_thumb = VideoThumbnail(
                            ex_data["video"],
                            ex_data["video_id"],
                            ex_data["nome"],
                            size_hint_x=0.25
                        )
                        
                        # Botão iniciar
                        btn_iniciar = AnimatedButton(
                            text='▶ INICIAR',
                            size_hint_x=0.2,
                            cor=CORES['sucesso']
                        )
                        btn_iniciar.bind(on_press=lambda x, nome=ex["exercicio"], tempo=tempo_ajustado: self.iniciar_timer(nome, tempo))
                        
                        ex_container.add_widget(ex_animation)
                        ex_container.add_widget(info_layout)
                        ex_container.add_widget(video_thumb)
                        ex_container.add_widget(btn_iniciar)
                    
                    dia_container.add_widget(ex_container)
            else:
                descanso_container = BoxLayout(
                    orientation='horizontal',
                    size_hint_y=None,
                    height='60dp',
                    spacing=15
                )
                
                descanso_icon = Label(
                    text='🚶‍♀️',
                    font_size='32sp',
                    size_hint_x=0.15
                )
                
                descanso_label = Label(
                    text='Descanso ativo (caminhada leve ou alongamentos suaves)',
                    font_size='16sp',
                    color=CORES['texto_secundario'],
                    halign='left',
                    size_hint_x=0.85
                )
                descanso_label.bind(size=descanso_label.setter('text_size'))
                
                descanso_container.add_widget(descanso_icon)
                descanso_container.add_widget(descanso_label)
                dia_container.add_widget(descanso_container)
            
            altura_base = 60
            if exercicios:
                altura_base += len(exercicios) * 130
            else:
                altura_base += 70
            
            dia_container.height = altura_base
            self.exercicios_layout.add_widget(dia_container)
    
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
        self.label_semana.text = f'SEMANA {self.semana_atual}'
        self.label_intensidade.text = f'Intensidade: {int(self.progressao[self.semana_atual]*100)}%'
    
    def iniciar_timer(self, nome_exercicio, tempo):
        if self.timer_ativo:
            return
        
        self.timer_ativo = True
        self.tempo_restante = tempo
        
        content = FloatLayout()
        
        with content.canvas.before:
            Color(*CORES['fundo_claro'])
            content.bg_rect = RoundedRectangle(size=(400, 300), pos=(0, 0), radius=[20])
        
        main_container = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=30,
            size_hint=(1, 1)
        )
        
        self.timer_label = Label(
            text=nome_exercicio,
            font_size='24sp',
            color=CORES['texto'],
            bold=True,
            size_hint_y=0.2,
            halign='center'
        )
        self.timer_label.bind(size=self.timer_label.setter('text_size'))
        
        self.tempo_label = Label(
            text=f'{self.tempo_restante}s',
            font_size='48sp',
            color=CORES['primaria'],
            bold=True,
            size_hint_y=0.3,
            halign='center'
        )
        self.tempo_label.bind(size=self.tempo_label.setter('text_size'))
        
        progress_container = BoxLayout(orientation='vertical', size_hint_y=0.3, spacing=10)
        
        self.progress_bar = ProgressBar(
            max=tempo,
            value=0,
            size_hint_y=0.5
        )
        
        progress_label = Label(
            text='Progresso',
            font_size='14sp',
            color=CORES['texto_secundario'],
            size_hint_y=0.5
        )
        
        progress_container.add_widget(progress_label)
        progress_container.add_widget(self.progress_bar)
        
        btn_parar = AnimatedButton(
            text='⏹ PARAR',
            size_hint_y=0.2,
            cor=CORES['erro']
        )
        btn_parar.bind(on_press=self.parar_timer)
        
        main_container.add_widget(self.timer_label)
        main_container.add_widget(self.tempo_label)
        main_container.add_widget(progress_container)
        main_container.add_widget(btn_parar)
        
        content.add_widget(main_container)
        
        self.timer_popup = Popup(
            title='',
            content=content,
            size_hint=(0.6, 0.7),
            auto_dismiss=False,
            separator_height=0
        )
        
        self.timer_popup.open()
        
        self.timer_event = Clock.schedule_interval(lambda dt: self.atualizar_timer(nome_exercicio, tempo), 1)
    
    def atualizar_timer(self, nome_exercicio, tempo_total):
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.tempo_label.text = f'{self.tempo_restante}s'
            self.progress_bar.value = tempo_total - self.tempo_restante
            
            if self.tempo_restante <= 5:
                self.tempo_label.color = CORES['erro']
            elif self.tempo_restante <= 10:
                self.tempo_label.color = CORES['aviso']
            else:
                self.tempo_label.color = CORES['primaria']
            
            return True
        else:
            self.tempo_label.text = 'CONCLUÍDO!'
            self.tempo_label.color = CORES['sucesso']
            self.timer_label.text = f'{nome_exercicio} ✅'
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
class ExerciciosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'exercicios'
        
        with self.canvas.before:
            Color(*CORES['fundo'])
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_bg, pos=self._update_bg)
        self.build_layout()
    
    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def build_layout(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=15)
        
        btn_voltar = AnimatedButton(
            text='← VOLTAR',
            size_hint_x=0.2,
            cor=CORES['erro']
        )
        btn_voltar.bind(on_press=self.voltar)
        
        title = Label(
            text='🎥 EXERCÍCIOS COM VÍDEOS',
            font_size='24sp',
            color=CORES['texto'],
            bold=True
        )
        
        header.add_widget(btn_voltar)
        header.add_widget(title)
        header.add_widget(Label(size_hint_x=0.2))
        
        scroll = ScrollView()
        exercicios_layout = BoxLayout(orientation='vertical', spacing=20, size_hint_y=None)
        exercicios_layout.bind(minimum_height=exercicios_layout.setter('height'))
        
        for ex in EXERCICIOS_DATA:
            ex_container = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height='280dp',
                spacing=20,
                padding=20
            )
            
            with ex_container.canvas.before:
                Color(*CORES['fundo_claro'])
                ex_container.bg_rect = RoundedRectangle(
                    size=ex_container.size,
                    pos=ex_container.pos,
                    radius=[15]
                )
            
            ex_container.bind(
                size=lambda instance, value: setattr(instance.bg_rect, 'size', instance.size),
                pos=lambda instance, value: setattr(instance.bg_rect, 'pos', instance.pos)
            )
            
            # Lado esquerdo: Animação + Vídeo
            left_container = BoxLayout(orientation='vertical', size_hint_x=0.4, spacing=10)
            
            # Animação do exercício
            ex_animation = ExerciseAnimation(
                ex["tipo"],
                size_hint_y=0.5
            )
            
            # Thumbnail do vídeo
            video_thumb = VideoThumbnail(
                ex["video"],
                ex["video_id"],
                ex["nome"],
                size_hint_y=0.5
            )
            
            left_container.add_widget(ex_animation)
            left_container.add_widget(video_thumb)
            
            # Lado direito: Informações
            info_container = BoxLayout(orientation='vertical', size_hint_x=0.6, spacing=10)
            
            # Nome do exercício
            nome_label = Label(
                text=ex["nome"],
                font_size='20sp',
                size_hint_y=None,
                height='40dp',
                color=CORES['texto'],
                bold=True,
                halign='left'
            )
            nome_label.bind(size=nome_label.setter('text_size'))
            
            # Detalhes em scroll
            detalhes_scroll = ScrollView(size_hint_y=1)
            detalhes_layout = BoxLayout(orientation='vertical', spacing=8, size_hint_y=None)
            detalhes_layout.bind(minimum_height=detalhes_layout.setter('height'))
            
            # Objetivo
            objetivo_label = Label(
                text=f'🎯 OBJETIVO:\n{ex["objetivo"]}',
                font_size='14sp',
                color=CORES['texto'],
                halign='left',
                valign='top',
                size_hint_y=None,
                text_size=(None, None)
            )
            objetivo_label.bind(size=objetivo_label.setter('text_size'))
            
            # Execução
            execucao_label = Label(
                text=f'🧭 EXECUÇÃO:\n{ex["execucao"]}',
                font_size='14sp',
                color=CORES['texto_secundario'],
                halign='left',
                valign='top',
                size_hint_y=None,
                text_size=(None, None)
            )
            execucao_label.bind(size=execucao_label.setter('text_size'))
            
            # Séries
            series_label = Label(
                text=f'🔁 SÉRIES: {ex["series"]}',
                font_size='14sp',
                color=CORES['primaria'],
                halign='left',
                valign='top',
                size_hint_y=None,
                height='30dp'
            )
            series_label.bind(size=series_label.setter('text_size'))
            
            # Erros
            erros_label = Label(
                text=f'⚠️ ERROS A EVITAR:\n{ex["erros"]}',
                font_size='14sp',
                color=CORES['aviso'],
                halign='left',
                valign='top',
                size_hint_y=None,
                text_size=(None, None)
            )
            erros_label.bind(size=erros_label.setter('text_size'))
            
            # Calcular alturas
            for label in [objetivo_label, execucao_label, erros_label]:
                label.text_size = (300, None)
                label.height = label.texture_size[1] + 10
            
            detalhes_layout.add_widget(objetivo_label)
            detalhes_layout.add_widget(execucao_label)
            detalhes_layout.add_widget(series_label)
            detalhes_layout.add_widget(erros_label)
            
            detalhes_scroll.add_widget(detalhes_layout)
            
            info_container.add_widget(nome_label)
            info_container.add_widget(detalhes_scroll)
            
            ex_container.add_widget(left_container)
            ex_container.add_widget(info_container)
            
            exercicios_layout.add_widget(ex_container)
        
        scroll.add_widget(exercicios_layout)
        
        main_layout.add_widget(header)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
    
    def voltar(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'

class ProgressoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'progresso'
        
        with self.canvas.before:
            Color(*CORES['fundo'])
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_bg, pos=self._update_bg)
        
        self.progresso_data = self.carregar_progresso()
        self.build_layout()
    
    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def carregar_progresso(self):
        if os.path.exists("progresso.json"):
            with open("progresso.json", "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "Semana": 1,
            "Dias": {
                "Segunda-feira": {"Peso": "", "Notas": ""},
                "Quarta-feira": {"Peso": "", "Notas": ""},
                "Quinta-feira": {"Peso": "", "Notas": ""},
                "Sexta-feira": {"Peso": "", "Notas": ""}
            }
        }
    
    def salvar_progresso(self):
        with open("progresso.json", "w", encoding="utf-8") as f:
            json.dump(self.progresso_data, f, indent=4, ensure_ascii=False)
    
    def build_layout(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        header = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=15)
        
        btn_voltar = AnimatedButton(
            text='← VOLTAR',
            size_hint_x=0.2,
            cor=CORES['erro']
        )
        btn_voltar.bind(on_press=self.voltar)
        
        title = Label(
            text='📊 PROGRESSO & NOTAS',
            font_size='24sp',
            color=CORES['texto'],
            bold=True
        )
        
        header.add_widget(btn_voltar)
        header.add_widget(title)
        header.add_widget(Label(size_hint_x=0.2))
        
        scroll = ScrollView()
        progresso_layout = BoxLayout(orientation='vertical', spacing=20, size_hint_y=None)
        progresso_layout.bind(minimum_height=progresso_layout.setter('height'))
        
        for dia, dados in self.progresso_data["Dias"].items():
            dia_container = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height='200dp',
                spacing=15,
                padding=20
            )
            
            with dia_container.canvas.before:
                Color(*CORES['fundo_claro'])
                dia_container.bg_rect = RoundedRectangle(
                    size=dia_container.size,
                    pos=dia_container.pos,
                    radius=[15]
                )
            
            dia_container.bind(
                size=lambda instance, value: setattr(instance.bg_rect, 'size', instance.size),
                pos=lambda instance, value: setattr(instance.bg_rect, 'pos', instance.pos)
            )
            
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
            
            campos_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='120dp', spacing=20)
            
            peso_container = BoxLayout(orientation='vertical', size_hint_x=0.3, spacing=5)
            peso_label = Label(
                text='⚖️ Peso (kg)',
                font_size='14sp',
                color=CORES['texto_secundario'],
                size_hint_y=None,
                height='30dp'
            )
            
            peso_input = TextInput(
                text=dados["Peso"],
                multiline=False,
                size_hint_y=None,
                height='40dp',
                background_color=CORES['fundo'],
                foreground_color=CORES['texto'],
                cursor_color=CORES['primaria'],
                font_size='16sp'
            )
            peso_input.bind(text=lambda instance, value, d=dia: self.atualizar_peso(d, value))
            
            peso_container.add_widget(peso_label)
            peso_container.add_widget(peso_input)
            
            notas_container = BoxLayout(orientation='vertical', size_hint_x=0.7, spacing=5)
            notas_label = Label(
                text='📝 Notas do Treino',
                font_size='14sp',
                color=CORES['texto_secundario'],
                size_hint_y=None,
                height='30dp'
            )
            
            notas_input = TextInput(
                text=dados["Notas"],
                multiline=True,
                size_hint_y=None,
                height='80dp',
                background_color=CORES['fundo'],
                foreground_color=CORES['texto'],
                cursor_color=CORES['primaria'],
                font_size='14sp'
            )
            notas_input.bind(text=lambda instance, value, d=dia: self.atualizar_notas(d, value))
            
            notas_container.add_widget(notas_label)
            notas_container.add_widget(notas_input)
            
            campos_layout.add_widget(peso_container)
            campos_layout.add_widget(notas_container)
            
            dia_container.add_widget(dia_label)
            dia_container.add_widget(campos_layout)
            
            progresso_layout.add_widget(dia_container)
        
        btn_salvar = AnimatedButton(
            text='💾 SALVAR PROGRESSO',
            size_hint_y=None,
            height='60dp',
            cor=CORES['sucesso']
        )
        btn_salvar.bind(on_press=self.salvar_dados)
        
        progresso_layout.add_widget(btn_salvar)
        
        scroll.add_widget(progresso_layout)
        
        main_layout.add_widget(header)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
    
    def atualizar_peso(self, dia, valor):
        self.progresso_data["Dias"][dia]["Peso"] = valor
    
    def atualizar_notas(self, dia, valor):
        self.progresso_data["Dias"][dia]["Notas"] = valor
    
    def salvar_dados(self, instance):
        self.salvar_progresso()
        
        content = BoxLayout(orientation='vertical', spacing=20, padding=30)
        
        icon_label = Label(
            text='✅',
            font_size='48sp',
            size_hint_y=0.4
        )
        
        msg_label = Label(
            text='Progresso salvo com sucesso!',
            font_size='18sp',
            color=CORES['texto'],
            size_hint_y=0.6
        )
        
        content.add_widget(icon_label)
        content.add_widget(msg_label)
        
        popup = Popup(
            title='',
            content=content,
            size_hint=(0.4, 0.3),
            separator_height=0
        )
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 2)
    
    def voltar(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'

class ExercicioApp(App):
    def build(self):
        Window.clearcolor = CORES['fundo']
        
        sm = ScreenManager()
        sm.transition = SlideTransition()
        
        sm.add_widget(MenuScreen())
        sm.add_widget(SemanaScreen())
        sm.add_widget(ExerciciosScreen())
        sm.add_widget(ProgressoScreen())
        
        return sm

if __name__ == '__main__':
    ExercicioApp().run()