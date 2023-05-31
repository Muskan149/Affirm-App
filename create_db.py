import psycopg2
import os
from datetime import datetime

DATABASE_URL = os.environ.get("DATABASE_URL")

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
