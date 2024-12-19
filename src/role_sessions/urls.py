from flask import request

from src.app import app
from . import controllers


@app.route("/role_sessions", methods=['GET', 'POST'])
def list_create_role_session():
    if request.method == 'GET':
        return controllers.list_all_role_sessions_controller()
    if request.method == 'POST':
        return controllers.create_role_session_controller()
    return 'Method not allowed'


@app.route("/role_sessions/<role_session_id>", methods=['GET'])
def retrieve_role_sessions(role_session_id):
    if request.method == 'GET':
        return controllers.retrieve_single_role_session(role_session_id)
    return 'Method not allowed'
