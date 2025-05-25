from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chart.html")

@app.route("/api/data")
def get_data():
    conn = sqlite3.connect("bar_data.db")
    cur = conn.cursor()
    cur.execute("SELECT label, value FROM bars")
    data = [{"label": row[0], "value": row[1]} for row in cur.fetchall()]
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
