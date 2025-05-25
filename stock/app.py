# app.py
from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("stock_chart.html")

@app.route('/api/stocks')
def api_stocks():
    conn = sqlite3.connect("stocks.db")
    cur = conn.cursor()
    cur.execute("SELECT date, price FROM stock_prices ORDER BY date")
    rows = cur.fetchall()
    conn.close()
    return jsonify([{"date": r[0], "price": r[1]} for r in rows])

if __name__ == '__main__':
    app.run(debug=True)
