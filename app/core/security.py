# app/core/security.py

from passlib.context import CryptContext
from itsdangerous import URLSafeTimedSerializer, BadSignature
from datetime import datetime

from app.core.config import settings

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# CSRF token generation & verification
serializer = URLSafeTimedSerializer(settings.CSRF_SECRET)

def generate_csrf_token(data: str) -> str:
    """Generate a signed CSRF token containing `data` (e.g., session ID)."""
    return serializer.dumps(data)

def verify_csrf_token(token: str, max_age: int = 3600) -> str:
    """Return the original data if token is valid and not older than max_age seconds."""
    try:
        return serializer.loads(token, max_age=max_age)
    except BadSignature:
        return None
