class Player():
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.lost = 0
        self.draws = 0

class Team():
    def __init__(self, name):
        self.name = name
        self.players = []
        self.win = 0
        self.lost = 0
        self.draws = 0
    
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)
