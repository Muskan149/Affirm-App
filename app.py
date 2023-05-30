from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

from time import sleep
from affirm import return_affirmations
import psycopg2


app = Flask(__name__, template_folder='templates')


DATABASE_URL = os.environ.get("DATABASE_URL")
con = psycopg2.connect(DATABASE_URL)
cur = con.cursor()

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# Create the AffirmationGenerator table
table_create_query = """
    CREATE TABLE AffirmationGenerator (
        ID SERIAL PRIMARY KEY,
        grievance TEXT,
        affirmation_1 TEXT,
        affirmation_2 TEXT,
        affirmation_3 TEXT,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
"""


@app.route("/", methods=["POST", "GET"])
def index():
    affirmations = []
    grievance = ""
    flashMessage = False
    requestPosted = False
    if request.method == 'POST':
        requestPosted = True
        grievance = request.form['grievance']

        affirmations = return_affirmations(grievance)
        # affirmations = [grievance, grievance, grievance]

        # new_session = AffirmationGenerator(
        #     grievance=grievance,
        #     affirmation_1=affirmations[0],
        #     affirmation_2=affirmations[1],
        #     affirmation_3=affirmations[2]
        # )
        flashMessage = True

        # try:
        #     print("committing to DB..")
        #     db.session.add(new_session)
        #     db.session.commit()
        # except:
        #     print("failed")

    return render_template("index.html", grievance=grievance, affirmations=affirmations, flashMessage=flashMessage, requestPosted=requestPosted)


if __name__ == "__main__":
    print("starting app...")
    app.run(debug=True, port=3413)
