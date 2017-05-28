# Additional challenge:

# I used help from http://stackoverflow.com/questions/8419564/difference-between-two-dates
from datetime import *

# 1.
a = input('Please enter a month: ')
b = input('Please enter a day: ')
c = input('Please enter a year: ')
if len(str(a)) == 1:
    a = '0' + a
if len(str(b)) == 1:
    b = '0' + b
if len(str(c)) == 1:
    c = '000' + c
if len(str(c)) == 2:
    c = '00' + c
if len(str(c)) == 3:
    c = '0' + c
0
today = c + '-' + b + '-' + a
date = str(date.today())
print('date entered: ' + today)
print("today's date: " + date)
try:
    today = datetime.strptime(today, "%Y-%m-%d")
    date = datetime.strptime(date, "%Y-%m-%d")
    days = abs((today - date).days)


    if days <= 1:
        print('that was ' + str(day) + ' days ago')
    if days > 1:
        print('that was ' + str(days) + ' days ago')

except:
    print('One of the inputs was incorrect. Aborting the process...')

input('Press enter button to exit')