import unittest
from app import app

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_sql_injection(self):
        response = self.app.post('/items', json={'name': "' OR '1'='1", 'description': 'Test'})
        self.assertNotIn("error", response.get_json())

    def test_no_input(self):
        response = self.app.post('/items', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
