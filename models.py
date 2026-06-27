from enum import Enum

class MatchStatus(Enum):
    DA_INIZIARE = 1
    IN_CORSO = 2
    FINITA = 3

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
        self.points = 0
        self.win = 0
        self.lost = 0
        self.draws = 0
    def add_player(self, player):
        self.players.append(player)
    def remove_player(self, player):
        self.players.remove(player)
    def add_points(self, points):
        self.points += points
    

class Match():
    def __init__(self, team_a, team_b):
        self.date
        self.team_a_pts = 0
        self.team_b_pts = 0
        self.team_a = team_a
        self.team_b = team_b
        self.status = MatchStatus.DA_INIZIARE
    def add_points(self, points_a, points_b):
        self.team_a.add_points(points_a)
        self.team_b.add_points(points_b)

    
    
    