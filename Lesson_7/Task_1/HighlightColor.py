from selenium.webdriver.common.by import By

class HighlightColor:


    def __init__(self, driver):
        self._driver = driver
        
    def zip_code_color(self):
        color = self._driver.find_element(By.ID, "zip-code").value_of_css_property("color")
        return color

    def first_name_color(self):
        color = self._driver.find_element(By.ID, "first-name").value_of_css_property("color")
        return color
    
    def last_name_color(self):
        color = self._driver.find_element(By.ID, "last-name").value_of_css_property("color")
        return color        

    def address_color(self):
        color = self._driver.find_element(By.ID, "address").value_of_css_property("color")
        return color
    
    def city_color(self):
        color = self._driver.find_element(By.ID, "city").value_of_css_property("color")
        return color
    
    def country_color(self):
        color = self._driver.find_element(By.ID, "country").value_of_css_property("color")
        return color
    
    def email_color(self):
        color = self._driver.find_element(By.ID, "e-mail").value_of_css_property("color")
        return color
    
    def number_color(self):
        color = self._driver.find_element(By.ID, "phone").value_of_css_property("color")
        return color

    def job_color(self):
        color = self._driver.find_element(By.ID, "job-position").value_of_css_property("color")
        return color

    def company_color(self): 
        color = self._driver.find_element(By.ID, "company").value_of_css_property("color")
        return color
    
