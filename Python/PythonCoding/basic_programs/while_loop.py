"""

"""

# natural numbers printing

'''
num=int(input('enter a number: '))

value =1

while value<=num :
    print(value)
    value += 1
'''

num=input('enter a number: ')
print(len(num))
count=len(num)
sum = 0
n=int(num)
org = n
while n>0:
    rem =n%10
    sum =sum + rem**count
    n = n//10

if org==sum:
    print('Its an armstrong number')
else:
    print('Not an armstrong number: ')
