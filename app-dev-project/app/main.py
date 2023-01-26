from fastapi.middleware.wsgi import WSGIMiddleware
from functools import lru_cache
import logging
import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api import ping, summaries
from app.db_app.init_db import init_db
from app.core.config import settings
from app.api.api_v1.api import api_router
from starlette.middleware.cors import CORSMiddleware
import sentry_sdk


log = logging.getLogger("uvicorn")

@lru_cache()
def create_application() -> FastAPI:
    application = FastAPI(openapi_url=f"{settings.API_V1_STR}/openapi.json")
    
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    
    
    application.include_router(ping.router)
    application.include_router(api_router, prefix=settings.API_V1_STR)
    # application.include_router(
    #     summaries.router, prefix="/summaries", tags=["summaries"]
    # )

    return application


app = create_application()



@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")




