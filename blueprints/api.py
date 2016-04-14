# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template


bp_api = Blueprint('api', __name__)


@bp_api.route('/scantao')
def scantao():
    return render_template('scantao.html')


@bp_api.route('/g2048')
def g2048():
    return render_template('g2048.html')


@bp_api.route('/caitao')
def caitao():
    return render_template('caitao.html')
