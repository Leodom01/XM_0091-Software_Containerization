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
from bson import json_util

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
    
    # Retrieve reminders from MongoDB
    reminders = mongo.db.reminders.find()
    
    # Extract and serialize data into JSON
    resp = []
    for reminder in reminders:
        # Extract the fields you want from the reminder document
        reminder_data = {
            "title": reminder["title"],  # Replace with actual field names
            "body": reminder["body"],
            # Add more fields as needed
        }
        # Serialize the extracted data to JSON
        resp.append(json_util.dumps(reminder_data))
    
    # Return JSON response
    return jsonify({"reminders": resp})


@app.route("/reminders", methods=["POST"])
def add_reminder():
    app.logger.info("User added a reminder")
    
    # Retrieve the reminder data from the request's JSON payload
    reminder = request.json
    
    # Insert the reminder into MongoDB
    mongo.db.reminders.insert_one(reminder)
    
    # Convert the reminder object to a dictionary
    reminder_dict = {
        "title": reminder.get("title"),  # Replace with actual field names
        "body": reminder.get("body"),
        # Add more fields as needed
    }
    
    # Return the reminder dictionary in the response
    return jsonify(reminder_dict), 201



@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello World"}), 201


if __name__ == "__main__":
    app.secret_key = secrets.token_urlsafe(16)
    http_server = WSGIServer(("0.0.0.0", 8000), app)
    http_server.serve_forever()
