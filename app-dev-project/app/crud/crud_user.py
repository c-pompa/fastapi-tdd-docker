from typing import List, Union

from app.models.user_pydantic import UserPayloadSchema
from app.models.user_tort import Users  

# async def post(payload: UserPayloadSchema) -> int:
#     user = Users(firstname=payload.firstname, lastname=payload.lastname)
#     await user.save()
#     return user.id


# async def put(id: int, payload: UserPayloadSchema) -> Union[dict, None]:
#     user = await Users.filter(id=id).update(
#         firstname=payload.firstname, lastname=payload.lastname
#     )
#     if user:
#         updated_user = await Users.filter(id=id).first().values()
#         return updated_user
#     return None


# async def delete(id: int) -> int:
#     user = await Users.filter(id=id).first().delete()
#     return 


# async def get(id: int) -> Union[dict, None]:
#     user = await Users.filter(id=id).first().values()
#     if user:
#         return user
#     return None


 
# async def get_all() -> List:
#     user = await Users.from_queryset(Users.all())
#     return user



##  GET ALL 
async def get_all() -> List:
    summaries = await Users.all().values()
    return summaries

##  GET One
async def get(id: int) -> Union[dict, None]:
    user = await Users.filter(id=id).first().values()
    if user:
        return user
    return None

##  POST One: user
async def post(payload: UserPayloadSchema) -> int:
    user = Users(firstname=payload.firstname, lastname=payload.lastname)
    await user.save()
    return user.id

##  POST Multiple: user
async def put(id: int, payload: UserPayloadSchema) -> Union[dict, None]:
    user = await Users.filter(id=id).update(
        firstname=payload.firstname 
    )
    if user:
        updated_user = await Users.filter(id=id).first().values()
        return updated_user
    return None


async def delete(id: int) -> int:
    user = await Users.filter(id=id).first().delete()
    return user





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
#     current_user: Users = Security(get_current_user, scopes=["me"])
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
