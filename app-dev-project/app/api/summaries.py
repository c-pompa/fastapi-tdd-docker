# project/app/api/summaries.py
"""
Here, we defined a handler that expects a payload, payload: SummaryPayloadSchema, with a URL.

Essentially, when the route is hit with a POST request, FastAPI will read the body of the request and validate the data:

    If valid, the data will be available in the payload parameter. FastAPI also generates JSON Schema definitions that are then used to automatically generate the OpenAPI schema and the API documentation.
    If invalid, an error is immediately returned.

It's worth noting that we used the async declaration here since the database communication will be asynchronous. In other words, there are no blocking I/O operations in the handler.
"""
from typing import List

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {"id": summary_id, "url": payload.url}
    return response_object


## 2. Update [Summaries] in /api
@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()


