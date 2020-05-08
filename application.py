from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cookingblog():
    return render_template("cookingblog.html")

@app.route("/ramen")
def ramen():
    return render_template("ramen.html")
