from enum import Enum
import datetime

class MatchStatus(Enum):
    DA_INIZIARE = "da iniziare"
    IN_CORSO = "in corso"
    FINITA = "finita"

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
    def get_players(self):
        players_names = ", ".join(player.name for player in self.players)
        return players_names
    def add_player(self, player):
        self.players.append(player)
    def remove_player(self, player):
        self.players.remove(player)
    def __str__(self):
        return f" -- Team \"{self.name.upper()}\" composto dai membri: {self.get_players()}."
    
    

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
    def __str__(self):
        return f" -- Match {self.status.value} || {self.team_a.name} {self.team_a_pts} - {self.team_b_pts} {self.team_b.name}."

    
    
    