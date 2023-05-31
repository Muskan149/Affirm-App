from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

from time import sleep
from affirm import return_affirmations

import psycopg2
from datetime import datetime


app = Flask(__name__, template_folder='templates')

TEMPERATURE = 0.5

DATABASE_URL = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL.strip())
cursor = conn.cursor()


@app.route("/", methods=["POST", "GET"])
def index():
    affirmations = []
    grievance = ""
    flashMessage = False
    requestPosted = False
    if request.method == 'POST':
        requestPosted = True
        grievance = request.form['grievance']

        affirmations = return_affirmations(
            grievance.lower().strip(), TEMPERATURE)

        # Insert records into the table with the current date and time
        records = [(grievance, affirmations[0], affirmations[1],
                    affirmations[2], datetime.now())]
        for record in records:
            cursor.execute("""
                INSERT INTO AffirmationsGenerator (grievance, aff1, aff2, aff3, date_created)
                VALUES (%s, %s, %s, %s, %s);
            """, record)

        conn.commit()
        conn.close()

        flashMessage = True

    return render_template("index.html", grievance=grievance, affirmations=affirmations, flashMessage=flashMessage, requestPosted=requestPosted)


if __name__ == "__main__":
    print("starting app...")
    app.run(debug=True, port=3413)
