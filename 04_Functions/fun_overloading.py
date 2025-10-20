#POLMORPHISM:
#->Same func. name but diff args
'''
def fun(a,b):
    print("values of A is:",a,"\nValues of B is:",b,"\n")

fun(10,20)
fun(8,2.9)
fun(15.9,11)
fun("WAJID","TAMBOLI")
fun(8,"CADD CENTRE")
'''

#OPERATER OVERLOADING:
'''
print(10+20)
print("Wajid "+"Tamboli")
print(5*3)
print("Wajid"*3)
'''

#FUNCTION OVERLOADING:
'''
def product(a,b):
    print(a*b)
def product(a,b,c):
    print(a*b*c)
product(5,2,10)
'''
