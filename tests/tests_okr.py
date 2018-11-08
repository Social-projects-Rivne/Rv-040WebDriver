"""Tests for okr page"""

from constants.constants import InitUsers
from tests import SeleniumTestBase


class OkrTests(SeleniumTestBase):
    """Class for okr tests"""

    def setUp(self):
        """Initialize login page"""
        super().setUp()
        self.login_page.login(InitUsers.admin_email, InitUsers.password)

    def test_add_okr(self):
        """Add new OKR. If OKR created test pass (positive)"""
        name = "test"
        self.okr_page.add_okr(name, "1", "1", "1")
        self.assertIn(name, self.browser.driver.page_source)
        self.assertTrue(self.okr_page.message_window())
        self.assertTrue(self.okr_page.message_window_text())
