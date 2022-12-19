from flask import Flask
from database import connection
from apps.user.views import user
from apps.auth.views import auth


def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    app.config.from_object("config.DevelopmentConfig")

    # setup all our dependencies
    connection.init_app(app)

    # register blueprint
    app.register_blueprint(user)
    app.register_blueprint(auth)

    return app


if __name__ == "__main__":
    create_app().run()
