import os, requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("FIREBASE_API_KEY")
BASE = "https://identitytoolkit.googleapis.com/v1"

class FirebaseAuthClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or API_KEY
        if not self.api_key:
            raise ValueError("FIREBASE_API_KEY não configurada (.env)")

    def sign_up(self, email: str, password: str):
        url = f"{BASE}/accounts:signUp?key={self.api_key}"
        r = requests.post(url, json={"email": email, "password": password, "returnSecureToken": True}, timeout=15)
        r.raise_for_status()
        return r.json()

    def sign_in(self, email: str, password: str):
        url = f"{BASE}/accounts:signInWithPassword?key={self.api_key}"
        r = requests.post(url, json={"email": email, "password": password, "returnSecureToken": True}, timeout=15)
        r.raise_for_status()
        return r.json()

    def send_password_reset(self, email: str):
        url = f"{BASE}/accounts:sendOobCode?key={self.api_key}"
        r = requests.post(url, json={"requestType": "PASSWORD_RESET", "email": email}, timeout=15)
        r.raise_for_status()
        return r.json()

    def delete_account(self, id_token: str):
        url = f"{BASE}/accounts:delete?key={self.api_key}"
        r = requests.post(url, json={"idToken": id_token}, timeout=15)
        r.raise_for_status()
        return r.json()
