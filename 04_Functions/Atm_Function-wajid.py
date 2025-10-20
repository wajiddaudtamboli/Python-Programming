 #ATM Project using function
def withdraw(wt,bal):
    wt=int(input("Enter the withdraw amount: Rs."))
    if wt>bal:
        print("Insufficient balance\n")
    else:
        bal=bal-wt
    return bal

def deposit():
    dp=int(input("Enter the deposit amount:Rs."))
    return dp

pin=1234
bal=5000
print("***********************\n")
n=int(input("Enter the Pin number: "))
print("\n***********************")


if pin==n:
    
     print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    print("WELCOME TO BANK OF INDIA")
    print("SAAT RASTA, SOLAPUR")

    while True:
        print("1 Account Details")
	#print("2 Bank Account")
	print("3 Cash Witdrawal")
	print("4 Cash  Deposit")
	print("5 Receipt")
	print("6 EXIT")

	print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        choice=int(input("Enter your choice: "))
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        if choice==1:
            
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            print("NAME:WAJID DAUD TAMBOLI")
	    print("ACCOUNT NO:XXXX7342016")
	    print("IFCSC CODE:SBI456")
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        elif choice==2:
            
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
	    print("Your Bank balance is Rs.",bal)
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")       
		
        elif choice==3:
            
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            print("The Cash withdrawal is Rs.",wt)
            withdraw(wt,bal)
            print("The balance remaining after withdraw is Rs.",wt)	   	    
            print("\nXXXXXXXXXXXXXXXXXXXXXXX\n")
                   
	elif choice==4:
            
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")      
            deposit(dp)
            bal=bal+dp
            print("You have deposited Rs.",dp)
            print("Now your bank balance is Rs.",bal)
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")       

        elif choice==5:
            
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            print("         WELCOME TO BANK OF INDIA       ")
            print("           SAAT RASTA, SOLAPUR         \n")
            print("NAME:WAJID DAUD TAMBOLI")
	    print("ACCOUNT NO:XXXX7342016")
	    print("Your Bank balance is Rs.",bal)
	    print("The Cash withdrawal is Rs.",wt)
            print("You have deposited Rs.",dp)
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            
        elif choice==6:
            
	    exit()
	
else:
    print("XXXXXXXXXXXXXXXXXXXXXXX\n")               
    print("\n Invalid Credentials")
    print("\nXXXXXXXXXXXXXXXXXXXXXXX\n")
    

