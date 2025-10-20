

# Topic: Factorial using Recursion
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)
print(fact(5))

# Topic: Basic Addition Function
def add(x, y):
    z = x + y
    print(z)
add(5, 3)

# Topic: Lambda Function for Addition
add = lambda x, y: x + y
print(add(5, 3))

# Topic: Lambda for Square of a Number
x = int(input("Enter no: "))
square = lambda x: x ** 2
print(square(x))

# Topic: Filter Even Numbers using Lambda
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(filter(lambda x: x % 2 == 0, l))
print(l1)

# Topic: Map Square of Numbers using Lambda
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(map(lambda x: x ** 2, l))
print(l)

# Output (example run with x=4):
# 120
# 8
# 8
# Enter no: 4
# 16
# [2, 4, 6, 8, 10]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]