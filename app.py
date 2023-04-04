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

# Route for rendering the registration form
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

# Route for handling the registration form submission
@app.route('/register', methods=['POST'])
def register_submit():
    email = request.form['email']
    password = request.form['password']
    confirmpassword = request.form['confirmpassword']
    
    # Check if password and confirm password fields match
    if password != confirmpassword:
        return 'Error: Passwords do not match'
    
    # Check if user with the same email already exists in the database
    if User.query.filter_by(email=email).first():
        return 'Error: User with the same email already exists'
    
    # Create a new user and add it to the database
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    
    return 'User registered successfully!'

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
