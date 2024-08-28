from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), )

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")


login = driver.find_element(By.ID, 'username')
login.send_keys("tomsmith")


password = driver.find_element(By.ID, 'password')
password.send_keys("SuperSecretPassword!")


driver.find_element(By.CSS_SELECTOR, ".radius").click()

