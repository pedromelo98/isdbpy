from control import app
from flask import render_template, request
from dao import connection
from dao import tv_show

connect, cursor = connection.get_connection(app)

cursor.execute(f"SELECT * FROM tvshows")
data = cursor.fetchall()

@app.route('/')
def index():
    return render_template('index.html', tv_shows=data)


@app.route('/tv_shows')
def tv_shows():
    return render_template('tv_shows.html', tv_shows=data)


@app.route("/tv_show")
def _tv_show():
    id = request.args.get("id")
    tvs = tv_show.get_tv_show(app, id)
    return render_template('tv_show.html', tv_show=tvs, tv_shows=data)

