from pydantic_settings import BaseSettings, SettingsConfigDict
import os

print("DEBUG os.getenv =", os.getenv("DATABASE_URL"))


class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

print("DEBUG settings =", settings.database_url)