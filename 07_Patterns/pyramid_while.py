#pyramid
'''
i=0
j=0
k=0
l=0
while i<=3:
    j=i
    while j<=3:
        print(" ",end="")
        j=j+1
        k=0
        l=0
    while k<=0:
        while l<=i:
            print("*",end=" ")
            l=l+1
        print("\n",end="")
        k=k+1
    print("\n",end="")
    i=i+1
#
n=3
i=0
j=0
k=0
while i<=n:

    while j<=n+i-1:
        print(end=" ")
        j=j+1
    k=0
    while k!=2*i+1:
        print("*",end=" ")
        k=k+1
    print("\n")
    i=i+1


while cond:
    stms
    inc/dec

#
for i in range(1,6+1):
    print(i)
    i=i+1
#
l=[5,6,7,8,9]
for i in l:
    print(l[2])
#
n=int(input("Enter your no"))
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
#
for i in range(0,10):
    if i%2==0:
        print(i)
#
for i in range (0,10):
    print(i)


i=0
while i<=26:

    c=65
    j=0
    while j<=27-i:
       print(" ",end="")
       j=j+1

    k=0
    while k<=i:
        print(chr(c),end=" ")
        k=k+1

        c=c+1

    i=i+1
    print(i)


row=int(input("Enter no of rows"))
star=1
space=row-1
while row>0:
    print(' '*space+'* '*star)
    space=space-1
    star=star+1
    row=row-1



row=int(input("Enter no of rows"))
star=row-1
space=0
while row>=0 and space<=row:
    print(' '*space+'* '*star)
    space=space+1
    star=star-1
    row=row+1
    


'''


i=0
j=0
k=0
l=0
while i<=3:
    j=i
    while j<=3:
        print(" ",end="")
        j=j+1
        k=0
        l=0
    while k<=0:
        while l<=i:
            print("*",end=" ")
            l=l+1
        print("\n",end="")
        k=k+1
    print("\n",end="")
    i=i+1

