# Computer Names
x = input('Please enter your full name: ')
x = x.split(' ')
name = x[0][0:3].lower() + x[-1][:3][::-1].lower()
print('\nYour computer name is:', name)

input('\nPress Enter to exit...')