import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


driver = webdriver.Chrome()


driver.implicitly_wait(50)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window

clickk = driver.find_element(By.ID, "delay")
ActionChains(driver)\
    .double_click(clickk)\
    .perform()
clickk.clear
    

time = driver.find_element(By.ID, "delay")
time.send_keys("45")


driver.find_element(By.XPATH, '//span[text()="7"]').click()
driver.find_element(By.XPATH, '//span[text()="+"]').click()
driver.find_element(By.XPATH, '//span[text()="8"]').click()
driver.find_element(By.XPATH, '//span[text()="="]').click()

res = driver.find_element(By.XPATH,'//div[text()="15"]').text


def test():
    assert res == '15'


driver.quit()