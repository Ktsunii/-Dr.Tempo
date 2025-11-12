from api_clients.auth_client import FirebaseAuthClient

class AuthService:
    def __init__(self, client: FirebaseAuthClient | None = None):
        self.client = client or FirebaseAuthClient()
        self._session = None

    def signup(self, email: str, password: str):
        data = self.client.sign_up(email, password)
        return self._save_session(data)

    def login(self, email: str, password: str):
        data = self.client.sign_in(email, password)
        return self._save_session(data)

    def reset_password(self, email: str):
        return self.client.send_password_reset(email)

    def delete_account(self):
        if not self._session:
            raise ValueError("Usuário não autenticado")
        return self.client.delete_account(self._session["idToken"])

    def current_user(self):
        return self._session

    def _save_session(self, data: dict):
        self._session = {
            "email": data.get("email"),
            "idToken": data.get("idToken"),
            "refreshToken": data.get("refreshToken"),
            "localId": data.get("localId"),
        }
        return self._session
