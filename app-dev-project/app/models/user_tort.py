from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

## we defined a new database model called User
class User(models.Model):
    firstname = fields.TextField()
    url = fields.TextField()
    lastname = fields.TextField()
    email = fields.TextField()
    hashed_password = fields.TextField()
    is_active = fields.BooleanField()
    is_superuser = fields.BooleanField()
    # items = fields.ForeignKeyRelation(model_name:='Item', related_name='owner' | None = None)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname


UserSchema = pydantic_model_creator(User)


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