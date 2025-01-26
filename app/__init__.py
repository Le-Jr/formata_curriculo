from flask import Flask
from .routes import main
from .config import Config
from .services.curriculum_service import init_mongo





def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_mongo(app)

    app.register_blueprint(main) 
    return app



