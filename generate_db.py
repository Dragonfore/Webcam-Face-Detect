import sqlite3

try:
    conn = sqlite3.connect("program_performance.db")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS performance ( id integer PRIMARY KEY, time blob, memory real, cpu_usage real); """)
except Exception as e:
    print(e)

conn.close()

