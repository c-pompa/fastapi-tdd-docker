from pydantic import AnyHttpUrl, BaseModel

class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl
    summary: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str