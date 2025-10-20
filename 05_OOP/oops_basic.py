#oops-- object oriented programing
'''
class-- blueprint or prototype
        not real world entity 
        


object --- instance of class
            real world entity


#syntax:

class class_name:
    attributes-- variables of class
    method define():
    def fun_name():'''

'''
class fruit:
    name='apple'
    name1='mango'



obj=fruit()
print(obj.name)
print(obj.name1)

'''
'''
#self  keyword --- to access atrribute values
class emp:
    name='abc'

    def emp_info(self):
        print("name is",self.name)

obj=emp()
obj.emp_info()'''

'''
def fun(a):
    print(a)

fun(6)
'''
'''
class emp:
    def __init__(self,name,sal):
       self.name1=name
       self.sal1=sal
       
    def emp_info(self):
        print("name of emp",self.name1,"sal of emp",self.sal1)
    


obj=emp('saifan',10000)
obj.emp_info()
'''
class emp:
    emp_id=20 
    def emp_info(self):
        name='abc'
        print("name is",self.emp_id)
        
    def emp_info1(self):
        print(self.emp_id)

obj=emp()
obj.emp_info()
obj.emp_info1()
















        





















 
