# database/seed.py
# Populate database with climbing gym information
from app import create_app, db
from app.models import ClimbingGym, ClimbingBoard 
from app.enums import eClimbBoard

app = create_app()

with app.app_context():
    #Drop all tables and recreate (optional)
    db.drop_all()
    db.create_all()

    # Create climbing boards
    kilter_board_adj_45 = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=45.0)
    
    db.session.add_all([
        kilter_board_adj_45
    ])
    db.session.commit()

    # Create climbing gyms
    # City Bouldering
    cb_aldgate = ClimbingGym(name="City Bouldering Aldgate")
    cb_aldgate.climb_boards.append(kilter_board_adj_45)

    db.session.add_all([
        cb_aldgate
    ])
    db.session.commit()


