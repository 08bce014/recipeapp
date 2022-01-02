from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_model(self):
        """Test for creating user model"""
        email = "abc@xyz.com"
        password = "abc"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        """Test for create user with normailized email"""
        email = 'abc@WXYZ.com'
        user = get_user_model().objects.create_user(
            email=email, password='test'
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_with_no_email(self):
        """Test for create user without email is invalid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    def test_create_superuser(self):
        """Test for creating superuser"""
        email = 'abc@xyz.com'
        user = get_user_model().objects.create_superuser(
            email=email,
            password='test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
