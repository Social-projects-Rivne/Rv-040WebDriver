"""Task page"""

from constants.constants import PagesPath
from locators.my_tasks_page_lockators import TaskPageLocators
from pages.base_page import BasePage
from ui.button import Button
from ui.text_box import TextBox
from util.utils import get_full_url


class TaskPage(BasePage):
    """Task page action methods"""

    def __init__(self, browser, base_url):
        """Initialize OKR Page"""
        super().__init__(browser)
        self.base_url = (get_full_url(base_url, PagesPath.tasks))

        self.task_button = Button(self.browser.driver,
                                  TaskPageLocators.task_button_locator)

        self.task_title = TextBox(self.browser.driver,
                                  TaskPageLocators.task_title_locator)

        self.task_description = TextBox(self.browser.driver,
                                        TaskPageLocators.task_description_locator)

        self.task_team = Button(self.browser.driver,
                                TaskPageLocators.task_team_locator)

        self.task_team_support = Button(self.browser.driver,
                                        TaskPageLocators.task_team_locator_support)

        self.task_priority = Button(self.browser.driver,
                                        TaskPageLocators.task_priority_locator)
        self.task_priority_high = Button(self.browser.driver,
                                        TaskPageLocators.task_priority_high_locator)

        self.task_create_new_button = Button(self.browser.driver,
                                        TaskPageLocators.task_create_button_locator)



    def add_task(self, title, description):
        """Add task"""
        self.task_button.click()
        self.task_title.send_keys(title)
        self.task_description.send_keys(description)
        self.task_team.click()
        self.task_team_support.click()
        self.task_priority.click()
        self.task_priority_high.click()
        self.task_create_new_button.click()


