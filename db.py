from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'dibyanshu#75@18ram'
    app.config['MYSQL_DB'] = 'auth_db'

    mysql.init_app(app)