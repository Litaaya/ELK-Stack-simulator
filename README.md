# Log Simulation & ELK Stack Monitoring System

**Litaaya**

This project simulates real-time log generation for a fintech-like environment, injects malicious behaviors, and visualizes logs using the ELK Stack (Elasticsearch, Logstash, Kibana) with Filebeat

## Features

- Real-time generation of multiple log formats:
  - Apache/Nginx logs (`access.log`)
  - Syslog (`sys.log`)
  - Custom logs (`custom.log`)
  - JSON transaction logs (`transactions.log`)
- Random injection of malicious log entries (e.g., SQLi, insider threats, SSH brute force)
- Visualization via Kibana
- ELK Stack & Filebeat fully containerized using Docker Compose

---

## How to Run

### Clone the repo

```bash
git clone https://github.com/Litaaya/ELK-Stack-simulator.git
cd ./ELK_Stack
```
### Run local

- To start this project, you can open two terminal:
  - The first one:
  ```
  cd ./generator
  python main.py
  ```
  - The second one: Note that you need your Docker Desktop open so you can run your docker container here
  ```
  cd ./ELK_Stack
  docker compose up -d
  ```
- If you want to stop the progress, using:
  - Ctrl C for the generator terminal
  - Command for the ELK_Stack terminal:
  ```
  docker compose down
  ```
  

