

# Topic: Basic Function without Arguments
def add():
    x = 10
    y = 3
    z = x + y
    print(z)
add()

# Topic: Positional Arguments
def add(x, y):
    z = x + y
    print(z)
x = 13
y = 19
add(x, y)

# Topic: Keyword Arguments
def person(name, age):
    print("name =", name)
    print("age =", age)
person(age=23, name="omkar")

# Topic: Default Arguments
def person(name, age=12):
    print("name =", name)
    print("age =", age)
person("omkar")

# Topic: Arbitrary Arguments with Sum
def sum1(x, *y):
    print(x, type(x))
    print(y, type(y))
    for i in y:
        x = x + i
    print(x)
sum1(2, 5, 10, 88, 99, 33, 23, 51, 24)

# Topic: Arbitrary Arguments with Return
def sum1(*y):
    x = 0
    for i in y:
        x = x + i
    print("inside function =", x)
    return x
x = sum1(2, 5, 10, 88, 99, 33, 23, 51, 24)
r = x - 35
print("outside function =", r)

# Output:
# 13
# 32
# name = omkar
# age = 23
# name = omkar
# age = 12
# 2 <class 'int'>
# (5, 10, 88, 99, 33, 23, 51, 24) <class 'tuple'>
# 335
# inside function = 335
# outside function = 300