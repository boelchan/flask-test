from flask import Flask
from database import database
from apps.crud.views import crud
from apps.auth.views import auth


def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    app.config.from_object("config.DevelopmentConfig")

    # setup all our dependencies
    database.init_app(app)

    # register blueprint
    app.register_blueprint(crud)
    app.register_blueprint(auth)

    return app


if __name__ == "__main__":
    create_app().run()
