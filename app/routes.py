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
            return redirect(url_for('main_routes.dashboard'))
        
        else:
            return "Failed to login, check your credentials"
        
    return render_template('login.html')

@main_routes.route('/dashboard')
def dashboard():
    username = session.get('username')  # Get username from session
    return render_template('dashboard.html', username=username)