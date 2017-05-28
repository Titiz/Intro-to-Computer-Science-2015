import helpers
import time
# Your job is to develop this function

def find_path(board, row, col, spaces = 0):
    if helpers.islegal(board, row, col):
        a = board[row][col]
        if board[row][col] == '.' or board[row][col] == 'o':
            time.sleep(0.5)
            board[row][col] = '^'
            helpers.print_board(board)


            helpers.debug('+down', spaces)
            if find_path(board, row + 1, col, spaces + 1):
                helpers.debug('-down', spaces)
                return True
            print('NO')
            helpers.debug('+up', spaces)
            if find_path(board, row - 1, col, spaces + 1):
                helpers.debug('-up', spaces)
                return True
            print('NO')
            helpers.debug('+right', spaces)
            if find_path(board, row, col + 1, spaces + 1):
                helpers.debug('-right', spaces)
                return True
            print('NO')
            helpers.debug('+left', spaces)
            if find_path(board, row, col - 1, spaces + 1):
                helpers.debug('-left', spaces)
                return True
            print('NO')

        elif board[row][col] == 'x':
            return True

        board[row][col] = a
        return False


    helpers.print_board(board)












board = helpers.get_board('board.mz')
print(find_path(board, 0, 0))
helpers.print_board(board)
print('-' * 50)

find_path(board, 0, 0)

print('-' * 50)
helpers.print_board(board)
