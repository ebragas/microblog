from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# creates the application object
# __name__ becomes the name of the package
app = Flask(__name__)
app.config.from_object(Config)  # imports config from class; accessible via bracket notation
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# workaround to circular imports; a flask problem
from app import routes, models
