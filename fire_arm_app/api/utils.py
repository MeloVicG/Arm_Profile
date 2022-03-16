from flask_cors import CORS
from flask import Flask
# from api.v1.firearm_controller import v1_firearm_profile_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    # app.register_blueprint(v1_firearm_profile_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3' # needs to go before SQLAlchemy()
    app.config['SECRET_KEY'] = "SECRET_KEY"
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app