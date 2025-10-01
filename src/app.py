from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # change for production

db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Routes
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data["password"])
    user = User(username=data["username"], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password, data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token)
    return jsonify({"msg": "Bad credentials"}), 401

@app.route("/tasks", methods=["GET", "POST"])
@jwt_required()
def tasks():
    if request.method == "POST":
        data = request.get_json()
        task = Task(title=data["title"])
        db.session.add(task)
        db.session.commit()
        return jsonify({"msg": "Task created"}), 201
    else:
        tasks = Task.query.all()
        return jsonify([{"id": t.id, "title": t.title, "done": t.done} for t in tasks])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
