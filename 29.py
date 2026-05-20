name = input("enter u r  name ")
year_of_birth = int(input("enter u r year of birth :"))

current_year = 2026 
age = current_year - year_of_birth

if age >= 60 :
 print(name,"is a senior citizen")
else:
 print(name,"is not a  senior citizen ")