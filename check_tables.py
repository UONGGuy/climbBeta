# check_tables.py
# Script to list out database table values

from app import create_app
from app.models import *

app = create_app()

with app.app_context():

    # Query ClimbingGyms
    climbing_gyms = ClimbingGym.query.all()
    for gym in climbing_gyms:
        print(gym)
    
    # Query ClimbingBoards
    climbing_boards = ClimbingBoard.query.all()
    for board in climbing_boards:
        print(board)
    
