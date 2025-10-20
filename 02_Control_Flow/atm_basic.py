#atm basic
pin=int(input("Enter your pin "))
if pin==1234:
    print("Correct PIN")
    print("\n1 for Account Detail \n2 for Check Balance \n3 for Cash Withdraw")
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










