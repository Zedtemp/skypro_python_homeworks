import requests
from Employee import Employer
import pytest


api = Employer("https://x-clients-be.onrender.com/")


def test_get_employ():
    employer_list = api.get_employ_list("3669")

    assert len(employer_list) == 0

def test_add_new():
    body = api.get_employ_list("3669")

    fname = "Alex"
    lname = "Gus"
    company_id = 3669
    email = "123qwe@mai.ru"
    phone = 79999999999
    
    new_employer  = api.add_new_employer(fname, lname, company_id, email, phone)
    new_id = new_employer["id"]
    body = api.get_employ_list("3669")
    len_after = len(body)
    assert len_after  > 0
    assert new_id is not None
    assert body[-1]['firstName'] == "Alex"
    assert body[-1]['lastName'] == "Gus"
    assert body[-1]['id'] == new_id
    assert body[-1]['phone'] == "79999999999"
    
def test_add_new_without_token():

    fname = "Alex"
    lname = "Gus"
    company_id = 3669
    phone = 79999999999
    
    new_employer  = api.add_new_employer_without_token(fname, lname, company_id, phone)
    assert new_employer['message'] == 'Unauthorized'

def test_add_new_without_body():
    body = api.get_employ_list("3669")


    
    new_employer  = api.add_new_employer_without_body()
    assert new_employer['message'] == 'Internal server error'
  

def test_employer_info():
    last_employer = api.get_last_employer("3669")
    employer = api.get_employer_by_id(last_employer)
    
    assert employer is not None
    assert employer['firstName'] == "Alex"
    assert employer['lastName'] == "Gus"
    assert employer['phone'] == "79999999999"
    
def test_change_employer():
    last_employer = api.get_last_employer("3669")
    api.get_employer_by_id(last_employer)
    lname = "Gusss"
    email = "123qwe@mai.ru"
    url = "https://x-clients-be.onrender.com/docs/#/auth/AuthController_login"
    phone = 79999933333
    active = True

    change = api.change_employer(last_employer,lname, email,url, phone, active)

    assert change is not None
    assert change['email'] == "123qwe@mai.ru"
    assert change['url'] == "https://x-clients-be.onrender.com/docs/#/auth/AuthController_login"
    