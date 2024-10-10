import sqlite3


conn = sqlite3.connect("discordDB")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        message TEXT,
        time TEXT
        )
''')


conn.commit()
conn.close()