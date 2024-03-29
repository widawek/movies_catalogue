import requests
import os
import json
import random

current_directory = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_directory, 'instance/config.cfg')

if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        config_data = json.load(f)
else:
    config_data = {}

user = config_data.get('user')
api_key = config_data.get('api_key')
token = config_data.get('access_token')


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_by_category(category):
    endpoint = f"https://api.themoviedb.org/3/movie/{category}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies(how_many, category='popular'):
    if how_many > 20:
        how_many = 20
    data = get_movies_by_category(category)['results']
    random.shuffle(data)
    return data[:how_many]


def get_configuration_info():
    endpoint = "https://api.themoviedb.org/3/configuration"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=4))


def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    cast = response.json()['cast']
    return cast


def get_random_image(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    images = response.json()['backdrops']
    return random.choice(images)
