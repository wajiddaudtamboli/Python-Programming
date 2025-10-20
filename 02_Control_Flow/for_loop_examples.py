#for loop
c=0
n=int(input("Enter your no "))
l=[1,2,4,1,2,1,4,4,3,4]
for i in l:
    if i==n:
        c=c+1
print(c)

n=int(input("Enter your no. "))
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")

for i in range(0,10):
    if i%2==0:
        print(i)
