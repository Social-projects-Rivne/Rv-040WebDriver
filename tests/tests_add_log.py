"""Tests for dashboard page"""

from tests import SeleniumTestBase
from constants.constants import InitUsers


class AddLogTests(SeleniumTestBase):
    """Class for add log tests"""

    def setUp(self):
        """Initialize Dashboard page"""
        super().setUp()

    def test_add_log(self):
        self.login_page.login(InitUsers.admin_email, InitUsers.password)
        self.dashboard_page.navigate_to()
        self.dashboard_page.add_log()
        self.assertTrue(self.dashboard_page.message_window())
