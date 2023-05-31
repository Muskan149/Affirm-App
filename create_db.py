import psycopg2
import os
from datetime import datetime

DATABASE_URL = "postgres://imvazwungjfjxx:37aa9b99e512dfe7bb3c27389c136f5985e8724e64e38450ab71f2cc7a18b02f@ec2-34-197-91-131.compute-1.amazonaws.com:5432/darklg0coehpt8"

conn = psycopg2.connect(DATABASE_URL.strip())
cursor = conn.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE AffirmationsGenerator (
        id SERIAL PRIMARY KEY,
        grievance TEXT,
        aff1 TEXT,
        aff2 TEXT,
        aff3 TEXT,
        date_created TIMESTAMP DEFAULT NULL
    );
""")

conn.commit()
conn.close()
