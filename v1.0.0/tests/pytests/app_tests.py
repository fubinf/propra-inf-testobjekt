import sys
sys.path.append("v1.0.0")

import pytest
from app import app, db, User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            hashed_password = generate_password_hash('password', method='scrypt')
            test_user = User(username='testuser', password_hash=hashed_password)
            db.session.add(test_user)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_successful_login(client):
    response = client.post('/login', data=dict(
        username='testuser',
        password='password'
    ), follow_redirects=True)
    assert response.status_code == 200

def test_failed_login(client):
    response = client.post('/login', data=dict(
        username='wronguser',
        password='wrongpassword'
    ), follow_redirects=True)
    assert response.status_code == 401

def test_profile_access(client):
    pass

def test_logout(client):
    pass

def test_change_password(client):
    pass

def test_image_upload(client):
    pass

def test_reset_password(client):
    pass