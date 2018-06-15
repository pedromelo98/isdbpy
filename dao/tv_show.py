from dao import connection
from model import tv_show


def get_all_tv_show(app):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT * FROM tv_shows ORDER BY name")
    data = cursor.fetchall()
    return data


def get_tv_show(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT name, description, seasons, birth, poster, trailer, id_genre FROM tv_shows WHERE id={id}")
    data = cursor.fetchone()
    tvshow = tv_show.TvShow(id, data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    return tvshow


def get_tv_show_by_name(app, name):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT * FROM tv_shows WHERE name LIKE '%{name}%'")
    data = cursor.fetchone()
    tvshow = tv_show.TvShow(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    return tvshow


def get_tv_show_by_genre(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"SELECT * FROM tv_shows WHERE id_genre={id}")
    datas = cursor.fetchall()
    tv_shows = []
    for data in datas:
        _tv_show = tv_show.TvShow(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        tv_shows.append(_tv_show)

    return tv_shows


def insert_tv_show(app, name, description, seasons, birth, poster, trailer, id_genre):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"INSERT INTO tv_shows (name, description, seasons, birth, poster, trailer, id_genre) "
                   f"VALUES ('{name}', '{description}', '{seasons}', '{birth}', '{poster}', '{trailer}', '{id_genre}')")
    cursor.close()
    connect.commit()
    connect.close()


def delete_tv_show(app, id):
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"DELETE FROM tv_shows WHERE id={id}")
    connect.commit()


def edit_tv_show(app, id, name, description, seasons, birth, poster, trailer, id_genre):
    print(id)
    connect, cursor = connection.get_connection(app)
    cursor.execute(f"UPDATE tv_shows SET name='{name}', description='{description}', seasons='{seasons}', "
                   f"birth='{birth}', poster='{poster}', trailer='{trailer}', id_genre='{id_genre}' WHERE id={id}")
    connect.commit()
