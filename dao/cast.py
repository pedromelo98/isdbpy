from dao import connection
from model import cast


def get_cast_ad(app, id_tvshow):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT id_actor, id_director FROM cast WHERE id_tvshow ={id_tvshow}")
    data = cursor.fetchall()
    return data