# Upper Pyramid 
i=0
while i<=5:
    j=0
    while j<=5-i:
        print("",end=" ")
        j=j+1
    k=0
    while k<=i:
        print("*",end=" ")
        k=k+1
    i=i+1
    print(i)
# Lower Pyramid

i=0
while i<=5:
    j=0
    while j<=i:
        print("",end=" ")
        j=j+1
    k=0
    while k<=5-i:
        print("*",end=" ")
        k=k+1
    i=i+1
    print(i)
