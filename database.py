```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        return conn
    except Error as e:
        print(e)

def save_application_to_database(conn, application_form):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO applications VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (application_form['user_id'], application_form['job_id'], application_form['user_profile'], 
                        application_form['application_status'], application_form['job_position'], 
                        application_form['salary'], application_form['benefits'], 
                        application_form['application_deadline'], application_form['recruiter_contact'], 
                        application_form['application_form']))
        conn.commit()
    except Error as e:
        print(e)

def retrieve_application_from_database(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM applications WHERE user_id=?", (user_id,))
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(e)

def update_application_status(conn, user_id, application_status):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET application_status = ? WHERE user_id = ?", (application_status, user_id))
        conn.commit()
    except Error as e:
        print(e)

def update_user_profile(conn, user_id, user_profile):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET user_profile = ? WHERE user_id = ?", (user_profile, user_id))
        conn.commit()
    except Error as e:
        print(e)
```