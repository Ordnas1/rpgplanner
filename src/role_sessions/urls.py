from flask import request, Blueprint


from . import controllers

role_sessions = Blueprint("role_sessions", __name__, url_prefix="/role_sessions")


@role_sessions.route("/", methods=["GET", "POST"])
def list_create_role_session():
    if request.method == "GET":
        return controllers.list_all_role_sessions_controller()
    if request.method == "POST":
        return controllers.create_role_session_controller()
    return "Method not allowed"


@role_sessions.route("/<role_session_id>", methods=["GET"])
def retrieve_role_sessions(role_session_id):
    if request.method == "GET":
        return controllers.retrieve_single_role_session(role_session_id)
    return "Method not allowed"
