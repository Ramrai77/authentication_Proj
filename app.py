from flask import Flask, request, jsonify, render_template
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from db import init_db
from models import create_user, get_user_by_email

app = Flask(__name__)
CORS(app)

# Initialize DB
init_db(app)

bcrypt = Bcrypt(app)

# ---------------- UI ROUTES ----------------
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')

# ---------------- REGISTER API ----------------
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        create_user(name, email, hashed_password)
        return jsonify({"message": "User registered successfully"})
    except Exception as e:
        return jsonify({"message": "Email already exists"}), 400


# ---------------- LOGIN API ----------------
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    user = get_user_by_email(email)

    if user and bcrypt.check_password_hash(user[3], password):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid email or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)