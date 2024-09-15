from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def timer(self):
        click = self._driver.find_element(By.ID, "delay")
        ActionChains(self._driver)\
            .double_click(click)\
            .perform()
        time = self._driver.find_element(By.ID, "delay")
        time.send_keys("45")

    def nums(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def result(self):
        WebDriverWait(self._driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="15"]')))
        res = self._driver.find_element(By.XPATH, '//div[text()="15"]').text
        return int(res)
