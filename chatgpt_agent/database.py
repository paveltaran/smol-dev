```python
import sqlite3
from chatgpt_agent.config import DATABASE_CONFIG
from chatgpt_agent.programmer import Programmer

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_CONFIG['name'])
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS programmers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                skills TEXT,
                experience INTEGER,
                availability TEXT
            )
        """)

    def insert_programmer(self, programmer: Programmer):
        self.cursor.execute("""
            INSERT INTO programmers (name, skills, experience, availability)
            VALUES (?, ?, ?, ?)
        """, (programmer.name, programmer.skills, programmer.experience, programmer.availability))
        self.conn.commit()

    def update_programmer(self, programmer: Programmer):
        self.cursor.execute("""
            UPDATE programmers
            SET name = ?, skills = ?, experience = ?, availability = ?
            WHERE id = ?
        """, (programmer.name, programmer.skills, programmer.experience, programmer.availability, programmer.id))
        self.conn.commit()

    def delete_programmer(self, programmer_id: int):
        self.cursor.execute("""
            DELETE FROM programmers
            WHERE id = ?
        """, (programmer_id,))
        self.conn.commit()

    def select_programmer(self, programmer_id: int):
        self.cursor.execute("""
            SELECT * FROM programmers
            WHERE id = ?
        """, (programmer_id,))
        return self.cursor.fetchone()

    def select_all_programmers(self):
        self.cursor.execute("""
            SELECT * FROM programmers
        """)
        return self.cursor.fetchall()
```