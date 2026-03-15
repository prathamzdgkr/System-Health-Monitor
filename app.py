from flask import Flask, jsonify, render_template
from collector import collect_metrics
from database import create_table, insert_data, connect_db
from analyzer import detect_anomaly

import threading
import time

def auto_collect():

    while True:

        data = collect_metrics()

        cpu = data["cpu"]
        memory = data["memory"]
        disk = data["disk"]

        insert_data(cpu, memory, disk)

        alerts = detect_anomaly(cpu, memory, disk)

        if alerts:
            print("ALERT:", alerts)

        time.sleep(5)

app = Flask(__name__)

thread = threading.Thread(target=auto_collect)
thread.daemon = True
thread.start()

create_table()

@app.route("/collect")
def collect():

    data = collect_metrics()

    cpu = data["cpu"]
    memory = data["memory"]
    disk = data["disk"]

    insert_data(cpu, memory, disk)

    alerts = detect_anomaly(cpu, memory, disk)

    return jsonify({
        "metrics": data,
        "alerts": alerts
    })

@app.route("/metrics")
def metrics():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM metrics")
    data = cursor.fetchall()

    conn.close()

    return jsonify(data)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)