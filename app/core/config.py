# app/core/config.py

from pydantic import BaseSettings, EmailStr

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CSRF
    CSRF_SECRET: str

    # Email (if needed later)
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    EMAILS_FROM_EMAIL: EmailStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
