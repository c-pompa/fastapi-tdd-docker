

# import logging
# # import os
# from datetime import datetime, timedelta
# from enum import Enum
# from typing import List, Union

# from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.middleware.wsgi import WSGIMiddleware
# from fastapi.security import (
#     OAuth2PasswordBearer,
#     OAuth2PasswordRequestForm,
#     SecurityScopes,
# )
# from flask import Flask, escape, request
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from pydantic import BaseModel, ValidationError


# from app.api import ping, summaries
# from app.config import Settings, get_settings
# from app.db import init_db

import logging
import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api import ping, summaries
from app.db import init_db

log = logging.getLogger("uvicorn")


# flask_app = Flask(__name__)



def create_application() -> FastAPI:
    
    application = FastAPI()

    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
        )

    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_application()
# app.mount("/v1", WSGIMiddleware(flask_app))


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")






# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "REPLACE_WITH_OPENSSL_HEX_KEY" 
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # Create a utility function to hash a password coming from the user.
# # And another utility to verify if a received password matches the hash stored.
# # And another one to authenticate and return a user.
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "$2b$12$gSvqqUPvlXP2tfVFaWK1Be7DlH.PKZbv5H8KnzzVgXXbVxpva.pFm",
#         "disabled": True,
#     },
# }


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: Union[str, None] = None
#     scopes: List[str] = []


# #  Model: User
# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password: str

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="token",
#     scopes={"me": "Read information about the current user.", "items": "Read items."},
# )

# ###################################################################################
# #  Flask App Execute. Front End
# @flask_app.route("/")
# def flask_main():
#     name = request.args.get("name", "chris")
#     return f"Hello, {escape(name)} from Flask!"

# ###################################################################################

# ###################################################################################
# #  FastAPI App Execute. Back End
# app = FastAPI()
# ###################################################################################

# @app.get("/v2")
# def read_main():
#     return {"message": "Hello World"}


# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# ## Model: Custom Names
# class reportNames(str, Enum):
#     balancesheet = "balancesheet"
#     incomestatement = "incomestatement"
#     lenet = "lenet"


# async def get_current_user(
#     security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
# ):
#     if security_scopes.scopes:
#         authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
#     else:
#         authenticate_value = "Bearer"
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": authenticate_value},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_scopes = payload.get("scopes", [])
#         token_data = TokenData(scopes=token_scopes, username=username)
#     except (JWTError, ValidationError):
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     for scope in security_scopes.scopes:
#         if scope not in token_data.scopes:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Not enough permissions",
#                 headers={"WWW-Authenticate": authenticate_value},
#             )
#     return user


# async def get_current_active_user(
#     current_user: User = Security(get_current_user, scopes=["me"])
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# ##################################################################
# #  ROUTES
# ##################################################################

# #  Default: Root
# #  To Do: show all api routes, user login, reports to access
# @app.get("/")
# async def root(settings: Settings = Depends(get_settings)):
#     return {
#         "Home Page Text": "Displaying home page.",
#         "environment": settings.environment,
#         "testing": settings.testing,
#     }
#     # return render_template("index.html", info=information_data)


# ####################################################################
# #  Tests stuff - delete

# def create_application() -> FastAPI:
#     application = FastAPI()
#     application.include_router(ping.router)
#     application.include_router(
#         summaries.router, prefix="/summaries", tags=["summaries"]
#     )  # new

#     return application

# ####################################################################

# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username, "scopes": form_data.scopes},
#         expires_delta=access_token_expires,
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# ## Get User -> Me
# @app.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: User = Security(get_current_active_user, scopes=["items"])
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]


# # @app.get("/items/")
# # async def read_items(token: str = Depends(oauth2_scheme)):
# #     return {"token": token}


# @app.get("/status/")
# async def read_system_status(current_user: User = Depends(get_current_user)):
#     return {"status": "ok"}


# ## Default get_model
# @app.get("/reports/{report_name}")
# async def get_model(report_name: reportNames):
#     if report_name is reportNames.balancesheet:
#         return {
#             "report_name": report_name,
#             "message": "Balance Sheet Reporting information will be sent.",
#         }

#     if report_name.value == "incomestatement":
#         return {
#             "report_name": report_name,
#             "message": "Income Statment Reporting information will be sent.",
#         }

#     return {"report_name": report_name, "message": "Have some residuals"}


# ## User logged in, Select report name, Year optional (default return all years)
# @app.get("/users/{user_id}/reports/{report_name}/{year_}")
# async def get_model(
#     user_id: int,
#     report_name: reportNames,
#     year: str | None = None,
#     update: bool = False,
# ):
#     item = {"report_name": report_name, "owner_id": user_id, "year": year}

#     if report_name is reportNames.balancesheet and update is not False:
#         item.update({"description": "balancesheet has been updated."})
#     elif (
#         report_name is reportNames.incomestatement
#         and update is not False
#         and year is not None
#     ):
#         item.update({"description": year + " Incomestatement has been updated."})
#     elif report_name is reportNames.incomestatement and update is not False:
#         item.update({"description": "Incomestatement has been updated."})
#     elif not update:
#         item.update({"description": "Report not updated. Displaying current results."})
#     return item


# app.mount("/v1", WSGIMiddleware(flask_app))

# app = create_application()
