from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI API Service"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    
    # API Key for an external LLM provider. If empty, the service will return mock data.
    LLM_API_KEY: str = ""
    
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
