from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class ApiConfig(BaseModel):
    key: str = os.getenv("API_KEY", default="")

class Settings(BaseSettings):
    api: ApiConfig = ApiConfig()
    # model_config = SettingsConfigDict(env_file=".env")


settings = Settings()