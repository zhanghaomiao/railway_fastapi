import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/fastapi_db")
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Railway Demo")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings() 