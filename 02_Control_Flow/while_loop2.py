#Pyramid in chr
'''
i=0
j=0
k=0
l=0
while i<=3:
    j=i
    while j<=3:
        print(' ',end='')
        j=j+1
        k=0
        l=0
    while k<=0:
        while l<=i:
            print(chr(65),end=' ')
            l=l+1
        print('\n',end='')
        k=k+1
    print('\n',end='')
    i=i+1


#
row=int(input("Enter no of rows"))
star=1
space=row-1
while row>0:
    print(" "*space+"* "*star)
    space=space-1
    star=star+1
    row=row-1

#ascii-- american standard code
n=97
while n<=122:
    
    print(chr(n),n)
    n=n+1

# pyramid in alphabets or charectars
row=int(input("Enter no of rows"))
star=1
space=row-1
while row>0:
    print(" "*space+chr(65)*star)
    space=space-1
    star=star+1
    row=row-1

'''










    
