import sys
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

# Ajoutez le chemin du répertoire parent au chemin de recherche des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from db import db

class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('sqlite:///test_database.db')

        with self.app.app_context():
            db.create_all()


        self.client = self.app.test_client()

    def tearDown(self):
        
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_blogs(self):

        payload = {
            'title' : 'Blog 2',
            'Contenu' : 'Contenu de blog 2'
        }

        #Ajouter des blog pour tester la fonction

        self.client.post('/create_blog', data=json.dumps(payload), 
                                 content_type='application/json')

        response = self.client.get('/blogs')

        expected_response = {'blogs': 
                             [{'Contenu': 'Contenu de blog 2', 'id': 1, 'title': 'Blog 2'}], 
                             'status': 'success'}

        self.assertEqual(response.get_json(), expected_response)
        self.assertEqual(response.status_code, 200)

    def test_add_blog(self):
        payload = {
            'title' : 'Blog 2',
            'Contenu' : 'Contenu de blog 2'
        }

        # mock_blogs.query.filter_by.return_value.first.return_value = None
        # mock_blogs.return_value = mock_blogs
        # mock_blogs.title = payload['title']
        # mock_blogs.Contenu = payload['Contenu']

        response = self.client.post('/create_blog', data=json.dumps(payload), 
                                 content_type='application/json')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Blog Added')

if __name__ == '__main__':
    unittest.main()
