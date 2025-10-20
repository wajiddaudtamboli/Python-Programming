'''
                                        INHERITANCE PRACTICE:
                                        
*Inheritance-one class deriverd from another class is called inheritance.

*Base class /super class /parant class-main class

*Derived class /sub class /child class-derived class

*Advantage-Reusability

                                    Types of Inheritance -
1.Single Inheritance - a class is deriverd from a parent class is called single inheritance.
2.Multilevel Inheritance
3.Multiple Inheritance
4.Hybrid Inheritance

'''

#SINGLE INHERITANCE:
'''
class Animal:
    
    def eat(self):
        print("Eating")

class dog(Animal):
    
    def bark(self):
        print("Bark")

obj=dog()
obj.eat()
obj.bark()
'''

#MULTILEVEL INHERITANCE:
'''
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
'''

'''
class A:
    def fun1():
        a=10
        return a

class B(A):
    def fun2():
        b=20
        return b
    
class C(B):
    def fun3():
        print(A.fun1()+B.fun2())

obj=C
C.fun3()
'''

#MULTIPLE INHERITANCE:
"""
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
        print("ADDITION OF {0} AND {1} IS {2}".format(self.a,self.b,self.a+self.b))

obj=C(20,30)
"""

'''
class TeamMember:
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid

class Workers:
    def __init__(self,salary,post):
        self.salary=salary
        self.post=post

class Teamleader(TeamMember,Workers):
    def __init__(self,name,uid,salary,post,exp):
        self.exp=exp
        TeamMember.__init__(self,name,uid)
        Workers.__init__(self,salary,post)
        print("Name:{0} UID:{1} Salary:{2} Post:{3} Experience:{4}".format(self.name,self.uid,self.salary,self.post,self.exp))

t=Teamleader("Wajid_Tamboli",786,2000,"Trainer",1)
'''

'''
class Marks1:
    def __init__(self,mm1):
        self.mm1=mm1

class Marks2:
    def __init__(self,mm2):
        self.mm2=mm2

class student(Marks1,Marks2):
    def __init__(self,n,mm1,mm2):
        Marks1.__init__(self,mm1)
        Marks2.__init__(self,mm2)
        self.n=n
        per=(self.mm1/self.mm2)/2
        
        print("Name:{0} Per:{1}".format(self.n,str(per)))

n=(input("Enter your name: "))
mm1=int(input("Enter your marks1:"))
mm2=int(input("Enter your marks2:"))
obj=student(n,mm1,mm2)
'''
    
#HYBRID INHERITANCE:
'''
class Marks1:
    def __init__(self,mm1):
        self.mm1=mm1

class Marks2:
    def __init__(self,mm2):
        self.mm2=mm2

class Student(Marks1,Marks2):
    def __init__(self,name):
        self.name=name

class Data(Student):        
    def __init__(self,n,mm1,mm2):
        Marks1.__init__(self,mm1)
        Marks2.__init__(self,mm2)
        self.n=n
        per=(self.mm1/self.mm2)/2
        
        print("Name:{0}\nPer:{1}".format(self.n,str(per)))

n=(input("Enter your name: "))
mm1=int(input("Enter your marks1:"))
mm2=int(input("Enter your marks2:"))
obj=Data(n,mm1,mm2)
'''    
