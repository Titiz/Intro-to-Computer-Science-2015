import time, random
class Question:
    def  __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self):
        return input(self.question)



class Timer:
    def __init__(self, watches = [], begin = 0):
        self.watches = watches
        self.begin = begin
    def start(self):
        self.begin = time.time()

    def stop(self):
        self.watches.append(time.time() - self.begin)

    def results(self):
        for i in self.watches:
            print(i)
        print('Average:', sum(self.watches)/len(self.watches))



question_list = [
    Question('You cannot keep me until you have given me. What am I?', 'your word'),
    Question('Imagine you are in a dark room with a locked door. All you have with you is a rope and a pencil. \n'
             'You can hear the rain outside, but there are no windows. How do you get out?', 'stop imagining')
]
T = Timer()

for item in question_list:
    T.start()
    while item.ask() != item.answer:
        continue
    T.stop()

T.results()


# 2.


class Slot:
    def __init__(self, credits):
        self.credits = credits

    def __str__(self):
        return 'Credits Remaining: ' + str(self.credits)

    def pull(self, bet):
        i = []
        for j in range(3):
            i.append(random.randint(0, 9))

        print(i)

        if i.count(i[0]) == len(i):
            self.credits += bet * 2
            return True
        else:
            self.credits -= bet
            return False

S_1 = Slot(100)

wins = 0
for i in range(10):
    wins += int(S_1.pull(random.randint(5, 20)))
    print(S_1)

print('Amount of wins: ', wins)

# 3.
class RockPaperScissors:
    def __init__(self, hand):
        self.hand = hand

    def __str__(self):
        return str(self.hand)

    def __gt__(self, opponent):
        levels = ['rock', 'paper', 'scissors', 'rock']
        if levels[levels.index(self.hand)] == levels[levels.index(opponent.hand) + 1]:
            return True
        else:
            return False



signs = ['rock', 'paper', 'scissors']
for i in range(100):
    print(i+1)
    RPS_1 = RockPaperScissors(signs[random.randint(0, 2)])
    RPS_2 = RockPaperScissors(signs[random.randint(0, 2)])
    print(RPS_1, 'vs', RPS_2)
    print(RPS_1 > RPS_2)

# 4.


class Fibonacci:
    def __init__(self, bound):
        self.bound = bound
        self.i = -1


    def fib(self, i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return self.fib(i-1)+self.fib(i-2)

    def __iter__(self):
        return self


    def __next__(self):
        if self.i < self.bound:
            self.i += 1
            return self.fib(self.i)
        else:
            raise StopIteration



for i in Fibonacci(5):
    print(i)

