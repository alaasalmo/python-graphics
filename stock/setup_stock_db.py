import sqlite3
from datetime import datetime, timedelta
import random

conn = sqlite3.connect("stocks.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS stock_prices")
cur.execute("CREATE TABLE stock_prices (id INTEGER PRIMARY KEY, date TEXT, price REAL)")

# Generate 30 days of random stock prices
base_date = datetime.now() - timedelta(days=30)
data = [
    ((base_date + timedelta(days=i)).strftime('%Y-%m-%d'), round(100 + random.uniform(-5, 5), 2))
    for i in range(30)
]

print(data)

cur.executemany("INSERT INTO stock_prices (date, price) VALUES (?, ?)", data)

conn.commit()
conn.close()
print("✅ Stock data inserted.")
