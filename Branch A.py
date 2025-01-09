SECRET_KEY = "nowy_tajny_klucz"

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return "Token wygasł"
    except jwt.InvalidTokenError:
        return "Token jest nieprawidłowy"
