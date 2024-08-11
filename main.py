from fastapi import FastAPI

from api.router import router
from core.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.title,
        description=settings.description,
        version=settings.version,
        debug=settings.debug,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        openapi_url=settings.openapi_url,
        openapi_prefix=settings.openapi_prefix,
    )

    application.include_router(router, prefix=settings.api_prefix)

    return application


app = get_application()


@app.get("/")
def read_root():
    return {"Service": "FastaAPI with Redis"}
