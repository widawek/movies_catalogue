from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def homepage():
    movies = [
        ("Matrix", "https://fwcdn.pl/fpo/06/28/628/7685907.6.jpg",
         "https://www.filmweb.pl/film/Matrix-1999-628"),
        ("The Godfather", "https://fwcdn.pl/fpo/10/89/1089/7196615.6.jpg",
         "https://www.filmweb.pl/film/Ojciec+chrzestny-1972-1089"),
        ("Forest Gump", "https://fwcdn.pl/fpo/09/98/998/8021615.6.jpg",
         "https://www.filmweb.pl/film/Forrest+Gump-1994-998"),
        ("Attack of the Killer Donuts", "https://fwcdn.pl/fpo/79/41/747941/7774868.6.jpg",
         "https://www.filmweb.pl/film/Atak+krwio%C5%BCerczych+donat%C3%B3w-2016-747941")
              ]
    return render_template("homepage.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
