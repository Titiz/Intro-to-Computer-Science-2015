import timeit
# 7. Transposing a Matrix:

matrix = [[0, 1, 2, 3], [0, 4, 5, 6], [0, 7, 8, 9]]
n = 0
m = 0
for item in matrix:
    n += 1
for item in matrix[0]:
    m += 1
starting_list = []
added_list = []
for item in range(m):
    for i in range(n):
        added_list.append(0)
    starting_list.append(added_list)
    added_list = []

print('Original Matrix: ')

for item in matrix:
    print(str(item).replace('[', '').replace(']', '').replace(',', ''))

for item in matrix:
    for i in item:
        x = item.index(i)
        y = matrix.index(item)
        starting_list[x][y] = i
print('\nTransposed Matrix:')

for item in starting_list:
    print(str(item).replace('[', '').replace(']', '').replace(',', ''))


# 8. a.
import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string = ''
for i in range(2**10):
    string += letters[random.randint(0, 25)]

print('\nOriginal string:', string)
start_time = timeit.default_timer()
new_string = ''
for i in range(len(string)):
    try:
        new_string += string[i+1]
    except IndexError:
        new_string += string[0]
print('Rotated string', new_string)

print('\nFor loop took: ', timeit.default_timer() - start_time, 'seconds')

# 8. b.
start_time = timeit.default_timer()
new_string_sliced = string[1:] + string[0]
print('Sliced took: ', timeit.default_timer() - start_time, 'seconds')
