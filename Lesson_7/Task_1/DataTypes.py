from selenium.webdriver.common.by import By


class DataType:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    def first_name(self, first):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(first)

    def last_name(self, last):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(last)

    def address(self, address):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(address)

    def zip_code(self, zipcode):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(zipcode)

    def city(self, city):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(city)

    def country(self, country):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(country)

    def email(self, email):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)

    def phone_number(self, phone):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(phone)

    def job_position(self, job):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(job)

    def company(self, company):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(company)

    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, ".btn").click()
