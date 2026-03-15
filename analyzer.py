def detect_anomaly(cpu, memory, disk):

    alerts = []

    if cpu > 85:
        alerts.append("High CPU usage detected")

    if memory > 85:
        alerts.append("High Memory usage detected")

    if disk > 90:
        alerts.append("Disk almost full")

    return alerts