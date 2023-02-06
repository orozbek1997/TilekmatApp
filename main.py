from kivymd.app import MDApp
from kivy.lang import Builder



class Authorization(MDApp):
    def build(self):
        Authorization_menu = """
#главная страница входа
MDScreen:
    md_bg_color: 'gray'
    MDBoxLayout:
        orientation: 'vertical'
        adaptive_size: True
        spacing: 9
        pos_hint: {'center_x': .5, 'center_y': .4}
        
        AnchorLayout:
            
            BoxLayout:
                orientation: 'vertical'
                spacing: 4
                MDTextFieldRect:
                    hint_text: 'Введите логин'
                    size_hint: 1.9, None
                    height: "30dp"
                    pos_hint: {'center_x': .5, 'center_y': .6}
                
                MDTextFieldRect:
                    hint_text: 'Введите пароль'
                    size_hint: 1.9, None
                    height: "30dp"
                    pos_hint: {'center_x': .5, 'center_y': 5}
    
        MDFillRoundFlatButton:
            text: "войти"
            #size_hint: (.1, .1)
            pos_hint: {'center_x': .5, 'center_y': .5}
        MDTextButton:
            text: "Зарегистрироваться"                       
            pos_hint: {'center_x': .5, 'center_y': .5}
            color: 'blue'
            font_size: 12
        MDTextButton:
            text: "Забыли пароль?"                       
            pos_hint: {'center_x': .5, 'center_y': .5}
            color: 'blue'
            font_size: 12
            
"""
        return Builder.load_string(Authorization_menu)


Authorization().run()