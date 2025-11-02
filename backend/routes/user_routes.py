from flask import Blueprint, request, jsonify
from models.user_model import UserModel

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    username = data.get('username')
    if not username:
        return {"error": "username required"}, 400
    user = UserModel.create(username=username)
    return {"user_id": user.id, "username": user.username}

@user_bp.route('/<user_id>/progress', methods=['GET'])
def get_progress(user_id):
    user = UserModel.get(user_id)
    if not user:
        return {"error": "not found"}, 404
    return {"user_id": user.id, "progress": user.progress}
