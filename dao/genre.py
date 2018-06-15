from dao import connection
from model import genre


def get_all_genres(app):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT * FROM genres")
    data = cursor.fetchall()
    return data


def get_genre(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT name FROM genres WHERE id={id}")
    data = cursor.fetchone()
    genre_by_id = genre.Genre(id, data[0])
    return genre_by_id


def get_genre_by_name(app, name):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT * FROM genres WHERE name='{name}'")
    data = cursor.fetchone()
    genre_by_name = genre.Genre(data[0], data[1])
    return genre_by_name
