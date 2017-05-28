# If-statements

# 1.

x = int(input('Please give me an integer: '))
if x % 2 == 0:
    print('Your number is even!')
else:
    print('Your number is odd!')

# 2. (a)
source = 'Adam made him take a placard'
s1 = 'a'
s2 = 'z'
target = ''
for letter in source:
    if letter == s1:
        target += s2
    else:
        target += letter
print(target)
# 2. (b)
target = ''
for letter in source:
    if letter == s1:
        target += s2
    elif letter == s1.upper():
        target += s2.upper()
    else:
        target += letter
print(target)

# 2 (c)
source = input('Your string: ')
s1 = input('Unwanted Character: ')
s2 = input('Replacement Character: ')
target = ''
for letter in source:
    if letter == s1:
        target += s2
    elif letter == s1.upper():
        target += s2.upper()
    else:
        target += letter
print(target)

# 2 (d)
source = input('Your string: ')
s1 = input('Unwanted Characters: ')
s2 = input('Replacement Character: ')
target = ''

for i in s1:
    for letter in source:
        if letter == i:
            target += s2
        elif letter == i.upper():
            target += s2.upper()
        else:
            target += letter
    source = target
    if s1[-1] != i:
        target = ''
print(target)