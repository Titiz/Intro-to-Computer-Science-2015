__author__ = 'Titas'
    def move(self, board, spaces):
        self.location.occupants.remove(self)
        previous = self.location.position
        for i in range(spaces):
            if len(self.location.next) == 1:
                self.location = board[int(self.location.next[0])]
            else:
                print('You can choose to the following paths:') # Choice of pathway
                for i in range(len(self.location.next)):
                    print(i, self.location.next[i])
                a = int(input('Would you like to go to:'))
                self.location = board[int(self.location.next[a])]
        after = self.location.position
        if after < previous and after < 12:  # 500 cash if you go through earth
            self.money += 500
            print('You have completed a circle around the solar system! You get 500 cash!')
            print('Your current balance is', self.money)