#chr
"""
n=65
m=97
while n<=90:
    while m<=122:
        print(chr(m),m)
        m=m+1
    print(chr(n),n)
    n=n+1

#print('Omkar '*5)
#pyramid with chr
row=int(input("Enter no of rows"))
star=1
space=row-1
i=65
while row>0:
    print(" "*space+chr(i)*star)
    space=space-1
    i=i+1
    star=star+2
    row=row-1
#chr
i=0
j=0
while i<=4:
    j=0
    while j<=i:
        print(chr(65),end="")
        j=j+1
    print("\n",end="")
    i=i+1

#
n=int(input("Enter your no "))
i=65
j=0
while i<=n:
    j=0
    while j<3:
        print(chr(i),end="")
        j=j+1
        i=i+1
    print("\n",end="")
"""
#rightangle triangle in chr 
i=65
j=65
while i<=69:
    j=65
    while j<=i:
        print(chr(i),end="")
        j=j+1
    print("\n",end="")
    i=i+1





















