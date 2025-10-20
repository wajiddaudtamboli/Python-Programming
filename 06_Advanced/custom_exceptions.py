'''
class Error(Exception):

    pass

class ValueToLarge(Error):

    pass


class ValueToSmall(Error):

    pass

while True:
    

    try:
        

        n=10

        n1=int(input("enter no"))


        if n1>n:

            raise ValueToLarge

        elif n1<n:

            raise ValueToSmall

        elif n1==n:

            print("you gusse right no")
            break


    except ValueToLarge:

        print("plz enter small value")

    except ValueToSmall:

        print("plz enter large value")
##
n=1
while n<=10:
    print(n)
    n=n+1
'''

class Erroe(Exception):
    pass
class ValueToLarge(Exception):
    pass
class ValueToSmall(Exception):
    pass

while True:
    try:
        n=10
        n1=int(input("Enter Your No."))

        if n1>n:
            raise ValueToLarge

        elif n1<n:
            
            raise ValueToSmall
        


        elif n1==n:
            print("You Gusse Right Value")
            break

    except ValueToLarge:
        print("Please Enter Small Value")

    except ValueToSmall:
        print("Please Enter Large Value")


    

