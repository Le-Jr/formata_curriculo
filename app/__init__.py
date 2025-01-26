from flask import Flask
from .routes import main
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(main) 
    return app



