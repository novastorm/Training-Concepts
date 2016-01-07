from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from application import app as application
from application import db

migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()