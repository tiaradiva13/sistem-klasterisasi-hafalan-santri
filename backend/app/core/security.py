
from passlib.context import CryptContext
from jose import jwt

SECRET_KEY="change_secret"
ALGORITHM="HS256"

pwd=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    return pwd.hash(password)

def verify_password(password, hashed):
    return pwd.verify(password, hashed)

def create_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
