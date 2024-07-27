from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.configs.db import ConfigDB
import logging

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigDB)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.routes.user_router import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')
    return app
