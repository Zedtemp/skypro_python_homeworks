is_year_leap = input()
is_year_leap = int(is_year_leap)
if (is_year_leap % 4 == 0):
    print("Год ", is_year_leap, True)
else:
    print("Год ", is_year_leap, False)
    