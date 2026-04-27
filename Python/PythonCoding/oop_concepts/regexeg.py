import re

'''
#begininng and end matching
txt = input('Enter a text: ') #India is my country
bpat = input('Enter beginning pattern: ') #India
epat = input('Enter ending pattern: ') #country
bpat = '^' + bpat # for the begining matching
epat = epat + '$' # for the end matching
if re.search(pattern=bpat, string=txt): #re. search finds for the pattern in the string 
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')

if re.search(pattern=epat, string=txt):
    print('Ending pattern available')
else:
    print('Ending pattern not available')
'''

'''
# full search
mbno = input('Enter the num: ')

# pat = '[0-9]'
pat = r"[0-9]+"

if re.fullmatch(pattern=pat, string=mbno): #instead of search
    print('only digits')
else:
    print('other characters available')
'''
# re.match

'''
un= input('Enter UN: ')

#pat = r"^[a-z_]{8}$" #for 8 characters including lowercase a-z and underscore
pat = r"^[a-z_]{8,}$"
if re.match(pattern=pat, string =un):
    print('Valid')
else:
    print('Not valid')
'''

'''
#email(consisting of everything means characters)

emailadd = input('Email: ')
pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat, string =emailadd):
    print('Valid')
else:
    print('Not valid')
'''

#pwd
'''
pwdtxt = input('PWD: ')
# forward lookup it will search the whole string for it not only the first character --. (?=) and .* will 
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[-_@]).{8,}$" 

if re.match(pattern=pat, string =pwdtxt):
    print('Valid')
else:
    print('Not valid')
  '''

# substitute all the extra white spaces (re.sub)

txt = input('text: ')

pat = r"\s+"
# print(re.sub(pattern=pat, string=txt, repl='__')) #here we have to give a replacement value
print(re.split(pattern=pat, string=txt,))

