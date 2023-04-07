from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json
from flask_mysqldb import MySQL
from website import db
import MySQLdb

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home_page.html')

@views.route('/home_page')
def home_page():
    return render_template('home_page.html')


@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/services')
def services():
    return render_template('services.html')

@views.route('/hub')
def hub():
    return render_template('hub.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/blog')
def blog():
    return render_template('blog.html')

@views.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = db.engine.raw_connection().cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
@views.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  
@views.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = db.engine.raw_connection().cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user (name, email, password) VALUES (%s, %s, %s)', (userName, email, password,))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

    #Dashboard
@views.route('/my_dashboard')
@login_required
def my_dashboard():
    return render_template('my_dashboard.html')