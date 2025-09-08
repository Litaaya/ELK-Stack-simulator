import random
from datetime import datetime

users = ["Sage", "Jill", "Maya", "Josy", "Isabella"]
ips = ["192.168.1.10", "10.0.0.5", "172.16.0.22"]

# JSON log bất thường (transactions)
def malicious_json_log():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "user": random.choice(users),
        "action": "transfer",
        "location": "Unknown",
        "ip": random.choice(ips),
        "amount": random.choice([99999, 123456, 88888, 543210])  # Rất lớn, bất thường
    }

# Syslog bất thường (ssh brute-force)
def malicious_syslog():
    return f'<34>{datetime.utcnow().strftime("%b %d %H:%M:%S")} fintech-host sshd[12345]: Failed password for invalid user admin from {random.choice(ips)} port 2222 ssh2'

# Nginx log chứa SQLi/XSS/scan
def malicious_nginx_log():
    suspicious_uris = [
        "/login?user=admin'--",
        "/api/data?input=<script>alert(1)</script>",
        "/search?q=../../../etc/passwd",
        "/admin?debug=true",
        "/login?user=admin' OR '1'='1",
    ]
    uri = random.choice(suspicious_uris)
    return f'{random.choice(ips)} - - [{datetime.utcnow().strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET {uri} HTTP/1.1" 200 {random.randint(1000, 5000)}'

# Custom log chứa truy cập trái phép
def malicious_custom_log():
    paths = ["/etc/passwd", "/admin", "/root/.ssh/id_rsa", "/internal/config.yaml"]
    return f"[{datetime.utcnow()}] User:{random.choice(users)} accessed {random.choice(paths)} from IP:{random.choice(ips)}"

def generate_malicious_by_type(log_type):
    if log_type == "transactions":
        return malicious_json_log()
    elif log_type == "access":
        return malicious_nginx_log()
    elif log_type == "sys":
        return malicious_syslog()
    elif log_type == "custom":
        return malicious_custom_log()
    else:
        return f"[{datetime.utcnow()}] Unknown malicious log type: {log_type}"
