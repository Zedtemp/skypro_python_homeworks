from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), )

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")


input_line = driver.find_element(By.CSS_SELECTOR, "input")
input_line.send_keys(1000)
input_line.clear()
input_line.send_keys(999)

