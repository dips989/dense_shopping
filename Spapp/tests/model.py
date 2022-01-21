from django.test import TestCase
from Spapp.models import SignUp, Contact_Us, Category


class TestAppModel(TestCase):

    def test_model_str(self):
        first_name = SignUp.objects.create(first_name="Django Testing")
        last_name = SignUp.objects.create(last_name="This is a description")
        username = SignUp.objects.create(username="Hello World")
        self.assertEqual(str(username), "Hello World")

    def test_model_contact(self):
        name = Contact_Us.objects.create(name="Django Testing")
        self.assertEqual(str(name), "Hello World")

    def test_model_category(self):
        cat_name = Category.objects.create(cat_name="Django Testing")
        self.assertEqual(str(cat_name), "Hello World")
