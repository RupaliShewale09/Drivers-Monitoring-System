import sqlite3
from datetime import datetime

class DrowsinessDatabase:
    def __init__(self, db_name="drowsiness_logs.db"):
        self.conn = sqlite3.connect(db_name) 
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create the table for logging drowsiness events
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS drowsiness_events (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                timestamp TEXT,
                                ear REAL,
                                mar REAL,
                                yaw_angle REAL,
                                status TEXT)''')
        self.conn.commit()

    def log_drowsiness(self, ear, mar,yaw_angle, status):
        # Insert a drowsiness event into the database
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO drowsiness_events (timestamp, ear, mar, yaw_angle, status) VALUES (?, ?, ?, ?, ?)",
                            (timestamp, ear, mar, yaw_angle, status))
        self.conn.commit()

    def fetch_logs(self):
        self.cursor.execute("SELECT * FROM drowsiness_events")
        return self.cursor.fetchall()  # Returns list of tuples

    def close_connection(self):
        self.conn.close()
