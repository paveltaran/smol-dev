import sqlite3
from config import settings

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(settings.DATABASE_PATH)
        self.cursor = self.conn.cursor()

    def save_programmer(self, programmer):
        query = '''INSERT INTO programmers(name, skills, experience_years, language) 
                   VALUES(?,?,?,?)'''
        self.cursor.execute(query, (programmer.name, programmer.skills, programmer.experience_years, programmer.language))
        self.conn.commit()

    def get_programmer(self, name):
        query = '''SELECT * FROM programmers WHERE name = ?'''
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()

DATABASE = Database()