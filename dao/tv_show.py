from dao import connection
from model import tv_show


def get_tv_show(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT name, description, cast, duration, poster, trailer FROM tvshows WHERE id={id}")
    data = cursor.fetchone()
    tvshow = tv_show.TvShow(id, data[0], data[1], data[2], data[3], data[4], data[5])
    return tvshow
