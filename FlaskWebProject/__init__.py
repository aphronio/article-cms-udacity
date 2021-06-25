"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session


app = Flask(__name__)
app.config.from_object(Config)

default_logging_level = logging.INFO
app.logger.setLevel(default_logging_level)
app.logger.debug("main debug")
app.logger.info("main info")
app.logger.warning("main warning")
app.logger.error("main error")
app.logger.critical("main critical")

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
