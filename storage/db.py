"""

initialize SQLite database and schema
insert lookup records
retrieve prior records by ABN or recent history
store metadata such as timestamps, status, export path, and screenshot path

The storage layer should hide SQL details from the service and CLI layers.

"""

import sqlite3

dbList = []
recordList = []

#init sqlite connection and create tables if they dont exist, this is called at the start of the program in main.py, so its ready to go when the user starts interacting with the CLI
def initDatabase():
    conn = sqlite3.connect("abnlookup.db")
  
    cursor = conn.cursor()

    # Create the records table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            abn TEXT NOT NULL,
            name TEXT,
            status TEXT,
            timestamp TEXT,
            export_path TEXT,
            screenshot_path TEXT
        )
    ''')

    conn.commit()
    conn.close()


#storage for records, metadata and logs,




