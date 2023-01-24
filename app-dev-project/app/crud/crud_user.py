from typing import List, Union

from app.models.user_pydantic import UserPayloadSchema
from app.models.user_tort import UserSchema  


async def post(payload: UserPayloadSchema) -> int:
    user = UserSchema(first_name=payload.firstname, last_name=payload.lastname)
    await user.save()
    return user.id


async def put(id: int, payload: UserPayloadSchema) -> Union[dict, None]:
    user = await UserSchema.filter(id=id).update(
        first_name=payload.firstname, last_name=payload.lastname
    )
    if user:
        updated_user = await UserSchema.filter(id=id).first().values()
        return updated_user
    return None

