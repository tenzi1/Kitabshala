from django.test import TestCase

from kitab.models import Kitab

class KitabTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.kitab = Kitab.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='1200.00'
        )

    def test_kitab_listing(self):
        self.assertEqual(f"{self.kitab.title}", "Harry Potter")
        self.assertEqual(f"{self.kitab.author}", "JK Rowling")
        self.assertEqual(f"{self.kitab.price}", "1200.00")

    

