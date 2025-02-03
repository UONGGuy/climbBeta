# tests/base_test.py
import unittest
from app import create_app, db

def base_set_up_module(module_name):
    print(f"Running tests in module: {module_name}")

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_class='config.test_config.TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        # Explicitly close session
        db.session.close()
        # Explicitly close database connection within app context
        with self.app.app_context():
            db.engine.dispose()
        self.app_context.pop()
