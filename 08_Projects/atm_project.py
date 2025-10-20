

import time
print()
print()
print("--------Welcome To The ATM Service--------".center(70))
print()
pin=int(input("Enter your pin: ".rjust(40)))
print()
print()
balance=200000
depo=0
withd=0
if pin==2305:
    print("...........Login Successful............".center(70))
    while True:
        print()
        print("_______________________________".center(70))
        print("    MAIN MENU    ".center(70))
        print("_______________________________".center(70))
        print("1.Account Details".rjust(40))
        print("2.Account Balance".rjust(40))
        print("3.Deposite       ".rjust(40))
        print("4.Withdraw       ".rjust(40))
        print("5.Receipt        ".rjust(40))
        print("6.Exit           ".rjust(40))
        ch=int(input("Enter your choice: ".rjust(40)))
        if ch==1:
            print("_______________________________".center(70))
            print()
            print("..........1.Account Details..........".center(70))
            print("\n")
            print("Account Holders Naame: Simran Tamboli".center(70))
            print("Account No: 1234567890               ".center(70))
            print("Account Type: Saving Account         ".center(70))
            print("Mobile No : ******9730               ".center(70))

        elif ch==2:
            print("_______________________________".center(70))
            print("......2.Account Balance........".center(70))
            print("\n")
            print("Total Balance : Rs.".rjust(40),balance)
        elif ch==3:
            print("_______________________________".center(70))
            print("...........3.Deposite..........".center(70))
            print("\n")
            depo=int(input("Enter deposite amount: ".rjust(40)))
            balance=balance+depo
        elif ch==4:
            print("_______________________________".center(70))
            print("...........4.Withdraw..........".center(70))
            print("\n")
            withd=int(input("Enter withdrawal amount: ".rjust(40)))
            balance=balance-withd
        elif ch==5:
            
            print("...............RECEIPT...............".center(70))
            print("\n")
            print("Date and Time\t".rjust(30),time.ctime())
            print(".....................................".center(70))
            print("Account Holders Naame: Simran Tamboli".center(70))
            print("Account No: 1234567890               ".center(70))
            print("Account Type: Saving Account         ".center(70))
            print("Mobile No : ******9730               ".center(70))
            print("Withdrawal Amount:".rjust(34),withd)
            print("Deposite Amount:".rjust(32),depo)
            print("Total Balance:".rjust(30),balance)

            
            f=open("ATM Receipt.txt",'a')
            f.write("\n................RECEIPT..............")
            f.write("\n")
            f.write("\nDate and Time\t"+time.ctime())
            f.write("\n.....................................")
            f.write("\nAccount Holders Naame: Simran Tamboli")
            f.write("\nAccount No: 1234567890  ")
            f.write("\nAccount Type: Saving Account")
            f.write("\nMobile No : ******9730 ")
            f.write("\nWithdrawal Amount:"+str (withd))
            f.write("\nDeposite Amount:"+str (depo))
            f.write("\nTotal Balance:"+str (balance))
            f.write("\n.......................................")
            f.close()
            
        elif ch==6:
            exit()
        else:
            print("Invalid choice".center(70))
else:
    print("Invalid Pin".rjust(40))
        
        
        
    
        
