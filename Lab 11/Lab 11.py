def multiplier(lst):
    lst2 = []
    for item in lst:
        for i in range(2):
            lst2.append(item)
    return lst2

print(multiplier([1,2,3]))

def consumer(lst):
    lst2 = lst.copy()
    a = max(lst)
    lst2.pop(lst2.index(a))
    return lst2

print(consumer([1, 2, 5, 5, 3]))

def blender(lst):
    sum = [0]
    for item in lst:
        sum[0] += item
    return sum

print(blender([1,2,3]))

# Use the functions to produce 1.
lst = [1, 1, 1, 1, 5]

print((blender(consumer(consumer(multiplier(multiplier(lst)))))))

# Use the functions to produce 2.
lst = [2, 4, 5]

print(blender(consumer(consumer(consumer(multiplier(multiplier(consumer(consumer(multiplier(multiplier(lst)))))))))))


# Rock paper scissors

def rock_paper_scissors(hand_1, hand_2):
    levels = ['rock', 'paper', 'scissors', 'rock']
    if levels[levels.index(hand_2)] == levels[levels.index(hand_1) + 1]:
        winner = 'hand 2'
    elif levels[levels.index(hand_2)] == levels[levels.index(hand_1)]:
        winner = 'no one'
    else:
        winner = 'hand 1'
    print('hand 1 inputs:', hand_1)
    print('hand 2 inputs:', hand_2)
    return winner

print(rock_paper_scissors('paper', 'rock'),'wins\n')

import random


def computer_game():
    while True:
        AI = ['rock', 'paper', 'scissors'][random.randint(0, 2)]
        winner = rock_paper_scissors(input('rock, paper, scissors?'), AI)
        if winner != 'no one':
            print('the winner is', winner)
            break
        else:
            print("It's a draw, do it again!")

computer_game()

print('\n\n RPC Tourney')
# Extra RPC Tourney

def user_player():
    return input('rock, paper or scissors? ').lower()


def computer_player():
    return ['rock', 'paper', 'scissors'][random.randint(0, 2)]


def rock_paper_scissors_rounds(hand_1, hand_2):
    levels = ['rock', 'paper', 'scissors', 'rock']
    a = False
    while a == False:
        print('hand 1 inputs:', hand_1)
        print('hand 2 inputs:', hand_2)
        if levels[levels.index(hand_2)] == levels[levels.index(hand_1) + 1]:
            print('hand 2 wins the round')
            a = 1
            return a
        elif levels[levels.index(hand_2)] == levels[levels.index(hand_1)]:
            print('Draw! Do it again!')
            a = 2
            return a
        else:
            print('hand 1 wins the round')
            a = 0
            return a


def game(rounds, function1, function2):
    count = [0, 0]
    i = 0
    while i < rounds:
        try:
            count[rock_paper_scissors_rounds(function1(), function2())] += 1
            i += 1
        except IndexError:
            pass


    if count[0] == count[1]:
        return 2
    else:
        return count.index(max(count))

print(game(4, user_player, computer_player))

