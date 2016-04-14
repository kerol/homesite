# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect


# database orm
db = SQLAlchemy()

# CSRF
csrf = CsrfProtect()