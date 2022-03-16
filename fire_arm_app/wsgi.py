# from api import app
from api import create_app
from models.Shooter_Models import db
# from api.v1.firearm_controller import v1_firearm_profile_bp

app = create_app()

# app.register_blueprint(v1_firearm_profile_bp)

if __name__== "__main__":
    #creates the db if it does not exist
    
    db.create_all()
    db.init_app(app)
    app.run(debug = True)