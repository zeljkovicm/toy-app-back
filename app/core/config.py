from pathlib import Path
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(
        ENV_FILE), case_sensitive=False, extra="ignore")

    db_scheme: str = "postgresql+psycopg"
    db_host: str = ""
    db_port: int = 5432
    db_user: str = ""
    db_password: str = ""
    db_name: str = ""

    def database_uri(self) -> str:
        return PostgresDsn.build(
            scheme=self.db_scheme,
            host=self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_password,
            path=self.db_name
        )


class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(
        ENV_FILE), case_sensitive=False, extra="ignore")

    jwt_secret_key: str = "CHANGE ME"
    jwt_algorithm: str = "HS256"
    jwt_access_expiration_minutes: int = 0
    jwt_refresh_expiration_minutes: int = 0


class AppSettings:
    db_settings: DBSettings = DBSettings()
    jwt_settings: JWTSettings = JWTSettings()


settings: AppSettings = AppSettings()
