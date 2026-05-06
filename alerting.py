import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_alert(alert):

    message = f"""
HIGH ALERT

Type: {alert['type']}
Severity: {alert['severity']}
Attacker: {alert['attacker']}

Description:
{alert['description']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })
