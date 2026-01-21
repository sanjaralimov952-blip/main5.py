# main5.py
import sqlite3
from datetime import datetime

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    date TEXT
)
""")
conn.commit()


def add_task(text):
    date = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
    cursor.execute(
        "INSERT INTO tasks (text, date) VALUES (?, ?)",
        (text, date)
    )
    conn.commit()


def get_tasks():
    cursor.execute("SELECT id, text, date FROM tasks")
    return cursor.fetchall()


def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
