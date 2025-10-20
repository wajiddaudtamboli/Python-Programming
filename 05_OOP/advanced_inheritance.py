# WAJID DAUD TAMBOLI

# Topic: Single Inheritance
class P:
    def fun():
        print("this is fun class p")

class C(P):
    def fun1():
        print("this is fun1 class c")

o = C
o.fun()
o.fun1()

# Topic: Single Inheritance with Constructor
class Parent:
    def __init__(self, x):
        self.x = x
    def fun(self):
        print("this is fun class p", self.x)

class Child(Parent):
    def __init__(self, y, x):
        self.y = y
        Parent.__init__(self, x)
    def fun1(self):
        z = self.y + self.x
        print("this is fun1 class c", z)

c = Child(5, 6)
c.fun1()
c.fun()

# Topic: Multilevel Inheritance
class Gchild(Child):
    def __init__(self, y, x, z):
        self.z = z
        Child.__init__(self, y, x)
    def fun2(self):
        z = self.y + self.x + self.z
        print("this is fun2 class c", z)

c = Gchild(5, 6, 10)
c.fun1()
c.fun()
c.fun2()

# Topic: Multiple Inheritance
class Father:
    def __init__(self, x):
        self.x = x
    def fun(self):
        print("this is fun class p", self.x)

class Mother:
    def __init__(self, y):
        self.y = y
    def fun1(self):
        z = self.y + self.x
        print("this is fun1 class c", z)

class Child(Father, Mother):
    def __init__(self, y, x, z):
        self.z = z
        Mother.__init__(self, y)
        Father.__init__(self, x)
    def fun2(self):
        z = self.y + self.x + self.z
        print("this is fun2 class c", z)

c = Child(5, 6, 10)
c.fun1()
c.fun()
c.fun2()

# Topic: Hybrid Inheritance
class Gchild(Child):
    def __init__(self, y, x, z):
        Child.__init__(self, y, x, z)
    def fun3(self):
        result = (self.y + self.x + self.z) / 3
        print("percentage is =", result)

c = Gchild(50, 60, 100)
c.fun1()
c.fun()
c.fun2()
c.fun3()

# Output:
# this is fun class p
# this is fun1 class c
# this is fun1 class c 11
# this is fun class p 6
# this is fun1 class c 11
# this is fun class p 6
# this is fun2 class c 21
# this is fun1 class c 11
# this is fun class p 6
# this is fun2 class c 21
# this is fun1 class c 110
# this is fun class p 60
# this is fun2 class c 210
# percentage is = 70.0