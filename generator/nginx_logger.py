import random
from datetime import datetime

ips = ["192.168.1.10", "10.0.0.5", "172.16.0.22"]
resources = ["/", "/login", "/transfer", "/api/v1/data"]

def generate():
    ip = random.choice(ips)
    resource = random.choice(resources)
    log = f'{ip} - - [{datetime.utcnow().strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET {resource} HTTP/1.1" 200 1234'
    return log
