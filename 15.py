#whlie loop
# A loop that continues to execute a block of code as long  as  a specific condition is true .

is_failed = True
i = 1
while is_failed :

    if i%2!=0 :
        i = i+1
        continue

    print(f"try {i}")
    i = i+1
    
    if i > 5:
        break

print("You have failed 5 times. Better luck next time !")


i = 0
while i <= 10 :
    x = 0
    while  x <= i :
        print( " Manoj ", end="_")
        x += 1

    
    i += 1
