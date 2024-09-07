from time import sleep
import pytest
from selenium import webdriver  
from Calc import Calc


def test_task_2():
    driver = webdriver.Chrome()
    calc = Calc(driver)

    calc.timer()
    calc.nums()
    res = calc.result()
    assert res == 15

