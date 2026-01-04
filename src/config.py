from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    MONGODB_USER : str 
    MONGODB_PASSWORD : str 
    model_config = SettingsConfigDict(env_file="../.env",extra="ignore")
 
CONFIG = Settings() 
