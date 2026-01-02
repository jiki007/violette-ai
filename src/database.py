import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "violette.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    conn.commit()
    conn.close()

def save_message(role,text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO memory (role,content) VALUES (?, ?)', (role,text))
    conn.commit()
    conn.close()

def load_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #Loading all messages ordered by time
    cursor.execute('SELECT role, content FROM memory ORDER BY id ASC')
    rows = cursor.fetchall()
    conn.close()

    formatted_history = []
    for role, content in rows:
        formatted_history.append({
            "role":role,
            "parts":[{"text":content}]
        })

    return formatted_history

