# from typing import List, Union

# from app.models.pydantic import UserPayloadSchema
# from app.models.tortoise import TextSummary


# async def post(payload: UserPayloadSchema) -> int:
#     summary = TextSummary(url=payload.url, summary=payload.user)
#     await summary.save()
#     return summary.id


# async def put(id: int, payload: UserPayloadSchema) -> Union[dict, None]:
#     summary = await TextSummary.filter(id=id).update(
#         url=payload.url, summary=payload.summary
#     )
#     if summary:
#         updated_summary = await TextSummary.filter(id=id).first().values()
#         return updated_summary
#     return None


# async def delete(id: int) -> int:
#     summary = await TextSummary.filter(id=id).first().delete()
#     return 


# async def get(id: int) -> Union[dict, None]:
#     summary = await TextSummary.filter(id=id).first().values()
#     if summary:
#         return summary
#     return None


# ## 3. Add the CRUD util
# async def get_all() -> List:
#     summaries = await TextSummary.all().values()
#     return summaries
