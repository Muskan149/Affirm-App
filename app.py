from flask import Flask, render_template, url_for, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

from time import sleep
from affirm import return_affirmations

app = Flask(__name__, template_folder='templates')

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://ckhujrdmpferqb:2705aba81a2cd017cebcf7fccd287660331016650776310ee86d65efa43a8d0a@ec2-3-208-74-199.compute-1.amazonaws.com:5432/d6gvklrdds9kho'
db = SQLAlchemy(app)


class AffirmationGenerator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grievance = db.Column(db.String(300), nullable=False)
    affirmation_1 = db.Column(db.String(300), nullable=False)
    affirmation_2 = db.Column(db.String(300), nullable=False)
    affirmation_3 = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Affirmations: {self.affirmation}>'


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
        new_session = AffirmationGenerator(
            grievance=grievance,
            affirmation_1=affirmations[0],
            affirmation_2=affirmations[1],
            affirmation_3=affirmations[2]
        )
        flashMessage = True

        try:
            print("committing to DB..")
            db.session.add(new_session)
            db.session.commit()
        except:
            print("failed")

    return render_template("index.html", grievance=grievance, affirmations=affirmations, flashMessage=flashMessage, requestPosted=requestPosted)


if __name__ == "__main__":
    print("starting app...")
    app.run(debug=True)
