"""
Tests for the Django admin modifications
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """ tests for Django admin."""

    """ setup method , run before avery added test.Use camelcase in naming!"""

    def setUp(self):
        """ Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password = 'testpass123',
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password = 'testpass123',
            name = 'Test User'
        )


    """ Don't foget to name every test 'test_...' ! Not recognized as test otherwise!"""
    def test_users_list(self):
        """ Test that users are listed on page."""

        """Reverse admin urls listed in Django documentation : page that lists users"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)


    def test_edit_user_page(self):
        """ Test the user page works"""
        url = reverse('admin:core_user_change',args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)


    def test_create_user_page(self):
        """ Test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)