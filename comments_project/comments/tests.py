from django.test import TestCase


class TestComments(TestCase):

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 302)