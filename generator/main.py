# generator/main.py
import time
import random
from pathlib import Path

from json_logger import generate as generate_json_log
from nginx_logger import generate as generate_nginx_log
from syslog_logger import generate as generate_syslog
from custom_logger import generate as generate_custom_log
from malicious_injector import generate_malicious_by_type

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def write_log(filename, content):
    filepath = LOG_DIR / filename
    with open(filepath, "a") as f:
        f.write(str(content) + "\n")

def generate_normal_logs():
    write_log("transactions.log", generate_json_log())
    write_log("access.log", generate_nginx_log())
    write_log("sys.log", generate_syslog())
    write_log("custom.log", generate_custom_log())
    print("[+] Normal logs written.")

def generate_malicious_logs():
    num_logs = random.randint(1, 10)
    log_types = ["transactions", "access", "sys", "custom"]

    print(f"[!] Injecting {num_logs} malicious log(s)...")
    for _ in range(num_logs):
        log_type = random.choice(log_types)
        log = generate_malicious_by_type(log_type)
        write_log(f"{log_type}.log", log)
        print(f"    → Malicious log added to {log_type}.log")

def main_loop():
    iteration = 0
    while True:
        generate_normal_logs()

        # Mỗi 10 giây: inject malicious logs
        if iteration % 2 == 0:
            generate_malicious_logs()

        iteration += 1
        time.sleep(2) # Thời gian generate logs

if __name__ == "__main__":
    main_loop()
