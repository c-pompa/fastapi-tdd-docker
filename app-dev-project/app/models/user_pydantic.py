from pydantic import AnyHttpUrl, BaseModel

class UserPayloadSchema(BaseModel):
    firstname = str
    lastname = str

    # items = fields.ForeignKeyRelation(model_name:='Item', related_name='owner' | None = None)
    # created_at = fields.DatetimeField(auto_now_add=True)


## Auth Classes
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str


# class UserResponseSchema(UserPayloadSchema):
#     id: int


# class UserUpdatePayloadSchema(UserPayloadSchema):
#     firstname: str