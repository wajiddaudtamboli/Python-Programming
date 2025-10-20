#ATM PROJECT THROUGH CLASS & OBJECT:
#CLASS & OBJECT:

class atm:
    def __init__(self,b):
        
        self.wt=0
        self.bal=b
        self.dp=0

    def accountdetails(self):

        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        print("        NAME:WAJID DAUD TAMBOLI         ")
        print("         ACCOUNT NO:XXXX7342024         ")
        print("           IFCSC CODE:SBI456            ")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def balenq(self):
        
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        print("Your Bank balance is Rs.",self.bal)
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def withdraw(self):

        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        self.wt=int(input("Enter the withdraw amount: Rs."))
        if self.wt>self.bal:
            print("Insufficient balance\n")
        else:
            self.bal=self.bal-self.wt
        print("The Cash withdrawal is Rs.",self.wt)
        print("The balance remaining after withdraw is Rs.",self.bal)	   	    
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")    
            
    def deposit(self):

        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        self.dp=int(input("Enter the deposit amount: Rs."))
        print("You have deposited Rs.",self.dp)
        self.bal=self.bal+self.dp
        print("Now your bank balance is Rs.",self.bal)
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

    def ministatement(self):

        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        print("         WELCOME TO BANK OF INDIA       ")
        print("           SAAT RASTA, SOLAPUR        \n")
        print("            MINI STATEMENT\n")
        print("NAME:WAJID DAUD TAMBOLI")
        print("ACCOUNT NO:XXXX7342024")
        print("Your Bank balance is Rs.",self.bal)
        print("The Cash withdrawal is Rs.",self.wt)
        print("You have deposited Rs.",self.dp)
        print("\nDATE:01-06-2024  AND TIMING:15:40")
        print("       HELPLINE NO:9667933839")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

        
p=1234
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print("ATM PROJECT THROUGH CLASS & OBJECT")
print("     BY-WAJID DAUD TAMBOLI")
print("  CHECKED BY: MUJAHID FULMAMDI\n")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print("***********************************\n")
pin=int(input("     Enter your Pin: "))
print("\n***********************************")
b=5000
if pin==p:
    
    obj=atm(b)
    
    while True:

        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        print("       WELCOME TO BANK OF INDIA")
        print("         SAAT RASTA, SOLAPUR\n")
        print("1 Account Details")
        print("2 Balance Inquiry")
        print("3 Cash Witdrawal")
        print("4 Cash  Deposit")
        print("5 Receipt")
        print("6 EXIT")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        ch=int(input("Enter your choice: "))
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        if ch==1:

            obj.accountdetails()

        elif ch==2:

            obj.balenq()

        elif ch==3:

            obj.withdraw()

        elif ch==4:

            obj.deposit()

        elif ch==5:

            obj.ministatement()       
            
        elif ch==5:

            exit()
        
else:
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")               
    print("         Invalid Credentials")
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")	    

	

	
