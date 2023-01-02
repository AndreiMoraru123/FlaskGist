import unittest
from app import app


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_search(self):
        # Test that searching for a valid username returns a successful response
        response = self.app.post('/search', data={'username': 'octocat'})
        self.assertEqual(response.status_code, 200)

        # Test that searching for an invalid username returns a 404 Not Found response
        response = self.app.post('/search', data={'username': 'invalid-username'})
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
