from flask import Blueprint, jsonify

data_bp = Blueprint('data', __name__)

@data_bp.route('/data', methods=['GET'])
def get_data():
    # Logic to get data (e.g., call logs, SMS, etc.)
    return jsonify({"message": "List of data"})
