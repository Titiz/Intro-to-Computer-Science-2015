##
# Question 1
##
x = 0
summation = 0
while x < 6:
    summation += x
    x += 1
print(summation)
##
# Question 2
##
import random

months = 12
account_max = 100
his_account = []
her_account = []
for i in range(months):
    his_account.append(random.randrange(account_max))
    her_account.append(random.randrange(account_max))

print('His: ', his_account)
print('Hers:', her_account)

# (Your code here)
current_month = 0
success_months = [0, 0]
message = ["He had more prosperous months", 'She had more prosperous months']
while current_month < 12:
    success_months[int(his_account[current_month] > her_account[current_month])] += 1
    current_month += 1
print('His prosperous months:', success_months[1])
print('Her prosperous months:', success_months[0])

if success_months[0] == success_months[1]:
    print('They both had the same amount of prosperous months')
else:
    print(message[int(success_months[0] > success_months[1])])



##
# Question 3
##
initial = 'When the saints go marching in'

rev1 = ''
# (Your for loop here)
for i in range(1, len(initial)+1):
    rev1 += initial[-i]
print(rev1)
rev2 = ''
# (Your while loop here)
i = 1
while i != len(initial)+1:
    rev2 += initial[-i]
    i += 1
print(rev2)

initial = initial[::-1]
print('Your string reverse:', rev1 == initial and rev2 == initial)

##
# Question 4
##
a = ''
friends = []
while a != 'stop':
    a = input("Enter your friend's name, or 'stop' to finish: ")
    if a != 'stop':
        friends.append(a)
if len(friends) == 1:
    print('You have 1 friend. He is:')
else:
    print("You have", len(friends), 'friends. They are:')
for item in friends:

    if len(friends) > 1:
        if item == friends[-2]:
            print(item + ', and')
        elif item == friends[-1]:
            print(item)
        else:
            print(item + ',')
    else:
        print(friends[0])
##
# Bonus: Horse Race
##

n_horses = 10
matrix = []
generated_row = []
# I start with 1 for all horses to ensure that all of them begin at the starting line.
for i in range(n_horses):
    generated_row.append(1)
check_string = ''

for item in generated_row:
    check_string += str(item)
matrix.append(generated_row[:])
while check_string != '0'*n_horses:
    check_string = ''
    for i in range(n_horses):
        if generated_row[i] != 0:
            generated_row[i] = random.randint(0, 10)
    for item in generated_row:
        check_string += str(item)
    matrix.append(generated_row[:])

import time
print('\n3...')
time.sleep(0.5)
print('2...')
time.sleep(0.5)
print('1...')
time.sleep(0.5)
print('GO!!!\n\n')


star_row = []
for item in matrix:
    star_row = []
    for i in item:
        if i == 0:
            i = '  '
        else:
            i = '* '
        star_row.append(i)
    time.sleep(0.3)
    print(''.join(star_row))

for i in range(n_horses):
    if matrix[-2][i] != 0:
        print("Horse number", i+1, 'won the race!')



