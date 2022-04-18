from flask_cors import CORS
from flask import Flask
# from api.v1.firearm_controller import v1_firearm_profile_bp


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(v1_firearm_profile_bp)

    CORS(app)
    # CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
    # app.config['CORS_HEADERS'] = 'Content-Type'


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3' # needs to go before SQLAlchemy()
    app.config['SECRET_KEY'] = "SECRET_KEY"
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app