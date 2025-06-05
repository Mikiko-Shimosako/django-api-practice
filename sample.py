import sqlite3

conn = sqlite3.connect('example.db')  # DB に接続（なければ自動生成）
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

conn.commit()
conn.close()
