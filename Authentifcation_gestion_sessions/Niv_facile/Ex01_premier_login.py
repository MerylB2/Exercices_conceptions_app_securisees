# identifie les variables
def login(username, password):
    CREDENTIALS = {
        "username": "admin",
        "password": "password123"
    }

    if password == CREDENTIALS["password"] and username == CREDENTIALS["username"]:
        return {"status": "sucess", "message": "connexion reussie"}
    else:
        return {"status": "error", "message": "Echec de connexion"}
    
print(login("admin", "password123"))
print(login("admin", "wrong"))
print(login("user", "password123"))



