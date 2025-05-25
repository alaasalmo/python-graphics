# setup_db.py
import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS nodes")
cur.execute("DROP TABLE IF EXISTS edges")

cur.execute("CREATE TABLE nodes (id INTEGER PRIMARY KEY, x INTEGER, y INTEGER, color TEXT)")
cur.execute("CREATE TABLE edges (id INTEGER PRIMARY KEY, from_id INTEGER, to_id INTEGER)")

# Add sample nodes
nodes = [
    (1, 100, 100, 'red'),
    (2, 200, 150, 'green'),
    (3, 300, 200, 'blue'),
    (4, 400, 250, 'orange'),
    (5, 180, 180, 'gray'),
    (6, 80, 80, 'black'),

]
cur.executemany("INSERT INTO nodes (id, x, y, color) VALUES (?, ?, ?, ?)", nodes)

# Add sample edges (connect node 1 to 2, 2 to 3, etc.)
edges = [
    (1, 1, 2),
    (2, 2, 3),
    (3, 3, 4),
    (4, 4, 1),
    (5, 5, 1),
    (6, 6, 5),

]
cur.executemany("INSERT INTO edges (id, from_id, to_id) VALUES (?, ?, ?)", edges)

conn.commit()
conn.close()
print("Nodes and edges created.")
