Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dict1={1:10, 2:20, 3:30}
>>> dict1
{1: 10, 2: 20, 3: 30}
>>> dict1[2]
20
>>> dict2={'a':10, 'b':20, 'c':30}
>>> dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['c']
30
>>> stud={'rno':101, 'name':'Arpit', 'city':'GGN'}
>>> stud['name']
'Arpit'
>>> stud['name']='Ady'
>>> stud
{'rno': 101, 'name': 'Ady', 'city': 'GGN'}
>>> stud['fname']='xxx'
>>> stud
{'rno': 101, 'name': 'Ady', 'city': 'GGN', 'fname': 'xxx'}
>>> stud.get('name')
'Ady'
>>> stud.keys()
dict_keys(['rno', 'name', 'city', 'fname'])
>>> stud.values()
dict_values([101, 'Ady', 'GGN', 'xxx'])
>>> stud.pop('fname')
'xxx'
>>> stud
{'rno': 101, 'name': 'Ady', 'city': 'GGN'}
