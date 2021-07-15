from typing import List
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./sql_app.db"
    # Security
    SECRET_KEY = "3e7fbb1509a651e69f6804eaa7cefd5c8dfa6059c5a25034fe9ce683fcc0c838"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SIGNING_ALGORITHM = "HS256"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:3000/",
        "http://localhost:3000",
    ]


settings = Settings()
