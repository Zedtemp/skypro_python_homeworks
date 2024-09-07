from selenium.webdriver.common.by import By

class Delivery:

    def __init__(self, driver):
        self._driver = driver

    def first_name(self,first):
        self._driver.find_element(By.ID, "first-name").send_keys(first)

    def last_name(self,last):
        self._driver.find_element(By.ID, "last-name").send_keys(last)

    def post_code(self,post):
        self._driver.find_element(By.ID, "postal-code").send_keys(post)

    def confirm(self):
        self._driver.find_element(By.ID, "continue").click()
