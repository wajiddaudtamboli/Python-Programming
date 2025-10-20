Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={}
>>> type(s)
<class 'dict'>
>>> s=set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> s={11,22,33,44,55,"omkar","rahul",21,22,23,22}
>>> s
{33, 'omkar', 11, 44, 23, 21, 'rahul', 22, 55}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s[0]=34
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[0]=34
TypeError: 'set' object does not support item assignment
>>> # function
>>> type(s)
<class 'set'>
>>> len(s)
9
>>> id(d)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    id(d)
NameError: name 'd' is not defined
>>> id(s)
2199150419072
>>> max(s)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    max(s)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> s
{33, 'omkar', 11, 44, 23, 21, 'rahul', 22, 55}
>>> min(s)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    min(s)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> sum(s)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sum(s)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> list(reversed(s))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list(reversed(s))
TypeError: 'set' object is not reversible
>>> sorted(s)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sorted(s)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
>>> #methods
\
>>> 
>>> s.add(101)
>>> s
{33, 'omkar', 101, 11, 44, 23, 21, 'rahul', 22, 55}
>>> s1=s.copy()
>>> s
{33, 'omkar', 101, 11, 44, 23, 21, 'rahul', 22, 55}
>>> s1
{33, 'omkar', 101, 11, 44, 23, 21, 'rahul', 22, 55}
>>> s.update([99,88,77,66,55])
>>> s
{33, 'omkar', 99, 66, 101, 11, 44, 77, 23, 21, 'rahul', 22, 55, 88}
>>> s.difference(s1)
{88, 66, 99, 77}
>>> s.difference_update(s1)
>>> s
{66, 99, 77, 88}
>>> s={33, 'omkar', 99, 66, 101, 11, 44, 77, 23, 21, 'rahul', 22, 55, 88}
>>> s.discard('omkar')
>>> s
{33, 66, 99, 101, 11, 44, 77, 23, 21, 'rahul', 22, 55, 88}
>>> s.intersection(s1)
{33, 101, 11, 44, 21, 'rahul', 23, 22, 55}
>>> s.isdisjoint(s1)
False
>>> s.issubset(s1)
False
>>> s.issuperset(s1)
False
>>> s.pop()
33
>>> s.remove("rahul")
>>> s
{66, 99, 101, 11, 44, 77, 23, 21, 22, 55, 88}
>>> s.symmetric_difference(s1)
{33, 'omkar', 66, 99, 77, 'rahul', 88}
>>> s.union(s1)
{66, 'omkar', 11, 77, 21, 22, 23, 88, 'rahul', 33, 99, 101, 44, 55}
>>> s={66, 99, 101, 11, 44, 77, 23, 21, 22, 55, 88}
>>> s
{66, 99, 101, 11, 44, 77, 21, 22, 23, 55, 88}
>>> max(s)
101
>>> min(s)
11
>>> sum(s)
607
>>> list(reversed(s))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list(reversed(s))
TypeError: 'set' object is not reversible
>>> sorted(s)
[11, 21, 22, 23, 44, 55, 66, 77, 88, 99, 101]
>>> 
