from selenium.webdriver.common.by import By

class Inventory:

    def __init__(self, driver):
        self._driver = driver

    def add_backpack(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_tshirt(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def cart(self):
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def checkout(self):
        self._driver.find_element(By.ID, "checkout").click()

