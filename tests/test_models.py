# tests/test_models.py
import unittest
from tests.base_test import BaseTestCase, base_set_up_module
from app import db
from app.models import ClimbingGym, ClimbingBoard, Franchiser
from app.enums import eClimbBoard, eFranchiser

def setUpModule():
    base_set_up_module(__name__)

class ModelsTestCase(BaseTestCase):

    def test_franchiser_creation(self):
        franchiser = Franchiser(name=eFranchiser.CITY_BOULDERING)
        db.session.add(franchiser)
        db.session.commit()
        franchisers = Franchiser.query.all()
        self.assertIsNotNone(franchisers, franchiser)
        self.assertIsNotNone(franchiser.id)
        self.assertEqual(franchiser.name, eFranchiser.CITY_BOULDERING)

    def test_climbing_board_creation(self):
        board = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=45.0)
        db.session.add(board)
        db.session.commit()
        self.assertIsNotNone(board.id)
        self.assertEqual(board.board_type, eClimbBoard.KILTER_BOARD)
        self.assertEqual(board.is_adjustable, True)
        self.assertEqual(board.angle_of_incline, 45.0)

    def test_climbing_gym_creation(self):
        franchiser = Franchiser(name=eFranchiser.CITY_BOULDERING)
        gym = ClimbingGym(name="Test Climbing Gym Vanilla", franchiser=franchiser)
        db.session.add(franchiser)
        db.session.add(gym)
        db.session.commit()
        self.assertIsNotNone(gym.id)
        self.assertEqual(gym.name, "Test Climbing Gym Vanilla")

    def test_climbing_gym_with_boards(self):
        franchiser = Franchiser(name=eFranchiser.CITY_BOULDERING)
        gym = ClimbingGym(name="Test Climbing Gym with Boards", franchiser=franchiser)
        board1 = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=70.0)
        board2 = ClimbingBoard(board_type=eClimbBoard.MOONBAORD, is_adjustable=False, angle_of_incline=50.0)
        gym.boards.append(board1)
        gym.boards.append(board2)
        db.session.add(gym)
        db.session.commit()
        self.assertIn(board1, gym.boards)
        self.assertIn(board2, gym.boards)

if __name__ == '__main__':
    unittest.main()
