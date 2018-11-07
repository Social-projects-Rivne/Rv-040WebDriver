""" Testing ability to add new user to Fluxday.IO by different users"""


import selenium
from constants.constants import InitUsers, PagesPath
from tests import SeleniumTestBase
import time

from util.utils import get_full_url


class AddUserTests(SeleniumTestBase):
    """ Add new user testing"""

    def setUp(self):

        super().setUp()

    def test_new_user_by_admin(self):
        """ability to add new user by admin"""

        self.login_page.login(InitUsers.admin_email, InitUsers.password)
        self.browser.go_to_url(get_full_url(self.base_url, PagesPath.users))
        time.sleep(7)
