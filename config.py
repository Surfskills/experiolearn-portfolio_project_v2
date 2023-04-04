import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re  

# MySQL configuration
mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '@#Linkedin1'
app.config['MYSQL_DATABASE_DB'] = 'user_profile_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
DB_PORT = 3306
mysql.init_app(app)

# Flask configuration
DEBUG = True
SECRET_KEY = 'my_secret_key'
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/user_profile_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
