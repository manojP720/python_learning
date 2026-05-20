def fibonacci(n):
    a = 0 
    b = 1 
    print("fibonacci sequence:")
    for i in range(n):
        print(a,end =" ")
        c = a + b
        a = b
        b = c
    N = int(input("enter the value of N"))
    fibonacci(N)