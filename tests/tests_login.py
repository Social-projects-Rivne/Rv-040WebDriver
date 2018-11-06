"""Tests for login page"""

import unittest

from pages import login_page


class LoginTests(unittest.TestCase):
    """Class for login tests"""

    def setUp(self):
        """Initialize login page"""
        self.login_page = login_page.LoginPage()

    def test_login_incorrect_email_and_password(self):
        """Incorrect login test with fake user and password (negative)"""
        self.login_page.login("test@email.com", "password123")
