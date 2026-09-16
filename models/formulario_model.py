import sqlite3
from database.db import get_db_connection

class FormularioModel:

    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO formulario (user_id, nome, email, data_nascimento, cpf, genero)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def find_by_id(formulario_id):
        conn = get_db_connection()
        formulario = conn.execute('SELECT * FROM formulario WHERE id = ?', (formulario_id,)).fetchone()
        conn.close()
        return formulario

    @staticmethod
    def update_formulario(formulario_id, data):
        conn = get_db_connection()
        try:
            formulario = conn.execute('SELECT * FROM formulario WHERE id = ?', (formulario_id,)).fetchone()
            if not formulario:
                return None

            nome = data.get('nome', formulario['nome'])
            email = data.get('email', formulario['email'])
            data_nascimento = data.get('data_nascimento', formulario['data_nascimento'])
            cpf = data.get('cpf', formulario['cpf'])
            genero = data.get('genero', formulario['genero'])

            conn.execute('''UPDATE formulario
                         SET nome = ?, email = ?, data_nascimento = ?, cpf = ?, genero = ?
                         WHERE id = ?''',
                         (nome, email, data_nascimento, cpf, genero, formulario_id))
            conn.commit()
            return True
        finally:
            conn.close()

    @staticmethod
    def delete_formulario(formulario_id):
        conn = get_db_connection()
        formulario = conn.execute('SELECT * FROM formulario WHERE id = ?', (formulario_id,)).fetchone()
        if not formulario:
            conn.close()
            return None

        conn.execute('DELETE FROM formulario WHERE id = ?', (formulario_id,))
        conn.commit()
        conn.close()
        return True