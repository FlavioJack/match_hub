from models import Player, Team, Match

def main():
    flavio = Player("Flavio")
    matteo = Player("Matteo")
    gabri = Player("Gabri")
    taccio = Player("Taccio")

    team_a = Team("siegehub")
    team_b = Team("teamvito")

    team_a.add_player(flavio)
    team_a.add_player(matteo)

    team_b.add_player(gabri)
    team_b.add_player(taccio)

    match1 = Match(team_a, team_b)

    print(team_a)
    print(team_b)
    print(match1)

    return







if __name__ == "__main__":
    main()



