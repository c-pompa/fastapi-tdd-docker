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
    user = Users(firstname=payload.firstname, user="")
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