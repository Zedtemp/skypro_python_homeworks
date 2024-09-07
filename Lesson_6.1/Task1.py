import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.maximize_window


def AddData():
    Data = driver.find_element(By.CSS_SELECTOR, "input[name=first-name]")
    Data.send_keys(
        "Иван",Keys.TAB, 
        "Петров",Keys.TAB, 
         "Ленина, 55-3",Keys.TAB, 
        Keys.TAB, "Москва",
        Keys.TAB, "Россия",
        Keys.TAB,"test@skypro.com",
        Keys.TAB, "+7985899998787",
        Keys.TAB,"QA",
        Keys.TAB,"SkyPro",
        Keys.TAB, Keys.RETURN  
        )
    

AddData()

ZipAreaColor = driver.find_element(By.ID, "zip-code").value_of_css_property("color")
FirstNameColor = driver.find_element(By.ID, "first-name").value_of_css_property("color")
LastNameColor = driver.find_element(By.ID, "last-name").value_of_css_property("color")
AddressColor = driver.find_element(By.ID, "address").value_of_css_property("color")
CityColor = driver.find_element(By.ID, "city").value_of_css_property("color")
CountryColor = driver.find_element(By.ID, "country").value_of_css_property("color")
EmailColor = driver.find_element(By.ID, "e-mail").value_of_css_property("color")
NumberColor = driver.find_element(By.ID, "phone").value_of_css_property("color")
JobColor = driver.find_element(By.ID, "job-position").value_of_css_property("color")
CompanyColor = driver.find_element(By.ID, "company").value_of_css_property("color")


def testZipAreaColor():
    col = ZipAreaColor
    assert col == "rgba(132, 32, 41, 1)"


def testOtherColor():
    col = FirstNameColor and LastNameColor and AddressColor and CityColor and CountryColor and EmailColor and NumberColor and JobColor and CompanyColor
    assert col == "rgba(15, 81, 50, 1)"


driver.quit()