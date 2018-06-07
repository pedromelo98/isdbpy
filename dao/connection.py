from flaskext.mysql import MySQL


def get_connection(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'isdb'

    mysql = MySQL()
    mysql.init_app(app)

    connection = mysql.connect()
    cursor = connection.cursor()

    return connection, cursor

