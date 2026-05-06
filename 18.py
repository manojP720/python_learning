# for loop  allows us to iterate over a sequence (like a list,tuple,string) or other iterable objects.its a control flow statement that executes a piece of code repeatedly for each item in the sequence or item in the items of and items of and items in the iterable object.    
# syntax of for loop
# for variable in sequence: 
from operator import index


cities = ["delhi", "mumbai", "kolkota", "chennai"]
for city in cities :
    print(city)


bag = ["red","blue","green"]
for color in bag :
    print( color, end=" ")
      



for i in range (1,15,3 ) :
    print(i/3)


name = "Manoj"
for letter in name :
    print(letter )


name = "Manoj"
for index, letter in enumerate(name) :
    print(letter *(index +1))


l = [143,124,145,156]
for indexx, num in enumerate(l) :
    print(f"{num} is the {indexx}th element in the list")