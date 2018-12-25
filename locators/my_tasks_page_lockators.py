"""My tasks page locators"""

from selenium.webdriver.common.by import By


class TaskPageLocators:
    """A class for task page locators. All task page locators should come here"""

    task_button_locator = (By.XPATH, '/html/body/div[1]/nav/section/ul[1]/li/a')
    task_title_locator = (By.XPATH, '//*[@id="task_name"]')
    task_description_locator = (By.XPATH, '//*[@id="task_description"]')
    task_team_locator = (By.XPATH, '//*[@id="s2id_task_team_id"]/a')
    task_team_locator_support = (By.XPATH, '/html/body/div[6]/ul')
    task_priority_locator = (By.XPATH, '//*[@id="s2id_task_priority"]/a')
    task_priority_high_locator = (By.XPATH, '/html/body/div[7]/ul')
    task_create_button_locator = (By.XPATH, '//*[@id="new_task"]/div[3]/div[2]/input')



