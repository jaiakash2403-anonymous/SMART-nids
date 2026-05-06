import sqlite3
import json
import time
from alerting import send_alert

DB = "collector.db"

THRESHOLD = 5

def run():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT id, raw FROM events")
    rows = c.fetchall()

    grouped = {}

    for rid, raw in rows:
        ev = json.loads(raw)

        src = ev.get("src", "unknown")

        grouped.setdefault(src, []).append(rid)

    for src, ids in grouped.items():

        if len(ids) >= THRESHOLD:

            description = f"Repeated suspicious activity from {src}"

            c.execute("""
                INSERT INTO incidents
                (
                    attacker,
                    type,
                    severity,
                    description,
                    related_event_ids,
                    risk_score,
                    confidence,
                    mitre,
                    created
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                src,
                "repeated_signature",
                "high",
                description,
                json.dumps(ids),
                90,
                0.95,
                "TA0001",
                time.time()
            ))

            conn.commit()

            print(f"[INCIDENT] {description}")

            send_alert({
                "type": "repeated_signature",
                "severity": "high",
                "attacker": src,
                "description": description
            })

    conn.close()

if __name__ == "__main__":
    print("Correlator started")

    while True:
        run()
        time.sleep(10)
