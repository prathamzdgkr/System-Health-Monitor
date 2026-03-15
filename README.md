# System Health Monitoring & Alert System

A Python-based system monitoring tool that collects CPU, memory, and disk usage metrics and detects abnormal system behavior.

## Features
- Real-time system metrics collection
- Automatic monitoring every 5 seconds
- Anomaly detection for high resource usage
- REST APIs for system metrics
- Simple web dashboard for monitoring

## Tech Stack
- Python
- Flask
- SQLite
- psutil

## Project Structure

system-health-monitor
│
├── app.py
├── collector.py
├── analyzer.py
├── database.py
│
├── dashboard.html      
│
└── requirements.txt

## Installation

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open browser

http://127.0.0.1:5000

## API Endpoints

/collect → collect system metrics  
/metrics → retrieve stored metrics
