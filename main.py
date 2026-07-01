from models import Player, Team, Match

def registration(name, register, regtype):
    if regtype == 1:
        new_player = Player(name)
        register[name] = new_player
        return new_player
    elif regtype == 2:
        new_team = Team(name)
        register[name] = new_team
        return new_team
        

        
        
        

#def create_match(team_a, team_b):


def main():

    players_register = {}
    teams_register = {}
    matches_register = {}

  
    #match1 = Match(team_a, team_b)
   
    sel_menu = "0"
    while sel_menu.strip()!="":
        print("\n\n########## MAIN MENU ##########")
        print(" 1.Creare Player")
        print(" 2.Creare Team")
        print(" 3.Creare Match")

        sel_menu = input("Seleziona il menu: ")

        if sel_menu == "1":
            player_name = input("Inserisci il nome del giocatore: ")
            while player_name.strip() == "":
                player_name = input("Non puoi lasciare campo vuoto, inserisci il nome del giocatore: ")
            if player_name in players_register:
                print("❌ Nome già in uso, scegline un altro!")
            else:
                registration(player_name, players_register, 1)
                print(f"✅ Nome \"{player_name}\" inserito correttamente!")
        elif sel_menu == "2":
            team_name = input("Inserisci il nome del team: ")
            new_team = registration(team_name, teams_register, 2)

            print("Giocatori disponibili: ", end="")
            for player in players_register.keys():
                print(player, end=" ")
            print("")
            # choose names, append to list and foreach list's element (player name) 
            # pick from the player objects register and add to the team object
            print("Adesso aggiungi nomi di giocatori tra quelli disponibili")
            players_for_team = []
            sel_name = input("Digita nome giocatore + Enter, altrimenti Enter per terminare: ").strip()
            while sel_name != "":
                if sel_name in players_register.keys():
                    players_for_team.append(sel_name)
                else: 
                    print("Nome non presente tra quelli disponibili")
                sel_name = input("Digita nome giocatore + Enter, altrimenti Enter per terminare: ").strip()
            for player in players_for_team:
                new_team.add_player(players_register[player])
        elif sel_menu == "3":
            print("Elenco dei team presenti: ")
            for t in teams_register: 
                print(t)




if __name__ == "__main__":
    main()



