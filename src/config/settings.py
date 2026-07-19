'''Settings configuration module for user service.'''

from pydantic_settings import BaseSettings, SettingsConfigDict

class FinBudUserSettings(BaseSettings):
    pass

user_settings = FinBudUserSettings()
