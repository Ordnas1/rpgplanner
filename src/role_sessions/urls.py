from flask import request, Blueprint
from flask_jwt_extended import jwt_required, current_user

from . import controllers

role_sessions = Blueprint("role_sessions", __name__, url_prefix="/role_sessions")
role_systems = Blueprint("role_systems", __name__, url_prefix="/role_system")


@role_sessions.route("/", methods=["GET", "POST"])
@jwt_required()
def list_create_role_session():
    if request.method == "GET":
        return controllers.list_all_role_sessions_controller()
    if request.method == "POST":
        return controllers.create_role_session_controller()
    return "Method not allowed"


@role_sessions.route("/<role_session_id>", methods=["GET"])
@jwt_required()
def retrieve_role_sessions(role_session_id):
    if request.method == "GET":
        return controllers.retrieve_single_role_session(role_session_id)
    return "Method not allowed"


@role_systems.route("/", methods=["GET", "POST"])
@jwt_required()
def list_create_role_system():
    if request.method == "GET":
        return controllers.list_all_role_systems_controller(current_user.id)
    if request.method == "POST":
        return controllers.create_role_system_controller(current_user.id)
    return "Method not allowed"
