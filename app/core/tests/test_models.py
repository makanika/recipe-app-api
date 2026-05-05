"""Tests for models."""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Tests for models."""
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized.

        Django's normalize_email() only lowercases the domain (after @).
        Our create_user() also calls .lower() on the whole string so that
        the local part (before @) is lowercased too.

        The four cases deliberately cover every combination:
          test1 — local part already lowercase, domain ALL CAPS
          Test2 — local part mixed case, domain mixed case  ← previously failing
          TEST3 — local part ALL CAPS, domain ALL CAPS
          test4 — local part lowercase, domain mixed case
        All four should be stored as fully lowercase.
        """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.COM', 'test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'test3@example.com'],
            ['test4@Example.Com', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpass123')

    def test_create_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'superuser@example.com',
            'superpass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)