from passlib.context import CryptContext
import hashlib


pwd = CryptContext(schemes= ["argon2"], deprecated = "auto")

def hash_password(password: str):
    return pwd.hash(password)

def verify_password(plain, hash):
    return pwd.verify(plain, hash)

def hash_token(token: str):
    return hashlib.sha256(token.encode()).hexdigest()
