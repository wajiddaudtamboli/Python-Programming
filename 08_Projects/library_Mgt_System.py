#LIBRARY MANAGEMENT SYSTEM:
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("               LIBRARY BOOK MANAGEMENT SYSTEM: ")
print("                    GENERAL GUIDELINES:\n")
print("Book returned within 4 day-> No Fine\nBook returned in 5 days->1 rs Extra fine\nBook returned between 5 days to 10 days->2 rs Extra fine")
print("Book returned between 11 days to 30 days->5 rs Extra fine\nBook Returned after 30 days->Memership Cancelled\n")
book=int(input("Enter the code of the book: "))
bookamt=int(input("Enter the book amount: "))
days=int(input("Enter the no. of days: "))

if days<5:
    print("\n#############################################################\n")
    print("                    Book returned within 4 day\n")
    print("                          No Fine")
    print("\n#############################################################\n")

elif days==5:
    print("\n#############################################################\n")
    print("            Book returned in 5 days->1 rs Extra fine=Rs.1")
    print("                       Your fine is Rs.",days)
    print("\n##############################################################\n")

elif days>5 and days<=10:
    print("\n##############################################################\n")
    print("Book returned within 5 days            ->1 rs Extra fine= 1 X 5 = Rs. 5")
    remdays=days-5
    fine=2
    print("Book returned between 5 days to 10 days->2 rs Extra fine=",remdays,"X",fine,"=Rs.",remdays*fine)
    fine1=(remdays*fine)+5
    print("              Your fine is Rs.",fine1)
    print("\n###############################################################\n")

elif days>10 and days<=30:
    print("\n###############################################################\n")
    print("Book returned within 5 days            ->1 rs Extra fine= 1 X 5 = Rs. 5")
    print("Book returned between 5 days to 10 days->1 rs Extra fine= 2 X 5 = Rs. 10")
    remdays=days-10
    fine=5
    print("Book returned between 11 days to 30 days->5 rs Extra fine=",remdays,"X",fine,"=Rs.",remdays*fine)
    fine1=(remdays*fine)+5+10
    print("                      Your fine is Rs.",fine1)
    print("\n################################################################\n")

else:
    print("\n################################################################\n")
    print("                    Book Returned after 30 days\n")
    print("                         Memership Cancelled")
    print("\n################################################################\n")

print("                       THANKS FOR VISITING")    
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")    
    
