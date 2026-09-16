from models.formulario_model import FormularioModel

class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')
        email = data.get('email')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        genero = data.get('genero')

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400

        formulario = FormularioModel.create_formulario(
            user_id, nome, email, data_nascimento, cpf, genero)
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201

        return {"error": "Erro ao criar formulário"}, 500

    @staticmethod
    def get_formulario(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404

        return {
            "id": formulario['id'],
            "user_id": formulario['user_id'],
            "nome": formulario['nome'],
            "email": formulario['email'],
            "data_nascimento": formulario['data_nascimento'],
            "cpf": formulario['cpf'],
            "genero": formulario['genero']
        }, 200

    @staticmethod
    def update_formulario(formulario_id, data):
        result = FormularioModel.update_formulario(formulario_id, data)
        if result is None:
            return {"error": "Formulário não encontrado"}, 404

        return {"message": "Formulário atualizado com sucesso"}, 200

    @staticmethod
    def delete_formulario(formulario_id):
        result = FormularioModel.delete_formulario(formulario_id)
        if result is None:
            return {"error": "Formulário não encontrado"}, 404

        return {"message": "Formulário excluído com sucesso"}, 200