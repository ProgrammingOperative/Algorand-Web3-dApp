import os
from datetime import datetime
from functools import wraps
from pathlib import Path

import jwt
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f'sqlite:///{Path().cwd() / "db_web.db"}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]

        if not token:
            return make_response(
                jsonify({"success": False, "data": "Token missing"}), 403
            )

        try:
            data = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            current_user = Users.query.filter_by(id=data["id"]).first()
        except:
            return make_response(
                jsonify({"success": False, "data": "Token is invalid"}), 401
            )

        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorated
