import os
from flask import Flask
from dynaconf import FlaskDynaconf


def create_app():
    """Initialize the Flask app instance"""
    app = Flask(__name__)
    dynaconf = FlaskDynaconf(extensions_list=True)

    with app.app_context():

        # Initialize plugins
        os.environ['ROOT_PATH_FOR_DYNACONF'] = app.root_path
        dynaconf.init_app(app)
        app.config["SECRET_KEY"] = bytearray(app.config["SECRET_KEY"], 'UTF-8')
        # print(app.config["SECRET_KEY"])

        # import the routes
        from . import intro

        # register the blueprints
        app.register_blueprint(intro.intro_bp)

        return app
