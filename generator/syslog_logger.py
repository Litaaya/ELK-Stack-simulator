import random
from datetime import datetime

users = ["Sage", "Jill", "Maya", "Josy", "Isabella"]
ips = ["10.0.0.5", "172.16.0.22"]

def generate():
    return f'<34>{datetime.utcnow().strftime("%b %d %H:%M:%S")} fintech-host sshd[12345]: Accepted password for {random.choice(users)} from {random.choice(ips)} port 22 ssh2'
