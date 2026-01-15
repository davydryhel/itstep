import sqlite3

connection = sqlite3.connect("itstep_DB.sl3")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS first_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
""")

cursor.execute("INSERT INTO first_table (name) VALUES (?);", ("Nick",))

connection.commit()

cursor.execute("SELECT * FROM first_table;")
print(cursor.fetchall())

connection.close()