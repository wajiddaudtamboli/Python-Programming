#RIGHT ANGLE TRIANGLE IN CHR
"""
i=65
j=65
while i<=95:
    j=65
    while j<=i:
        print(chr(i),end=' ')
        j=j+1
    print("\n",end="")
    i=i+1

k=1
while k<=10:
    print(k)
    k=k+1
 """
#Alphabat triangle
i=0
while i<=26:
    c=65
    j=0
    while j<=27-i:
        print("",end=" ")
        j=j+1
    k=0
    while k<=i:
        print(chr(c),end=" ")
        k=k+1
        c=c+1
    i=i+1
    print(i)
