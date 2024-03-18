import unittest
from flask import current_app
from app import create_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_contect = self.app.app_contect()
        self.app_contect.psuh()

    def tearDown(self):
        self.app_contect.pop()

    def test_app(self):
        self.assertIsNone(current_app)

    if __name__ == '__main__':
        unittest.main()