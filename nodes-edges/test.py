import sqlite3
conn = sqlite3.connect("data.db")
cur = conn.cursor()
for row in cur.execute("SELECT id, x, y FROM nodes"):
    print(row)