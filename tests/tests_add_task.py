"""Test for adding task"""
from time import sleep

from constants.constants import InitUsers
from tests import SeleniumTestBase


class TaskAddTests(SeleniumTestBase):
    """Class for add task tests"""

    def setUp(self):
        """Initialize login page"""
        super().setUp()
        self.login_page.login(InitUsers.admin_email, InitUsers.password)

    title = 'test task'
    description = 'description for test task'

    def test_add_task(self):
        """Add new Task. If task created test pass (positive)"""
        name = "test"
        self.task_page.add_task(TaskAddTests.title, TaskAddTests.description)
        self.assertIn('test task', self.browser.driver.page_source)