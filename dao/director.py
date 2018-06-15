from dao import connection
from model import director


def get_director(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT * from director WHERE id ={id}")
    data = cursor.fetchone()
    return data
