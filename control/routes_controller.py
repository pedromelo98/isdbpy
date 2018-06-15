from control import app
from flask import render_template, request
from dao import tv_show, genre, actor, cast, director

@app.route('/')
def index():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    return render_template('index.html', tv_shows=data, genres=genres)


@app.route('/tv_shows')
def tv_shows():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    return render_template('tv_shows.html', tv_shows=data, genres=genres)


@app.route("/tv_show")
def _tv_show():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    id = request.args.get("id")
    tvs = tv_show.get_tv_show(app, id)
    genre_by_id = genre.get_genre(app, tvs.genre)
    cast_ = cast.get_cast_ad(app, id)
    actors = []
    director_ = []
    if cast_:
        for person in cast_:
            act = actor.get_actor(app,  person[0])
            actors.append(act)
        director_ = director.get_director(app, cast_[0][1])
    return render_template('tv_show.html', tv_show=tvs, tv_shows=data, genres=genres, genre=genre_by_id, actors=actors, director=director_)


@app.route("/actor")
def _actor():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    id = request.args.get("id")
    actor_by_id = actor.get_actor(app, id)
    return render_template('actor.html', tv_shows=data, genres=genres, actor=actor_by_id)


@app.route("/tv_show_by_genre")
def tv_show_by_genre():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    id = request.args.get("id")
    tv_shows_by_genre_id = tv_show.get_tv_show_by_genre(app, id)
    genre_by_id = genre.get_genre(app, id)
    return render_template('tv_show_by_genre.html', tv_shows=data, genres=genres, genre=genre_by_id, tv_shows_by_genre_id=tv_shows_by_genre_id)


@app.route("/tv_show_by_name")
def _tv_show_by_name():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    name = request.args.get("name")
    tvs = tv_show.get_tv_show_by_name(app, name)
    genre_by_id = genre.get_genre(app, tvs.genre)
    cast_ = cast.get_cast_ad(app, tvs.id)
    actors = []
    director_ = []
    if cast_:
        for people in cast_:
            act = actor.get_actor(app,  people[0])
            actors.append(act)
        director_ = director.get_director(app, cast_[0][1])
    return render_template('tv_show.html', tv_show=tvs, tv_shows=data, genres=genres, genre=genre_by_id, actors=actors, director=director_)


@app.route('/insert_tv_show')
def insert_tv_show():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    return render_template('insert_tv_show.html', tv_shows=data, genres=genres)


@app.route('/insert_success')
def insert_success():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    name = request.args.get("name")
    description = request.args.get("description")
    seasons = request.args.get("seasons")
    birth = request.args.get("birth")
    poster = request.args.get("poster")
    trailer = request.args.get("trailer")
    genre_name = request.args.get("genre")
    genre_by_name = genre.get_genre_by_name(app, genre_name)
    tv_show.insert_tv_show(app, name, description, seasons, birth, poster, trailer, genre_by_name.id)
    return render_template('index.html', tv_shows=data, genres=genres)


@app.route('/delete_tv_show')
def delete_tv_show():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    id = request.args.get("id")
    tv_show.delete_tv_show(app, id)
    return render_template('tv_shows.html', tv_shows=data, genres=genres)


@app.route("/actor_by_name")
def _actor_by_name():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    name = request.args.get("name")
    actor_by_name = actor.get_actor_by_name(app, name)
    return render_template('actor.html', tv_shows=data, genres=genres, actor=actor_by_name)


@app.route('/edit_tv_show')
def edit_tv_show():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    id = request.args.get("id")
    tvs = tv_show.get_tv_show(app, id)
    genre_by_id = genre.get_genre(app, tvs.genre)
    return render_template('edit_tv_show.html', tv_shows=data, genres=genres, tv_show=tvs, genre=genre_by_id)


@app.route('/edit_success')
def edit_success():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    id = request.args.get("id")
    name = request.args.get("name")
    description = request.args.get("description")
    seasons = request.args.get("seasons")
    birth = request.args.get("birth")
    poster = request.args.get("poster")
    trailer = request.args.get("trailer")
    genre_name = request.args.get("genre")
    genre_by_name = genre.get_genre_by_name(app, genre_name)
    tv_show.edit_tv_show(app, id, name, description, seasons, birth, poster, trailer, genre_by_name.id)
    return render_template('index.html', tv_shows=data, genres=genres)


@app.route('/actors')
def actors_():
    data = tv_show.get_all_tv_show(app)
    genres = genre.get_all_genres(app)
    actors = actor.get_all_actors(app)
    return render_template('actors.html', tv_shows=data, genres=genres, actors=actors)
