"""
Date: 22-4-2026
Desc: learning various if statements formats.
"""

#biggest of 2 numbers

'''
num1=int(input('Enter a number: '))
num2=int(input('Enter another  number: '))

if num1==num2:
    print('Both are equal.')
elif num1 > num2 :
    print(num1, ' is big.')
else:
    print(num2, ' is big.')
'''

# biggest of 3 numbers

'''
num1=int(input('Enter a number: '))
num2=int(input('Enter second  number: '))
num3=int(input('Enter third  number: '))

if num1 == num2 and num2 == num3:
    print('All values are same.')
elif num1==num2 or num2==num3 or num3==num1:
    print('2 numbers are same')
if num1>num2 and num1>num3:
    print(num1, ' is the biggest.')
elif num2>num1 and num2>num3:
    print(num2, ' is the biggest.')
elif num3>num2 and num3>num1:
    print(num3, ' is the biggest.')
'''

# weekday(match case)

ch =int(input('Enter a choice 1-7: '))

match (ch):
    case 1:
        print('Mon')
    case 2:
        print('Tue')
    case 3:
        print('wed')
    case 4:
        print('Thurs')
    case 5:
        print('Fri')
    case 6:
        print('Sat')
    case 7:
        print('Sun')
    case _:
        print('Invalid choice')