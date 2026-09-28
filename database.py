import sqlite3

def create_table():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        salary INTEGER
    )
    """)

    
