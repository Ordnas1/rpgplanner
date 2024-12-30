from marshmallow_sqlalchemy.fields import Nested

from src.role_sessions.models import RoleSession, RoleSystem, Player
from src import ma


class RoleSystemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RoleSystem


class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player


class RoleSessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RoleSession

    role_system = Nested(RoleSystemSchema, exclude=("created_on", "updated_on"))
    players = Nested(PlayerSchema, many=True, exclude=("created_on", "updated_on"))


list_role_sessions_schema = RoleSessionSchema(many=True)
get_role_session_schema = RoleSessionSchema()


list_role_system_schema = RoleSystemSchema(many=True)
get_role_system_schema = RoleSystemSchema()
role_system_data_schema = RoleSystemSchema(only=("name", "description"))
