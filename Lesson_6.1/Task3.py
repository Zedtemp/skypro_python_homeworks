import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


driver = webdriver.Chrome()


driver.get("https://www.saucedemo.com/")
driver.maximize_window


login = driver.find_element(By.ID, "user-name")
login.send_keys("standard_user", Keys.TAB,
                "secret_sauce", Keys.TAB,Keys.RETURN
                  )


driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()

dostavka = driver.find_element(By.ID, "first-name")
dostavka.send_keys("Alexander", Keys.TAB,
                   "Guselnikov", Keys.TAB,
                   "140013"
                    )


driver.find_element(By.ID, "continue").click()

total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

driver.quit()

def test():
    assert total == 'Total: $58.29'