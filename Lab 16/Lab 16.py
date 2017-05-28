class Automobile:
    def __init__(self, make, model, mileage, price):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        self.text = ''

    def __str__(self):
        self.text += 'Make: ' + self.make + ' \n'
        self.text += 'Model: ' + self.model + ' \n'
        self.text += 'Mileage: ' + str(self.mileage) + ' \n'
        self.text += 'Price: ' + str(self.price) + ' \n'
        return self.text



class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.doors = doors

    def __str__(self):
        super().__str__()
        self.text += 'Doors: ' + str(self.doors)
        return self.text


class Truck(Automobile):
    def __init__(self, make, model, mileage, price, wheels):
        super().__init__(make, model, mileage, price)
        self.wheels = wheels

    def __str__(self):
        super().__str__()
        self.text += 'Wheels: ' + str(self.wheels)
        return self.text


class SUV(Automobile):
    def __init__(self, make, model, mileage, price, capacity):
        super().__init__(make, model, mileage, price)
        self.capacity = capacity

    def __str__(self):
        super().__str__()
        self.text += 'Doors: ' + str(self.capacity)
        return self.text


def print_auto(auto):
    print(auto)


car = Car('a', 'WOW', 100, 2000000, 9)
truck = Truck('b', 'Now', 10, 23, 2)
suv = SUV('c', 'Bow', 1000, 0.7, 1)

print(car)
print(truck)
print(suv)


from random import randint

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __gt__(self, other):
        suits = ['hearts', 'spades', 'diamonds', 'clovers']
        if self.number > other.number:
            return True
        elif self.number < other.number:
            return False
        else:
            if suits.index(self.suit) > suits.index(other.suit):
                return True
            elif suits.index(self.suit) < suits.index(other.suit):
                return False

class Deck(list):
    def __init__(self):
        suits = ['hearts', 'spades', 'diamonds', 'clovers']
        for i in range(52):
            self.append(Card(randint(0,10), suits[randint(0,3)]))


    def deal(self):
        return self.pop(0)

class Hand:
    def __init__(self, name):
        self.name = name
        self.card = 0
        self.wins = 0

    def __gt__(self, other):
        if self.wins > other.wins:
            return True
        else:
            return False

    def __str__(self):
        return self.name

a = Deck()
h1 = Hand('Player 1')
h2 = Hand('Player 2')

while a:
    h1.card = a.deal()
    h2.card = a.deal()
    if h1.card > h2.card:
        h1.wins += 1
    else:
        h2.wins += 1

print(h1, 'has', h1.wins, 'wins')
print(h2, 'has', h2.wins, 'wins')
if h1 > h2:
    print(h1, 'wins!')
elif h2 > h1:
    print(h2, 'wins!')
else:
    print("It's a TIE!")