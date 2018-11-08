"""Dashboard page"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from constants.constants import PagesPath
from pages.base_page import BasePage
from ui.button import Button
from locators.dashboard_page_locators import DashboardPageLocators
from util.utils import get_full_url


class DashboardPage(BasePage):
    """Dashboard page action methods come here."""

    def __init__(self, browser, base_url):
        """Initialize Dashboard Page"""
        super().__init__(browser)
        self.base_url = (get_full_url(base_url, PagesPath.dashboard))
        self.dashboard_button = Button(self.browser, DashboardPageLocators.dashboard_button_locator)
        self.add_log_button = Button(self.browser, DashboardPageLocators.add_log_button_locator)

    def navigate_to(self):
        """Go to Dashboard page"""
        self.dashboard_button.click()

    def add_log(self):
        self.add_log_button.click()

    def message_window(self):
        return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                     (DashboardPageLocators.message_window_locator))

    def message_window_text(self):
        return WebDriverWait(self.browser, 10).until(ec.text_to_be_present_in_element
                                                     (DashboardPageLocators.message_window_locator, "You have no task"))
