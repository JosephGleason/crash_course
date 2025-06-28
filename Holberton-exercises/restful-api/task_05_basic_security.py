# Task 5: API Security
# 1) Basic HTTP Auth
# 2) JWT token-based Auth
# 3) Role-based access control

# 1) IMPORTS
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth  # for Basic Auth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity)

# 2) APP & AUTH SETUP
app = Flask(__name__) # Create the Flask “app” instance
app.config['SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth() # Create the Basic Auth “bouncer”

# 3) IN-MEMORY USERS STORE
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password #decorator that tells the auth object “use this function to check credentials.”
def verify_password(username, password):
    user = users.get(username) #1. look up user record
    if not user:
        return False # no such user deny access
    if check_password_hash(user["password"], password):
        return True #pass match allow
    return False #pass wrong deny

@app.route("/basic-protected")   # 1) Flask route decorator: binds this URL to the function below
@auth.login_required             # 2) Basic Auth decorator: blocks unauthorized access
def basic_protected():
    return "Basic Auth: Access Granted"

if __name__ == "__main__":
    app.run()
