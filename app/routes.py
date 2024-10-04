from flask import Blueprint, render_template, request, redirect, url_for, session
import pronotepy

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return "Welcome to this third party pronote client!"

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login
        username = request.form.get('username')
        password = request.form.get('password')
        pronote_url = request.form.get('pronote_url')

        client = pronotepy.Client(pronote_url, username, password)

        if client.logged_in:
            session['username'] = username  # Store username in session
            session['full_name'] = client.info.name
            session['profile_picture'] = client.info.profile_picture.url
            return redirect(url_for('main_routes.dashboard'))
        
        else:
            return "Failed to login, check your credentials"
        
    return render_template('login.html')

@main_routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', 
                           username=session.get('username'), 
                           full_name=session.get('full_name'),
                           profile_picture=session.get('profile_picture'),
                           )
