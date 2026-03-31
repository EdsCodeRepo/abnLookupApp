"""

initialize SQLite database and schema
insert lookup records
retrieve prior records by ABN or recent history
store metadata such as timestamps, status, export path, and screenshot path

The storage layer should hide SQL details from the service and CLI layers.

"""

import sqlite3

#init sqlite connection and create tables if they dont exist, this is called at the start of the program in main.py, so its ready to go when the user starts interacting with the CLI
def initDatabase():
    conn = sqlite3.connect("abnlookup.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            abn TEXT,
            name TEXT,
            status TEXT,
            entityType TEXT,
            timestamp TEXT,
            export_path TEXT,
            screenshot_path TEXT
        )
    """)
    conn.commit()
    conn.close()

def saveRecord(recordedData):
    conn = sqlite3.connect("abnlookup.db")
    cursor = conn.cursor()
    # Create the records table if it doesn't exist
    
    cursor.execute(""" 
        INSERT INTO records(abn, name, status, entityType, timestamp, export_Path, screenshot_Path)
        VALUES (?, ?, ?, ?, ?, ?, ?) """,
       (
        recordedData['abn'],
        recordedData['name'], 
        recordedData['status'],
        recordedData['entityType'],
        recordedData['timestamp'],
        recordedData.get('exportPath'),
        recordedData.get('screenshotPath')
      ))

    conn.commit()
    recordId = cursor.lastrowid
    conn.close()
    return recordId


def getAllRecords():
    conn = sqlite3.connect("abnlookup.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT id, abn, name, status, entityType, timestamp, export_Path, screenshot_Path 
                      FROM records
                      ORDER BY id DESC
    """)               
    records = cursor.fetchall()
    conn.close()
    return records
#storage for records, metadata and logs,




