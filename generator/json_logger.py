import random
from datetime import datetime

users = ["Sage", "Jill", "Maya", "Josy", "Isabella"]
actions = ["login", "logout", "transfer", "check_balance"]
locations = ["Hanoi", "Saigon", "Danang", "London"]
ips = ["192.168.1.10", "10.0.0.5", "172.16.0.22"]

def generate():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "user": random.choice(users),
        "action": random.choice(actions),
        "location": random.choice(locations),
        "ip": random.choice(ips),
        "status": random.choice(["success", "fail"]),
        "amount": round(random.uniform(10, 10000), 2)
    }
