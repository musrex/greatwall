import os
import logging
from flask import Flask
from flask import(
    Blueprint, render_template, url_for
)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    instance_path = 'main'
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(instance_path, 'greatwall.sqlite')
    )

    logger = logging.getLogger(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import menu
    app.register_blueprint(menu.bp)
    app.add_url_rule('/', endpoint='index')

    @app.errorhandler(400)
    def bad_request(error):
        # log the error
        logger.error(f'Bad Request: {error}')
        return render_template('400.html'), 400
    
    return app