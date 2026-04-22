"""
Day-1
Date: 22-4-2026
"""

# count how many times "a" appears in a string

text=input('Enter the string: ')
count=0

for i, ch in enumerate(text):
    if ch=='a':
        count += 1
print('Count of a: ', count)
