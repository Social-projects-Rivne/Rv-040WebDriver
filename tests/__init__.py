import unittest

import os
from selenium import webdriver
from pages.login_page import LoginPage
from pages.users_page import UserPage
from tests.browser import Browser
from constants.constants import PagesPath
from ui.button import Button
from ui.text_box import TextBox
from util.utils import get_full_url

class SeleniumTestBase(unittest.TestCase):

    def setUp(self):
        self.browser = Browser(self._get_driver())
        self.base_url = self._get_base_url()
        self.login_page = LoginPage(self.browser, self.base_url)
        self.user_page = UserPage(self.browser, self.user_page)

    def _get_driver(self):
        if self._get_desired_browser_type() == 'firefox':
            driver = webdriver.Firefox()

        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-translate')
            options.add_argument('--ignore-gpu-blacklist')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(options=options)
        return driver

    def _get_desired_browser_type(self):
        return os.environ.get('BROWSER')


    def _get_base_url(self):
        return os.environ.get('URL', 'https://app.fluxday.io')
