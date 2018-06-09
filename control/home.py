from control import app
from flask import render_template, request
from dao import connection
from dao import tv_show
from dao import genre

connect, cursor = connection.get_connection(app)

cursor.execute(f"SELECT * FROM tv_shows")
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
    return render_template('tv_show.html', tv_show=tvs, tv_shows=data, genres=genres, genre=genre_by_id)

