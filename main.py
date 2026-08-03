from datetime import datetime
import json
import os

START_DATE = datetime(2026, 8, 3)
DEADLINE = datetime(2026, 12, 17)

LOG_FILE = "log.json"


def calculate():
    today = datetime.now()

    days_passed = (today - START_DATE).days
    days_remaining = (DEADLINE - today).days

    # KPI (قابل تغییر)
    cec = 52
    celpip = 10
    docs = 65

    # Status Logic
    if days_remaining < 100:
        status = "CRITICAL 🔴"
    elif days_remaining < 130:
        status = "WARNING 🟡"
    else:
        status = "SAFE 🟢"

    return {
        "days_passed": days_passed,
        "days_remaining": days_remaining,
        "cec": cec,
        "celpip": celpip,
        "docs": docs,
        "status": status,
        "date": today.strftime("%Y-%m-%d %H:%M:%S")
    }


def save_log(data):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


if __name__ == "__main__":
    result = calculate()

    print("=== PR COUNTDOWN ===")
    print(f"Days Used: {result['days_passed']}")
    print(f"Days Remaining: {result['days_remaining']}")

    print("\n=== KPI STATUS ===")
    print(f"CEC Readiness: {result['cec']}%")
    print(f"CELPIP Progress: {result['celpip']}%")
    print(f"Documents Ready: {result['docs']}%")

    print(f"\nSystem Status: {result['status']}")

    save_log(result)
    print("\nLog saved successfully ✅")