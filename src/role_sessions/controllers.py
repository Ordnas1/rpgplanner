from uuid import uuid4

from marshmallow import ValidationError
from flask import jsonify, request

from src import db
from .models import RoleSession, RoleSystem
from .schemas import (
    list_role_sessions_schema,
    list_role_system_schema,
    get_role_system_schema,
    role_system_data_schema,
)


def list_all_role_sessions_controller():
    sessions = RoleSession.query.all()
    return list_role_sessions_schema.dump(sessions)


def create_role_session_controller():
    request_form = request.json
    new_id = str(uuid4())
    new_session = RoleSession(
        id=new_id,
        name=request_form["name"],
        start_time=request_form["start_time"],
        end_time=request_form["end_time"],
    )

    db.session.add(new_session)
    db.session.commit()

    response = RoleSession.query.get(new_id).to_dict()
    return jsonify(response)


def retrieve_single_role_session(role_session_id):
    response = RoleSession.query.get(role_session_id).to_dict()
    return jsonify(response)


def list_all_role_systems_controller(user_id):
    return list_role_system_schema.dump(RoleSystem.query.filter_by(creator_id=user_id))


def retrieve_single_role_system_controller(role_system_id):
    return get_role_system_schema(RoleSystem.query.get(role_system_id))


def create_role_system_controller(user_id):
    request_data = request.get_json()

    try:
        result = role_system_data_schema.load(request_data)
    except ValidationError as err:
        return err.messages, 400
    new_system = RoleSystem(
        name=result["name"],
        description=result["description"],
        creator_id=user_id,
    )

    db.session.add(new_system)
    db.session.commit()

    return get_role_system_schema.dump(new_system)
