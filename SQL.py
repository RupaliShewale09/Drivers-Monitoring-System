import sqlite3
from datetime import datetime, date  

class DrowsinessDatabase:
    def __init__(self, db_name="drowsiness_logs.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.table_name = self.get_today_table_name()
        self.create_table_for_today()
        self.create_events_table()

    def get_today_table_name(self):
        today = datetime.now().strftime("%Y_%m_%d")
        return f"drowsiness_{today}"

    def create_events_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS drowsiness_events (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                timestamp TEXT,
                                ear REAL,
                                mar REAL,
                                yaw_angle REAL,
                                status TEXT)''')
        self.conn.commit()

    def create_table_for_today(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                timestamp TEXT,
                                ear REAL,
                                mar REAL,
                                yaw_angle REAL,
                                status TEXT)''')
        self.conn.commit()

    def log_drowsiness(self, ear, mar, yaw_angle, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.cursor.execute("INSERT INTO drowsiness_events (timestamp, ear, mar, yaw_angle, status) VALUES (?, ?, ?, ?, ?)",
                           (timestamp, ear, mar, yaw_angle, status))
        self.conn.commit()
        
        self.cursor.execute(f"INSERT INTO {self.table_name} (timestamp, ear, mar, yaw_angle, status) VALUES (?, ?, ?, ?, ?)",
                            (timestamp, ear, mar, yaw_angle, status))
        self.conn.commit()

    def fetch_today_logs(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
