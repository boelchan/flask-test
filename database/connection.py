from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_app(app):
    migrate = Migrate(app, db)
    migrate.init_app(app)

    db.init_app(app)
    # db.create_all(app)
