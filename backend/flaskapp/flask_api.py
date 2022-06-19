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