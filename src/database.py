
import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS artifacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    path TEXT,
    size INTEGER,
    file_type TEXT,
    modified_time TEXT,
    age_days INTEGER,
    status TEXT
)
""")

connection.commit()
connection.close()

print("Database initialized successfully.")
