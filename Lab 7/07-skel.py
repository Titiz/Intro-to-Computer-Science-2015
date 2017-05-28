##
# Lab 7 Skeleton code.
##

######################################################################
# BEGIN: do not alter this section
######################################################################
import random

def genkey():
    key = ''
    a = ord('a') # the ASCII character for lowercase a
    n = a + 13   # the ASCII character for lowercase n

    for i in range(3):
        rand = random.randrange(a, n)
        key += chr(rand)
        
    return key

dragon_color = [
    'black',
    'white',
    'red',
    'blue',
    ]
dragon_breed = [
    'Antipodean Opaleye',
    'Chinese Fireball',
    'Common Welsh Green',
    'Hebridean Black',
    'Hungarian Horntail',
    'Norwegian Ridgeback',
    'Peruvian Vipertooth',
    'Romanian Longhorn',
    'Swedish Short-Snout',
    'Ukrainian Ironbelly',
    ]
######################################################################
# END: do not alter this section
######################################################################

##
# Question 1
##

phone_book = {
    'peter': 876554,
    'sam': 324235,
    'titas': 369369
}

while True:
    name = input('Please enter a name: ').lower()
    if name == '':
        break
    elif name in phone_book:
        print(phone_book[name])
    else:
        print('Name not found')
##
# Question 2
##
letters = {}
string = input('Please enter a string: ')
for letter in string:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1
# Using help from http://stackoverflow.com/questions/16600174/return-output-of-dictionary-to-alphabetical-order
for key, value in sorted(letters.items()):
    print(str(key) + ' -> ' + str(value))
##
# Question 3.1
##
usrdict = {}

for i in range(100):
    key = genkey()
    while key in usrdict:
        key = genkey()
    usrdict[key] = random.randint(0, 10)

print(usrdict)
print('Do you have 100 elements?', len(usrdict) == 100)

##
# Question 3.2
##

usrdict_inverted = {}

for item in usrdict:
    if usrdict[item] not in usrdict_inverted:
        usrdict_inverted[usrdict[item]] = [item]
    else:
        usrdict_inverted[usrdict[item]].append(item)

print(usrdict_inverted)

##
# Extra credit
##
print('\nDragons:')

# 1.
dragon_list = []

for i in range(300):
    dragon = {
        'color': dragon_color[random.randint(0, len(dragon_color)-1)],
        'age': random.randint(0, 100),
        'size': random.randint(0, 20),
        'breed': dragon_breed[random.randint(0, len(dragon_breed)-1)]
    }
    dragon_list.append(dragon)

print(dragon_list)

# 2.

while True:
    value_count = 0
    value = input('What do you want to know: ')
    value = value.split(' ')
    if value[0] in dragon_list[0]:
        if value[0] == 'breed':
            for item in dragon_list:
                if str(item[value[0]]) == str(value[1]) + ' ' + str(value[2]):
                    value_count += 1
            print(value_count, value[0], value[1], value[2], 'dragons')
        else:
            for item in dragon_list:
                if str(item[value[0]]) == str(value[1]):
                    value_count += 1
            print(value_count, value[0],  value[1], 'dragons')
    elif value[0] == 'stop':
        break
    else:
        print('Not found')


# 3.

for item in dragon_breed:
    size_list = []
    for dragon in dragon_list:
        if dragon['breed'] == item:
            size_list.append(dragon['size'])
    max_size = max(size_list)
    elder_dragons = []
    for dragon in dragon_list:
        if dragon['size'] == max_size and dragon['breed'] == item:
            elder_dragons.append(dragon)
    print(item, 'biggest dragons:\n', elder_dragons)

# 4.
tot_age = 0
tot_size = 0
breeds = {}
for dragon in dragon_list:
    tot_age += dragon['age']
    tot_size += dragon['size']
    if dragon['breed'] in breeds:
        breeds[dragon['breed']] += 1
    else:
        breeds[dragon['breed']] = 1
avg_age = tot_age / len(dragon_list)
avg_size = tot_size / len(dragon_list)
breed_avg = {}
for item in breeds:
    breed_avg[item] = breeds[item]/len(dragon_list)

print("Average age:", round(avg_age, 2))
print("Average size:", round(avg_size, 2))
print("Breed Percentages:")
for item in breed_avg:
    print(item + ' : ' + str(round(breed_avg[item]*100, 2)) + '%')

# Now we fight!

# 1.
print('\n')
survivors = []
for i in range(1, len(dragon_list) - 2):
    if not (dragon_list[i-1]['size'] > dragon_list[i]['size'] < dragon_list[i+1]['size']):
        survivors.append(dragon_list[i])
print('The number of surviving dragons after slaughter #1:', len(survivors))

# 2.
survivors_1 = []

for i in range(1, len(dragon_list) - 2):
    if (
            not (dragon_list[i-1]['size'] > dragon_list[i]['size'] < dragon_list[i+1]['size'] and dragon_list[i-1]['breed']!= dragon_list[i]['breed'] != dragon_list[i+1]['breed']) and
            not (dragon_list[i-1]['breed'] != dragon_list[i]['breed'] and dragon_list[i-1]['size'] >= dragon_list[0]['size'] * 2 ) and
            not (dragon_list[i+1]['breed'] != dragon_list[i]['breed'] and dragon_list[i+1]['size'] >= dragon_list[0]['size'] * 2)
    ):
        survivors_1.append(dragon_list[i])

print('The number of surviving dragons after slaughter #2:', len(survivors_1))

# 3.
survivors_1 = dragon_list[::1]
survivors_2 = []
while len(survivors_1) >= 100:
    for dragon in survivors_1:
        dragon['age'] += 1
        if dragon['age'] <= 100:
            survivors_2.append(dragon)
    survivors_1 = survivors_2
    survivors_2 = []

print('the number of surviving dragons after slaughter #3:', len(survivors_1))

# Top challenge:
print('\nCalculating the most detrimental situation using a hundred trials...\n')

total_1 = 0
total_2 = 0
total_3 = 0
for i in range(100):
    dragon_list = []
    for i in range(300):
        dragon = {
            'color': dragon_color[random.randint(0, len(dragon_color)-1)],
            'age': random.randint(0, 100),
            'size': random.randint(0, 20),
            'breed': dragon_breed[random.randint(0, len(dragon_breed)-1)]
        }
        dragon_list.append(dragon)

    survivors = []
    for i in range(1, len(dragon_list) - 2):
        if not (dragon_list[i-1]['size'] > dragon_list[i]['size'] < dragon_list[i+1]['size']):
            survivors.append(dragon_list[i])
    total_1 += len(dragon_list) - len(survivors)



    survivors_1 = []
    for i in range(1, len(dragon_list) - 2):
        if (
                not (dragon_list[i-1]['size'] > dragon_list[i]['size'] < dragon_list[i+1]['size'] and dragon_list[i-1]['breed']!= dragon_list[i]['breed'] != dragon_list[i+1]['breed']) and
                not (dragon_list[i-1]['breed'] != dragon_list[i]['breed'] and dragon_list[i-1]['size'] >= dragon_list[0]['size'] * 2 ) and
                not (dragon_list[i+1]['breed'] != dragon_list[i]['breed'] and dragon_list[i+1]['size'] >= dragon_list[0]['size'] * 2)
        ):
            survivors_1.append(dragon_list[i])
    total_2 += len(dragon_list) - len(survivors_1)

    survivors_1 = dragon_list[::1]
    survivors_2 = []
    while len(survivors_1) >= 100:
        for dragon in survivors_1:
            dragon['age'] += 1
            if dragon['age'] <= 100:
                survivors_2.append(dragon)
        survivors_1 = survivors_2
        survivors_2 = []
    total_3 += len(dragon_list) - len(survivors_1)


print('The total amount of dead dragons for fight #1 was', total_1, 'which makes the average', total_1/100, 'per fight')
print('The total amount of dead dragons for fight #2 was', total_2, 'which makes the average', total_2/100, 'per fight')
print('The total amount of dead dragons for fight #3 was', total_3, 'which makes the average', total_3/100, 'per fight')
print('\n')
if total_1 > total_2 and total_1 > total_3:
    print('fight #1 was most detrimental to the population.')

elif total_2 > total_1 and total_2 > total_3:
    print('fight #2 was most detrimental to the population.')

elif total_3 > total_1 and total_3 > total_1:
    print('fight #3 was most detrimental to the population, proving that time kills.')