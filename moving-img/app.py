from flask import Flask, render_template, jsonify
import sqlite3
import random

app = Flask(__name__)

# Create or update data in SQLite
def update_position():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS position (id INTEGER PRIMARY KEY, x INTEGER, y INTEGER)")
    cur.execute("DELETE FROM position")
    x = random.randint(50, 500)
    y = random.randint(50, 300)
    cur.execute("INSERT INTO position (x, y) VALUES (?, ?)", (x, y))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/position')
def get_position():
    update_position()  # Simulate new position each call
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("SELECT x, y FROM position ORDER BY id DESC LIMIT 1")
    x, y = cur.fetchone()
    conn.close()
    return jsonify({'x': x, 'y': y})

if __name__ == '__main__':
    app.run(debug=True)
