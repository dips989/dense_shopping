from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Spapp.views import signup, index, contact_page, productview

class TestUrl(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_index_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_list_index_url_is_resolves(self):
        url = reverse('contact_page')
        self.assertEquals(resolve(url).func, contact_page)

    def test_list_index_url_is_resolves(self):
        url = reverse('productview', args=[1])
        self.assertEquals(resolve(url).func, productview)
