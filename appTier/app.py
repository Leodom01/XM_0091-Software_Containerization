from flask import Flask, jsonify, request, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from gevent.pywsgi import WSGIServer
from logging.config import dictConfig

app = Flask(__name__)

# Logging Config
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# MongoDB Config
# TODO: Replace with our MongoDB URI
app.config["MONGO_URI"] = "db-svc.default.svc.cluster.local:27017"  # URI from mongodb container
mongo = PyMongo(app)

# JWT Config with random key
app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)


# User Authentication Routes
@app.route('/register', methods=['POST'])
def register():
    app.logger.info('Registering user')
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({'username': username, 'password': hashed_password})
    return jsonify({"message": "User registered"}), 201


@app.route('/login', methods=['POST'])
def login():
    user = mongo.db.users.find_one({'username': request.json.get('username')})
    app.logger.info('user login')
    if user and check_password_hash(user['password'], request.json.get('password')):
        access_token = create_access_token(identity=user['username'])
        session['jwt'] = access_token
        return jsonify({"message": "login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401


# Reminder CRUD Operations
@app.route('/reminders', methods=['GET'])
@jwt_required()
def get_reminders():
    app.logger.info('User request reminders')
    reminders = mongo.db.reminders.find()
    return jsonify([reminder for reminder in reminders])


@app.route('/reminders', methods=['POST'])
@jwt_required()
def add_reminder():
    app.logger.info('user added reminder')
    reminder = request.json
    mongo.db.reminders.insert_one(reminder)
    return jsonify(reminder), 201


@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hello World"}), 201


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8000), app)
    http_server.serve_forever()
