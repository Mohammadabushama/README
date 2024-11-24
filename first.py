from flask import Flask

def create_app():
    app = Flask(__name__)
    # Additional setup can go here

    app.route('/')
    
    return app
    