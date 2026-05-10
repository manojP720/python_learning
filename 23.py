class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def add(c1,c2):
        return Complex(c1.real+c2.real,
                c1.imag+c2.imag)
    
    n=int(input("Enter the number of complex numbers: "))
    r=int(input("Enter the number of real numbers: "))
    i=int(input("Enter the number of imaginary numbers: "))


    result=Complex(r,i)

    for k in range(n-1):
        r=int(input("Enter the number of real numbers: "))
        i=int(input("Enter the number of imaginary numbers: "))


        c=Complex(r,i)
        result=Complex.add(result,c)

print("Sum=",result.real,"+",result.imag,"i")   

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def add(c1,c2):
        return Complex(c1.real+c2.real,
                c1.imag+c2.imag)
    
    n=int(input("Enter the number of complex numbers: "))
    r=int(input("Enter the number of real numbers: "))
    i=int(input("Enter the number of imaginary numbers: "))


    result=Complex(r,i)

    for k in range(n-1):
        r=int(input("Enter the number of real numbers: "))
        i=int(input("Enter the number of imaginary numbers: "))


        c=Complex(r,i)
        result=Complex.add(result,c)

print("Sum=",result.real,"+",result.imag,"i")   