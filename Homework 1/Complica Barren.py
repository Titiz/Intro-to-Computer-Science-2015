import random
# The purpose of this application is to make a simple game of Complica.
# We begin by setting the size of the board and the amount of checkers that have to be connected
# in order for a winning event to occur
cols = 7
rows = 6
win_check = 4

# We then create the board which will be the basis of the game.
board = []
for i in range(rows):
    board.append([])
    for j in range(cols):
        board[i].append(' ')

# We define the function that will display the board and the current placement of the checkers
# to the user. It takes the parameter l, which is the board.


def board_print(l):
    numbers = ''
    for i in range(cols):
        numbers += '  ' + str(i) + ' '
    line = '   '
    for item in l[::-1]:
        print('   +' + '---+' * len(item))
        for i in item:
            line += ('| ' + i + ' ')
        print(line + '|')
        line = '   '
    print('   +' + '---+' * len(item))
    print('   ' + numbers)

# We define a function to check all of the rows for a winning combination of checkers.
# We use the wins number to account for cases where both players win. This function
# builds a string from the characters in each row and checks each string for the winning
# combinations which is the symbol times the winning amount.


def check_rows(l, symbol):
    wins = 0
    check_string = ''
    for item in l:
        for i in item:
            check_string += i
            if check_string == symbol * win_check:
                wins += 1
            elif len(check_string) == win_check:
                check_string = check_string[1:]
        check_string = ''
    return wins

# We define a function to check all of the columns for a winning combination of checkers.
# Takes parameter l (the board) and the symbol in question. Works by going through the
# i element of every column on the board, and again forming a string which is then checked.

def check_cols(l, symbol):
    wins = 0
    check_string = ''
    for i in range(cols):
        for item in l:
            check_string += item[i]
            if check_string == symbol * win_check:
                wins += 1
            elif len(check_string) == win_check:
                check_string = check_string[1:]
        check_string = ''
    return wins

# We define a function to add any symbol to a row and move all of the checkers down if the column
# is filled to the top. We will be using parameters 'X' and 'Y' for the symbol.


def add_checker(col, l, symbol):
    row_amount = 0
    for i in range(rows):
        if l[i][col] == ' ':
            l[i][col] = symbol
            break
        else:
            row_amount += 1
        if row_amount >= rows:
            for j in range(rows-1):
                l[j][col] = l[j+1][col]
            l[rows-1][col] = symbol


# We print the board and set the winner parameter which will be set as the variable to be
# changed for the while loop to finish.

board_print(board)


winner = ''

# Finally, we loop over the player choosing which column the checker 'X' should be placed in,
# the computer putting in a random 'O' character in one of the columns and checking whether
# the player or the computer has more winning combinations on the current board. If one of them
# has more winning combinations, that player wins. If both have equal amount of winning combinations,
# the game continues.

while winner == '':
    x = int(input('Please select a column to insert your checker: '))
    add_checker(x, board, 'X')
    board_print(board)
    x_wins = check_cols(board, 'X') + check_rows(board, 'X')
    o_wins = check_cols(board, 'O') + check_rows(board, 'O')
    if x_wins > o_wins:
        winner = 'Player'
        break
    if o_wins > x_wins:
        winner = "AI"
        break
    x_wins = o_wins = 0
    print('\n')
    add_checker(random.randint(0, cols-1), board, 'O')
    x_wins = check_cols(board, 'X') + check_rows(board, 'X')
    o_wins = check_cols(board, 'O') + check_rows(board, 'O')
    if x_wins > o_wins:
        winner = 'Player'
    if o_wins > x_wins:
        winner = "AI"
    x_wins = o_wins = 0
    board_print(board)

print("\nThe winner is", winner)

