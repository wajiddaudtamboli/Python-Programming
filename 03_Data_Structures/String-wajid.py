Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #string data s
>>> s=''
>>> s
''
>>> s1=""
>>> s1
''
>>> s2=str()
>>> s2
''
>>> s3=''''''
>>> s3
''
>>> s="wajidahemd"
>>> s
'wajidahemd'
>>> 
>>> s1="wajid123.4@gmail.com"
>>> s
'wajidahemd'
>>> s[0]
'w'
>>> s[4]
'd'
>>> s[8]
'm'
>>> s[12]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s[12]
IndexError: string index out of range
>>> s
'wajidahemd'
>>> s[-1]
'd'
>>> s[-4]
'h'
>>> s-8
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s-8
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> s
'wajidahemd'
>>> s[3:7]
'idah'
>>> s[:5]
'wajid'
>>> s[6:]
'hemd'
>>> s
'wajidahemd'
>>> 
>>> s[0]='s'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[0]='s'
TypeError: 'str' object does not support item assignment
>>> 
>>> # built in fun
>>> 
>>> type(s)
<class 'str'>
>>> len(s)
10
>>> id(s)
2624000335216
>>> max(s)
'w'
>>> 
>>> ord('a')
97
>>> ord('b')
98
>>> ord('z')
122
>>> ord('A')
65
>>> ord('z')
122
>>> ord('Z')
90
>>> ord('1')
49
>>> 
>>> chr(98)
'b'
>>> chr(89)
'Y'
>>> 
>>> isinstance(s,str)
True
>>> isinstance(3.3,str)
False
>>> 
>>> reversed(s)
<reversed object at 0x00000262F29B15C0>
>>> str(reversed(s))
'<reversed object at 0x00000262F293C160>'
>>> list(reversed(s))
['d', 'm', 'e', 'h', 'a', 'd', 'i', 'j', 'a', 'w']
>>> sorted(s)
['a', 'a', 'd', 'd', 'e', 'h', 'i', 'j', 'm', 'w']
>>> 
>>> #methods
>>> 
>>> s.capitalize()
'Wajidahemd'
>>> s.casefold()
'wajidahemd'
>>> s.center(100)
'                                             wajidahemd                                             '
>>> s.count('a')
2
>>> s.find()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.find()
TypeError: find() takes at least 1 argument (0 given)
>>> s.find('h')
6
>>> s.encode()
b'wajidahemd'
>>> s.endswith('d')
True
>>> s1="w\ta\tj\ti\td"
>>> s1
'w\ta\tj\ti\td'
>>> s1.expandtabs(20)
'w                   a                   j                   i                   d'
>>> s1.expandtabs(2)
'w a j i d'
>>> x=5
>>> y=10
>>> 
>>> print("value of x= and value y =",x,y)
value of x= and value y = 5 10
>>> print("value of x={0} and value y ={1}".format(x,y))
value of x=5 and value y =10
>>> z=20
>>> print("value of x={0} and value y ={1} z={1}".format(x,y,z))
value of x=5 and value y =10 z=10
>>> print("value of x={0} and value y ={1} z={2}".format(x,y,z))
value of x=5 and value y =10 z=20
>>> s.index('h')
6
>>> s.isalnum()
True
>>> s1.isalnum()
False
>>> s.isalpha()
True
>>> s.isdecimal()
False
>>> s.isdigit()
False
>>> s.isidentifier()
True
>>> s.islower()
True
>>> s.isnumeric()
False
>>> s.isprintable()
True
>>> s.isspace()
False
>>> s.istitle()
False
>>> s.isupper()
False
>>> s2="1234"
>>> s.join(s2)
'1wajidahemd2wajidahemd3wajidahemd4'
>>> s.ljust(50)
'wajidahemd                                        '
>>> s.lower()
'wajidahemd'
>>> s.partition('d')
('waji', 'd', 'ahemd')
>>> s.rjust(50)
'                                        wajidahemd'
>>> s.replace('w','s')
'sajidahemd'
>>> s.rfind('h')
6
>>> s.rindex('h')
6
>>> s.split('d')
['waji', 'ahem', '']
>>> s.startswith('w')
True
>>> s.swapcase()
'WAJIDAHEMD'
>>> s.title()
'Wajidahemd'
>>> s.upper()
'WAJIDAHEMD'
>>> s.zfill(10)
'wajidahemd'
>>> s.zfill(15)
'00000wajidahemd'
>>> 


>>> 

>>> 

>>> 
