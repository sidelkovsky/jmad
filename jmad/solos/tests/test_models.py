from django.test import TestCase

from solos.models import Solo


class SoloModelTestCase(TestCase):

    def setUp(self) -> None:
        self.solo = Solo.objects.create(
            track='Falling in Love with Love',
            artist='Oscar Peterson',
            instrument='piano',
        )
        self.solo1 = Solo.objects.create(
            instrument='saxophone',
            artist='John Coltrane',
            track='My Favorite Things'
        )
        self.solo2 = Solo.objects.create(
            instrument='saxophone',
            artist='Cannonball Adderley',
            track='All Blues'
        )
        self.solo3 = Solo.objects.create(
            instrument='saxophone',
            artist='Cannonball Adderley',
            track='Waltz for Debby'
        )

    def test_solo_basic(self):
        """
        Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Oscar Peterson')
