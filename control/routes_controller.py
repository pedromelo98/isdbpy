from control import app
from flask import render_template, request
from dao import connection, tv_show, genre, actor

connect, cursor = connection.get_connection(app)

cursor.execute(f"SELECT * FROM tv_shows ORDER BY name")
data = cursor.fetchall()

cursor.execute(f"SELECT * FROM genres")
genres = cursor.fetchall()

@app.route('/')
def index():
    return render_template('index.html', tv_shows=data, genres=genres)


@app.route('/tv_shows')
def tv_shows():
    return render_template('tv_shows.html', tv_shows=data, genres=genres)


@app.route("/tv_show")
def _tv_show():
    id = request.args.get("id")
    tvs = tv_show.get_tv_show(app, id)
    genre_by_id = genre.get_genre(app, tvs.genre)
    cursor.execute(f"SELECT id_actor, id_director FROM cast WHERE id_tvshow ={id}")
    cast = cursor.fetchall()
    actors = []
    for people in cast:
        act = actor.get_actor(app,  people[0])
        actors.append(act)
    cursor.execute(f"SELECT * from director WHERE id ={cast[0][1]}")
    director = cursor.fetchone()
    return render_template('tv_show.html', tv_show=tvs, tv_shows=data, genres=genres, genre=genre_by_id, actors=actors, director=director)


@app.route("/actor")
def _actor():
    id = request.args.get("id")
    actor_by_id = actor.get_actor(app, id)
    return render_template('actor.html', tv_shows=data, genres=genres, actor=actor_by_id)
