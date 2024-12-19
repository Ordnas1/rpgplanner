from flask import Blueprint
from src.auth.controllers import register_controller

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    return register_controller()
