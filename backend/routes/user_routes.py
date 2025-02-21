from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    # Logic to get users (e.g., from database)
    return jsonify({"message": "List of users"})
