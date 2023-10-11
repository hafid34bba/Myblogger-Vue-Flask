from app import app
import unittest
from unittest.mock import patch, Mock

import json

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app =app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('app.Blogs.query')
    def test_blogs(self, mock_query):

        blog1 = Mock()
        blog1.id = 1
        blog1.title = "First blog"
        blog1.Contenu = "Create what ever you want, till now we are just trying some new stuffs"

        blog2 = Mock()
        blog2.id = 2
        blog2.title = "Blog 1"
        blog2.Contenu = "Contenu de blog 1"

        mock_query.all.return_value = [blog1, blog2]


        response = self.app.get('/blogs')
       

        # Assurez-vous que la requête a été appelée
        mock_query.all.assert_called_once()

        data = response.get_json()

        expected_response = {
            "status" : "success",
                "blogs" : [ {"id": 1,
                                    "title" :"First blog",
                "Contenu" : "Create what ever you want, till now we are just trying some new stuffs"}

            , {
                "id" : 2,
                "title" : "Blog 1",
                "Contenu" : "Contenu de blog 1"}]
                }


        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, expected_response)
 
    def test_add_blog_error(self):
        response = self.app.get('/create_blog')
        self.assertEqual(response.status_code, 405)

    @patch('app.db.session.add')  # Mock db.session.add method
    @patch('app.db.session.commit')
    def test_add_blog_post(self, mock_commit, mock_add):
        payload = {
            'title' : 'Blog 2',
            'Contenu' : 'Contenu de blog 2'
        }

        # mock_blogs.query.filter_by.return_value.first.return_value = None
        # mock_blogs.return_value = mock_blogs
        # mock_blogs.title = payload['title']
        # mock_blogs.Contenu = payload['Contenu']

        response = self.app.post('/create_blog', data=json.dumps(payload), 
                                 content_type='application/json')
        data = response.get_json()

        mock_add.assert_called_once()  # Check if db.session.add was called once
        mock_commit.assert_called_once()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Blog Added')

if __name__ == '__main__':
    unittest.main()