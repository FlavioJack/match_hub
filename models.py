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

    def get_name(self):
        return self.name
    def get_stats(self):
        return [self.win, self.lost, self.draws]
    def reset_stats(self):
        self.win = self.lost = self.draws = 0
    def add_win(self, n):
        self.win += n
    def add_lost(self, n):
        self.win += n
    def add_draw(self, n):
        self.win += n
    def __str__(self):
        l = self.get_stats()
        return f" --> Player \"{self.get_name()}\", vittorie: {l[0]} sconfitte: {l[1]} pareggi: {l[2]};"

class Team():
    def __init__(self, name):
        self.name = name
        self.players = []
        self.score = 0
        self.win = 0
        self.lost = 0
        self.draws = 0

    def get_name(self):
        return self.name
    def get_players(self):
        players_names = ", ".join(player.name for player in self.players)
        return players_names
    def reset_players(self):
        self.players.clear()
    def add_player(self, player):
        self.players.append(player)
    def remove_player(self, player):
        self.players.remove(player)
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score
    def add_score(self, score):
        self.score += score
    def get_stats(self):
        return [self.win, self.lost, self.draws]
    def reset_stats(self):
        self.win = self.lost = self.draws = 0
    def add_win(self, n):
        self.win += n
    def add_lost(self, n):
        self.win += n
    def add_draws(self, n):
        self.win += n
    
    def __str__(self):
        l = self.get_stats()
        return f" --> Team \"{self.get_name()}\" - membri: {self.get_players()} - vittorie: {l[0]}, sconfitte: {l[1]}, pareggi: {l[2]};"
    
    

class Match():
    def __init__(self, team_a, team_b):
        self.name = f"{team_a.get_name()} vs {team_b.get_name()}"
        self.date = datetime.date.today()
        self.team_a = team_a
        self.team_b = team_b
        self.status = MatchStatus.DA_INIZIARE
    def get_name(self):
        return self.name
    def get_date(self):
        return self.date
    def get_teams_names(self):
        return [self.team_a.get_name(), self.team_b.get_name()]
    def get_score(self):
        return [self.team_a.get_score(), self.team_b.get_score()]
    def add_score(self, score_a, score_b):
        self.team_a.add_score(score_a)
        self.team_b.add_score(score_b)
    def get_status(self):
        return self.status.value
    def __str__(self):
        return f" --> Match {self.get_status()} || {self.get_teams_names()[0]} {self.get_score()[0]} - {self.get_score()[1]} {self.get_teams_names()[1]} || {self.get_date()}."

    
    
    