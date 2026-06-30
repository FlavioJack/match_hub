from models import Player, Team, Match

def registration(name, register, regtype):
    if name in register:
        print("❌ Nome già in uso, scegline un altro!")
    else:
        if regtype == 1:
            new_player = Player(name)
            register[name] = new_player
        elif regtype == 2:
            new_team = Team(name)
            register[name] = new_team
        
        print(f"✅ Nome \"{name}\" inserito correttamente!")

#def create_match(team_a, team_b):


def main():

    players_register = {}
    teams_register = {}
    matches_register = {}

  
    #match1 = Match(team_a, team_b)
   

    while(True):
        print("\n\n########## MAIN MENU ##########")
        print(" 1.Creare Player")
        print(" 2.Creare Team")
        print(" 3.Creare Match")

        sel_menu = int(input("Seleziona il menu: "))
        if sel_menu == 1:
            player_name = input("Inserisci il nome del giocatore: ")
            registration(player_name, players_register, 1)
        elif sel_menu == 2:
            team_name = input("Inserisci il nome del team: ")
            registration(team_name, teams_register, 2)
            print("Giocatori disponibili: ", end="")
            for player in players_register.keys():
                print(player, end=" ")
            print("")
            print("Adesso aggiungi giocatori tra quelli disponibili")
            temp = []
            # scegli le key dei nomi, aggiungi a temp, per ogni elemento di temp aggiungi al team

        elif sel_menu == 3:
            print("Elenco dei team presenti: ")
            for t in teams_register: 
                print(t)




if __name__ == "__main__":
    main()



