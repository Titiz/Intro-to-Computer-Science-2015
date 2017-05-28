# Reading and write skills
import random
# 1.
f = open('number.txt', 'w')
for i in range(10):
    f.write(str(random.randint(0,10))+'\n')
f.close()
# 2.
f = open('number.txt', 'r')
sum = 0
for i in f:
    sum += int(i)
f.close
print(sum)

# Persistent phone book
# 1.

phone_book = {}
while True:
    name = input('Please enter a name: ').lower()
    if name == '':
        break
    elif name in phone_book:
        print('Name already present in phonebook')
    else:
        number = input("Please enter the user's number: ")
        phone_book[name] = number
f = open('phonebook.txt', 'a')
for i in phone_book:
    f.write(str(i) + ', ' + str(phone_book[i]) + '\n')
f.close()
# 2.
f = open('phonebook.txt', 'r')
i_phone_book = {}
for i in f:
    if i != '\n':
        i = i.split(', ')
        i_phone_book[i[0]] = i[1].strip()
print(i_phone_book)

# 3.

while True:
    name = input('Please enter a name: ').lower()
    if name == '':
        break
    elif name in i_phone_book:
        print(i_phone_book[name])
    else:
        print('Name not found')
##
# Memory extension:
##


f = open('Memory.txt', 'r')
raw_rows = []
for i in f:
    raw_rows.append(i.strip())
f.close()
rows = []
row = []
for item in raw_rows:
    for i in item:
        row.append(i)
    rows.append(row)
    row = []


board_empty = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
# board = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H']]
# boardletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']*2
# random.shuffle(boardletters)

board = rows

for i in board:
    dec2 = ''
    dec = '+---' * len(i) + '+'
    for j in i:
        dec2 += '| ' + j + ' '
    print(dec)
    print(dec2 + '|')
print(dec)


Game_not_over = True

while Game_not_over:
##    for i in board:
##        dec2 = ''
##        dec = '+---' * len(i) + '+'
##        for j in i:
##            dec2 += '| ' + j + ' '
##        print(dec)
##        print(dec2 + '|')
##    print(dec)

    coordinates1 = input("Enter row,col 1 (to skip write 'stop')")
    if coordinates1 == 'stop':
        break
    coordinates2 = input("Enter row,col 2 ")
    coordinates1 = coordinates1.split(",")
    coordinates2 = coordinates2.split(",")
    ##
    ##print(coordinates1)
    ##print(coordinates2)

    a = int(coordinates1[0])
    b = int(coordinates1[1])
    c = int(coordinates2[0])
    d = int(coordinates2[1])

    if board[a][b] == board[c][d]:
        print("Yep!")
        board_empty[a][b]=board[a][b]
        board_empty[c][d]=board[c][d]
    else:
        print(board[a][b],board[c][d])

    for i in board_empty:
        dec2 = ''
        dec = '+---' * len(i) + '+'
        for j in i:
            dec2 += '| ' + j + ' '
        print(dec)
        print(dec2 + '|')
    print(dec)

    Game_not_over = False

    for i in board_empty:
        if ' ' in i:
            Game_not_over = True
print('Game Over')