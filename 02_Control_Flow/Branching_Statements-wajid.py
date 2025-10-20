#BRANCHING STATEMENTS:

#1.Simple if:
'''
print("XXXXXXXXXXXXXXXXXXXXX\n")
print("   EVEN CHECKER    ")
a=int(input("Enter the no."))
if a%2==0:
    print("The no. is Even",a)
print("XXXXXXXXXXXXXXXXXXXXX\n")
'''

#2.if else:
#EVEN/ODD 
'''
print("XXXXXXXXXXXXXXXXXXXXX\n")
print("   EVEN/ODD CHECKER    ")
a=int(input("Enter the no."))
if a%2==0:
    print("The no. is Even",a)
else:
    print("The no. is Odd",a)
print("XXXXXXXXXXXXXXXXXXXXX\n")
'''

#POSITIVE/NEGATIVE
'''
print("XXXXXXXXXXXXXXXXXXXXXXX\n")
print("POSITIVE/NEGATIVE CHECKER")
a=int(input("Enter the no."))
if a>=0:
    print("The no. is Positive",a)
else:
    print("The no. is Negative",a)
print("XXXXXXXXXXXXXXXXXXXXXXX\n")
'''

#EQUAL/UNEQUAL
'''
print("XXXXXXXXXXXXXXXXXXXXXXX\n")
print("EQUAL/UNEQUAL CHECKER")
a=int(input("Enter the no."))
b=int(input("Enter the no."))
if a==b:
    print("The numbers are Equal")
else:
    print("The numbers are Unequal")
print("XXXXXXXXXXXXXXXXXXXXXXX\n")
'''

#MULTIPLE OF 5
'''
print("XXXXXXXXXXXXXXXXXXXXXXX\n")
print("MULTIPLE OF 5 CHECKER")
a=int(input("Enter the no."))
if a%5==0:
    print("Series of 5")
else:
    print("Not Series of 5")
print("XXXXXXXXXXXXXXXXXXXXXXX\n")
'''

#3.if elif:
#COLLEGE ALLOTMENT PORAL
'''
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
print("CSE COLLEGE ALLOTMENT PORAL\n")
score=int(input("Enter the no."))
if score>=90 and score<=100:
    print("IIT BOMBAY->100%-90%->CSE")
elif score>=80 and score<=89:
    print("NIT NAGPUR->89%-80->CSE%")
elif score>=70 and score<=79:
    print("IIIT KANPUR->79%-70%->CSE")
elif score>=60 and score<=69:
    print("BITS PILANI GUJARAT->60%-69%->CSE")
elif score>=50 and score<=59:
    print("COEP PUNE->50%-59%->CSE")
elif score>=40 and score<=49:
    print("NKCOET SOLAPUR->40%-49%-CSE")
elif score>=33 and score<=39:
    print("VVP SOLAPUR->33%-40%-CSE")    
else:
    print("NOT ELEGIBLE FOR COUNSELLING")
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
'''
