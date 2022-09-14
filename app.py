from flask import Flask, render_template , request
from music import checker , sercher , lists

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rec" , methods = ["POST" , "GET"])
def rec():
    if request.method == "POST":
        na = request.form["music_id"]
        if checker(na) == 1:
            boom = 100
            n, g, r, p = sercher(na)
            return render_template("recom.html", n= n , g = g, boom = boom , r = r , p = p)
        else:
            boom = 420
            return render_template("recom.html",boom = boom )


    boom = 0
    return render_template("recom.html", boom = boom)


@app.route("/list")
def list():
    a, g = lists()

    return render_template("list.html", a = a , g = g)



if __name__ == "__main__":
    app.run(debug=False)
