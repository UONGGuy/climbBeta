# tests/test_models.py
import unittest
from tests.base_test import BaseTestCase, base_set_up_module
from app import create_app, db
from app.models import ClimbingGym, ClimbingBoard
from app.enums import eClimbBoard

def setUpModule():
    base_set_up_module(__name__)

class ModelsTestCase(BaseTestCase):

    def test_climbing_board_creation(self):
        board = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=45.0)
        db.session.add(board)
        db.session.commit()
        self.assertIsNotNone(board.id)
        self.assertEqual(board.board_type, eClimbBoard.KILTER_BOARD)
        self.assertEqual(board.is_adjustable, True)
        self.assertEqual(board.angle_of_incline, 45.0)

    def test_climbing_gym_creation(self):
        gym = ClimbingGym(name="Test Climbing Gym Vanilla")
        db.session.add(gym)
        db.session.commit()
        self.assertIsNotNone(gym.id)
        self.assertEqual(gym.name, "Test Climbing Gym Vanilla")

    def test_climbing_gym_with_boards(self):
        gym = ClimbingGym(name = "Test Climbing Gym with Boards")
        board1 = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=70.0)
        board2 = ClimbingBoard(board_type=eClimbBoard.MOONBAORD, is_adjustable=False, angle_of_incline=50.0)
        gym.climb_boards.append(board1)
        gym.climb_boards.append(board2)
        db.session.add(gym)
        db.session.commit()
        self.assertIn(board1, gym.climb_boards)
        self.assertIn(board2, gym.climb_boards)

if __name__ == '__main__':
    unittest.main()
