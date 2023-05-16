from flask import Flask, render_template, url_for, request, redirect
# from affirm import return_affirmations 

# import requests

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=["POST", "GET"])
def index():
    grievance = ""
    visible = False
    if request.method == 'POST':
        print("POSTED")
        grievance = request.form['grievance']
        visible = True
    print(visible)
    return render_template("index.html", grievance=grievance, visible=visible)


if __name__ == "__main__":
    print("hi")
    app.run(debug=True)
