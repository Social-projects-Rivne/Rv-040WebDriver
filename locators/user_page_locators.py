from selenium.webdriver.common.by import By


class UsrPageLocators:

    """ Class for user page locators"""

    user_button_locator = (By.XPATH, "/html/body/div[2]/div[1]/ul[2]/li[5]/a")

    new_user_button_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/a")

    new_name_textbox_locator = (By.CSS_SELECTOR, "#user_name")

    new_nickname_textbox_locator = (By.CSS_SELECTOR, "#user_nickname")
    new_email_textbox_locator = (By.CSS_SELECTOR, "#user_email")
    new_employee_code_textbox_locator = (By.CSS_SELECTOR, "#user_employee_code")
    new_role_button_locator = (By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/div[6]/div[2]/div/a/span[1]")
    new_password_textbox_locator = (By.CSS_SELECTOR, "#user_password")
    new_confirm_password_textbox_locator = (By.CSS_SELECTOR, "#user_password_confirmation")
    new_user_save_button_locator = (By.CSS_SELECTOR, "#new_user > div.small-12.columns.form-action-up"
                                                     " > div.right > input")
    new_user_message = (By.XPATH, "/html/body/div[2]/div[1]/div/div")
