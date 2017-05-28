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