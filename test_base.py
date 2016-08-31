from Flask_Testing import TestCase
from app import app
from models import db

class BaseTestCase(TestCase):

    def create_app(Self):
        app.config.from_object('config.TestConfiguration')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
