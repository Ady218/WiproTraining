Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
id9s1)
SyntaxError: unmatched ')'
id(s1)
1900087752384
s2='hi'
id(s2)
140727917163960
s3=s1
id(s3)
1900087752384
s3
'hello'
s1
'hello'
s1='hi'
id(s1)
140727917163960
s1='india'
id(s1)
1900090825280


list1=[10,20,30,40]
list1
[10, 20, 30, 40]
type(list1)
<class 'list'>
list1[0]
10
list[3]
list[3]
list1[3]
40
list1[4]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list1[4]
IndexError: list index out of range
list[-1]
list[-1]
list1[-1]
40
list[0:3]
list[slice(0, 3, None)]
list1[0:3]
[10, 20, 30]
list[1:3:2]
list[slice(1, 3, 2)]
list1[1:3:2]
[20]
list1[0:3:2]
[10, 30]
list2 = list('hi', 'hello')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list2 = list('hi', 'hello')
TypeError: list expected at most 1 argument, got 2
s1
'india'
list2=list(s1)
list2
['i', 'n', 'd', 'i', 'a']
list3=list1
id(s1)
1900090825280
id(s3)
1900087752384
id(list1)
1900090738624
id(list2)
1900090700352
id(list3)
1900090738624
list4= [100, 'hi', 100, True, 69.36]
list4
[100, 'hi', 100, True, 69.36]
list4[5]='hey'
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list4[5]='hey'
IndexError: list assignment index out of range
list1.append('hey')
list1
[10, 20, 30, 40, 'hey']
list4.append(2000)
list4
[100, 'hi', 100, True, 69.36, 2000]
list1.remove('hey')
list1
[10, 20, 30, 40]
list4
[100, 'hi', 100, True, 69.36, 2000]
list4.remove(5)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list4.remove(5)
ValueError: list.remove(x): x not in list
list4.count(23)
0
list4.count(100)
2
list1.insert(2,200)
list1
[10, 20, 200, 30, 40]
id(list1)
1900090738624
list1.pop()
40
list1
[10, 20, 200, 30]
list1(2)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list1(2)
TypeError: 'list' object is not callable
list1.pop(2)
200
list1
[10, 20, 30]
list2
['i', 'n', 'd', 'i', 'a']
list2.clear()
list2
[]
del(list2)
list2
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list2=list1
list1
[10, 20, 30]
list2
[10, 20, 30]
id(list1)
1900090738624
id(list2)
1900090738624
list1[1]=200
list1
[10, 200, 30]
list2
[10, 200, 30]
id(list1)
1900090738624
id(list2)
1900090738624
list2 = list(list1)
list1
[10, 200, 30]
list2
[10, 200, 30]
id(list1)
1900090738624
id(list2)
1900090699520
list1[1]=20
list1
[10, 20, 30]
list2
[10, 200, 30]
tuple1 =(11,22,33,44,55)
tuple1
(11, 22, 33, 44, 55)
tuple1[3]
44
tuple1[3]=333
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    tuple1[3]=333
TypeError: 'tuple' object does not support item assignment
tuple1[0:4:2]
(11, 33)
tuple1[0:-1:2]
(11, 33)
tuple1.index(44)
3
tuple1.count(22)
1
tuple2=tuple1
tuple2
(11, 22, 33, 44, 55)
tuple1
(11, 22, 33, 44, 55)
id(tuple1)
1900088724928
id(tuple2)
1900088724928
list1
[10, 20, 30]
tuple3=tuple(list1)
tuple3
(10, 20, 30)
list1
[10, 20, 30]
list1.append(tuple1)
list1
[10, 20, 30, (11, 22, 33, 44, 55)]
list[0]
list[0]
list1[0]
10
list1[3]
(11, 22, 33, 44, 55)
list5=list(tuple1)
list5
[11, 22, 33, 44, 55]
>>> list5[1]
22
>>> list1
[10, 20, 30, (11, 22, 33, 44, 55)]
>>> list1[3:1]
[]
>>> list1[3][2]
33
>>> list1
[10, 20, 30, (11, 22, 33, 44, 55)]
>>> set1={10,20,30,40,50}
>>> set1
{50, 20, 40, 10, 30}
>>> set1[2]
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
>>> set1.add(25)
>>> set1
{50, 20, 40, 25, 10, 30}
>>> set1.add('25')
>>> set1
{50, '25', 20, 40, 25, 10, 30}
>>> set1.add(25)
>>> set1
{50, '25', 20, 40, 25, 10, 30}
>>> set2=set(set1)
>>> set2
{50, '25', 20, 40, 25, 10, 30}
>>> id(set1)
1900090483072
>>> id(set2)
1900090484192
>>> set2.remove('25')
>>> set2
{50, 20, 40, 25, 10, 30}
>>> set1.union(set2)
{40, 10, 50, '25', 20, 25, 30}
>>> set1.intersection(set2)
{40, 10, 50, 20, 25, 30}
set1.add(list1)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    set1.add(list1)
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
set1.add(tuple1)
set1
{50, '25', 20, 40, 25, 10, (11, 22, 33, 44, 55), 30}
