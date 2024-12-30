from uuid import uuid4

from flask import request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token

from src.auth.schemas import create_user_schema, list_user_schema, login_schema
from src.auth.models import User

from src import bcrypt, db, jwt


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


def register_controller():
    req_data = request.get_json()

    try:
        result = create_user_schema.load(req_data)
    except ValidationError as err:
        return err.messages, 400

    new_id = str(uuid4())
    new_user = User(
        id=new_id,
        username=result["username"],
        password=bcrypt.generate_password_hash(result["password"]).decode('utf-8'),
        email=result["email"],
        nickname=result["nickname"],
    )
    db.session.add(new_user)
    db.session.commit()

    response = list_user_schema.dump(User.query.get(new_id))
    return jsonify(response)


def login_controller():
    req_data = request.get_json()

    try:
        result = login_schema.load(req_data)
        print(result)
    except ValidationError as err:
        print("ERR")
        return err.messages, 400

    user = User.query.filter_by(username=result["username"]).first()

    if user and bcrypt.check_password_hash(user.password, result["password"]):
        access_token = create_access_token(identity=user)
        return jsonify({"id": user.id, "access_token": access_token})
    else:
        return jsonify({"message": "Login failed"}), 401
