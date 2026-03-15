import sqlite3

def connect_db():
    return sqlite3.connect("metrics.db")

def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpu REAL,
        memory REAL,
        disk REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_data(cpu, memory, disk):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO metrics(cpu,memory,disk) VALUES(?,?,?)",
        (cpu, memory, disk)
    )

    conn.commit()
    conn.close()