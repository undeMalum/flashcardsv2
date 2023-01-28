from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_app = MDApp.get_running_app()

    def change_theme(self):
        """
        Function to switch between light and dark theme
        """
        print(self.main_app.CURRENT_THEME)
        print(self.main_app.CURRENT_PRIMARY)
        print(self.main_app.CURRENT_ACCENT)
        print(self.main_app.PRIMARY_HUE)
        if self.main_app.CURRENT_THEME == "Light":
            self.main_app.CURRENT_THEME = "Dark"
            self.main_app.CURRENT_PRIMARY = "Green"
            self.main_app.CURRENT_ACCENT = "Green"
            self.main_app.PRIMARY_HUE = "A200"
        else:
            self.main_app.CURRENT_THEME = "Light"
            self.main_app.CURRENT_PRIMARY = "Red"
            self.main_app.CURRENT_ACCENT = "Red"
            self.main_app.PRIMARY_HUE = "A200"

    def create_account(self):
        """
        Function take user to create account screen.
        """
        self.manager.current = "create_screen"

    def go_to_login(self):
        """
        Function will take user to login screen
        """
        self.manager.current = "login_screen"


kv_startscreen = """
<StartScreen>
    FloatLayout:
        MDFillRoundFlatButton:
            text: "change theme"
            font_size: 20
            pos_hint: {'center_x': .2, 'center_y': .9}
            size_hint: .35, .07
            on_press: root.change_theme()
        MDLabel:
            text: "kv Flashcards"
            halign: 'center'
            font_size: 56
            pos_hint:{'center_x': .5, 'center_y': .65}
        MDFillRoundFlatButton:
            on_press: root.create_account()
            text: "Create Account"
            font_size: 24
            size_hint: .4, .1
            pos_hint: {'center_x': .5, 'center_y': .45}
        MDFillRoundFlatButton:
            on_press: root.go_to_login()
            text: "Login"
            font_size: 24
            pos_hint: {'center_x': .5, 'center_y': .3}
            size_hint: .4, .1
"""
