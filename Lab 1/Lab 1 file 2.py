# Putting it all together

# 2.

x = input('>>>')

print('lowercase: ' + x.lower())
print('uppercase: ' + x.upper())
print('title: ' + x.title())

# count the vowels
vowels = ['a','e','o','u','i', 'y']
vowel_count = (sum([x.count(i) for i in vowels]))
print('the number of vowels is ' + str(vowel_count) +'\n')

input('\nPress enter to close')