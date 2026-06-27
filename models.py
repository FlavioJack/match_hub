from enum import Enum
import datetime

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
    def get_points(self):
        return self.points
    def set_points(self, points):
        self.points = points
    def add_points(self, points):
        self.points += points
    def add_player(self, player):
        self.players.append(player)
    def remove_player(self, player):
        self.players.remove(player)
    
    

class Match():
    def __init__(self, team_a, team_b):
        self.date = datetime.date.today()
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_pts = self.team_a.get_points()
        self.team_b_pts = self.team_b.get_points()
        self.status = MatchStatus.DA_INIZIARE
    def get_points(self):
        return [self.team_a_pts, self.team_b_pts]
    def set_points(self, points):
        self.points = points
    def add_points(self, points_a, points_b):
        self.team_a.add_points(points_a)
        self.team_b.add_points(points_b)

    
    
    