from flask import Flask, request, session, render_template, redirect, url_for
from config import db
from models import User, UserStory
from werkzeug.security import generate_password_hash

import os
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testenvironment.db'
app.config['SECRET_KEY'] = 'abcdefghiABCDEFGHI1234554321'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)

with app.app_context():
    db.create_all()

    # create user
    if not User.query.first():
        with open('data/users.json') as file:
            data = json.load(file)
            
            hashed_password = generate_password_hash('password', method='scrypt')

            for item in data:
                new_user = User(
                    username=item['name'],
                    password_hash=hashed_password
                )
                db.session.add(new_user)
            
            db.session.commit()
            print("Benutzer erstellt.")
    else:
        print("Benutzer existiert bereits.")

    # create user stories
    if not UserStory.query.first():
        with open('data/user_stories.json') as file:
            data = json.load(file)
            
            for item in data:
                story = UserStory(
                    title=item['title'],
                    description=item['description']
                )
                db.session.add(story)
            
            db.session.commit()
            print("User Stories erstellt.")
    else:
        print("User Stories existieren bereits.")

@app.route('/')
def home():
    user_stories = UserStory.query.all()
    return render_template('login.html', user_stories=user_stories)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return redirect(url_for('profile'))
    else:
        return '''
                Falscher Benutzername oder Passwort. 
                <a href="/profile">Zurück zum Profil</a>
                ''', 401
    
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    user = User.query.get(session['user_id'])
    user_stories = UserStory.query.all()

    if user:
        return render_template('profile.html', user=user, user_stories=user_stories)
    else:
        return redirect(url_for('home'))
    
@app.route('/change-password', methods=['POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    user = User.query.get(session['user_id'])
    if not user:
        return '''
                Benutzer nicht gefunden. 
                <a href="/profile">Zurück zum Profil</a>
                ''', 404

    new_password = request.form['password']
    confirm_password = request.form['confirm_password']

    if new_password != confirm_password:
        return '''
                Passwörter stimmen nicht überein. 
                <a href="/profile">Zurück zum Profil</a>
                ''', 400

    user.password_hash = generate_password_hash(new_password)
    db.session.commit()

    return redirect(url_for('profile'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    if 'profile_image' not in request.files:
        return '''
                Keine Datei ausgewählt. 
                <a href="/profile">Zurück zum Profil</a>
                ''', 400

    file = request.files['profile_image']

    if file.filename == '':
        return '''
                Keine Datei ausgewählt. 
                <a href="/profile">Zurück zum Profil</a>
                ''', 400

    if file and allowed_file(file.filename):
        _, file_extension = os.path.splitext(file.filename)
        filename = f"profile_image_{session['user_id']}{file_extension}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('profile'))

    return '''
            Ungültiges Dateiformat. 
            <a href="/profile">Zurück zum Profil</a>
            ''', 400

@app.route('/reset-password')
def reset_password():
    users = User.query.all()
    if users:
        for user in users:
            new_password_hash = generate_password_hash('password')
            user.password_hash = new_password_hash
            db.session.commit()
        return '''
                Passwort wurde zurückgesetzt. 
                <a href="/">Zurück zur Login-Seite</a>
                ''', 200
    else:
        return '''
               Benutzer nicht gefunden. 
               <a href="/">Zurück zur Login-Seite</a>
               ''', 200

if __name__ == '__main__':
    app.run(debug=True)
