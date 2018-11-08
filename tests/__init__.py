"""Initialize main functional"""

import os
import unittest

from selenium import webdriver

from pages.login_page import LoginPage
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
        self.okr_page = OkrPage(self.browser, self.base_url)
        self.task_page = TaskPage(self.browser, self.base_url)

    def tearDown(self):
        """Close driver"""
        self.browser.driver.close()

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
