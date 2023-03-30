from flask import Flask, request, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
import MySQLdb.cursors
import re  

app = Flask(__name__, template_folder='templates')

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@#Linkedin1",
    database="user_profile_db"
)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
