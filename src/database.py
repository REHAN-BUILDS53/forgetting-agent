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

cursor.execute("""
INSERT INTO artifacts
(name, path, size, file_type, modified_time, age_days, status)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    "example.txt",
    "data/example.txt",
    100,
    ".txt",
    "2026-10-17 10:00:00",
    5,
    "RECENT"
))

connection.commit()

print("Record inserted successfully.")

connection.close()