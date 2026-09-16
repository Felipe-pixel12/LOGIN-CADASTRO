import sqlite3
from database.db import get_db_connection

class Usermodel:

    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def update_user(user_id, username=None, password=None):
        conn = get_db_connection()
        try:
            user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
            if not user:
                return None

            new_username = username if username else user['username']
            new_password = password if password else user['password']

            conn.execute('UPDATE users SET username = ?, password = ? WHERE id = ?',
                         (new_username, new_password, user_id))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        if not user:
            conn.close()
            return None

        conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        return True