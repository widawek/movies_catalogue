import requests
import os
import json

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


def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
