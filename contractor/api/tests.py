from django.test import TestCase
from clock.models.py import Clock
from django.contrib.auth.models import User
# Create your tests here.


class ClockApiTests(TestCase):
    def test_true(self):
        self.assertEqual(True, True)

    def test_get(self):
        response = self.client.get('/api/clocks')
        self.assertEqual(response.status_code, 200)

    def test_detail_clock(self):

        dict = {'nam': "TEST", 'tick': 1, 'tock': 2, "desc": "test"}

        response = self.client.post('/', dict)

        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/clocks/1')

        self.assertEqual(response.status_code, 200)
