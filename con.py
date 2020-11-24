from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "admin"
app.config["MYSQL_DATABASE_PASSWORD"] = "CAperez26"
app.config["MYSQL_DATABASE_DB"] = "recursos"
app.config["MYSQL_DATABASE_HOST"] = "dbcarlosp.cskfb61apkl5.us-east-2.rds.amazonaws.com"
app.config['MYSQL_DATABASE_SOCKET'] = None

mysql.init_app(app)