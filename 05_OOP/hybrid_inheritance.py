 
# Hybrid Inheritance
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

