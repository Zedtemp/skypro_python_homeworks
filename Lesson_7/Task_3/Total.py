from selenium.webdriver.common.by import By
import re
class Total:

    def __init__(self, driver):
        self._driver = driver

    def total_price(self):
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        res = re.sub("[Total: $]", "", total)
        return float(res)