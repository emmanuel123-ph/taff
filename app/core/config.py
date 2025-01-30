import os
from pydantic_settings import BaseSettings
from typing import Optional,Dict,Any
from pydantic import EmailStr, validator

# from pydantic import Base EmailStr,validator


def get_secret(secret_name, default):
    try:
        with open('/run/secrets/{0}'.format(secret_name), 'r') as secret_file:
            return secret_file.read().strip()
    except IOError:
        return os.getenv(secret_name, default)

class ConfigClass(BaseSettings):
    SECRET_KEY: str = get_secret("SECRET_KEY", 'H5zMm7XtCKNsab88JQCLkaY4d8hExSjghGyaJDy12M')
    ALGORITHM: str = get_secret("ALGORITHM", 'HS256')

    ADMIN_KEY: str = get_secret("ADMIN_KEY", "12346789abcdefghijklmnop")

    # 60 minutes * 24 hours * 355 days = 365 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(get_secret("ACCESS_TOKEN_EXPIRE_MINUTES", 30 * 24 * 365))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(get_secret("REFRESH_TOKEN_EXPIRE_MINUTES", 60 * 24 * 365))

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = get_secret("EMAIL_RESET_TOKEN_EXPIRE_HOURS", 8)

    # SQLALCHEMY_DATABASE_URL: str = get_secret("SQLALCHEMY_DATABASE_URL", 'postgresql://base_api_v2:Lcy96xP66EMBbrrr@dbe.comii.de:6020/sanctions_db_dev')
    SQLALCHEMY_DATABASE_URL: str = get_secret("SQLALCHEMY_DATABASE_URL", 'mysql+pymysql://root:@localhost:3306/testdb')

    SQLALCHEMY_POOL_SIZE: int = 100
    SQLALCHEMY_MAX_OVERFLOW: int = 0
    SQLALCHEMY_POOL_TIMEOUT: int = 30
    SQLALCHEMY_POOL_RECYCLE: int = get_secret("SQLALCHEMY_POOL_RECYCLE", 3600)
    SQLALCHEMY_ENGINE_OPTIONS: dict = {
        "pool_pre_ping": True,
        "pool_recycle": SQLALCHEMY_POOL_RECYCLE,
    }
    PREFERRED_LANGUAGE: str = get_secret("PREFERRED_LANGUAGE", 'fr')

    API_V1_STR: str = get_secret("API_V1_STR", "/api/v1")

    PROJECT_NAME: str = get_secret("PROJECT_NAME", "API FORMATION")
    PROJECT_VERSION: str = get_secret("PROJECT_VERSION", "0.0.1")

    # Redis config
    REDIS_HOST: str = get_secret("REDIS_HOST", "localhost")  # redis_develop
    REDIS_PORT: int = get_secret("REDIS_PORT", 6379)
    REDIS_DB: int = get_secret("REDIS_DB", 2)
    REDIS_CHARSET: str = get_secret("REDIS_CHARSET", "UTF-8")
    REDIS_DECODE_RESPONSES: bool = get_secret("REDIS_DECODE_RESPONSES", True)

    LOCAL: bool = os.getenv("LOCAL", True)

    class Config:
        case_sensitive = True


Config = ConfigClass()
