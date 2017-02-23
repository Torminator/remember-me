from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import models

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

#manager.run()

from app import views