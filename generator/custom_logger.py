import random
from datetime import datetime

users = ["Sage", "Jill", "Maya", "Josy", "Isabella"]

def generate():
    return f"[{datetime.utcnow()}] User:{random.choice(users)} transferred ${random.randint(100, 9999)} to Account:{random.randint(1000,9999)}"
