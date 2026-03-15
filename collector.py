import psutil

def collect_metrics():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    partitions = psutil.disk_partitions()

    disk_percent = 0

    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
            disk_percent = usage.percent
            break
        except:
            continue

    data = {
        "cpu": cpu,
        "memory": memory,
        "disk": disk_percent
    }

    return data