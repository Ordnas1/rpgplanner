from uuid import uuid4

from flask import request, jsonify
from marshmallow import ValidationError

from src.auth.schemas import create_user_schema, list_user_schema
from src.auth.models import User

from src import bcrypt, db


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
        password=bcrypt.generate_password_hash(result["password"]),
        email=result["email"],
        nickname=result["nickname"],
    )
    db.session.add(new_user)
    db.session.commit()

    response = list_user_schema.dump(User.query.get(new_id))
    return jsonify(response)
