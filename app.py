from flask import Flask, render_template, url_for, request, redirect
# from affirm import return_affirmations

# import requests

app = Flask(__name__, template_folder='templates')

 # grievance = ""
    # visible = False
    # if request.method == 'POST':
    #     print("POSTED")
    #     grievance = request.form['grievance']
    #     visible = True
    # print(visible)
    # return render_template("index.html", grievance=grievance, visible=visible)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("login-sign-up.html")


if __name__ == "__main__":
    print("running Affirm")
    app.run(debug=True)

