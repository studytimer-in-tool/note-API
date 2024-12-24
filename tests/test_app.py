import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_send_notes_missing_data(self):
        response = self.client.post('/send_notes', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)
