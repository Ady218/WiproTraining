"""

"""
'''
numbers=[11,22,98,63,45,20,45]

for i in numbers:
    print(i%10, end='\t')
'''

'''
numbers=(11,22,98,63,45,20,45)

for i in numbers:
    print(i%10, end='\t')
'''

#set
'''numbers={11,22,98,63,45,20,45}

for i in numbers:
    print(i%10, end='\t')
'''

#dictionary
'''
stud={'rno':101, 'name':'Arpit', 'city':'GGN'}

for i in stud:
    print(i)
'''
'''iterate in a dictionary use stud.items()'''
stud={'rno':101, 'name':'Arpit', 'city':'GGN'}

for k,v in stud.items():
    print(k, '--', v)