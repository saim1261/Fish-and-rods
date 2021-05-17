import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Rods, Fish

class TestBase(TestCase):
    def create_app(self):
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
    SECRET_KEY'TEST_SECRET_KEY
    DEBUG=True
)
return app     
 
def setUp(self):
        db.create_all()
        test_rod= Rods(description="New Rod")
        test_fish = Fish(description="New Fish")
        db.session.add(t_rod)
        db.session.add(t_fish)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

def test_update_get(self):
        response = self.client.get(url_for('update_rod'))
        self.assertEqual(response.status_code, 405)

def test_home_get(self):
        response = self.client.get(url_for(''))
        self.assertEqual(response.status_code, 405)        


