"""OKR page locators"""

from selenium.webdriver.common.by import By


class OkrPageLocators:
    """A class for main page locators. All main page locators should come here"""

    okr_button_locator = (By.XPATH, "/html/body/div[2]/div[1]/ul[2]/li[6]/a")
    new_okr_button_locator = (By.CSS_SELECTOR, ".dashed_link")
    # new_okr_button_locator = (By.XPATH, '//*[@id=pane2]/div[2]/a[1]')
    # new_okr_button_locator = (By.LINK_TEXT, "New OKR")
    # new_okr_button_locator = (By.CLASS_NAME, "dashed_link transition")
    okr_name_textbox_locator = (By.CSS_SELECTOR, "#okr_name")
    okr_start_date_textbox_locator = (By.CSS_SELECTOR, "#okr_start_date")
    okr_end_date_textbox_locator = (By.CSS_SELECTOR, "#okr_end_date")
    okr_objective_textbox_locator = (By.CSS_SELECTOR, "#okr_objectives_attributes_0_name")
    okr_objective_key1_textbox_locator = (By.CSS_SELECTOR, "#okr_objectives_attributes_0_key_results_attributes_0_name")
    okr_objective_key2_textbox_locator = (By.CSS_SELECTOR, "#okr_objectives_attributes_0_key_results_attributes_1_name")
    okr_save_button_locator = (By.CSS_SELECTOR, "# new_okr > div.small-12.columns.form-action-up > div.right > input")
    okr_approve_button_locator = (By.CSS_SELECTOR, ("#pane3 > div > div.right.options"
                                                    " > div > form > div > input.btn.btn-sec"))