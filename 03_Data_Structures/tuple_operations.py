Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Tuple
>>> t=(11,33,22,55,66,55,24,55,22,22)
>>> t
(11, 33, 22, 55, 66, 55, 24, 55, 22, 22)
>>> tyor
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tyor
NameError: name 'tyor' is not defined
>>> t
(11, 33, 22, 55, 66, 55, 24, 55, 22, 22)
>>> type(t)
<class 'tuple'>
>>> t=list(t)
>>> t
[11, 33, 22, 55, 66, 55, 24, 55, 22, 22]
>>> t
[11, 33, 22, 55, 66, 55, 24, 55, 22, 22]
>>> t=tuple(t)
>>> t
(11, 33, 22, 55, 66, 55, 24, 55, 22, 22)
>>> t.count()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> t.count(22)
3
>>> t.count(11)
1
>>> max(t)
66
>>> min(t)
11
>>> sum(t)
365
>>> reversed(t)
<reversed object at 0x000001DC7BA1B3A0>
>>> sorted(t)
[11, 22, 22, 22, 24, 33, 55, 55, 55, 66]
>>> t
(11, 33, 22, 55, 66, 55, 24, 55, 22, 22)
>>> t[5]
55
>>> t[-2]
22
>>> t[4:6]
(66, 55)
>>> t[3:]
(55, 66, 55, 24, 55, 22, 22)
>>> t(:6)
SyntaxError: invalid syntax
>>> t[:6]
(11, 33, 22, 55, 66, 55)
>>> t
(11, 33, 22, 55, 66, 55, 24, 55, 22, 22)
>>> t[2]=21
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t[2]=21
TypeError: 'tuple' object does not support item assignment
>>> l=list(t)
>>> l
[11, 33, 22, 55, 66, 55, 24, 55, 22, 22]
>>> l[1]=212
>>> l
[11, 212, 22, 55, 66, 55, 24, 55, 22, 22]
>>> l[3]='omkar'
>>> l
[11, 212, 22, 'omkar', 66, 55, 24, 55, 22, 22]
>>> l[4]=3.14
>>> 
l
>>> l
[11, 212, 22, 'omkar', 3.14, 55, 24, 55, 22, 22]
>>> t=tuple(l)
>>> t
(11, 212, 22, 'omkar', 3.14, 55, 24, 55, 22, 22)
>>> type(3)
<class 'int'>
>>> type(4)
<class 'int'>
>>> type(t[3])
<class 'str'>
>>> type(t[4])
<class 'float'>
>>> type(t[-1])
<class 'int'>
>>> sorted(t)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l=list(t)
>>> ll
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    ll
NameError: name 'll' is not defined
>>> l
[11, 212, 22, 'omkar', 3.14, 55, 24, 55, 22, 22]
>>> l[3]=24
>>> l
[11, 212, 22, 24, 3.14, 55, 24, 55, 22, 22]
>>> t=tuple(l)
>>> t
(11, 212, 22, 24, 3.14, 55, 24, 55, 22, 22)
>>> sorted(t)
[3.14, 11, 22, 22, 22, 24, 24, 55, 55, 212]
>>> max(t)
212
>>> min(t)
3.14
>>> sorted(t)
[3.14, 11, 22, 22, 22, 24, 24, 55, 55, 212]
>>> t[5]
55
>>> t[-2]
22
>>> t[-1]
22
>>> t
(11, 212, 22, 24, 3.14, 55, 24, 55, 22, 22)
>>> t[22]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t[22]
IndexError: tuple index out of range
>>> t(212)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    t(212)
TypeError: 'tuple' object is not callable
>>> t[212]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t[212]
IndexError: tuple index out of range
>>> t.count()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> t.count(212)
1
>>> t.index(22)
2
>>> t=(11,22,33,3.14,33,22,22,55,101,22)
>>> t
(11, 22, 33, 3.14, 33, 22, 22, 55, 101, 22)
>>> t.count(22)
4
>>> t=(11, 212, 22, 24, 3.14, 55, 24, 55, 22, 22)
>>> t.count(33)
0
>>> 