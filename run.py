from app import create_app

app = create_app()

if __name__ == '__main__':
    app.secret_key = 'your_secret_key_here' # Trust me bro haha
    app.run(debug=True)