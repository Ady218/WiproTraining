Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
9+2
11
x=5
x
5
type(x)
<class 'int'>
t=6.5
t
6.5
type(t)
<class 'float'>
y=4.56567652761232176312732372772362732632762783126831236812
type(y)
<class 'float'>
q='a'
q
'a'
type(q)
<class 'str'>
s1="hello mate"
s1
'hello mate'
type(s1)
<class 'str'>
s2=""""hello mate......
how are you??
i am good"""
s2
'"hello mate......\nhow are you??\ni am good'
type(s2)
<class 'str'>
b1=true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b1=true
NameError: name 'true' is not defined. Did you mean: 'True'?
b1=True
b1
True
type(b1)
<class 'bool'>
b2=False
b2
False
type(b2)
<class 'bool'>
c1=5+7j
c1
(5+7j)
type(c1)
<class 'complex'>
10+5
15
10-5
5
10*50
500
10/5
2.0
10//5
2
9/5
1.8
9//5
1
10%5
0
9%5
4
10**5
100000
5**10
9765625
10.0/2
5.0
10.0//2
5.0
10//2.0
5.0
a=5
a+=2
a
7
15<20
True
5<3
False
a=5
b=5
a==b
True
a=5
b=5.0
a==b
True
a!=b
False
d=5
e=8
d!=e
True
1 and 1
1
1 and 0
0
1 or 1
1
1 or 0
1
a and b
5.0
a>3 and b<10
True
a>3 and b>10
False
not a
False
x=-5
not x
False
y=0
not y
True
s1=''
s1
''
not s1
True
s1 =""
not s1
True
s1=1
not s1
False
r=None
r
not r
True
s1 =' '
not s1
False
5&3
1
5|3
7
5^3
6
a
5
a is int
False
a is type(int)
False
type(a) is int
True
~5
-6
~-5
4
a=5
b=a
a is b
True
a=5
b=float(a)
b
5.0
a=40
b=a
type(a)
<class 'int'>
type(b)
<class 'int'>
c=a+b
c
80
type(c)
<class 'int'>
a=5
b=str(a)
b
'5'
c=float(b)
c
5.0
a=5.56
b=float(a)
b
5.56
a
5.56
b= int(a)
b
5
x='hi'
y=int(x)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    y=int(x)
ValueError: invalid literal for int() with base 10: 'hi'
print('hi')
hi
print(hi)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print(hi)
NameError: name 'hi' is not defined
print(6)
6
print(6//3)
2
print(6/3)
2.0
print('ans' +6)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    print('ans' +6)
TypeError: can only concatenate str (not "int") to str
print('ans' +'6')
ans6
print(6 + 'ans')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    print(6 + 'ans')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> KeyboardInterrupt
>>> print('ans' +'6')
ans6
>>> print('ans' + '6+3')
ans6+3
>>> print('ans' , 6+3)
ans 9
>>> print('my brother's house')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("my brother's house")
...       
my brother's house
>>> input()
...       
hi
'hi'
>>> input()
...       
76587
'76587'
>>> 
================= RESTART: C:/Wipro Training/Python/firstpgm.py ================
Hello World
>>> 
=============== RESTART: C:/Wipro Training/Python/calculations.py ==============
Enter a number12
Enter another number number43
>>> 
>>> 
=============== RESTART: C:/Wipro Training/Python/calculations.py ==============
Enter a number12
Enter another number number32
>>> 
>>> 
=============== RESTART: C:/Wipro Training/Python/calculations.py ==============
Enter a number12
Enter another number number32
44
