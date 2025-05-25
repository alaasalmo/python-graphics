# app.py
from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_nodes():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT id, x, y, color FROM nodes")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "x": r[1], "y": r[2], "color": r[3]} for r in rows]

def get_edges():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT from_id, to_id FROM edges")
    rows = cur.fetchall()
    conn.close()
    return [{"from": r[0], "to": r[1]} for r in rows]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/data')
def api_data():
    return jsonify({
        "nodes": get_nodes(),
        "edges": get_edges()
    })

if __name__ == '__main__':
    app.run(debug=True)
