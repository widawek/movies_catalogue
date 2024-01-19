from flask import Flask, render_template, url_for
import tmdb_client

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/")
def homepage():
    movies = tmdb_client.get_movies(8)
    return render_template("homepage.html", movies=movies)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    return render_template("movie_details.html", movie=details)


if __name__ == "__main__":
    app.run(debug=True)
