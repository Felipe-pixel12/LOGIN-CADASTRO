from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return UserController.register_user(request.get_json())

@user_bp.route('/login', methods=['POST'])
def login():
    return UserController.login_user(request.get_json())

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return UserController.get_user(user_id)

@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    return UserController.update_user(user_id, request.get_json())

@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return UserController.delete_user(user_id)