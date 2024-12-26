from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 10000

    MY_EMAIL: str
    EMAIL_PASSWORD: str
    
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    AWS_BUCKET: str

    PROJECT_NAME: str = "XpenseMeter Backend"

    class Config:
        env_file = ".env"

settings = Settings()