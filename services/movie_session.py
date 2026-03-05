import datetime
from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
    )

    return new_movie_session


def get_movies_sessions(
        session_date: datetime.date = None
) -> QuerySet[MovieSession]:
    if session_date:
        sessions = MovieSession.objects.all()
        return sessions.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession | None:
    if movie_session_id:
        return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: Movie = None,
        cinema_hall_id: CinemaHall = None
) -> None:
    if show_time:
        sessions = MovieSession.objects.filter(id=session_id)
        sessions.update(show_time=show_time)
    if movie_id:
        sessions = MovieSession.objects.filter(id=session_id)
        sessions.update(movie=movie_id)
    if cinema_hall_id:
        sessions = MovieSession.objects.filter(id=session_id)
        sessions.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    sessions = MovieSession.objects.filter(id=session_id)
    sessions.delete()
