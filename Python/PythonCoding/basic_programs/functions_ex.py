"""

"""

'''
#functions (add)

def add(n1, n2):
    sum = n1 + n2 #or we can type return n1+n2 no need to store in sum
    return sum
#functions (sub)

def sub(n1, n2):
    return  n1 - n2

#functions (multiply)

def prod(n1, n2):
    return n1 * n2

#functions (div)

def div(n1, n2):
    pass

#driver

num1=int(input('Enter a number: '))
num2=int(input('Enter another number number: '))

res = sub(num1,num2) #positional arguments
print('result: ',res)
res2 = sub(n2=num1, n1=num2) #keyword arguments
print('result: ',res2)
'''

# arbitrary arguments

#function

'''
def add(nums):
    sum = 0
    for n in nums:
        sum = sum+n
    return sum

#driver
numbers = list()
count = int(input('How many numbers: '))

for _ in range(0, count):
    numbers.append(int(input('No. ')))
print(add(numbers))
'''

'''
def add(*nums):
    sum = 0
    for n in nums:
        sum = sum+n
    return sum
print(add(5,6,9))
'''

'''
#optional parameter

def add(n1, n2, n3=10): # here 10 is the optional value
    return  n1 + n2 + n3

#driver
num1=int(input('Enter a number: '))
num2=int(input('Enter another number number: '))

print(add(num1,num2))
print(add(num1,num2,100)) #optional paramater
'''

'''
#lambda (ex-add)

num1=int(input('Enter a number: '))
num2=int(input('Enter another number number: '))

add =lambda n1, n2 : n1+ n2

print(add(num1, num2))
'''

'''
# lambda square numbers

numbers = [1, 2, 3, 4, 5]

sq = lambda nums : [num * num for num in nums]
print(tuple(sq(numbers))) # to get the answer in tuple if needed we can do this
'''

# lambda square numbers with condition(if)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

sq = lambda nums : [num * num for num in nums if num%2==0 ] #if condition like we want print only those numbers which is divisble by 2
print(tuple(sq(numbers)))

