import logging
import os
from enum import Enum
from functools import lru_cache
from typing import List, Optional, Tuple

from dotenv import load_dotenv

load_dotenv()


class EnvironmentEnum(str, Enum):
    production = "production"
    local = "local"
    devel = "devel"
    staging = "staging"


class GlobalConfig():
    title: str = "Redis API"
    description: str = "Api redis service"
    openapi_prefix: str ="/api/v1"
    docs_url: str = "/docs"
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    version: str = "1.0.0"
    max_connection_count: int = 10
    min_connection_count: int = 10
    api_prefix: str = "/api"
    allowed_hosts: List[str] = ["*"]
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")
    debug: bool = False
    testing: bool = False
    timezone: str = "UTC"
    environment: EnvironmentEnum

    redis_host: str = os.environ.get("REDIS_HOST")
    redis_port: int = os.environ.get("REDIS_PORT")


class LocalConfig(GlobalConfig):
    """Local configurations."""

    debug: bool = True
    environment: EnvironmentEnum = EnvironmentEnum.local


class DevelConfig(GlobalConfig):
    """Devel configurations."""

    debug: bool = True
    environment: EnvironmentEnum = EnvironmentEnum.devel


class StagingConfig(GlobalConfig):
    """Staging configurations."""

    debug: bool = True
    environment: EnvironmentEnum = EnvironmentEnum.staging


class ProdConfig(GlobalConfig):
    """Production configurations."""

    debug: bool = False
    environment: EnvironmentEnum = EnvironmentEnum.production


class FactoryConfig:
    def __init__(self, environment: Optional[str]):
        self.environment = environment
        self.configurations_maps = {
            EnvironmentEnum.local.value: LocalConfig,
            EnvironmentEnum.devel.value: DevelConfig,
            EnvironmentEnum.staging.value: StagingConfig,
            EnvironmentEnum.production.value: ProdConfig,
        }

    def __call__(self) -> GlobalConfig:
        return self.configurations_maps[self.environment]()


@lru_cache()
def get_configuration() -> GlobalConfig:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    return FactoryConfig(os.environ.get("ENVIRONMENT"))()


settings = get_configuration()

if settings.environment != EnvironmentEnum.production.value:
    print(f"Loaded config {settings.environment} !!")
