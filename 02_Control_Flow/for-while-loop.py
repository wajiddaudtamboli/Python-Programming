#WHILE LOOP-
"""
Syntax:

for i in range(start):

for i in range(start,stop):

for i in range(start,stop,difference):
"""
#Display hello:
"""
for i in range(Hello,10):
    print(i)
"""    

#Numbers 1 to 10:
'''
for i in range(1,10,1):
    print(i)
'''    
#Table of 2:
'''
print("TABLE OF 2 is:")
for i in range(2,22,2):
    print(i)
'''

#Table from 1 to 100:
"""
print("TABLE FROM 1 TO 10 is:")
for i in range(1,11):
    for j in range (1,11):
        print(i,"X",j,"=",i*j,end="")
        print()
"""

#Prime no:
'''
print("PRIME NO. BTW 1 TO 20 ARE:")
for i in range(1,20):
    for j in range(2,i):
        if i%j==0:
            break;
    else:
        print(i)
'''

#Fibonacci Series:
'''
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("              Fibonacci Series:            \n")
n=int(input("Enter the range of fibonacci series: "))
i=1
n1=0
n2=1
print(n1)
print(n2)
for i in range(i,n):
    temp=n1+n2
    n1=n2
    n2=temp
    print(n2)
    i+=1
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
'''

#WHILE LOOP:        
"""
Syntax:
while cond:
    print(i)
    statement1->i+=1 or i-=1...
    statement2
"""

#Display hello:
'''
i=1
while i<=10:
    print("Hello")
    i+=1
'''

#No. from 1 to 10:
'''
i=1
while i<=10:
    print(i)
    i+=1
'''

#No. from 1 to 10 in reverse order:
'''
i=10
while i>=1:
    print(i)
    i-=1
'''

#Fibonacci Series:
'''
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("              Fibonacci Series:            \n")
n=int(input("Enter the range of fibonacci series: "))
i=1
n1=0
n2=1
print(n1)
print(n2)
while(i<n):
    temp=n1+n2
    n1=n2
    n2=temp
    print(n2)
    i+=1
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
'''

    
