#!/usr/bin/python3

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    user = list(users.keys())
    return jsonify(user)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>") #dynamic URL segment
def get_user(username): # Flask passes jane or john as username
    user = users.get(username) #checks the dictionary
    if user:
        return jsonify({"username": username, **user}) #combines the key and value
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()
