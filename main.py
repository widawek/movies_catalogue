from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def homepage():
    movies = [_ for _ in range(10)]
    return render_template("homepage.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
