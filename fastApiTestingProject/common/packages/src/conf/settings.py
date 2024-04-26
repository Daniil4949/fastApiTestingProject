"""Common settings module."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    """Common postgres settings."""

    driver: str = ""
    user: str = "postgres"
    password: str = "postgres"
    db: str = "postgres"
    host: str = "0.0.0.0"
    echo: bool = False

    @property
    def db_uri(self) -> str:
        """Return database uri."""
        return f"{self.driver}://{self.user}:{self.password}@{self.host}/{self.db}"

    model_config = SettingsConfigDict(extra='allow', env_prefix="POSTGRES_", env_file=[".env"])


class NotesService(BaseSettings):
    """Merch settings class."""

    host: str
    port: str
    secret_key: str
    name: str
    version: str
    description: str

    model_config = SettingsConfigDict(extra='allow', env_prefix="NOTES_APP_", env_file=[".env"])


class Settings(BaseSettings):
    notes_app: NotesService = NotesService()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
