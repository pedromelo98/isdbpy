from dao import connection
from model import actor


def get_actor(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT name, biografy, birthplace, birth, picture FROM actors WHERE id={id}")
    data = cursor.fetchone()
    actor_by_id = actor.Actor(id, data[0], data[1], data[2], data[3], data[4])
    return actor_by_id


def get_actor_by_name(app, name):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT * FROM actors WHERE name LIKE '%{name}%'")
    data = cursor.fetchone()
    actor_by_name = actor.Actor(data[0], data[1], data[2], data[3], data[4], data[5])
    return actor_by_name
