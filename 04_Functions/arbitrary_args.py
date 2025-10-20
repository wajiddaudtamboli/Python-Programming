# arbtriy arguments
"""
def sum1(x,*y):
    print(x,type(x))
    print(y,type(y))

    for i in y:
        x=x+i
    print(x)
sum1(5,41,41,20,22,33,24)

def sum1(*y):
    print(y)
    x=0
    for i in y:
        x=x+i

    print("inside function =",x)
sum1(5,41,41,20,22,33,24)


## def inside of the function
# Addition
print("Addition")
def add():
    x=int(input("Enter No ="))
    y=int(input("Enter No ="))
    z=x+y
    print(z)
add()

# Substraction
print("Substraction")
def sub():
    x=int(input("Enter No ="))
    y=int(input("Enter No ="))
    z=x-y
    print(z)
sub()

# Multiplaction
print("Multiplaction")
def mul():
    x=int(input("Enter No ="))
    y=int(input("Enter No ="))
    z=x*y
    print(z)
mul()

# Division
print("Division")
def div():
    x=int(input("Enter No ="))
    y=int(input("Enter No ="))
    z=x/y
    print(z)
div()
"""


## def out of function
# Addition
print("Addition")
def add(x,y):
    z=x+y
    print(z)
x=int(input("Enter No ="))
y=int(input("Enter No ="))
add(x,y)

# Substraction
print("Substraction")
def sub():

    z=x-y
    print(z)
x=int(input("Enter No ="))
y=int(input("Enter No ="))
sub()

# Multiplaction
print("Multiplaction")
def mul():

    z=x*y
    print(z)
x=int(input("Enter No ="))
y=int(input("Enter No ="))
mul()

# Division
print("Division")
def div():

    z=x/y
    print(z)
x=int(input("Enter No ="))
y=int(input("Enter No ="))
div()

