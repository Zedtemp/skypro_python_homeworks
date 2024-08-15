from Address import Adress
from Mailing import Mailing

to_address = Adress(123456,"Moscow", "str. Kukushkina", 777, 77)
from_address = Adress(654321, "Novosibirsk", "str. Kolotushkina", 666, 66)
mailing = Mailing(123456789, to_address, from_address, 5000)

print(mailing)

