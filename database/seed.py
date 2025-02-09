# database/seed.py
# Populate database with climbing gym information
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import ClimbingGym, ClimbingBoard, Franchiser
from app.enums import eClimbBoard, eFranchiser

app = create_app()

with app.app_context():
    #Drop all tables and recreate (optional)
    db.drop_all()
    db.create_all()

    # Create franchisers
    city_bouldering = Franchiser(name=eFranchiser.CITY_BOULDERING)
    stronghold = Franchiser(name=eFranchiser.STRONGHOLD_CLIMBING_CENTERS)

    # Add franchisers to session
    db.session.add_all([
        city_bouldering, stronghold
    ])
    # Commit session to generate franchiser IDs
    db.session.commit()


    # Create climbing boards
    kilter_board_adj_45 = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=45.0)

    # Add climbing boards to session
    db.session.add_all([
        kilter_board_adj_45
    ])
    # Commit session to generate climbing board IDs
    db.session.commit()


    # Create climbing gyms

    ## City Bouldering
    cb_aldgate = ClimbingGym(name="City Bouldering Aldgate", franchiser_id=city_bouldering.id)
    cb_stratford = ClimbingGym(name="City Bouldering Stratford", franchiser_id=city_bouldering.id)
    cb_white_city = ClimbingGym(name="White City Bouldering", franchiser_id=city_bouldering.id)
    ## Stronghold
    stronghold_TH = ClimbingGym(name="Stronghold Tottenham Hale", franchiser_id=stronghold.id)
    stronghold_LF = ClimbingGym(name="Stronghold London Fields", franchiser_id=stronghold.id)

    # Add climbing gyms to session
    db.session.add_all([
        cb_aldgate, cb_stratford, cb_white_city,
        stronghold_LF, stronghold_TH

    ])
    # Commit session to generate climbing gym IDs
    db.session.commit()

    # Establish relationships after committing all features and gyms
    
    ## CB Aldgate
    cb_aldgate.boards.append(kilter_board_adj_45)
    
    db.session.commit()
