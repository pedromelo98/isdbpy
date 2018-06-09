from dao import connection
from model import genre


def get_genre(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT name FROM genres WHERE id={id}")
    data = cursor.fetchone()
    genre_by_id = genre.Genre(id, data[0])
    return genre_by_id
