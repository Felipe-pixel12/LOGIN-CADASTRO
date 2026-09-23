from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify(UserController.login_user(request.get_json()))

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return jsonify(UserController.get_user(user_id))

@user_bp.route('/', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    return jsonify(UserController.update_user(user_id, request.get_json()))

@user_bp.route('/', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return jsonify(UserController.delete_user(user_id))