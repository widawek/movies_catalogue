from flask import Flask, render_template, redirect
import tmdb_client

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


def get_movie_info(movie):
    movie_info = {}
    movie_info['title'] = movie['title']
    movie_info['poster_path'] = movie['poster_path']
    return movie_info


@app.route("/")
def homepage():
    movies = tmdb_client.get_movies(8)
    return render_template("homepage.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
