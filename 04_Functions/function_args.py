
# built in function
# user define function



'''
def add():
    
    x=5
    y=10

    z=x+y
    print(z)

add()



def sub():

    x=5
    y=2

    z=x-y

    print("sub is=",z)

    
sub()
'''

# parameters or agrs

# actuall para meter or args
# formal parameter or args

# positional args
# keyword args
# defualt args
# arbtriy args


'''
# positional args
def add(x1,y1):
    


    z=x1+y1
    print(z)
    

#============
x=15
y=5
add(x,y)



def person(name,age):
    
    print("name=",name)
    print("age=",age)

#==========Start=======
name=input("enter name")
age=int(input("enter age"))

person(name,age)


# keyword args


def person(name,age):
    
    print("name=",name)
    print("age=",age)

#==========Start=======
person(age=25,name="mujahid")
#name=input("enter name")
#age=int(input("enter age"))
#person(age=age,name=name)

'''
"""
# defualt args
def person(name,age=18):
    
    print("name=",name)
    print("age=",age)

#==========Start=======

person("mujahid",25)

def person(name,age=18):
    
    print("name=",name)
    print("age=",age)

#==========Start=======

person("mujahid")

# arbtriy args

def sum1(x,*y):
    print(x,type(x))
    print(y,type(y))

    for i in y:
        x=x+i
        
    print(x)

#========
sum1(5,10,88,99,6,32,15,2)



def sum1(*y):
   
    x=0

    for i in y:
        x=x+i
        
    print("inside fun=",x)

#================
print(sum1(5,10,88,99,6,32,15,2))
"""

def sum1(*y):
   
    x=0

    for i in y:
        x=x+i
        
    print("inside fun =",x)

    return x

#================
#print(sum1(5,10,88,99,6,32,15,2))

x=sum1(5,10,88,99,6,32,15,2)
r=x-57
print("out side fun =",r)


