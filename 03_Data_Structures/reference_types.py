#CLOSURE:
'''
def outer(n):
    def inner(m):
        return n+m
    return inner

f=outer(10)
print(f(2))
'''

#REFERENCE:
'''
def first(msg):
    print(msg)

first("WAJID")
second=first
second("HELLO")
'''
