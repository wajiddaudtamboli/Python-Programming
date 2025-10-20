'''
rows=int(input("Enter number of rows: "))
for i in range (rows):
    for j in range (i+1):
        print(j+1,end=" ")
    print()

def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
num=7
result=factorial(num)
print("The factorial of",num,"is",result)

#lower pyramid
for i in range (5):
    for j in range(5-i):
        print("*",end=" ")
    print()

n=0
while n<=10:
    print(n)
    n=n+1

n=int(input("Enter no."))
i=1
sum1=0
while i<=n:
    print(i)
    sum1=sum1+i
    i=i+1
print(sum1)
'''


#lower pyramid
def pyramid(n):
    for i in range (n):
        for j in range(n-i):
            print("*",end=" ")
        print()
pyramid(5)
