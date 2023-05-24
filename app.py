from flask import Flask, render_template, url_for, request, redirect
from time import sleep
from affirm import return_affirmations

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=["POST", "GET"])
def index():
    affirmations = []
    grievance = ""
    flashMessage = False
    requestPosted = False
    if request.method == 'POST':
        requestPosted = True
        print(requestPosted)
        print( not flashMessage)
        grievance = request.form['grievance']
        sleep(4.2)
        affirmations = [grievance, grievance, grievance]
        # affirmations = return_affirmations(grievance)
        flashMessage = True
    print(flashMessage)
    print(grievance)
    return render_template("index.html", grievance=grievance, affirmations=affirmations, flashMessage=flashMessage, requestPosted=requestPosted)


if __name__ == "__main__":
    app.run(debug=True)
