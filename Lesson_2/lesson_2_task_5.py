month_to_season = input("Введите месяц : ")
month = int(month_to_season)
if month < 1 :
    print("Введите корректное число от 1 до 12")
if month > 12 :
      print("Введите корректное число от 1 до 12")


season = ' '
if month == 12 or month == 1 or month == 2:
        season = "Winter"
elif month == 3 or month == 4 or month == 5: 
        season = ("Spring")
elif month == 6 or month == 7 or month == 8: 
        season = ("Summer")
elif month == 9 or month == 10 or month == 11: 
        season = ("Autumn")        
print(season)
