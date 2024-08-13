from smartphone import Smartphone
catalog = []

sasmung = Smartphone("Sasmsung", "Galaxy S20" , "+79997777777")
honor = Smartphone("Honor", 50, "+79996666666")
apple = Smartphone("Apple", "Iphone 11", "+79995555555")
nokia = Smartphone("Nokia", "N72", "+79994444444")
siemens = Smartphone("Siemens", "C115", "+79993333333")

catalog.append(sasmung)
catalog.append(honor)
catalog.append(apple)
catalog.append(nokia)
catalog.append(siemens)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.number}" )
 