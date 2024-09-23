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

    def test_new_user_email_normalized(self):
        """ Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com','Test2@example.com'],
            ['TEST3@EXAMPLE.COM','TEST3@example.com'],
            ['test4@example.COM','test4@example.com']
        ]

        for email,expected in sample_emails:
            user = get_user_model().objects.create_user(email,'sample123')
            self.assertEqual(user.email,expected)
