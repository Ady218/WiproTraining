Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper
<built-in method upper of str object at 0x0000024EC0CD37E0>
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hELLO'
s1.casefold
<built-in method casefold of str object at 0x0000024EC0FC1BC0>
s1.casefold()
'hello'
s1='HeLLo'
s1.casefold()
'hello'
s1
'HeLLo'
s1.count('l')
0

s1.count('L')
2
s1.endswith('o')
True
s1.endswith('0')
False
s1.find('L')
2
s1.find('e')
1
s1.find('0')
-1
s1.index('o')
4
s1.index('y')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1.index('y')
ValueError: substring not found
s1.isalpha()
True
s1.isdigit()
False
s1.join('abcde')
'aHeLLobHeLLocHeLLodHeLLoe'
s1.join('12345')
'1HeLLo2HeLLo3HeLLo4HeLLo5'
s1.replace('L','l')
'Hello'
s1
'HeLLo'
s1='Hello there how are you'
s1
'Hello there how are you'
s1..split('')
SyntaxError: invalid syntax
s1.split('')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s1.split('')
ValueError: empty separator

s1.split('')

s1.split('')
SyntaxError: multiple statements found while compiling a single statement

s1.split(' ')
['Hello', 'there', 'how', 'are', 'you']
s1= 'Hello there - how are you'
s1
'Hello there - how are you'
s1.split('-')
['Hello there ', ' how are you']
s1.swapcase()
'hELLO THERE - HOW ARE YOU'
s1='hello there!!!'
len(s1)
14
s1[1]
'e'
s1[5]
' '
s1[13]
'!'
s1[-4]
'e'
s1[-14]
'h'
s1[-15]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s1[-15]
IndexError: string index out of range
s1[0:5]
'hello'
s1[0:6]
'hello '
s1[0:10]
'hello ther'
s1[0:]
'hello there!!!'
s1[:]
'hello there!!!'
s1[2:12:2]
'lotee'
s1[::2]
'hlotee!'
s1[::3]
'hltr!'
s1[-15:-10]
'hell'
s1[-10:-15]
''
s1[-15::2]
'hlotee!'
s1[-15::-2]
''
s1[::-2]
'!!rh le'

================== RESTART: C:/Wipro Training/Python/str1ex.py =================
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
>>> 
================== RESTART: C:/Wipro Training/Python/str1ex.py =================
Traceback (most recent call last):
  File "C:/Wipro Training/Python/str1ex.py", line 4, in <module>
    print(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> 
================== RESTART: C:/Wipro Training/Python/str1ex.py =================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
>>> 
================== RESTART: C:/Wipro Training/Python/str1ex.py =================
h
e
l
l
o
>>> 
================== RESTART: C:/Wipro Training/Python/str1ex.py =================
h
e
l
l
o
