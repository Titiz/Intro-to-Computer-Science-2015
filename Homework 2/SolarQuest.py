import random
f = open('solarquest.csv', 'r')
f.readline() #Eliminate first line of the csv file

class Square: # Class used to defined a location on the board
    def __init__(self, position, name, next, type, orbit, group, purchase, rent, fuel):
        self.position = int(position)
        self.name = name
        self.next = next.split(';')
        self.type = type
        self.orbit = orbit
        self.group = group
        if purchase != '':
            self.purchase = int(purchase)
        else:
            self.purchase = purchase
        if rent != '':
            self.rent = int(rent)
        else:
            self.rent = 0
        if fuel.strip() != '':
            self.fuel = int(fuel)
        else:
            self.fuel = fuel
        self.occupants = []
        self.owner = None
        if self.type == 'space dock':
            self.fuel_station = True
        else:
            self.fuel_station = False


class Board(dict): # The board that is played on. Creates both the players and location from the csv file
    def __init__(self, f, players):
        self.players = []
        for item in f:
            lst = item.split(',')
            self[int(lst[0])] = Square(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8])
        for item in players:
            player = Player(item, self[0])
            self[0].occupants.append(player)
            self.players.append(player)


class Player: # Player class with the required attributes and operations.
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.active = True
        self.money = 1500
        self.fuel = 12
        self.fuel_stations = 3
        self.owned = []
        self.active = True

    def move(self, board, spaces):
        self.location.occupants.remove(self)
        previous = self.location.position
        for i in range(spaces):
            if len(self.location.next) == 1:
                self.location = board[int(self.location.next[0])]
            else:
                print('You can choose to the following paths:') # Choice of pathway
                for i in range(len(self.location.next)):
                    print(str(i) + ':', self.location.next[i])
                a = int(input('Where would you like to go to?'))
                self.location = board[int(self.location.next[a])]
        after = self.location.position
        if after < previous and after < 12:  # 500 cash if you go through earth
            self.money += 500
            print('You have completed a circle around the solar system! You get 500 cash!')
            print('Your current balance is', self.money)

        self.location.occupants.append(self)

    def pay_rent(self):                         # I assumed that no rent is payed unless the owner of the planet
        if self.location.owner is not None:     # is one of the other players.
            self.money -= self.location.rent
            self.location.owner.money += self.location.rent
            if self.location.owner != self:
                print('You payed', self.location.rent, 'cash for rent to', self.location.owner.name)
                print('Your remaining balance:', self.money)
        else:
            print('You spend the night for free!')
        if self.location.position == 0:
            self.money -= self.location.rent
            print('You have landed on earth! You earn an extra 500 cash!')
            print('Your current balance is', self.money)

        if self.money < 0:
            self.active = False

    def buy_fuel(self):
        if self.location.fuel_station:
            if self.money - self.location.fuel > 0:
                self.fuel += 1
                if self.location.owner != self:
                    self.money -= self.location.fuel
                print('You have purchased 1 unit of fuel!')
                print('You now have', self.fuel, 'units in your tank')
                print('Your current balance:', self.money)
            else:
                print('You do not have sufficient funds')
        else:
            print('You cannot purchase fuel here!')

    def buy_property(self):
        if self.location.purchase != '':
            if self.location.owner is None:
                if self.location.purchase <= self.money:
                    self.owned.append(self.location)
                    self.location.owner = self
                    self.money -= self.location.purchase
                    print('Property successfully purchased!')
                    print('Your current balance:', self.money)
                else:
                    print('You do not have enough cash!')

            else:
                print('Property is already owned!')
        else:
            print('Property is not for sale!')


player_names = []

count = int(input('How many players? '))

for i in range(count): #Decide how many players are playing and their names.
    text = 'Enter the name of player ' + str(i+1) + ': '
    player = input(text)
    player_names.append(player)


board = Board(f, player_names)
turn = 1

options = ['Purchase Property', 'Get fuel', 'Plant fuel station', 'Move!', 'Board information', 'Player information', 'End turn']
while True:  # Loop to play the game
    pay = True  # Used specifically to separate the case where of landing on earth.
    end = False
    if len(board.players) <= 1:
        break
    p = (turn % len(board.players)) - 1
    print('\nIt is', board.players[p].name + "'s turn!\n")
    while True:  # Loop to go through the turn of each player.
        # First we check if any of the losing conditions are fulfilled:
        if board.players[p].fuel < 2:     # Only way that a spaceship is stuck is it has less fuel than the minimum roll
            if board.players[p].location.owner == board.players[p]:          # First we need to check if the player is
                if board.players[p].location.fuel_station is False:          # the owner and whether the place or the
                    if board.players[p].fuel_stations == 0:                  # player has a fuel station
                        board.players[p].active = False
                        end = True
            # If the player lands on a planet that is unowned, he either loses if he cannot buy fuel or the planet.
            else:
                if board.players[p].location.owner is None:
                    if board.players[p].location.purchase == '' and board.players[p].location.fuel_station is False:
                        board.players[p].active = False
                        end = True
                    elif board.players[p].location.purchase > board.players[p].money:
                        board.players[p].active = False
                        end = True
                else:
                    if board.players[p].location.fuel > board.players[p].money:  # Otherwise, the user has to have
                        board.players[p].active = False                          # enough cash to buy fuel
                        end = True
        if end is False:
            print('\nOptions:')
            if board.players[p].location.type == 'federation station':
                options.append('Buy Fuel Station')
            for i in range(len(options)):
                print(str(i)+': ' + options[i])
            print('\n')
            if options[-1] == 'Buy Fuel Station': #Added option when landing on a federation station.
                options.pop()
            action = input('>> ')
        else:
            action = '6'


        if action == '0':
            board.players[p].buy_property()

        if action == '1':
            board.players[p].buy_fuel()

        if action == '2':
            if board.players[p].location.owner == board.players[p]:
                if board.players[p].location.fuel_station is False:
                    if board.players[p].fuel_stations > 0:
                        board.players[p].location.fuel_station = True
                        board.players[p].fuel_stations -= 1
                        print("You have successfully placed a fuel station!")
                        print("you have", board.players[p].fuel_stations, 'fuel stations remaining!')
                    else:
                        print("You are out of fuel stations!")
                else:
                    print("There is already a fuel station here!")
            else:
                print('You do not own this location!')

        if action == '3':
            d_1 = random.randint(1, 6)
            d_2 = random.randint(1, 6)
            print('You rolled', d_1 + d_2)
            print('You have', board.players[p].fuel, 'fuel units in your tank')
            if board.players[p].fuel >= d_1 + d_2:
                board.players[p].move(board, d_1 + d_2)
                board.players[p].fuel -= d_1+d_2
                print('You use', d_1+d_2, 'units of fuel')
                print('You have', board.players[p].fuel, 'fuel units left in your tank')
                print('You are now at: ', board.players[p].location.name + '(' + str(board.players[p].location.position) + ')')
                end = True
            else:
                print('You do not have sufficient fuel!')
                print('You stay at your current location. \n')
                end = True

        if action == '4':
            for item in board:
                text = str(board[item].position) + ' : ' + board[item].name
                if board[item].fuel_station:
                    text += '*'
                text += ' : '
                for i in board[item].occupants:
                    text += i.name
                    if i != board[item].occupants[-1]:
                        text += ', '
                print(text)

        if action == '5':
            print('Player Name:', board.players[p].name)
            print("Player's Location:", board.players[p].location.name + '(' + str(board.players[p].location.position) + ')')
            print('Money:', board.players[p].money)
            text = 'Owned Planets: '
            for item in board.players[p].owned:
                text += item.name
                if item != board.players[p].owned[-1]:
                    text += ', '
            print(text)
            print('Fuel Units:', board.players[p].fuel)
            print('Fuel Stations:', board.players[p].fuel_stations)

        if action == '6':
            if board.players[p].location == board[0]:
                pay = False     # Prevents players from waiting on earth and collecting cash
            else:
                pay = True
            end = True

        if action == '7' and board.players[p].location.type == 'federation station':
            if board.players[p].money >= 500:
                board.players[p].money -= 500
                board.players[p].fuel_stations += 1
                print('You have successfully purchased a fuel station!')
                print('Your current fuel station amount:', board.players[p].fuel_stations)
                print('Your balance:', board.players[p].money)
            else:
                print('You do not have sufficient funds!')

        if end is True:
            if pay is True:
                board.players[p].pay_rent()
            for player in board.players:
                if player.active is False:
                    print(player.name, 'Loses!')
                    board.players.remove(player)
            break
    if len(board.players) == 1:
        print(board.players[0].name, ' IS THE WINNER!!!')  # Declaration of winner

    turn += 1




