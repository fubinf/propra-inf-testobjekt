import unittest
from app import app, db, User
from werkzeug.security import generate_password_hash

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        with app.app_context():
            db.create_all()
            hashed_password = generate_password_hash('password', method='scrypt')
            test_user = User(username='testuser', password_hash=hashed_password)
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_successful_login(self):
        response = self.app.post('/login', data=dict(
            username='testuser', 
            password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_failed_login(self):
        response = self.app.post('/login', data=dict(
            username='wronguser', 
            password='wrongpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 401)

    def test_profile_access(self):
        pass

    def test_logout(self):
        pass

    def test_change_password(self):
        pass

    def test_image_upload(self):
        pass

    def test_reset_password(self):
        pass

if __name__ == '__main__':
    unittest.main()
