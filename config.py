# -*- coding: utf-8 -*-


class DefaultConfig(object):
    """Default Configuration"""
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % ('kevin', 'kevin', '127.0.0.1', 'homesite')

    SECRET_KEY = 'secret key'