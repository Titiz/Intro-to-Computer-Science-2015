def islegal(board, row, col):
    positive = row >= 0 and col >= 0
    return positive and row < len(board) and col < len(board[row])

def get_board(fname):
    fp = open(fname)
    board = []
    for line in fp:
        board.append(list(line.strip()))
    fp.close()

    return board

def mkboard(rows, cols, filler=' '):
    board = []
    for i in range(rows):
        b = []
        for j in range(cols):
            b.append(filler)
        board.append(b)

    return board

def print_board(board):
    for row in board:
        print(' '.join(str(element) for element in row))
    return

def debug(string, spaces):
    print(' ' * spaces, string)
    return
