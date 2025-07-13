import json
import csv
import os
from datetime import datetime

CSV_PATH = "logs/log.csv"
JSON_PATH = "logs/log.json"

def log_interaction(prompt, model, latency, token_count):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "model": model,
        "latency_sec": round(latency, 3),
        "token_count": token_count
    }

    os.makedirs("logs", exist_ok=True)

    # CSV
    csv_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=log_entry.keys())
        if not csv_exists:
            writer.writeheader()
        writer.writerow(log_entry)

    # JSON
    logs = []
    if os.path.isfile(JSON_PATH):
        with open(JSON_PATH, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

    logs.append(log_entry)
    with open(JSON_PATH, "w") as f:
        json.dump(logs, f, indent=2)
