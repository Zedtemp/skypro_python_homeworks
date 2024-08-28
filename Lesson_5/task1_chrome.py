from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


for x in range(5):
    clickable = driver.find_element(By.CSS_SELECTOR,"[onclick='addElement()']")
    ActionChains(driver)\
        .click(clickable)\
        .perform()


delete = driver.find_elements(By.CSS_SELECTOR, "[onclick='deleteElement()']")
print(len(delete))
        
