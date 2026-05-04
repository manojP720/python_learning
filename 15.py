#whlie loop
# A loop that continues to execute a block of code as long  as  a specific condition is true .

is_failed = True
i = 1
while is_failed :
    print(f"try {i}")
    i = i+2
    if i > 10 :
        break

print("You have failed 10 times. Better luck next time !")