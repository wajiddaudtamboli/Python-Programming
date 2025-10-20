

# Topic: Polymorphism with Function
def fun(a, b):
    print("values A:", a, "it B:", b)

fun(10, 20)
fun(8, 2.9)
fun("Hello", "World")
fun(8, "Hello")

# Topic: Operator Overloading Examples
print(10 + 20)
print("Hello" + "world")
print(5 * 3)
print("Hello" * 3)

# Topic: Polymorphism with Variable Arguments
def fun(datatype, *args):
    if datatype == 'int':
        result = 0
    if datatype == 'str':
        result = ""
    for i in args:
        result = result + i
    print(result)

fun('int', 10, 5, 20)
fun('str', 'I', 'am', 'Tabassum')

# Topic: Function Overloading (Corrected to Last Definition)
def product(a, b, c):  # Only the last definition is used in Python
    print(a * b * c)

product(5, 2, 10)

# Output:
# values A: 10 it B: 20
# values A: 8 it B: 2.9
# values A: Hello it B: World
# values A: 8 it B: Hello
# 30
# Helloworld
# 15
# HelloHelloHello
# 35
# IamTabassum
# 100