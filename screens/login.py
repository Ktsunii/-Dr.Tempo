from kivy.uix.screenmanager import Screen
from services.auth_service import AuthService

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auth = AuthService()

    def do_login(self, email, password):
        try:
            if not email or "@" not in email:
                self.ids.login_msg.text = "Email inválido"
                return
            if not password or len(password) < 6:
                self.ids.login_msg.text = "Senha deve ter 6+ caracteres"
                return
            self.ids.login_msg.text = "Entrando..."
            self.auth.login(email, password)
            self.manager.current = "home"
        except Exception as e:
            self.ids.login_msg.text = f"Falha no login: {e}"

    def go_register(self):
        self.manager.current = "register"

    def go_reset(self, email):
        try:
            if not email:
                self.ids.login_msg.text = "Informe seu email"
                return
            self.auth.reset_password(email)
            self.ids.login_msg.text = "Email de recuperação enviado"
        except Exception as e:
            self.ids.login_msg.text = f"Erro: {e}"
