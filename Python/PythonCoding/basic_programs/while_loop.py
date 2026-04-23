"""
Date: 22-4-2026
Desc: learning while loops.
"""

# natural numbers printing

'''
num=int(input('enter a number: '))

value =1

while value<=num :
    print(value)
    value += 1
'''
# armstrong number
num=input('enter a number: ')
print(len(num))
count=len(num)
sum = 0
num=int(num)
org = num
while num>0:
    rem =num%10
    sum =sum + rem**count
    num = num//10

if org==sum:
    print('Its an armstrong number')
else:
    print('Not an armstrong number: ')
