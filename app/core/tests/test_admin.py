"""Tests for the Django admin modifications."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """Tests for the Django admin modifications."""
    def setUp(self):
        """Create user and client, and force login."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
            first_name='Admin',
            last_name='User'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
    def test_users_list(self):
        """Test that users are listed on user page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)
        self.assertContains(res, self.user.email)