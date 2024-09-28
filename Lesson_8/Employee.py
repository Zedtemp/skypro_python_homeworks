import requests


class Employer:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        auth = {
        'username': user,
        'password': password
         }
        authorization = requests.post(self.url + "auth/login", json=auth)
        return authorization.json()["userToken"]
    
    def get_last_employer(self, company_id: int):
        company = {'company' : company_id}
        resp = requests.get(self.url + "employee/", params=company )
        return resp.json()[-1]['id']

    def get_employ_list(self,company_id: int):
        company = {'company' : company_id}
        resp = requests.get(self.url + "employee/", params=company)
        return resp.json()
    
    def add_new_employer(self, fname, lname, company_id, email, phone):
        employer = {
        'firstName' : fname,
        'lastName' : lname,
        'companyId' : company_id,
        'email' : email,
        'phone' : phone
        } 
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        create = requests.post(self.url + "employee/",
                               json=employer, headers=my_headers)
        return create.json()

    def add_new_employer_without_body(self):
        employer = {} 
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        create = requests.post(self.url + "employee/",
                               json=employer, headers=my_headers)
        return create.json()

    def add_new_employer_without_token(self, fname, lname, company_id, phone):
        employer = {
        'firstName' : fname,
        'lastName' : lname,
        'companyId' : company_id,
        'phone' : phone
        } 
        create = requests.post(self.url + "employee/",
                               json=employer)
        return create.json()

    def get_employer_by_id(self,employer_id):
        resp =requests.get(self.url + "employee/" + str(employer_id))
        return resp.json()

    def change_employer(self,employer_id, lname, email,url, phone, active):
        employer =  {
        "lastName": lname,
        "email": email,
        "url": url,
        "phone": phone,
        "isActive": active
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()   
        change = requests.patch(self.url + "employee/" + str(employer_id),
                               json=employer, headers=my_headers)   
        return change.json()  