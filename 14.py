def DivExp (a,b):
    assert a >0 ,"Assertion Failed : a should be greater than 0"
    
    if b == 0:
     raise ZeroDivisionError("Expection : Division by zero is not allowed")
    c = a / b
    return c

try:
    a = int(input("Enter the value of a :    "))
    b = int(input("Enter the value of b :    "))
    result = DivExp(a,b)
    print("Result :" , result)
except AssertionError as ae:
    print(ae)
except ZeroDivisionError as zde:
    print(zde)  
except ValueError :
    print("Please enter valid integers for a and b.")