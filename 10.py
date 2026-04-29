#operators
x = 5
x *= 4
print(x)
a = 10
a += 9
print(a)
print(a == x)
print(a != x)
print(a > x)    
print(a < x)
print(a >= x)       
print(a <= x)   
#logical operators
print(a > 5 and a < 20) 
print(a > 5 or a < 20)
print(not(a > 5 and a < 20))
print("Love")

boy_name = input("Boy Name : ")
boy_age = input("Boy Age : ")
girl_name = input("Girl Name : ")
girl_age = input("Girl Age : ")

age_diff = abs(int(boy_age) - int(girl_age))

print(f"{boy_name} loves {girl_name}. Age difference is {age_diff}.")
print(" hello")
#membership operators
my_list = [1, 2, 3, 4, 5, 6, 8 ]
my_name = "Gagana B"
print( 1 in my_list)
print(7 in my_list)
print( 7 not in my_list)
print( "G" in my_name)
print( "g" in my_name)


my_sis = "Gagana"
my_teacher = "Gagana B"
print(("B" in  my_sis  ) and ("B" in my_teacher))
print(("B" in  my_sis  ) or ("B" in my_teacher))
