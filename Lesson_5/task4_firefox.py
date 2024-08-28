from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), )

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/entry_ad")

sleep(1)

driver.find_element(By.CSS_SELECTOR, ".modal-footer").click()