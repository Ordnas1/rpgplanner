"""Here we register routes within the public_api blueprint"""

from flask import Blueprint

from .role_sessions.urls import role_sessions

public_api = Blueprint("public_api", __name__, url_prefix="/api")

public_api.register_blueprint(role_sessions)
