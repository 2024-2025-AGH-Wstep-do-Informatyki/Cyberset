import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def create_token(user_id):
    expiration = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode({"user_id": user_id, "exp": expiration}, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
