from django.test import  TestCase
from django.urls import resolve

from solos.views import index

class SolosURLsTestCase(TestCase):

    def test_root_url_uses_index_view(self):
        """
        Test that the root of the site resovlves to the correct view function
        """
        root = resolve('/')
        self.assertEqual(root.func, index)

