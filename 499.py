import calendar

year = int(input("ENTER YEAR: "))
month = int(input("ENTER MONTH: "))

print("\n", calendar.month(year, month))


print("The calendar for the month is displayed above.")
print("The calendar for the year is displayed below.")
print("\n", calendar.calendar(year))
print("The calendar for the year is displayed above.")
print("The calendar for the year is displayed below.")
