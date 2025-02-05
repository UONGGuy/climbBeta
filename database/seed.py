# database/seed.py
# Populate database with climbing gym information
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
    # Add franchisers to session
    db.session.add_all([
        city_bouldering
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
    ### Aldgate
    cb_aldgate = ClimbingGym(name="City Bouldering Aldgate", franchiser_id=city_bouldering.id)
    cb_aldgate.boards.append(kilter_board_adj_45)
    ### Stratford
    cb_stratford = ClimbingGym(name="City Bouldering Stratford", franchiser_id=city_bouldering.id)
    # Add climbing gyms to session
    db.session.add_all([
        cb_aldgate, cb_stratford
    ])
    # Commit session to generate climbing gym IDs
    db.session.commit()


