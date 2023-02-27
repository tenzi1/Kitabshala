from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_data(self):
        self.assertContains(self.response,'Kitabshala' )

    def test_homepage_doesnot_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'hi this is not correct data')

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
