#lists
vegetables = ["carrot" , "raddish" , "cabbage" , "broccoli  " , "spinach" ]
print(vegetables[3])
print(vegetables)
lists = [ 1 , 2 , "bru" , 4.5 , False]
print(lists)
lists.pop(-1)
print(lists)
lists.append("true")
print(lists)
lists.insert(2 , "false")
print(lists)
lists.remove("false")
print(lists)
lists.append("command")
print(lists)
lists.insert(4, "python")
print(lists)
lists.pop(0)    
print(lists)
lists.pop(1)        
print(lists)
lists.pop(2)
print(lists)
lists[2] = "false"
print(lists)
print(lists[0:2])    
print(lists[0:4:2])    
fruits = ["apple" , "banana" , "grapes" , "orange" , "kiwi" , "melon" , "watermelon" , "peach" , "pear" , "plum"]
print(fruits[-2:0:-2])
print(fruits[1::3])
print(len(fruits))
num = [9,8,7,5,3,1,2,4,6]
print(list(reversed(num)))