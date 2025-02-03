# tests/test_routes.py
import unittest
from tests.base_test import BaseTestCase, base_set_up_module
from app import db
from app.models import ClimbingGym, ClimbingBoard
from app.enums import eClimbBoard

def setUpModule():
    base_set_up_module(__name__)

class RouteTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.client = self.app.test_client()

        # Seed the database
        gym = ClimbingGym(name="Test Gym")
        board = ClimbingBoard(board_type=eClimbBoard.KILTER_BOARD, is_adjustable=True, angle_of_incline=45.0)
        gym.climb_boards.append(board)
        db.session.add(gym)
        db.session.commit()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to ClimbBeta', response.data)

    def test_climbing_gym_details_route(self):
        response = self.client.get('/climbing_gym/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Gym', response.data)
        self.assertIn(b'Kilter Board', response.data) # Enum custom string representation

if __name__ == '__main__':
    unittest.main()
