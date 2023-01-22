from django.test import TestCase
from django.urls import reverse, resolve
from home.views import homepage, about, team, contact


class TestUrls(TestCase):
    def test_homepage_url_is_resolved(self):
        """Test home page is resolved"""
        url = reverse('index')
        self.assertEquals(resolve(url).func, homepage)

    def test_about_url_is_resolved(self):
        """Test about page is resolved"""
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_team_url_is_resolved(self):
        """Test team page is resolved"""
        url = reverse('team')
        self.assertEquals(resolve(url).func, team)

    def test_contact_url_is_resolved(self):
        """Test contact page is resolved"""
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)