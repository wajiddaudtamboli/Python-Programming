#ITERATOR AND GENERATOR:
#->Traverse through all elements
#__iter__()
#__next__()


'''
l=[1,2,3,4,5,6]
it=l.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
'''
#iter(l)
#next(it)

'''
l=[1,2,3]
it=iter(l)
print(next(it))
print(next(it))
print(next(it))
'''

'''
l=[1,2,3,4,3]
it=iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''

#Generator:
#Creating the iterator and using yield as return type
'''
def fun():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
f=fun()
for i in f:
    print(i)
'''

'''
def cube():
    n=1
    while n<=15:
        cube=n*n*n
        yield cube
        n+=2
c=cube()
for i in c:
    print(i)
'''

'''
def vowels():
    yield 'a'
    yield 'e'
    yield 'i'
    yield 'o'
    yield 'u'
v=vowels()    
for i in v:
    print(i)
'''    
    
