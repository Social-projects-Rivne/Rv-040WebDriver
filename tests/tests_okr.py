"""Tests for okr page"""

import time
from datetime import datetime

from constants.constants import InitUsers
from tests import SeleniumTestBase


class OkrTests(SeleniumTestBase):
    """Class for okr tests"""

    def setUp(self):
        """Initialize login page"""
        super().setUp()

    def test_okr(self):
        """Incorrect login test with fake user and password (negative)"""
        self.login_page.login(InitUsers.lead_email, InitUsers.password)
        # self.okr_page.navigate_okr()
        # self.okr_page.new_okr_button()
        self.okr_page.navigate_new_okr()
        self.okr_page.set_okr_name("test")
        self.okr_page.set_okr_dates(datetime.now(), datetime.now())
        time.sleep(5)
