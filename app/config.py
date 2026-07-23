from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Makkah & Umra"
    debug: bool = True
    # Standart holatda SQLite bilan ishga tushadi, .env orqali PostgreSQL'ga o'tkazish mumkin
    database_url: str = "sqlite:///./makkah.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
