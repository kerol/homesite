# -*- coding: utf-8 -*-

from flask import Flask

from extensions import db, csrf
from config import DefaultConfig


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object(DefaultConfig)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    csrf.init_app(app)


def register_blueprints(app):
    from blueprints.index import bp_index
    from blueprints.api import bp_api

    app.register_blueprint(bp_index, url_prefix='')
    app.register_blueprint(bp_api, url_prefix='/api')
