from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .database import db
from flask_login import login_user, logout_user, login_required, current_user
from . import auth

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):

            flash('Please check your login details and try again.', 'error')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('views.userprofile'))

    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.register'))

        new_user = User(name=name, email=email, password_hash=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        flash('Account created! You can now login', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home_page'))

@auth.route('/')
def index():
    return render_template('index.html')

@auth.route('/home_page')
def home_page():
    return render_template('home_page.html')

@auth.route('/about')
def about():
    return render_template('about.html')

@auth.route('/services')
def services():
    return render_template('services.html')

@auth.route('/hub')
def hub():
    return render_template('hub.html')

@auth.route('/contact')
def contact():
    return render_template('contact.html')

@auth.route('/blog')
def blog():
    return render_template('blog.html')

@auth.route('/userprofile')
@login_required
def userprofile():
    return render_template('userprofile.html')

@auth.route('/my_dashboard')
def my_dashboard():
    return render_template('my_dashboard.html')

@auth.route('/submit-form', methods=['GET', 'POST'])
@login_required
def submit_form():
    user_id = current_user.id
    user = User.query.get(user_id)

    if request.method == 'POST':
        first_name = request.form.get('firstname')
        last_name = request.form.get('secondname')
        mobile_number = request.form.get('phone')
        duration_of_stay = request.form.get('duration')
        education_level = request.form.get('education')
        course_studied = request.form.get('course')
        university_grad_year = request.form.get('university')
        interest_areas = request.form.get('interests')

        new_user = User(first_name=first_name, last_name=last_name, mobile_number=mobile_number, 
                duration_of_stay=duration_of_stay, education_level=education_level, 
                course_studied=course_studied, university_grad_year=university_grad_year,
                interests=interest_areas)


        db.session.commit()

        return redirect(url_for('auth.profile'))

    return render_template('submit_form.html')


