from uuid import uuid4

from flask import jsonify, request

from .models import RoleSession
from src import db


def list_all_role_sessions_controller():
    sessions = RoleSession.query.all()
    response = []
    for session in sessions:
        response.append(session.to_dict())
    return jsonify(response)


def create_role_session_controller():
    request_form = request.json
    new_id = str(uuid4())
    new_session = RoleSession(
        id=new_id,
        name=request_form['name'],
        start_time=request_form['start_time'],
        end_time=request_form['end_time'],
    )
    print(request_form, new_session)
    db.session.add(new_session)
    db.session.commit()

    response = RoleSession.query.get(new_id).to_dict()
    return jsonify(response)


def retrieve_single_role_session(role_session_id):
    response = RoleSession.query.get(role_session_id).to_dict()
    return jsonify(response)
