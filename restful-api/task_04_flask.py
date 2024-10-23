#!/usr/bin/python3
from flask import Flask, request, jsonify
app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_username(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    update_name = users[username]
    update_name["username"] = username

    return jsonify(update_name)

@app.route("/add_user", methods=["POST"])
def add_user():
    if request.get_json() is None:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    if "username" in users:
        return jsonify({"error": "Username already exists"}), 400

    users[data["username"]] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    dict = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": dict}), 201

if __name__ == "__main__":
    app.run(debug=True)
