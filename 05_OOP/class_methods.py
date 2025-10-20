

# Topic: Class with Static Methods
class abc:
    def fun1():
        print("fun1 class abc")
    def fun2():
        print("fun2 class abc")
    def fun3():
        print("fun3 class abc")

a = abc
a.fun1()
a.fun2()

# Topic: Class with Parameterized Static Methods
class abc:
    def add(x, y):
        result = x + y
        print("add fun class abc", result)
    def sub(x, y):
        result = x - y
        print("sub fun class abc", result)
    def multi(x, y):
        result = x * y
        print("multi fun class abc", result)

a = abc
a.add(5, 6)
a.sub(10, 5)
a.multi(2, 4)

# Topic: Class with Instance Methods
class abc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("hello")
    def xfun(self):
        print("x fun class abc", self.x)
    def yfun(self):
        print("y fun class abc", self.y)
    def zfun(self):
        z = self.x * self.y
        print("multi zfun class abc", z)

a = abc(5, 2)
a.xfun()
a.yfun()
a.zfun()

# Output:
# fun1 class abc
# fun2 class abc
# add fun class abc 11
# sub fun class abc 5
# multi fun class abc 8
# hello
# x fun class abc 5
# y fun class abc 2
# multi zfun class abc 10