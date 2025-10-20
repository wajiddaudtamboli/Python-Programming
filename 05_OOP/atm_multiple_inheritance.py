#ATM TROUGH MULTIPLE INHERITANCE:

class withdrawal:
    def __init__(self,wt):
        self.wt=wt
    
class deposit:
    def __init__(self,dp):
        self.dp=dp

class atm(withdrawal,deposit):
    def __init__(self,pin):        
        
        self.pin=pin
        self.p=1234
        self.bal=5000
        withdrawal.__init__(self,wt)
        deposit.__init__(self,dp)
        
        if self.pin==self.p:
            
            while True:

                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                print("                   WELCOME TO BANK OF INDIA")
                print("                          SAAT RASTA, SOLAPUR\n")
                print("1.Account Details")
                print("2.Balance Inquiry")
                print("3.Cash Witdrawal")
                print("4.Cash  Deposit")
                print("5.EXIT")
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                self.ch=int(input("Enter your choice: "))
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

                if self.ch==1:

                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                    print("                  NAME:WAJID DAUD TAMBOLI         ")
                    print("                 ACCOUNT NO:XXXX7342024         ")
                    print("                     IFCSC CODE:SBI456            ")
                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

                elif self.ch==2:

                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                    print("Your Bank balance is Rs.",self.bal)
                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

                elif self.ch==3:

                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                    
                    self.wt=int(input("Enter the withdraw amount: Rs."))
                    if self.wt>self.bal:
                        print("Insufficient balance\n")
                    else:
                        self.bal=self.bal-self.wt
                        print("The Cash withdrawal is Rs.",self.wt)
                        print("The balance remaining after withdraw is Rs.",self.bal)	   	    
                        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                               
                elif self.ch==4:

                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")                    
                    self.dp=int(input("Enter the deposit amount: Rs."))
                    print("You have deposited Rs.",self.dp)
                    self.bal=self.bal+self.dp
                    print("Now your bank balance is Rs.",self.bal)
                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")       
                    
                elif self.ch==5:

                    exit()
                
        else:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")               
            print("         Invalid Credentials")
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")	  
                

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print(" ATM PROJECT THROUGH MULTIPLE INHERITANCE:")
print("         BY-WAJID DAUD TAMBOLI")
print("     CHECKED BY: MUJAHID FULMAMDI\n")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print("***********************************\n")
pin=int(input("     Enter your Pin: "))
print("\n***********************************")
obj=atm(pin)
obj.atm()

