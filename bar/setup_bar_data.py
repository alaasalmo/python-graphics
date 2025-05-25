# setup_bar_data.py

import sqlite3
import random

conn = sqlite3.connect("bar_data.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS bars")
cur.execute("CREATE TABLE bars (label TEXT, value INTEGER)")

# Generate random data (without jsonify)
labels = ["A", "B", "C", "D", "E"]
data = [(label, random.randint(10, 30)) for label in labels]

# Insert into database
cur.executemany("INSERT INTO bars (label, value) VALUES (?, ?)", data)

conn.commit()
conn.close()

print("Database setup done with random data.")
