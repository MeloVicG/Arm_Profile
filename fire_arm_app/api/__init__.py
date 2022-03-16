from flask_cors import CORS
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from api.firearm_controller import v1_firearm_profile_bp
from api import utils


def create_app():
    # app = Flask(__name__) # app here goes with model - no longer needed in app
    app = utils.create_app() # we can throw a description here
    app.register_blueprint(v1_firearm_profile_bp)
    # # db = SQLAlchemy(app)
    # # this is also takes care of our declaritive base and session -Megan Amendola (youtube)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3' # needs to go before SQLAlchemy()
    # app.config['SECRET_KEY'] = "SECRET_KEY"
    # app.config['SQLALCHEMY_ECHO'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.create_all()
    # db.init_app(app)
    # CORS(app)

    return app