import unittest

import os
from selenium import webdriver
from pages.login_page import LoginPage
from tests.browser import Browser


class SeleniumTestBase(unittest.TestCase):

    def setUp(self):
        self.browser = Browser(self._get_driver())
        self.base_url = self._get_base_url()
        self.login_page = LoginPage(self.browser, self.base_url)

    def _get_driver(self):
        if self._get_desired_browser_type() == 'firefox':
            driver = webdriver.Firefox()

        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-translate')
            options.add_argument('--ignore-gpu-blacklist')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(chrome_options=options)
        return driver

    def _get_desired_browser_type(self):
        return os.environ.get('BROWSER')


    def _get_base_url(self):
        return os.environ.get('URL', 'https://app.fluxday.io')
