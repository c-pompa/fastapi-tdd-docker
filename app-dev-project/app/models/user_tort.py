##  Need to update tortoise libraies here

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

## we defined a new database model called User
class Users(models.Model):
    id = fields.IntField(pk=True)
    firstname = fields.CharField(max_length=30)
    lastname = fields.CharField(max_length=30)
    email = fields.CharField(max_length=30, null=True)
    url = fields.CharField(max_length=30, null=True)
    # hashed_password = fields.CharField(max_length=128, null=True)
    # is_active = fields.BooleanField()
    # is_superuser = fields.BooleanField()
    # items = fields.ForeignKeyRelation(model_name:='Item', related_name='owner' | None = None)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname


UserSchema = pydantic_model_creator(Users, name="User")
UserIn_Schema = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)


# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


# class User(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     full_name = Column(String, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     is_active = Column(Boolean(), default=True)
#     is_superuser = Column(Boolean(), default=False)
#     items = relationship("Item", back_populates="owner")