from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
from flask_session import Session
import MySQLdb.cursors
import re
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = "/tmp/flask_session"
app.config["SESSION_FILE_THRESHOLD"] = 100

Session(app)

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'experiolearn'



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/experiolearn'



from website import create_app
app = create_app()
app.secret_key = 'xyzsdfg' 


if __name__ == "__main__":
    app.run()
