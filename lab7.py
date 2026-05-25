def DivExp(a,b):
    assert a > 0 , "Assertion failed : 'a' must be greater than 0"

    if b == 0 :
        raise ZeroDivisionError("Exception:division by zero is not allowed ")
    
    c = a / b 
    return c 


try :
        
        a = int(input("enter the a :"))
        b = int(input("enter the b :"))
        result = DivExp (a,b)
        print("Result=",result)

except AssertionError as ae :
     print(ae)
except ZeroDivisionError as zde :
     print(zde)
except ValueError :
     print("Please enter valid integer values  ")                  