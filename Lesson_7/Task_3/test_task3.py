from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Auth_Page import Auth
from Inventory_Page import Inventory
from Delivery import Delivery
from Total import Total


def test_task_3():
    driver = webdriver.Chrome()
    auth = Auth(driver)

    auth.login("standard_user")
    auth.password("secret_sauce")
    auth.confirm_auth()

    inv = Inventory(driver)

    inv.add_backpack()
    inv.add_tshirt()
    inv.add_onesie()
    inv.cart()
    inv.checkout()

    delivery = Delivery(driver)

    delivery.first_name("Alexander")
    delivery.last_name("Guselnikov")
    delivery.post_code("140013")
    delivery.confirm()

    total = Total(driver)
    price = total.total_price()

    assert price == 58.29
