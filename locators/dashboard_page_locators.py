"""Locators"""

from selenium.webdriver.common.by import By


class DashboardPageLocators:
    """A class for dashboard page locators"""

    dashboard_button_locator = (By.XPATH, '/html/body/div[2]/div[1]/ul[2]/li[1]/a')
    add_log_button_locator = (By.XPATH, '//*[@id="week"]/div/div[1]/div[1]/a[2]')
    message_window_locator = (By.CSS_SELECTOR,
                              'body > div.row.ep-tracker > div.large-2.columns.pane1.show-for-large-up > div > div')
