from flask import Blueprint, jsonify, request
from src.services.user_service import fetch_all_users, fetch_user, add_user, remove_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = fetch_all_users()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = fetch_user(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = add_user(data['username'], data['email'])
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    remove_user(user_id)
    return '', 204
