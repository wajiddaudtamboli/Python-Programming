#EXCEPTION HANDLING:
'''
a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
try:
    print("The division is",a/b)
except:
    print("can not divide by 0")
print("EXEXUTED SUCCESSFULY")    
'''

'''
a=int(input("Enter the number:"))
try:
    print(a)
except valueError as e:
    print(e)
print("End of the program")    
'''

#ASSERTION:
'''
a=int(input("Enter the 1st no."))
b=int(input("Enter the 2nd no."))
assert b!=4
try:
    print(int(a)/int(b))
except AssertionError as e:
    print(e)
'''                                                                                                 
