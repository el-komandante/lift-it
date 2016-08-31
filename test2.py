from unittest import TestCase
from models import db, User, Cardio, Lift, Workout
from Flask_Testing import LiveServerTestCase, TestCase

class ServerTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_server_is_up(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)

class UserTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        db.create_all()
        db.session.add(User('Test', 'test@test.test', 'test'))
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()

    def setUp(self):
        self.savepoint1 = db.session.begin_nested()
        self.savepoint2 = db.session.begin_nested()

        self.session_backup = db.session
        db.session = self.savepoint2.session

    def tearDown(self):
        self.savepoint1.rollback()
        db.session = self.session_backup

    def test_user_exists(self):
        self.assertTrue(
            db.session.query(User).filter(User.username == 'Test').first()
            is not None
        )
