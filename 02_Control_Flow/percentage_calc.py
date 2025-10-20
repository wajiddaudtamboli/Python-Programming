a=int(input('Enter 1st sub marks '))
b=int(input('Enter 2nd sub marks '))
c=int(input('Enter 3rd sub marks '))
d=int(input('Enter 4th sub marks '))
e=int(input('Enter 5th sub marks '))
per=(a+b+c+d+e)/5

print(per,'%')

if per>=90:
    print('Admi in Ele')
elif per>=80:
    print("Admi in CSC")
elif per>=70:
    print("Admi in Civil")
elif per>=60:
    print('Admi in Mech')
elif per>=50:
    print('Admi in Entc')
else :
    print("Fail")
