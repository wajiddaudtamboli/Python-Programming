
## Inheritence
#1 Singal Inheritence
class Animal:

    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")

d=Dog()
d.eat()
d.bark()

#2 Multilevel Inheritance
class Animal:
    def __init__(self,name):
        print(name,"is animal")
        

class fly(Animal):
    def __init__(self,name):
        print(name,"can't fly")
        super().__init__(name)

class swim(fly):
    def __init__(self,name):
        print(name,"can't swim")
        super().__init__(name)


s=swim("Dog")

#3 Multiple Inheritence
class A:
    def __init__(self,a):
        self.a=a

class B:
    def __init__(self,b):
        self.b=b

class C(A,B):
    def __init__(self,a,b):

        A.__init__(self,a)
        B.__init__(self,b)
        print("Addition of {0} and {1} is {2}".format(self.a, self.b, self.a+self.b))
c=C(20,30)

#4 Hybrid Inheritance
class Marks1:
    def __init__(self,m1):
        self.m1=m1

class Marks2:
    def __init__(self,m2):
        self.m2=m2

class student(Marks1,Marks2):
    def __init__(self,name):
        self.name=name

class Data(student):
    def __init__(self,m1,m2,name):
        student.__init__(self,name)
        Marks1.__init__(self,m1)
        Marks2.__init__(self,m2)

        per=(self.m1+self.m2)/2
        print("Name:{0} in per:{1}".format(self.name,per))

n=input("Enter name:")
mm1=int(input("Enter marks1:"))
mm2=int(input("Enter marks2:"))
d=Data(mm1,mm2,n)

## Polymorphism
def fun(a,b):
    print("values A:",a,"it B:",b)

fun(10,20)
fun(8,2.9)
fun("Hello","World")
fun(8,"Hello")





