'''l=[4,6,5,7,8,1,3]

1: arrange list in ascending order

2: take input from user of particular index and then update
new element at that place
index=3
value=11
l=[4,6,5,11,8,1,3]


l=[4,6,5,4,8,4]
3: find repeated elements in list
4: 4 is repeated 3 times

#1
l=[4,6,5,7,8,1,3]
sum1=0
for i in l:
    sum1=sum1+i
print('\n',sum1)

#2
l=[3,2,2,5,4,5,3,6,8,5,2]
sum2=0
for i in l:
    sum2=sum2+i
    print(sum2)

#3 change the value
l=[3,2,2,5,4,5,3,6,8,5,2]
for i in l:
    l[3]=10
print('\n',l)

#4
l=[3,2,2,5,4,5,3,6,8,5,2]
for i in l:
    l.sort()
print('\n',l)

#5
l=[3,2,2,5,1,2,3,5,2,4]
c=0
a=int(input("Enter a  no. to check"))
for i in range(0,10):
    if(l[i]==a):
        c=c+1
print(a,"is repeated ",c,"times")
'''
#6 ascending order
l=[3,2,2,5,1,2,3,5,2,4]
c=0
for i in range(0,10):
    


