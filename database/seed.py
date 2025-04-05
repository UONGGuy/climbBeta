# database/seed.py
# Populate database with climbing gym information
from app import create_app, db
from app.models import ClimbingGym, ClimbingBoard, Franchiser
from app.enums import eClimbBoard, eFranchiser

def seed_database():
    app = create_app()  # Create the app instance
    
    with app.app_context():  # Ensure that the database operations are done within the app context
        # Drop all tables and recreate (optional)
        db.drop_all()
        db.create_all()

        # Create franchisers
        city_bouldering = Franchiser(name=eFranchiser.CITY_BOULDERING)
        db.session.add_all([city_bouldering])
        db.session.commit()

        # Create climbing boards
        kilter_board_adj_45 = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=45.0)
        db.session.add_all([kilter_board_adj_45])
        db.session.commit()

        # Create climbing gyms
        cb_aldgate = ClimbingGym(name="City Bouldering Aldgate", franchiser_id=city_bouldering.id)
        cb_aldgate.boards.append(kilter_board_adj_45)
        cb_stratford = ClimbingGym(name="City Bouldering Stratford", franchiser_id=city_bouldering.id)
        db.session.add_all([cb_aldgate, cb_stratford])
        db.session.commit()
