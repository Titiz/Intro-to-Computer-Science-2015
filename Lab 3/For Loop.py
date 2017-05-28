from random import randint
from math import pi


# For Loop
# 1.
sum = 0
for i in range(11):
    sum += i
print(sum)

# 2.
sum_2 = 0
for i in range(1000001):
    sum_2 += i
print(sum_2)

# 3. Find the number of instances of a string of length of 1 or more.

s1 = str(pi)
s2 = '14'
print('String:', s1)
print('Looking for:', s2)
number_found = 0
count = 0
for i in str(s1):
    number_found += int(s1[count:count+len(s2)] == str(s2))
    count += 1
print('amount found:', number_found)
# 4.
original_list = [3, 6, 9, 12, 15, 18]
sumlist = []
sumlist.append(original_list[0])
for i in range(0, len(original_list)):
    sumlist.append(sumlist[i] + original_list[i])
print(sumlist)

# 5.
lists_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
product_list = []
one_product = 1
for item in lists_of_lists:
    for i in item:
        one_product *= i
    product_list.append(one_product)
    one_product = 1
print(product_list)

# 6.
m = 5
n = 4
starting_list = []
added_list = []
for item in range(m):
    for i in range(n):
        added_list.append(randint(0, 9))
    starting_list.append(added_list)
    added_list = []
print(starting_list)



