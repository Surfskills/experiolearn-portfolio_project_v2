from flask import Flask, request, jsonify, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
import mysql.connector
import MySQLdb.cursors
import re  

app = Flask(__name__, template_folder='templates')

app = Flask(__name__)
bootstrap = Bootstrap(app)


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

@app.route('/home_page')
def home_page():
    return render_template('home_page.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/hub')
def hub():
    return render_template('hub.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

if __name__ == '__main__':
    app.run(debug=True)
