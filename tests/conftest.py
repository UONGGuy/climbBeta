# conftest.py
import unittest
from app import create_app, db
from config.test_config import TestConfig

class TestConfigTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(config_class=TestConfig)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()


    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

