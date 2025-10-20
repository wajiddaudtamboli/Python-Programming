'''                     
def sqr(n):
    while n<=10:
        s=n*n
        n=n+1
        yield s
f=sqr(1)
for i in f:
    print(i)
#

    
def sqr(n):
    while n>=1:
        s=n*n
        n=n-1
        yield s
f=sqr(10)
for i in f:
    print(i)


 '''
#ATM
pin=int(input("Enter your PIN"))

if pin==2525:
    print("Correct PIN")

    print("\n1 for Account Detail \n2 for Check Balence \n3 for Cash Withdraw")
    a=int(input("Enter Your Choice "))
    if a==1:
        print("Account Detail")
    elif a==2:
        print("Check Balance")
    elif a==3:
        print("Cash Withdraw")
    else:
        print("Wrong Choice")
else:
    print("Wrong PIN")



    
