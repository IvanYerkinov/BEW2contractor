from django.test import TestCase
from clock.models.py import Clock
from django.contrib.auth.models import User
# Create your tests here.


class ClockTests(TestCase):
    def test_true(self):
        self.assertEqual(True, True)

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        user = User.objects.create()

        dict = {'nam': "TEST", 'tick': 1, 'tock': 2, "desc": "test"}

        response = self.client.post('/', dict)

        self.assertEqual(response.status_code, 200)

        clock = Clock.objects.get(id=1)

        self.assertEqual(clock.name, "TEST")
