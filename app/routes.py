from flask import Blueprint, render_template, request
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
            return "Logged in successfully"
        
        else:
            return "Failed to login, check your credentials"
        
    return '''
        <form method="post">
            Pronote URL: <input type="text" name="pronote_url"><br>
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''