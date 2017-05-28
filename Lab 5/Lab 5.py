# 1.
age = int(input('What is your age?: '))
if 0 <= age <= 20:
    print('You are young!')
elif 20 < age <= 50:
    print("You still have a while to live, hopefully.")
elif 50 < age <= 120:
    print('Are your bones not aching yet?')
else:
    print('You are out of range')

# 2.

x = 10
if 15 > x > 5:
    print('inside')
else:
    print('outside')

# 3.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# Could also be done by combining fizz and buzz
# text = ''
# for i in range(1, 101):
#       if i % 3 == 0:
#       text += 'Fizz'
#   if i % 5 == 0:
#       text += 'Buzz'
#   elif i % 3 != 0 and i %5!= 0:
#       text += str(i)
#   print(text)
#   text = ''
# 4.

ListsOfLists = [['a', 'b', 'c', 'd'], ['d', 'e', 'f', 'c'], ['g', 'h', 'i', 'f'], ['g', 'h', 'i', 'f']]
line = '   '
for item in ListsOfLists:
    print('   +' + '-+' * len(item))
    for i in item:
        line += ('|' + i)
    print(line + '|')
    line = '   '
print('   +' + '-+' * len(item))

# 5. Bonus
print('\n')

list_of_lists = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def listprint(l):
    line = '   '
    for item in l[::-1]:
        print('   +' + '-+' * len(item))
        for i in item:
            line += ('|' + i)
        print(line + '|')
        line = '   '
    print('   +' + '-+' * len(item))

listprint(list_of_lists)

pos_initial = input('Please enter the first coordinate: ').split(',')
pos_final = input('Please enter the second coordinate:  ').split(',')


x_i = int(pos_initial[0])
y_i = int(pos_initial[1])
x_f = int(pos_final[0])
y_f = int(pos_final[1])

if x_i > x_f:
    a = x_f
    x_f = x_i
    x_i = a
if y_i > y_f:
    a = y_f
    y_f = y_i
    y_i = a


def change_box(x, y):
    list_of_lists[x][y] = 'X'

if x_i == x_f:
    for i in range(y_i, y_f+1):
        change_box(i, x_i)

if y_i == y_f:
    for i in range(x_i, x_f+1):
        change_box(y_i, i)



listprint(list_of_lists)