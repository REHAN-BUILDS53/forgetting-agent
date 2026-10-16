import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM artifacts")
records = cursor.fetchall()

for record in records:
    print(record)

connection.close()