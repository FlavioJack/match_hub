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
        

def show_player_menu():
    print("\n\n===== PLAYER MENU =====")
    print(" 1.Create Player")
    print(" 2.Show Players and Stats")
    print(" 3.Back to Main Menu")        
        
        

#def create_match(team_a, team_b):


def main():

    players_register = {}
    teams_register = {}
    matches_register = {}

  
    #match1 = Match(team_a, team_b)
   
    sel_menu = "0"
    while sel_menu.strip()!="":
        print("\n\n########## MAIN MENU ##########")
        print(" 1.Menu Player")
        print(" 2.Menu Team")
        print(" 3.Menu Match")

        sel_menu = input("Seleziona il menu: ")

        # MENU PLAYERS
        if sel_menu == "1":
            while True:
                show_player_menu()
                submenu = input("Seleziona il sottomenu: ")
                # CREATE PLAYER
                if submenu == "1":
                    print(" || CREAZIONE GIOCATORI || ")
                    while True:
                        player_name = input("Inserisci il nome del giocatore che vuoi aggiungere: ")
                        if player_name not in players_register and player_name.strip() != "":
                            registration(player_name, players_register, 1)
                            print(f"✅ Nome \"{player_name}\" inserito correttamente!")
                        elif player_name.strip() != "":
                            print("❌ Nome già in uso, scegline un altro!")
                        else:
                            break
                # SHOW PLAYERS STATS   
                elif submenu == "2":
                    print(" || ELENCO GIOCATORI E STATISTICHE || ")
                    for name in players_register:
                        print(players_register[name])
                # BACK TO MAIN MENU  
                elif submenu == "3": 
                    break
                else:
                    print("⚠️ Inserisci un valore tra 1 e 3")


            
        
        # MENU TEAMS
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
                    print("❌ Nome non presente tra quelli disponibili, controlla maiuscole e minuscole.")
                sel_name = input("Digita nome giocatore + Enter, altrimenti Enter per terminare: ").strip()
            for player in players_for_team:
                new_team.add_player(players_register[player])
        
        # CREATE MATCH
        elif sel_menu == "3":
            print("Elenco dei team presenti: ")
            for t in teams_register: 
                print(teams_register[t])

            team_a_name = ""
            team_a = None
            while team_a_name == "":
                team_a_name = input("Inserisci nome team 1: ").strip()
                if team_a_name in teams_register.keys() and team_a_name != "":
                    team_a = teams_register[team_a_name]
                    print(f"✅ Team {team_a_name} inserito correttamente!")
                    break
                else: 
                    print("❌ Nome non presente tra quelli disponibili, controlla maiuscole e minuscole.")
                    team_a_name = ""
            
            team_b_name = ""
            team_b = None
            while team_b_name == "":
                team_b_name = input("Inserisci nome team 2: ").strip()
                if team_b_name in teams_register.keys() and team_b_name != "":
                    team_b = teams_register[team_b_name]
                    print(f"✅ Team {team_b_name} inserito correttamente!")
                    break
                else: 
                    print("❌ Nome non presente tra quelli disponibili, controlla maiuscole e minuscole.")
                    team_b_name = ""
            
            new_match = Match(team_a, team_b)
            matches_register[new_match.get_name()] = new_match
            print(new_match)





if __name__ == "__main__":
    main()



