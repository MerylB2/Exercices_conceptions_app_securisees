import secrets
import time

class SessionManager:
    def __init__(self):
        self.sessions = {}  # {token: {"username": str, "created_at": float}}
    
    def create_session(self, username):
        token = secrets.token_urlsafe(32)
        self.sessions[token] = {
            "username": username,
            "created_at": time.time()
        }
        return token
    
    def is_logged_in(self, token):
        return token in self.sessions
    
    def get_username(self, token):
        if self.is_logged_in(token):
            return self.sessions[token]["username"]
        return None
    
    def logout(self, token):
        if token in self.sessions:
            del self.sessions[token]

# Test
manager = SessionManager()

# Login
token = manager.create_session("admin")
print(f"Token créé: {token}")

# Vérification
print(f"Connecté? {manager.is_logged_in(token)}")  # True
print(f"Username: {manager.get_username(token)}")  # admin

# Logout
manager.logout(token)
print(f"Connecté après logout? {manager.is_logged_in(token)}")  # False