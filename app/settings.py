from pydantic.v1 import BaseSettings


class WebAppSettings(BaseSettings):
    class Config:
        env_file = "local.env"
