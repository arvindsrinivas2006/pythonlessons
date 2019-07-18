from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from WelcomeScreen import WelcomeScreen

class TacocalculatorApp(App):
    screen_manager=ScreenManager()
    def build (self):
        welcome_screen=WelcomeScreen(name="WelcomeScreen")

        self.screen_manager.add_widget(welcome_screen)

        return self.screen_manager