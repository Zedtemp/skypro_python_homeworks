from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")


login = driver.find_element(By.ID, 'username')
login.send_keys("tomsmith")


password = driver.find_element(By.ID, 'password')
password.send_keys("SuperSecretPassword!")


driver.find_element(By.CSS_SELECTOR, ".radius").click()

