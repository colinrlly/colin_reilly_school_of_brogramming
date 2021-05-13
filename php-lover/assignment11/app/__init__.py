import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'calculator.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # connect to db
    from app.helper import db
    db.init_app(app)

    # register api
    from app.api import api_bp
    app.register_blueprint(api_bp)

    @app.route('/')
    def hello():
        return 'hello, wolrd'

    return app
