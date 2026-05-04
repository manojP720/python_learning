# snacks buying
# https://www.codewars.com/kata/5aee86c5783bbda2900000f/train/python
snaks_availables = 3 
money = 10
snaks_price = 3

while snaks_availables > 0 and money > 0 : 
    print(f"Snaks available : {snaks_availables} , money : {money}k")
    buy = input("Do you want to buy a snak ? (yes/no) ).lower()")
    if buy == "yes" : 
        money -= snaks_price
        snaks_availables -= 1 
    else :
        print("ok, maybe later")    