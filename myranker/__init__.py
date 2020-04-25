from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myranker.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.url_map.strict_slashes = False

    db.init_app(app)

    from myranker.main.routes import main
    from myranker.ranker.routes import ranker
    from myranker.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(ranker)
    app.register_blueprint(errors)

    return app
