"""Test for adding task"""


from constants.constants import InitUsers
from tests import SeleniumTestBase


class TaskAddTests(SeleniumTestBase):
    """Class for add task tests"""

    def setUp(self):
        """Initialize login page"""
        super().setUp()
        self.login_page.login(InitUsers.admin_email, InitUsers.password)

    TITLE = 'test task'
    DESCRIPTION = 'description for test task'

    def test_add_task(self):
        """Add new Task. If task created test pass (positive)"""
        self.task_page.add_task(TaskAddTests.TITLE, TaskAddTests.DESCRIPTION)
        self.assertIn('test task', self.browser.driver.page_source)
