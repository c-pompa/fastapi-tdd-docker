# from sqlalchemy.orm import Session
import logging 
import os

# from app import crud, schemas
# from app.core.config import settings
# from app.db import base  # noqa: F401

from fastapi import FastAPI
from tortoise import Tortoise, run_async 
from tortoise.contrib.fastapi import register_tortoise
# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


# def init_db(db: Session) -> None:
#     # Tables should be created with Alembic migrations
#     # But if you don't want to use migrations, create
#     # the tables un-commenting the next line
#     # Base.metadata.create_all(bind=engine)

#     user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
#     if not user:
#         user_in = schemas.UserCreate(
#             email=settings.FIRST_SUPERUSER,
#             password=settings.FIRST_SUPERUSER_PASSWORD,
#             is_superuser=True,
#         )
#         user = crud.user.create(db, obj_in=user_in)  # noqa: F841

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.user_tort", "app.models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}



log = logging.getLogger("uvicorn")  
def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.user_tort","app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models.user_tort","models.tortoise"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())

