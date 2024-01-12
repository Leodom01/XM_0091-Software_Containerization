from flask import Flask, jsonify, request, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)

# MongoDB Config
# TODO: Replace with our MongoDB URI
app.config["MONGO_URI"] = "mongodb://your_mongodb_uri"  # Replace with your MongoDB URI
mongo = PyMongo(app)

# JWT Config with random key
app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)


# User Authentication Routes
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({'username': username, 'password': hashed_password})
    return jsonify({"message": "User registered"}), 201


@app.route('/login', methods=['POST'])
def login():
    user = mongo.db.users.find_one({'username': request.json.get('username')})
    if user and check_password_hash(user['password'], request.json.get('password')):
        access_token = create_access_token(identity=user['username'])
        session['jwt'] = access_token
        return jsonify({"message": "login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401


# Reminder CRUD Operations
@app.route('/reminders', methods=['GET'])
@jwt_required()
def get_reminders():
    reminders = mongo.db.reminders.find()
    return jsonify([reminder for reminder in reminders])


@app.route('/reminders', methods=['POST'])
@jwt_required()
def add_reminder():
    reminder = request.json
    mongo.db.reminders.insert_one(reminder)
    return jsonify(reminder), 201


if __name__ == '__main__':
    app.run(debug=True)
