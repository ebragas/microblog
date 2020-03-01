from flask import Flask

# creates the application object
# __name__ becomes the name of the package
app = Flask(__name__)

# workaround to circular imports; a flask problem
from app import routes
