''' inheritance--- inherit properties and behaviour from parent
types of inheritance
parent class(base class) ---
child class(derived class) --- 







1 single --- one parent class and one child class   (father-son)
2 multi level --- one or more parent class and one or more child class (grandfather--father--son)
3 multiple
4 heirarchical'''

#single inheritance
'''class Parent:
    def print1(self):
        print("I am parent class")

class child(Parent):
    def print2(self):
        print("I am child class")

obj = child()
obj.print1()
obj.print2()
'''

#mulitlevel inheritance
class Grandfather:
    def __init__(self,name):
        self.na=name
        
    def print1(self):
        print("I am super parent class")


class father(Grandfather):
    def __init__(self,name,age):
        self.ag=age
        
        #Grandfather. __init__(self,name)
        super().__init__(name)
    def print2(self):
        print("I am parent class")
        #print(self.na)

class son(father):
    def __init__(self,na,ag):
        
        #father.__init__(self,na,ag)
        super().__init__(na,ag)
    
    def print3(self):
        print("I am child class")
        print(self.na,self.ag)


obj= son('saifan',22)
obj.print3()
obj.print2()
obj.print1()


















