SECRET_KEY = "your_secret_key"

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return "The token has expired"
    except jwt.InvalidTokenError:
        return "This token is invalid"
