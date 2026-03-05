from typing import List
from django.db.models import QuerySet

from db.models import Genre, Actor, Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()

    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    movies = Movie.objects.all()
    return movies.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        for genre_id in genres_ids:
            new_movie.genres.add(genre_id)

    if actors_ids:
        for actor_id in actors_ids:
            new_movie.actors.add(actor_id)

    return new_movie
