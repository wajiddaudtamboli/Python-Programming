#PERFECT NO.:
'''
sum=0
n=input("Enter a no.")
if n.isdigit():
    n=int(n)
    if n<=1:
        print("Perfect no.")
    else:        
        for i in range(1,n):
            if n%i==0:
                sum+=i
        if sum==n:                               
            print("Perfect no.")
        else:
            print("Not Perfect no.")            
else:
    print("Plz enter a valid +ve no.")
'''

#PALINDROME NO:
'''
n=input("Enter a no.")
if n.isdigit():
    if n==n[::-1]:
        print("Palindrome no.")
    else:
        print("Not Palindroime no.")
else:
    print("Plz enter a valid +ve no.")
'''


        
