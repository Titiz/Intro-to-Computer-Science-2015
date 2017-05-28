# 1.
def ftc(fahrenheit):
    celsius = 5/9*(fahrenheit -32)
    return celsius

def ctf(celsius):
    fahrenheit = celsius*9/5+32
    return fahrenheit

# 2.

def reverse_list(l):
    a = []
    for i in range(1, len(l)):
        a.append(l[-i])
    a.append(l[0])
    return a


print(reverse_list([0, 1, 2, 3]))


# 1.
def makeboard(m, n, filler):
    board = []
    for i in range(m):
        board.append([])
        for j in range(n):
            board[i].append(filler)
    return board
# 2.
def printboard(board):
    ceiling = '+'
    line = ''
    for item in board[::-1]:
        for i in item:
            ceiling += '---' + '-' * (len(i)-1) + '+'
            line += '| '+ str(i) + ' '
        line += '|'
        print(ceiling)
        print(line)
        if item is board[0]:
            print(ceiling)
        line = ''
        ceiling = '+'
# 3.
def update_board(board, i, j, decorator, filler):
    try:
        if board[j][i] == filler:
            board[j][i] = decorator
            return True
        else:
            return False
    except IndexError:
        return False

# 4.
def iswinner(board, decorator):
    # rows:
    string = ''
    for item in board:
        for i in item:
            string += i
        if string.count(decorator*3) > 0:
            return 'Winner is', decorator
        string = ''
    # columns:
    string = ''
    for i in range(len(board[0])):
        for j in range(len(board)):
            string += (board[j][i])

        if string.count(decorator*3) > 0:
            return 'Winner is', decorator
        string = ''
    # diagonals:
    check_string_left = ''
    check_string_right = ''
    string_list = []
    for i in range(len(board) - 2):
        for j in range(len(board[0]) - 2):
            for k in range(3):
                check_string_right += board[i+k][j+k]
                check_string_left += board[i+k][::-1][j+k]
            string_list.append(check_string_right)
            string_list.append(check_string_left)
            check_string_left = ''
            check_string_right = ''
    for item in string_list:
        if item == decorator * 3:
            return 'Winner is', decorator

def check_empty(board, i, j, filler):
    try:
        if board[j][i] == filler:
            return True
        else:
            return False
    except IndexError:
        return False

# Putting it together
board = makeboard(3, 3, ' ')

for i in range(len(board) * len(board[0])):
    printboard(board)
    a = input('Coordinate a,b: ')
    while check_empty(board, int(a[0]), int(a[-1]), ' ') == False:
        a = input('Coordinate a,b: ')
    update_board(board,int(a[0]), int(a[-1]), 'X', ' ')
    printboard(board)
    if iswinner(board, 'X') != None:
        print(iswinner(board, 'X'))
        break
    while check_empty(board, int(a[0]), int(a[-1]), ' ') == False:
        a = input('Coordinate a,b: ')
    update_board(board,int(a[0]), int(a[-1]), 'O', ' ')
    if iswinner(board, 'O') != None:
        print(iswinner(board, 'O'))
        break
    if i == len(board) * len(board[0]):
        print('There is no winner')
