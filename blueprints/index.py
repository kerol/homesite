# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template


bp_index = Blueprint('index', __name__)


@bp_index.route('/')
def index():
    #return render_template('base.html')
    return "Hello world!"
