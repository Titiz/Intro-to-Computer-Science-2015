# For-Loops
# 1.
myString = input('Input a String: ')
list_of_vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
for item in list_of_vowels:
    vowel_count += myString.lower().count(item)
print('The number of vowels in the string is', vowel_count)
# 2.
ListsOfLists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
dot_number = 1
for item in ListsOfLists:
    for i in item:
        print('.'*dot_number + i)
        dot_number += 2

dot_number_2 = 1
for item in ListsOfLists:
    for i in item:
        print('.'*dot_number_2 + i)
    dot_number_2 += 2