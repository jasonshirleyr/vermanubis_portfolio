from django.test import TestCase
from ..models import About, Music

class AboutTest(TestCase):
    def setUp(self):
        About.objects.create(
            about = "test"
        )
        
    def test_about(self):
        test = About.objects.get(about="test")
        self.assertEqual(test.get_about(), "test")