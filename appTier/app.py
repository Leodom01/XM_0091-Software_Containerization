import os
from flask import Flask, jsonify, request, session
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    set_access_cookies,
)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from gevent.pywsgi import WSGIServer
from logging.config import dictConfig

app = Flask(__name__)


# MongoDB Config
# TODO: Replace with our MongoDB URI
app.config["MONGO_URI"] = (
    "mongodb://"
    + os.environ["MONGODB_USER"]
    + ":"
    + os.environ["MONGODB_PW"]
    + "@"
    + os.environ["MONGODB_HOST"]
    + ":"
    + os.environ["MONGODB_PORT"]
    + "/"
    + os.environ["MONGODB_DB"]
)  # URI from mongodb container
mongo = PyMongo(app)

# JWT Config with random key
app.config["JWT_SECRET_KEY"] = secrets.token_urlsafe(16)
app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"]
# user header, authorization header, bearer token
app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # To reduce complexity
jwt = JWTManager(app)


# User Authentication Routes NOT USED
@app.route("/register", methods=["POST"])
def register():
    app.logger.info("Registering user")
    username = request.json.get("username")
    password = request.json.get("password")
    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({"username": username, "password": hashed_password})
    return jsonify({"message": "User registered"}), 201


@app.route("/login", methods=["POST"])
def login():
    user = mongo.db.users.find_one({"username": request.json.get("username")})
    app.logger.info("user login")
    if user and check_password_hash(user["password"], request.json.get("password")):
        access_token = create_access_token(identity=user["username"])
        resp = jsonify(access_token=access_token)
        # set_access_cookies(resp, access_token)
        return resp, 200
    return jsonify({"message": "Invalid credentials"}), 401


# Reminder CRUD Operations
@app.route("/reminders", methods=["GET"])
def get_reminders():
    app.logger.info("User request reminders")
    reminders = mongo.db.reminders.find()
    return jsonify([reminder for reminder in reminders])


@app.route("/reminders", methods=["POST"])
def add_reminder():
    app.logger.info("user added reminder")
    reminder = request.json
    mongo.db.reminders.insert_one(reminder)
    return jsonify(reminder), 201


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello World"}), 201


if __name__ == "__main__":
    app.secret_key = secrets.token_urlsafe(16)
    http_server = WSGIServer(("0.0.0.0", 8000), app)
    http_server.serve_forever()
