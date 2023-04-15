from flask import Blueprint, render_template, flash
from flask_login import current_user
from flask import session
from flask import request
from .models import Note
from . import db
import json



views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home_page.html')

@views.route('/home_page')
def home_page():
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        return render_template('home_age.html', logged_in=True, username=user.name)
    else:
        return render_template('home_page.html', logged_in=False)

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/services')
def services():
    return render_template('services.html')

@views.route('/hub')
def hub():
    return render_template('hub.html')

@views.route('/blog')
def contact():
    return render_template('blog.html')

@views.route('/userprofile')
def userprofile():
    return render_template('userprofile.html')



@views.route('/my_dashboard')
def my_dashboard():
    return render_template('my_dashboard.html')


@views.route('/profile')
def profile():
    return render_template('profile.html')



@views.route('/submit_form')
def submit_form():
    return render_template('submit_form.html')

@views.route('/deliverable_form', methods=['GET', 'POST'])
def deliverable_form():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("deliverable_form.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})