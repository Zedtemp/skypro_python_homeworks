from time import sleep
import pytest
from selenium import webdriver
from DataTypes import DataType
from HighlightColor import HighlightColor


def test_task_1():
    driver = webdriver.Chrome()
    data_type = DataType(driver)

    data_type.first_name("Иван")
    data_type.last_name("Петров")
    data_type.address("Ленина, 55-3")
    data_type.zip_code("")
    data_type.city("Москва")
    data_type.country("Россия")
    data_type.email("test@skypro.com")
    data_type.phone_number("+7985899998787")
    data_type.job_position("QA")
    data_type.company("SkyPro")
    data_type.click_submit()

    highlight_color = HighlightColor(driver)


    
    first_name_color = highlight_color.first_name_color()
    last_name_color = highlight_color.last_name_color()
    address_color = highlight_color.address_color()
    zip_code_highlight = highlight_color.zip_code_color()
    city_color = highlight_color.city_color()
    country_color = highlight_color.country_color()
    email_color = highlight_color.email_color()
    phone_number_color = highlight_color.number_color()
    job_color = highlight_color.job_color()
    company_color = highlight_color.company_color()

    assert zip_code_highlight == "rgba(132, 32, 41, 1)"
    assert first_name_color and last_name_color and address_color and city_color and country_color and email_color and phone_number_color and job_color and company_color == "rgba(15, 81, 50, 1)"
