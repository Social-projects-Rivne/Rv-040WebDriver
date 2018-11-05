"""Tests for login page"""

import unittest

from selenium import webdriver
from constants.constants import InitUrls


class LoginTests(unittest.TestCase):
    """Class for login tests"""

    def setUp(self):
        """Open webdriver chrome and initialize login page"""
        self.driver = webdriver.Chrome()
        self.driver.get(InitUrls.login)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        """Webdriver chrome close"""
        self.driver.close()
