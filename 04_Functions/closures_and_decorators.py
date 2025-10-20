

# Topic: Closure Example 1
def outer(n):
    def inner(m):
        return n * m
    return inner

f = outer(10)
print(f(2))

# Topic: Closure Example 2
def outer(n):
    def inner(m):
        def inside(p):
            return n * m * p
        return inside
    return inner

f = outer(10)
f1 = f(5)
print(f1(2))

# Topic: Decorators Example 1
def first(msg):
    print(msg)

first("hello")
second = first
second("hi")

# Topic: Decorators Example 2
third = second
third("bye")

# Output:
# 20
# 100
# hello
# hi
# bye