
# Particles in a box. They bounce off of the walls, but not from each other.


import os, time
from random import randint

class Particle:
    def __init__(self, position, velocity, identifier):
        self.position = position
        self.velocity = velocity
        self.identifier = identifier

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]



class Board:
    def __init__(self, m, n, filler):
        board = []
        for i in range(m):
            board.append([])
            for j in range(n):
                board[i].append(filler)
        self.board = board


    def __str__(self):
        final = ''
        ceiling = ''
        line = ''
        final += '■' + '----' * len(self.board) + ' ■' + '\n'
        for item in self.board[::-1]:
            ceiling += '|'
            line += '|'
            for i in item:
                ceiling += ' ' + '    ' * (len(i)-1) + '   '
                line += ' '+ str(i) + '  '
            line += ' '
            final += ceiling + ' |\n'
            final += line + '|\n'
            if item is self.board[0]:
                final += (ceiling)
            line = ''
            ceiling = ''
        final += '\n■' + '----' * len(self.board) + ' ■' + '\n'
        return final

    def update(self, p):
        if p.position[0] + p.velocity[0] < 0 or p.position[0] + p.velocity[0] > len(self.board[0])-1:
            p.velocity[0] *= -1
        if p.position[1] + p.velocity[1] < 0 or p.position[1] + p.velocity[1] > len(self.board)-1:
            p.velocity[1] *= -1
        self.board[p.position[0]][p.position[1]] = p.identifier


# Only works with square boards


particles = []
for i in range(6):
    particles.append(Particle([randint(0,9), randint(0,9)], [randint(-1, 1), randint(-1, 1)], chr(randint(37, 44))))
for i in range(100):
    board = Board(12, 12, ' ')
    for item in particles:
        board.update(item)
    # I skip a bunch of lines instead of using the os clear statement as it does not work on windows.
    print('\n' * 20)
    print(board)
    time.sleep(2 ** -2)
    for p in particles:
        p.move()