from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


driver.implicitly_wait(5)
driver.get("http://uitestingplayground.com/textinput")


word_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
word_input.send_keys("SkyPro")


driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
newText = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
txt = newText.text
print(txt)


driver.quit()