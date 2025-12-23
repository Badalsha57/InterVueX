import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("interview.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            question TEXT,
            answer TEXT,
            score REAL,
            confidence REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_interview(role, question, answer, score, confidence):
    conn = sqlite3.connect("interview.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO interviews (role, question, answer, score, confidence, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (role, question, answer, score, confidence, datetime.now()))
    conn.commit()
    conn.close()
