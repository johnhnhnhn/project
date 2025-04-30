from flask import Blueprint, jsonify

# Create a blueprint for routes
main = Blueprint("main", __name__)

# Sample route to test if backend is working
@main.route("/api/status", methods=["GET"])
def status():
    return jsonify({"message": "Flask backend is running!"})
