import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def create_token(user_id, role="user"):  # Dodano nowy parametr 'role'
    expiration = datetime.utcnow() + timedelta(minutes=30)  # Zmieniono czas ważności
    token = jwt.encode({"user_id": user_id, "role": role, "exp": expiration}, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"user_id": payload["user_id"], "role": payload.get("role", "user")}  # Zwraca teraz słownik
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

def is_token_valid(token):  # Dodano nową funkcję, która może powodować konflikt
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False
