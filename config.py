import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re  

# MySQL configuration
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '@#Linkedin1')
DB_NAME = 'user_profile_db'

# Flask configuration
DEBUG = True
SECRET_KEY = 'my_secret_key'
SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
