from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import Usermodel

class UserController:

    @staticmethod
    def register_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"},

        hashed_password = generate_password_hash(password)

        if Usermodel.create_user(username, hashed_password):
            return {"message": "Usuário registrado com sucesso"}, 20
        
        return {"error": "Nome de usuário já existe"}, 400
    
    @staticmethod
    def login_user(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha obrigátorios"},

        user = Usermodel.find_by_username(username)
        if user and check_password_hash(user['password'], password):
           access_token = create_access_token(identity=str(user['id']))
           return {"acess_token": access_token}, 200
        
        return {"error": "Nome de usuário ou senha inválios"}, 401
