from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Rise Nest Solutions (RNS) API"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite+aiosqlite:///./rns.db"
    ADMIN_API_KEY: str = "rns-admin-secret-2026"
    CORS_ORIGINS: list[str] = ["http://127.0.0.1:8001", "http://localhost:8001"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
