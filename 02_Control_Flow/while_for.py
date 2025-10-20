# While and For Loop Examples with Calculator

# Example 1: Print numbers 1 to 5
n = 1
while n <= 5:
    print(n)
    n = n + 1

print("-" * 30)

# Example 2: Print odd numbers
n = 1
print("Odd numbers:")
while n <= 10:
    if n % 2 != 0:
        print(n)
    n = n + 1

print("-" * 30)

# Example 3: Print even numbers
n = 1
print("Even numbers:")
while n <= 10:
    if n % 2 == 0:
        print(n)
    n = n + 1

print("-" * 30)

# Example 4: Print even and odd classification
n = 1
while n <= 10:
    if n % 2 == 0:
        print('even no', n)
    else:
        print('odd no', n)
    n = n + 1

print("-" * 30)

# Calculator using while loop
print('\n1. Add \n2. Sub \n3. Mul \n4. Div')

a = int(input('Enter your choice: '))
b = int(input('Enter first number: '))
c = int(input('Enter second number: '))

if a == 1:
    print("Addition:", b + c)
elif a == 2:
    print("Subtraction:", b - c)
elif a == 3:
    print("Multiplication:", b * c)
elif a == 4:
    if c != 0:
        print("Division:", b / c)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice")




    





