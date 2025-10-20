"""
#Table
n=int(input("Enter your no. "))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1

# sum of all no. from start to end
n=int(input("Enter your no. "))
i=1
sum1=0
while i<=n:
   # print(i)
    sum1=sum1+i
    i=i+1
print(sum1)

#sum of even no.
i=1
s=0
while i<=10:
    if i%2==0:
        print('Even no. ',i)
    s=s+i
    i=i+1
    print(s)

# sum of even and odd no.
i=1
s1=0
s=0
while i<=10:
    if i%2==0:
        print("even no. ",i)
        s=s+i
    else:
        print("odd no. ",i)
        s1=s1+i
    i=i+1
print(s+s1)
print(s,'+',s1,'=',s+s1)
"""
