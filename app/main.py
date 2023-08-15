import uvicorn
from fastapi import FastAPI
from routers.routers import api_router
from settings import WebAppSettings

SERVICE_NAME = "aa_template"


def create_app() -> FastAPI:
    app = FastAPI(
        title=SERVICE_NAME,
    )
    app.include_router(api_router)

    return app


if __name__ == "__main__":
    settings_ = WebAppSettings()

    app_ = create_app()
    uvicorn.run(app_, host="localhost", port=8000, log_config=None)
