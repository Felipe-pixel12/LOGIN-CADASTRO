import sqlite3
from database.db import get_db_connection

class Usemodel:
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?' , (username,)).fetchone()
        conn.close()
        return user
    
    @staticmethod
    def create_user(username, passaword):
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO (username, passaword) VALUES (?,?)', (username,passaword))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()