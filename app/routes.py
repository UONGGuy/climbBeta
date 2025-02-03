# app/routes.py
from flask import render_template
from app.models import ClimbingGym
from app import db

def register_routes(app):
    print ("Registering routes") # Debug

    @app.route('/')
    def index():
        print("Index route accessed") # Debug
        climbing_gyms = ClimbingGym.query.all()
        return render_template('index.html', climbing_gyms=climbing_gyms)
    
    @app.route('/climbing_gym/<int:climbing_gym_id>')
    def climbing_gym_details(climbing_gym_id):
        print("Gym details route accessed") # Debug
        climbing_gym = db.session.get(ClimbingGym, climbing_gym_id)
        return render_template('climbing_gym.html', climbing_gym=climbing_gym)
