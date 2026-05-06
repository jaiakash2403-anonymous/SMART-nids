# SMART-nids
an customizable nids
# Smart Network Intrusion Detection System

A lightweight real time Network Intrusion Detection System developed using Python.

## Features

- Real time packet monitoring
- Signature based detection
- Incident correlation
- Telegram alerting
- Dashboard visualization
- SQLite event logging

## Technologies Used

- Python
- Scapy
- Flask
- SQLite
- Telegram Bot API

## Installation

```bash
git clone <repo-url>

cd smart-nids

pip install -r requirements.txt
```

## Run Collector

```bash
python3 collector.py
```

## Run Correlator

```bash
python3 correlator.py
```

## Run NIDS Sensor

```bash
sudo python3 nids_sensor.py lo
```

## Run Dashboard

```bash
python3 dashboard.py
```

## Test Attack

```bash
sudo python3 - << 'EOF'
from scapy.all import IP, TCP, send

pkt = IP(dst="127.0.0.1")/TCP(dport=4444)/b"MALWARE_SIG"

send(pkt)

print("Attack packet sent")
EOF
```

## Dashboard URL

```text
http://127.0.0.1:8000
```
