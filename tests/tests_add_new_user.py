""" Testing ability to add new user to Fluxday.IO by different users"""


from constants.constants import InitUsers
from tests import SeleniumTestBase


class AddUserTests(SeleniumTestBase):
    """ Add new user testing"""

    def setUp(self):

        super().setUp()
        self.login_page.login(InitUsers.admin_email, InitUsers.password)

    def test_new_user_by_admin(self):
        """ability to add new user by admin"""
        new_user = "SuperUser"
        self.users_page.add_user(new_user, "newname", "NewEmail@email3423.com", 'code', "password", "password")
        self.assertIn(new_user, self.browser.driver.page_source)
        self.assertTrue(self.users_page.message_window())
        self.assertTrue(self.users_page.message_window_text())
