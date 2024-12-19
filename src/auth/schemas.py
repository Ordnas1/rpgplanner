from marshmallow.validate import Email, Length
from src.auth.models import User
from src import ma


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field(validate=Length(min=8))
    email = ma.auto_field(validate=Email())
    nickname = ma.auto_field()


list_user_schema = UserSchema(exclude=["password", "username"])
create_user_schema = UserSchema(exclude=["id"])
