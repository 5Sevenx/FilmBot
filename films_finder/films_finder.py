from io import BytesIO
from DB.bd_commands import get_film_name, add_film
from bot.bot import *
import requests

from fast_methods.fast_methods import wich_lan

load_dotenv()

TOKEN = os.getenv("FILMS_TOKEN")
TRASH_RECEIVER = os.getenv("TRASH_RECEIVER")


def get_geners(language):
    res = requests.get(
        "https://api.themoviedb.org/3/genre/movie/list",
        params={"api_key": TOKEN, "language": language}
    ).json()
    return {g['id']: g['name'] for g in res['genres']}



def search_movie(user_input,language):
    lan = wich_lan(language)
    result = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        params={"api_key":TOKEN, "query": user_input,"language":lan}
    ).json()

    if not result['results']:
        return None

    movie = result['results'][0]
    if get_film_name(movie['title'],lan) is None:
        genres = get_geners(lan)
        movie_genres = [genres[g] for g in movie['genre_ids'] if g in genres]
        title, overview, poster, year, genres = (
            movie['title'],
            movie['overview'],
            f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else None,
            movie['release_date'].split('-')[0] if movie.get('release_date') else '',
            movie_genres
        )
        resp = requests.get(poster)
        image_bytes = BytesIO(resp.content)
        messages = bot.send_photo(chat_id=TRASH_RECEIVER, photo=image_bytes)
        file_id = messages.photo[-1].file_id

        if lan == 'us':
            result = requests.get(
                "https://api.themoviedb.org/3/search/movie",
                params={"api_key": TOKEN, "query": user_input, "language": 'ru'}
            ).json()
            movie = result['results'][0]
            genres = get_geners('ru')
            movie_genres = [genres[g] for g in movie['genre_ids'] if g in genres]
            title_ru,overview_ru,genres_ru = (
                movie['title'],
                movie['overview'],
                movie_genres
            )
            add_film(title,overview,file_id,title_ru,genres,overview_ru,genres_ru)
        else:
            result = requests.get(
                "https://api.themoviedb.org/3/search/movie",
                params={"api_key": TOKEN, "query": user_input, "language": 'us'}
            ).json()
            movie = result['results'][0]
            genres = get_geners('us')
            movie_genres = [genres[g] for g in movie['genre_ids'] if g in genres]
            title_us, overview_us, genres_us = (
                movie['title'],
                movie['overview'],
                movie_genres
            )
            add_film(title_us,overview_us,file_id,title,genres_us,overview,genres)

        print(file_id)



