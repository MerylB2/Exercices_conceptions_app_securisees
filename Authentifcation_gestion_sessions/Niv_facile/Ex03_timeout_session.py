import secrets
import time

class SessionManagerWithTimeout:
    def __init__(self, timeout=300):  # 5 minutes = 300 secondes
        self.sessions = {}
        self.timeout = timeout
    
    def create_session(self, username):
        token = secrets.token_urlsafe(32)
        self.sessions[token] = {
            "username": username,
            "created_at": time.time(),
            "last_activity": time.time()
        }
        return token
    
    def is_logged_in(self, token):
        if token not in self.sessions:
            return False
        
        session = self.sessions[token]
        if time.time() - session["last_activity"] > self.timeout:
            del self.sessions[token]  # Session expirée
            return False
        
        # Mise à jour de l'activité
        session["last_activity"] = time.time()
        return True
    
    def cleanup_expired_sessions(self):
        """Nettoie toutes les sessions expirées"""
        current_time = time.time()
        expired_tokens = [
            token for token, session in self.sessions.items()
            if current_time - session["last_activity"] > self.timeout
        ]
        for token in expired_tokens:
            del self.sessions[token]
        return len(expired_tokens)

# Test
manager = SessionManagerWithTimeout(timeout=5)  # 5 secondes pour test

token1 = manager.create_session("user1")
token2 = manager.create_session("user2")

print(f"Sessions actives: {len(manager.sessions)}")
print(f"Token1 valide? {manager.is_logged_in(token1)}")

# Attendre expiration
time.sleep(6)

print(f"Token1 valide après 6s? {manager.is_logged_in(token1)}")  # False
print(f"Sessions nettoyées: {manager.cleanup_expired_sessions()}")