from kivy.uix.screenmanager import Screen
from services.auth_service import AuthService

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auth = AuthService()

    def do_register(self, email, password, confirm):
        try:
            if not email or "@" not in email:
                self.ids.reg_msg.text = "Email inválido"
                return
            if len(password) < 6:
                self.ids.reg_msg.text = "Senha deve ter 6+ caracteres"
                return
            if password != confirm:
                self.ids.reg_msg.text = "Senhas não conferem"
                return
            self.ids.reg_msg.text = "Criando conta..."
            self.auth.signup(email, password)
            self.manager.current = "home"
        except Exception as e:
            self.ids.reg_msg.text = f"Falha no cadastro: {e}"
