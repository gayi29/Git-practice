# app/database.py

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("data/jobs.db")
cursor = conn.cursor()

# Initialize database schema if needed
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_postings (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        requirements TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_applications (
        id INTEGER PRIMARY KEY,
        job_id INTEGER,
        applicant_name TEXT,
        applicant_email TEXT,
        resume TEXT,
        FOREIGN KEY (job_id) REFERENCES job_postings(id)
    )
""")

conn.commit()
