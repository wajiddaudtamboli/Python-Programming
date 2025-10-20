Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l
[]
>>> l=[223,232]
>>> l
[223, 232]
>>> l=[23,32,66,32,32,12,'rahul','shivaraj','mahesh','omkar',23]
>>> l
[23, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23]
>>> l[6]
'rahul'
>>> x=5
>>> x
5
>>> l[l]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l[l]
TypeError: list indices must be integers or slices, not list
>>> l=[l]
>>> l
[[23, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23]]
>>> l=[23,32,66,32,32,12,'rahul','shivaraj','mahesh','omkar',23]
>>> l
[23, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23]
>>> l[2]
66
>>> l[0]
23
>>> l.extend([23,32,25])
>>> l
[23, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23, 23, 32, 25]
>>> l=[23,32,66,32,32,12,'rahul','shivaraj','mahesh','omkar',23]
>>> 
>>> l.extend([3.14,5.55,63.32])
>>> l
[23, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[-1]
63.32
>>> l[-5]
'omkar'
>>> l
[23, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[5:8]
[12, 'rahul', 'shivaraj']
>>> l[8:]
['mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[:5]
[23, 32, 66, 32, 32]
>>> l[:]
[23, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[0]=233
>>> l
[233, 32, 66, 32, 32, 12, 'rahul', 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[6]=52
>>> l
[233, 32, 66, 32, 32, 12, 52, 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[6]=[22,33,44,65]
>>> l
[233, 32, 66, 32, 32, 12, [22, 33, 44, 65], 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[6]
[22, 33, 44, 65]
>>> l[6][2]=55
>>> l
[233, 32, 66, 32, 32, 12, [22, 33, 55, 65], 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[6][-1]
65
>>> #list buit in function
>>> type(l[2])
<class 'int'>
>>> type(l[6])
<class 'list'>
>>> type(l[8])
<class 'str'>
>>> type(l[12])
<class 'float'>
>>> type(l[-1])
<class 'float'>
>>> id()l
SyntaxError: invalid syntax
>>> id(l)
2531247573760
>>> max(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'list' and 'int'
>>> l[6]=25
>>> l
[233, 32, 66, 32, 32, 12, 25, 'shivaraj', 'mahesh', 'omkar', 23, 3.14, 5.55, 63.32]
>>> l[7]=66
>>> l[8]=25
>>> l[9]=3.14
>>> l
[233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32]
>>> max(l)
233
>>> min(l)
3.14
>>> sum(l)
621.15
>>> reversed(l)
<list_reverseiterator object at 0x0000024D5A1EADF0>
>>> l
[233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32]
>>> sorted(l)
[3.14, 3.14, 5.55, 12, 23, 25, 25, 32, 32, 32, 63.32, 66, 66, 233]
>>> l
[233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32]
>>> #list method
>>> l
[233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32]
>>> l.append(95)
>>> l
[233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> l1=l.copy()
>>> l1
[233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> l1.clear()
>>> l1
[]
>>> l
[233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> m
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    m
NameError: name 'm' is not defined
>>> l1
[]
>>> l.reverse()
>>> l
[95, 63.32, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233]
>>> l.reverse
<built-in method reverse of list object at 0x0000024D5A1CCB00>
>>> l[]
SyntaxError: invalid syntax
>>> l[22]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    l[22]
IndexError: list index out of range
>>> l.extend(92,23,52,26)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    l.extend(92,23,52,26)
TypeError: list.extend() takes exactly one argument (4 given)
>>> l.extend([23,523,33,25])
>>> l
[95, 63.32, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233, 23, 523, 33, 25]
>>> l.count(3.14)
2
>>> l.count(23)
2
>>> l[2]
5.55
>>> l.index(88)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    l.index(88)
ValueError: 88 is not in list
>>> l.index(23)
4
>>> l.insert(2,2223)
>>> l
[95, 63.32, 2223, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233, 23, 523, 33, 25]
>>> sum(l)
3543.15
>>> min()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    min()
TypeError: min expected at least 1 argument, got 0
>>> min(l)
3.14
>>> max(l)
2223
>>> l.pop()
25
>>> l.pop()
33
>>> l
[95, 63.32, 2223, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233, 23, 523]
>>> l.remove(2223)
>>> l
[95, 63.32, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233, 23, 523]
>>> l.reverse()
>>> l
[523, 23, 233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> l
[523, 23, 233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> l.reverse(l)
Traceback (most recent call last):;
  File "<pyshell#99>", line 1, in <module>
    l.reverse(l)
TypeError: list.reverse() takes no arguments (1 given)
>>> l
[523, 23, 233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> l.sort()
>>> l
[3.14, 3.14, 5.55, 12, 23, 23, 25, 25, 32, 32, 32, 63.32, 66, 66, 95, 233, 523]
>>> l=[523, 23, 233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> l
[523, 23, 233, 32, 66, 32, 32, 12, 25, 66, 25, 3.14, 23, 3.14, 5.55, 63.32, 95]
>>> sorted(l)
[3.14, 3.14, 5.55, 12, 23, 23, 25, 25, 32, 32, 32, 63.32, 66, 66, 95, 233, 523]
>>> l.reverse()
>>> l
[95, 63.32, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233, 23, 523]
>>> l
[95, 63.32, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233, 23, 523]
>>> sorted(L)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    sorted(L)
NameError: name 'L' is not defined
>>> sorted(L)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    sorted(L)
NameError: name 'L' is not defined
>>> sorted(l)
[3.14, 3.14, 5.55, 12, 23, 23, 25, 25, 32, 32, 32, 63.32, 66, 66, 95, 233, 523]
>>> l
[95, 63.32, 5.55, 3.14, 23, 3.14, 25, 66, 25, 12, 32, 32, 66, 32, 233, 23, 523]
>>> l.sort()
>>> l
[3.14, 3.14, 5.55, 12, 23, 23, 25, 25, 32, 32, 32, 63.32, 66, 66, 95, 233, 523]
>>> l
[3.14, 3.14, 5.55, 12, 23, 23, 25, 25, 32, 32, 32, 63.32, 66, 66, 95, 233, 523]
>>> 
======================================== RESTART: C:/Users/sai/Desktop/123.py ========================================
Hello world
Hello world
Hello world
Hello world
Hello world
>>> 
======================================== RESTART: C:/Users/sai/Desktop/123.py ========================================
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world

======================================== RESTART: C:/Users/sai/Desktop/123.py ========================================
Hello world
Hello world
Hello world
Hello world
Hello world
>>> 