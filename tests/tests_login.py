"""Tests for login page"""

from tests import SeleniumTestBase


class LoginTests(SeleniumTestBase):
    """Class for login tests"""

    def setUp(self):
        """Initialize login page"""
        super().setUp()

    def test_login_incorrect_email_and_password(self):
        """Incorrect login test with fake user and password (negative)"""
        self.login_page.login("test@email.com", "password123")
