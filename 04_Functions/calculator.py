#calculator
def addition(x,y):
    z=x+y
    print(z)

def subtraction(x,y):
    z=x-y
    print(z)

def multiplication(x,y):
    z=x*y
    print(z)

def division(x,y):
    z=x/y
    print(z)

def pyramid(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()
