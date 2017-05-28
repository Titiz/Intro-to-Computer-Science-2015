import random


def rock_paper_scissors_rounds(hand_1, hand_2):
    levels = ['rock', 'paper', 'scissors', 'rock']
    a = False
    while a == False:
        if levels[levels.index(hand_2)] == levels[levels.index(hand_1) + 1]:
            a = 1
            return a
        elif levels[levels.index(hand_2)] == levels[levels.index(hand_1)]:
            a = False
            return a
        else:
            a = 0
            return a



def game(rounds, function1, function2):
    count = [0, 0]
    i = 0
    while i < rounds:
        try:
            count[rock_paper_scissors_rounds(function1(), function2())] += 1
            i += 1
        except TypeError:
            pass

    print(count)
    if count[0] == count[1]:
        return 2
    else:
        return count.index(max(count))



# Strategy

def rock_only():
    return 'rock'

def paper_only():
    return 'paper'

def scissors_only():
    return 'scissors'

def s_p():
    return ['scissors', 'paper'][random.randint(0,1)]

def p_r():
    return ['rock', 'paper'][random.randint(0,1)]

def r_s():
    return ['scissors', 'rock'][random.randint(0,1)]

def all():
    return ['rock', 'paper', 'scissors'][random.randint(0, 2)]

players = [rock_only, paper_only, scissors_only, s_p, p_r, r_s, all]

for item in players:
    print(item())
def round_robin(lst):
    a = 0
    wins = {}
    while a != len(lst)-1:
        for i in range(a+1, len(lst)):
            outcome = game(100, lst[a], lst[i])
            print(outcome)
            if outcome == 0:
                if lst[a] in wins:
                    wins[lst[a]] += 1
                else:
                    wins[lst[a]] = 1
            elif outcome == 1:
                if lst[i] in wins:
                    wins[lst[i]] += 1
                else:
                    wins[lst[i]] = 1
        print(a)
        a += 1
    return wins

wins = round_robin(players)

print('\nMost wins:')
winner_functions = []
a = max(wins.values())
for item in wins:
    if wins[item] >= a - 1:
        print(item, ':', wins[item])
        winner_functions.append(item)



print('\nKnock Out:\n')
def knock_out(lst):

    while len(lst) != 1:
        outcome = game(100, lst[0], lst[1])
        print(outcome)
        if outcome == 0:
            a = lst.pop(0)
            lst.pop(0)
            lst.append(a)
        elif outcome == 1:
            a = lst.pop(1)
            lst.pop(0)
            lst.append(a)
    return lst[0]


winner = knock_out(winner_functions)


print('THE WINNER IS:', winner)


