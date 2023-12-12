import os
import yaml
from flask import Flask, send_from_directory
from pathlib import Path
from dynaconf import FlaskDynaconf
import logging
import logging.config


def create_app():
    """Initialize the Flask app instance"""
    app = Flask(__name__)
    # FlaskDynaconf 会自动读取settings.toml和.secrets.toml
    dynaconf = FlaskDynaconf(extensions_list=True)

    with app.app_context():

        # # create a route to the favicon.ico file
        @app.route('/favicon.ico')
        def favicon():
            # print('>>>', app.root_path)
            return send_from_directory(
                os.path.join(app.root_path, 'static', 'images'),
                'favicon.ico',
                mimetype="image/vnd.microsoft.icon"
            )

        # Initialize plugins
        os.environ['ROOT_PATH_FOR_DYNACONF'] = app.root_path
        dynaconf.init_app(app)
        # Flask debug toolbar 需要这个设置
        app.config["SECRET_KEY"] = bytearray(app.config["SECRET_KEY"], 'UTF-8')
        # print(app.config["SECRET_KEY"])

        # _configure_logging(app, dynaconf)  # 设置日志

        # import the routes
        from . import intro

        # register the blueprints
        app.register_blueprint(intro.intro_bp)

        return app

def _configure_logging(app, dynaconf):
    # configure logging
    logging_config_path = Path(app.root_path).parent / 'logging_config.yaml'
    with open(logging_config_path, "r") as fh:
        logging_config = yaml.safe_load(fh.read())
        env_logging_level = dynaconf.settings.get("logging_level", "INFO").upper()
        logging_level = logging.INFO if env_logging_level == "INFO" else logging.DEBUG
        logging_config['handlers']['console']['level'] = logging_level
        logging_config["loggers"][""]["level"] = logging_level
        logging.config.dictConfig(logging_config)
