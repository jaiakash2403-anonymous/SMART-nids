from flask import Flask
import requests

app = Flask(__name__)

COLLECTOR = "http://127.0.0.1:5000"

@app.route("/")
def dashboard():

    events = requests.get(f"{COLLECTOR}/events").json()
    incidents = requests.get(f"{COLLECTOR}/incidents").json()

    html = f"""
    <html>
    <head>
        <title>Smart NIDS Dashboard</title>
    </head>
    <body>

    <h1>Smart NIDS Dashboard</h1>

    <h2>Events</h2>
    <pre>{events}</pre>

    <h2>Incidents</h2>
    <pre>{incidents}</pre>

    </body>
    </html>
    """

    return html

if __name__ == "__main__":
    app.run(port=8000)
