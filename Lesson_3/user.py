class User:
  
    def __init__(self, first_name, last_name):
        print("Привет! ")
        self.first = first_name
        self.last = last_name

    def sayFirst(self):
        print("Меня зовут ", self.first)

    def sayLast(self):
        print("Моя фамилия ", self.last)

    def sayFull(self):
        print("Мои имя и фамилия ", self.first, self.last)

