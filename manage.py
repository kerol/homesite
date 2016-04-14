# -*- coding: utf-8 -*-
# !/usr/bin/env python

from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

import myapp
import extensions

app = myapp.create_app()
migrate = Migrate(app, extensions.db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)  # migrate, upgrade
manager.add_command('runserver', Server(host='localhost', port=5000))


@manager.command
def hello():
    print 'hello'


if __name__ == '__main__':
    manager.run()
