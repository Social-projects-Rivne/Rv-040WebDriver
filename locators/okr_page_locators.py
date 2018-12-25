"""OKR page locators"""

from selenium.webdriver.common.by import By


class OkrPageLocators:
    """A class for okr page locators. All main page locators should come here"""

    okr_button_locator = (By.XPATH, "/html/body/div[2]/div[1]/ul[2]/li[6]/a")
    # okr_new_button_locator = (By.CSS_SELECTOR, ".dashed_link")
    okr_new_button_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/a")
    okr_name_textbox_locator = (By.CSS_SELECTOR, "#okr_name")
    okr_start_date_home_button_locator = (By.CSS_SELECTOR, "body > div:nth-child(3) > div.xdsoft_datepicker.active >"
                                                           " div.xdsoft_mounthpicker > button.xdsoft_today_button")
    okr_start_date_button1_locator = (By.CSS_SELECTOR, "#okr_start_date")
    okr_start_date_button2_locator = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[5]")
    okr_end_date_home_button_locator = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/button[2]")
    okr_end_date_button1_locator = (By.CSS_SELECTOR, "#okr_end_date")
    okr_end_date_button2_locator = (By.XPATH, "/html/body/div[4]/div[1]/div[2]/table/tbody/tr[2]/td[4]")
    okr_objective_textbox_locator = (By.CSS_SELECTOR, "#okr_objectives_attributes_0_name")
    okr_objective_key1_textbox_locator = (By.CSS_SELECTOR, "#okr_objectives_attributes_0_key_results_attributes_0_name")
    okr_objective_key2_textbox_locator = (By.CSS_SELECTOR, "#okr_objectives_attributes_0_key_results_attributes_1_name")
    okr_save_button_locator = (By.CSS_SELECTOR, "#new_okr > div.small-12.columns.form-action-up > div.right > input")
    okr_approve_button_locator = (By.CSS_SELECTOR, "#pane3 > div > div.right.options > "
                                                   "div > form > div > input.btn.btn-sec")
    okr_message = (By.CSS_SELECTOR, ".alert-box")
