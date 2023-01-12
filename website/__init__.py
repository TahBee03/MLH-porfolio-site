from flask import Flask # Import Flask
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy
from os import path

db = SQLAlchemy() # Defines database
DB_NAME = 'portfolio.db' # Sets database name

# Function that creates Flask app
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.dirname(__file__), DB_NAME) # Specifies the location of the database
    db.init_app(app) # Links database with app

    from .views import views
    app.register_blueprint(views, url_prefix='/') # Registers blueprint

    from .models import Post
    with app.app_context():
        db.create_all()

    return app