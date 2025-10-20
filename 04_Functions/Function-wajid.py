#FUNC.
#Func. having no arg & no return type
#Addition
'''
print("***********************\n")
def add():
    a=int(input("Enter the 1st no. "))
    b=int(input("Enter the 1st no. "))
    print("The addition is",a+b)
add()    
print("\n***********************")
'''

#Arithematic Calculator
'''
print("***********************\n")
print(" ARITHEMATIC CALCULATOR \n")
def add():
    print("The addition is",a+b)
def sub():
    print("The subtraction is",a-b)
def mult():
    print("The multiplication is",a*b)
def div():
    print("The division is",a/b)
a=int(input("Enter the 1st no. "))
b=int(input("Enter the 1st no. "))    
add()
sub()
mult()
div()
print("\n***********************")
'''

#Func. having arg & no return type
'''
print("***********************\n")
def add(a,b):
    print("The addition is",a+b)
add(4,6)    
print("\n***********************")
'''

#Factoroial
'''
print("***********************\n")
print("     FACTORIAL FINDER   \n")
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)    
n=int(input("Enter the no."))
fact(n)    
print("\n***********************")
'''

'''
#Func. having arg & having return type
print("***********************\n")
print("    FACTORIAL FINDER  \n")
def fact1(n):
    fact=1
    for i in range(1,n+1):
        fact1=fact*i
        return fact1   
n=int(input("Enter the no."))
print(fact1)
fact1(n)    
print("\n***********************")
'''

'''
#Area Calculator:
def rect(l,b):
    aor=l*b
    print("\nThe area of rectangle is",aor)
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def sq(s):
    aos=s*s
    print("\nThe area of square is",aos)
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def cir(r):
    aor=3.14*r*r
    print("\nThe area of circle is",aor)
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def tri(b,h):
    aot=0.5*b*h
    print("\nThe area of triangle is",tri)
    print("\n*********************************")

print("*********************************\n")
print("       AREA CALCULATOR    \n")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("          RECTANGLE:       \n")
print("Enter the length of rectangle:")
l=int(input())
print("Enter the height of rectangle:")
b=int(input())
rect(l,b)

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("          SQUARE:       \n")
print("Enter the side of square:")
s=int(input())
sq(s)

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("          CIRCLE:       \n")
print("Enter the radius of circle:")
r=int(input())
cir(r)

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("          TRIANGLE:       \n")
print("Enter the height of Triangle:")
b=int(input())
print("Enter the base of Triangle:")
h=int(input())
tri(b,h)
'''

#Passing Func. as a parameter to another func.
'''
def take():
    a=int(input("Enter 1st No.: "))
    b=int(input("Enter 2nd No.: "))
    return a*b

def mult(p=take):
    print("The multiplication is",p)

mult(take())
'''

#with print
'''
def take():
    a=int(input("Enter 1st No.: "))
    b=int(input("Enter 2nd No.: "))
    print("The addition is",a+b)
    return a+b

def add(p=take):
    print("TASK EXECUTED COMPLETELY")

add(take())
'''
    
    


