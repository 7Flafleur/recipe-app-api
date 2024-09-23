"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email """
        email = 'test@example.com'
        password = 'testpass123'
        """ Call create_user method from get_user_model class with information above"""
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        """ check_password uses hashing"""
