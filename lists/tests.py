from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class homeTest(TestCase):

	def test_rootUrl_homePage(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)