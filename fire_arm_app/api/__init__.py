from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from api.v1.firearm_controller import v1_firearm_profile_bp
app = Flask(__name__) # app here goes with model - no longer needed in app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gun_profile.sqlite3' # needs to go before SQLAlchemy()
db = SQLAlchemy(app) 
# this is also takes care of our declaritive base and session -Megan Amendola (youtube)

app.config['SECRET_KEY'] = "SECRET_KEY"
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def create_app():
    db.create_all()
    db.init_app(app)
    CORS(app)
    # app.register_blueprint(v1_firearm_profile_bp)

    return app