from django.test import TestCase, Client
from django.urls import reverse

class URLTest(TestCase):

    def test_url(self):
        self.Client = Client()
        url = reverse('home')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)      
