from flask import Flask, render_template, url_for
import tmdb_client

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/")
def default_homepage():
    # Możesz wybrać domyślną kategorię lub obsłużyć to inaczej
    default_category = 'popular'
    movies = tmdb_client.get_movies(8, default_category)
    return render_template("homepage.html", movies=movies,
                           category=default_category)


@app.route("/<category>")
def homepage(category):
    movies = tmdb_client.get_movies(8, category)
    return render_template("homepage.html", movies=movies, category=category)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    image = tmdb_client.get_random_image(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast,
                           image=image)


if __name__ == "__main__":
    app.run(debug=True)
