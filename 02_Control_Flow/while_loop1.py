"""
#1
i=1
j=0
while i<=4:
    j=0
    while j<=4:
        print('*',end='')
        j=j+1
    print('\n',end='')
    i=i+1
#2
i=0
j=0
while i<=4:
    j=0
    while j<=4:
        print(i,end='')
        j=j+1
    print('\n',end='')
    i=i+1
#3
i=0
j=0
while i<=4:
    j=0
    while j<=4:
        print(j,end='')
        j=j+1
    print('\n',end='')
    i=i+1
#4
i=0
j=0
while i<=4:
    j=0
    while j<=i:
        print(i,end='')
        j=j+1
    print('\n',end='')
    i=i+1
#5
i=0
j=0
while i<=4:
    j=i
    while j<=4:
        print(i,end='')
        j=j+1
    print('\n',end='')
    i=i+1
#6
i=0
j=0
while i<=10:
    j=0
    while j<3:
        print(i,end=' ')
        j=j+1
        i=i+1
    print('\n',end='')

#
i=0
j=0
while i<=3:
    j=0
    while j<=i:
        print('#',end='')
        j=j+1
    print('\n',end='')
    i=i+1
#"""
i=0
j=0
k=0
l=0
while i<=3:
    j=i
    while j<=3:
        print('#',end='')
        j=j+1
        k=0
        l=0
    while k<=0:
        while l<=i:
            print("*",end="")
            l=l+1
        print("\n",end="")
        k=k+1
    print('\n',end='')
    i=i+1











    
