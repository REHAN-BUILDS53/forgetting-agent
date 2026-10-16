
from pathlib import Path
from datetime import datetime
import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS artifacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    path TEXT UNIQUE,
    size INTEGER,
    file_type TEXT,
    modified_time TEXT,
    age_days INTEGER,
    status TEXT
)
""")

connection.commit()

folder = Path("data")

if not folder.exists():
    print("Error: data folder not found.")
    connection.close()
    exit()

for item in folder.iterdir():
    if not item.is_file():
        continue

    modified_time = datetime.fromtimestamp(item.stat().st_mtime)
    age = datetime.now() - modified_time
    age_in_days = age.days

    if age_in_days >= 30:
        status = "OLD"
    else:
        status = "RECENT"

    print("Name:", item.name)
    print("Size:", item.stat().st_size, "bytes")
    print("Type:", item.suffix)
    print("Modified:", modified_time)
    print("Age:", age_in_days, "days")
    print("Status:", status)
    print()

    cursor.execute(
        "SELECT id FROM artifacts WHERE path = ?",
        (str(item),)
    )

    existing_record = cursor.fetchone()

    if existing_record:
        cursor.execute("""
            UPDATE artifacts
            SET name = ?, size = ?, file_type = ?,
                modified_time = ?, age_days = ?, status = ?
            WHERE path = ?
        """, (
            item.name,
            item.stat().st_size,
            item.suffix,
            modified_time.isoformat(),
            age_in_days,
            status,
            str(item)
        ))
    else:
        cursor.execute("""
            INSERT INTO artifacts
            (name, path, size, file_type, modified_time, age_days, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            item.name,
            str(item),
            item.stat().st_size,
            item.suffix,
            modified_time.isoformat(),
            age_in_days,
            status
        ))

    connection.commit()


connection.close()
print("Inventory saved successfully.")
