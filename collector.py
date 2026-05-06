from flask import Flask, request, jsonify
import sqlite3
import json
import time
import os

DB_PATH = "collector.db"

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            raw TEXT,
            sensor TEXT,
            type TEXT,
            timestamp REAL
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attacker TEXT,
            type TEXT,
            severity TEXT,
            description TEXT,
            related_event_ids TEXT,
            risk_score INTEGER,
            confidence REAL,
            mitre TEXT,
            created REAL
        )
    """)

    conn.commit()
    conn.close()

@app.route("/event", methods=["POST"])
def ingest():
    ev = request.json

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        "INSERT INTO events (raw, sensor, type, timestamp) VALUES (?, ?, ?, ?)",
        (
            json.dumps(ev),
            ev.get("sensor"),
            ev.get("type"),
            time.time()
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"status": "ok"})

@app.route("/events")
def events():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT * FROM events")
    rows = c.fetchall()

    conn.close()

    return jsonify(rows)

@app.route("/incidents")
def incidents():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT * FROM incidents")
    rows = c.fetchall()

    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
