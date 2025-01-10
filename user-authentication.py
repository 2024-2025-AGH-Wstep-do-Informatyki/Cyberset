import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def create_token(user_id):  # Usunięto parametr 'role' z poprzedniej wersji
    expiration = datetime.utcnow() + timedelta(hours=2)  # Zmieniono czas ważności na 2 godziny
    token = jwt.encode({"user_id": user_id, "exp": expiration}, SECRET_KEY, algorithm="HS256")
    return {"token": token, "expires_at": expiration.isoformat()}  # Zwracana wartość to teraz słownik

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        # Dodano dodatkowe sprawdzanie czasu ważności
        if datetime.utcnow() > datetime.fromtimestamp(payload["exp"]):
            return "Token manually expired"
        return payload

    except jwt.ExpiredSignatureError:
        raise ValueError("Token expired")  # Zmieniono sposób obsługi błędu
    except jwt.InvalidTokenError as e:
        return f"Invalid token: {str(e)}"  # Dodano więcej szczegółów do błędu
      
def refresh_token(token):  # Nowa funkcja do odświeżania tokena
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], options={"verify_exp": False})
        new_expiration = datetime.utcnow() + timedelta(hours=1)
        payload["exp"] = new_expiration
        new_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return {"token": new_token, "expires_at": new_expiration.isoformat()}
    except jwt.InvalidTokenError:

        return "Cannot refresh invalid token"

