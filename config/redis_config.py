from pydantic_settings import BaseSettings, SettingsConfigDict

class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', 
        env_prefix='REDIS_',
        extra='ignore'
        )

    host: str
    port: int
    db: int
    password: str | None = None

settings = RedisSettings()