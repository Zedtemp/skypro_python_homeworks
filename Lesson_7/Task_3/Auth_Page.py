from selenium.webdriver.common.by import By


class Auth:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    def login(self, login):
        self._driver.find_element(By.ID, "user-name").send_keys(login)

    def password(self, password):
        self._driver.find_element(By.ID, "password").send_keys(password)

    def confirm_auth(self):
        self._driver.find_element(By.ID, "login-button").click()
