"""Initialize main functional"""

import unittest
import os
from datetime import datetime

from selenium import webdriver

from pages.login_page import LoginPage
from pages.users_page import UserPage
from pages.my_tasks_page import TaskPage
from pages.okr_page import OkrPage
from tests.browser import Browser


class SeleniumTestBase(unittest.TestCase):
    """Main class for testing"""

    def setUp(self):
        """Initialize browser, base_url, pages"""
        self.browser = Browser(self._get_driver())
        self.base_url = self._get_base_url()
        self.login_page = LoginPage(self.browser, self.base_url)
        self.users_page = UserPage(self.browser, self.base_url)
        self.okr_page = OkrPage(self.browser, self.base_url)
        self.task_page = TaskPage(self.browser, self.base_url)


    def tearDown(self):
        """Close driver"""
        self.screen_shot()
        self.browser.driver.close()

    def screen_shot(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                now = datetime.now()
                dir_name = os.path.dirname(__file__)
                self.browser.driver.get_screenshot_as_file(dir_name + "/../screenshots/" + str(method) + str(now) + ".png")

    def _get_driver(self):
        """Get web driver"""
        if self._get_desired_browser_type() == 'firefox':
            driver = webdriver.Firefox()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-translate')
            options.add_argument('--ignore-gpu-blacklist')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
        return driver

    @staticmethod
    def _get_desired_browser_type():
        """Get browser type. Chrome default"""
        return os.environ.get('BROWSER')

    @staticmethod
    def _get_base_url():
        """Get base ulr"""
        return os.environ.get('URL', 'https://app.fluxday.io')
