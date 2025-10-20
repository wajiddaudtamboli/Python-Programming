#Check your username and password
"""
a=input("Enter your username ")
b=int(input("Enter your password "))
if a=='Omkar':
    print("correct username ")
    if b==123:
        print("correct password ")
    else:
        print("wrong password ")
else:
    print("wrong username")

#Calculator
n=1
while n<=5:
    print("\n1 for Add \n2 for Sub \n3 for Multi \n4 for Div")
    a=int(input("Enter your choice "))
    b=int(input("Enter your No. "))
    c=int(input("Enter your NO. "))

    if a==1:
        print("Add",b+c)
    elif a==2:
        print("Sub",b-c)
    elif a==3:
        print("Multi",b*c)
    elif a==4:
        print("Div",b/c)
    else:
        print("Invalid choice")
    n=n+1
    
"""
#ATM
print("\n1 for English \n2 for Hindi \n3 for Marathi")
n=int(input("Enter your Language "))
if n==1:
    print("English")
elif n==2:
    print("Hindi")
elif n==3:
    print("Marathi")
else:
    print("Invalid choice")
pin=int(input("Enter your pin "))

if pin==1234:
    print("Correct PIN")
else:
    print("Wrong PIN")

print("\n1 for Account Detail \n2 for Check Balence \n3 for Cash Waitdraw")
a=int(input("Enter Your Choice "))
if a==1:
    print("Account Detail")
if a==2:
    print("Check Balence")
if a==3:
    print("Cash Waitdraw")
else:
    print("Wrong Choice")

"""
n=int(input("Enter your Language "))
pin=int(input("Enter your pin "))
a=int(input("Enter Your Choice "))
if n==1:
    print("English")
elif n==2:
    print("Hindi")
elif n==3:
    print("Marathi")
    if pin==1234:
        print("Correct PIN")
        if a==1:
            print("Account Detail")
        elif a==2:
            print("Check Balence")
        elif a==3:
            print("Cash Waitdraw")
        else:
            print("Wrong Choice")
    else:
        print("Wrong PIN")
else:
    print("Invalid choice")
"""











