from models import Player, Team, Match

ENTER_NAME_EXIT = "Inserisci il nome del giocatore o premi Enter per tornare indietro: "
ENTER_NAME_CANCEL = "Inserisci il nome del giocatore o premi Enter per annullare: "
ENTER_VAL_RANGE = "⚠️ Inserisci un valore tra 1 e 4"
NAME_NOT_VALID = "❌ Nome non presente tra quelli disponibili, controlla maiuscole e minuscole."
SELECT_SUBMENU = "Seleziona il sottomenu: "

def registration(name, register, regtype):
    if regtype == 1:
        new_player = Player(name)
        register[name] = new_player
        return new_player
    elif regtype == 2:
        new_team = Team(name)
        register[name] = new_team
        return new_team
        
def show_main_menu():
    print("\n\n########## MAIN MENU ##########")
    print(" 1.Giocatori")
    print(" 2.Squadre")
    print(" 3.Partite")
    print(" 4.Salvataggi")

def show_player_menu():
    print("\n\n===== PLAYER MENU =====")
    print(" 1.Create Player")
    print(" 2.Show Players and Stats")
    print(" 3.Modify Player")
    print(" 4.Back to Main Menu")      

def show_player_modify_menu():
    print("\n\n===== PLAYER -> MODIFY =====")
    print(" 1.Change Name")
    print(" 2.Reset Player's Stats")
    print(" 3.Delete Player")
    print(" 4.Back to Player Menu")  

def show_team_menu():
    print("\n\n===== TEAM MENU =====")
    print(" 1.Create Team")
    print(" 2.Show Teams and Stats")
    print(" 3.Modify Team")
    print(" 4.Back to Main Menu")   

def show_match_menu():
    print("\n\n===== MATCH MENU =====")
    print(" 1.Create Match")
    print(" 2.Show Match and Stats")
    print(" 3.Modify Match")
    print(" 4.Back to Main Menu")  

def show_save_menu():
    print("\n\n===== IMPORT/EXPORT FILE MENU =====")
    print(" 1.Import file")
    print(" 2.Export file")
    print(" 3.Back to Main Menu")  
        





def main():

    players_register = {}
    teams_register = {}
    matches_register = {}

  
    #match1 = Match(team_a, team_b)
   
    sel_menu = "0"
    while sel_menu.strip()!="":
        show_main_menu()

        sel_menu = input("Seleziona il menu o premi Enter per uscire: ").strip()

        # MENU PLAYERS
        if sel_menu == "1":
            while True:
                show_player_menu()
                submenu = input("Seleziona il sottomenu: ").strip()
                # CREATE PLAYER
                if submenu == "1":
                    print(" || CREAZIONE GIOCATORI || ")
                    while True:
                        player_name = input("Inserisci il nome del giocatore che vuoi aggiungere o premi Enter per uscire: ").strip()
                        if player_name not in players_register and player_name != "":
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
                # EDIT/DELETE PLAYER
                elif submenu == "3":
                    print(" || MODIFICA O ELIMINA GIOCATORE || ")
                    while True:
                        player_name = input(ENTER_NAME_CANCEL).strip()
                        if player_name == "":
                            break
                        elif player_name in players_register:
                            player = players_register[player_name]
                            show_player_modify_menu()
                            submenu = input(SELECT_SUBMENU).strip()
                            # CHANGE NAME
                            if submenu == "1":
                                new_name = input("Inserisci il nuovo nome: ")
                                try:
                                    player.set_name(new_name)
                                    players_register.pop(player_name)
                                    players_register[new_name] = player
                                except:
                                    print("Errore!")
                                else:
                                    print(f"✅ Nome \"{player_name}\" -> \"{new_name}\" modificato correttamente!")
                            # RESET STATS
                            elif submenu == "2":
                                try:
                                    player.reset_stats()
                                except:
                                    print("Errore!")
                                else:
                                    print("Statistiche di \"{player_name}\" resettate correttamente!")
                                
                            # DELETE PLAYER
                            elif submenu == "3":
                                try:
                                    players_register.pop(player_name)
                                except:
                                    print("Errore!")
                                else:
                                    print(f"✅ Giocatore {player_name} eliminato con successo!")
                            # RETURN TO NAME INSERTION
                            elif submenu == "4":
                                continue
                            else: print(ENTER_VAL_RANGE)
                        else: print(NAME_NOT_VALID)
                # BACK TO MAIN MENU  
                elif submenu == "4": 
                    break
                else: print(ENTER_VAL_RANGE)

        # MENU TEAMS
        elif sel_menu == "2":
            while True:
                show_team_menu()
                submenu = input("Seleziona il sottomenu: ").strip()
                # CREATE TEAM
                if submenu == "1":
                    print(" || CREAZIONE SQUADRA || ")
                    while True:
                        team_name = input("Inserisci il nome dell squadra o premi Enter per uscire: ").strip()
                        if team_name == "":
                            break
                        new_team = registration(team_name, teams_register, 2)
                        print("Giocatori disponibili: ", end="")
                        for player in players_register.keys():
                            print(player, end=" ")
                        print("")
                        # choose names, append to list and foreach list's element (player name) 
                        # pick from the player objects register and add to the team object
                        print("Adesso aggiungi nomi di giocatori tra quelli disponibili.")
                        players_for_team = []
                        sel_name = input("Digita nome giocatore + Enter, altrimenti Enter per terminare: ").strip()
                        while sel_name != "":
                            if sel_name in players_register.keys():
                                players_for_team.append(sel_name)
                            else: print(NAME_NOT_VALID)
                            sel_name = input("Digita nome giocatore + Enter, altrimenti Enter per terminare: ").strip()
                        for player in players_for_team:
                            new_team.add_player(players_register[player])
                # SHOW TEAMS STATS
                elif submenu == "2":
                    print(" || ELENCO SQUADRE E STATISTICHE || ")
                    for name in teams_register:
                        print(teams_register[name])
                # EDIT/DELETE TEAM
                elif submenu == "3":
                    print(" || MODIFICA O ELIMINA SQUADRA || ")
                # BACK TO MAIN MENU
                elif submenu == "4": 
                    break
                else: print(ENTER_VAL_RANGE)
        
        # MENU MATCH
        elif sel_menu == "3":
            while True:
                show_match_menu()
                submenu = input("Seleziona il sottomenu: ").strip()
                # CREATE MATCH
                if submenu == "1":
                    while True:
                        print(" || CREAZIONE PARTITE || ")
                        choice = input("Premi 1 per l'elenco delle squadre presenti o premi Enter per uscire: ")
                        if choice == "":
                            break
                        else:
                            for t in teams_register: 
                                print(teams_register[t])
 
                        while True:
                            team_a_name = input("Inserisci nome squadra 1: ").strip()
                            if team_a_name in teams_register and team_a_name != "":
                                team_a = teams_register[team_a_name]
                                print(f"✅ Squadra {team_a_name} inserita correttamente!")
                                break
                            else: print(NAME_NOT_VALID)
                        
                        while True:
                            team_b_name = input("Inserisci nome squadra 2: ").strip()
                            if team_b_name in teams_register and team_b_name != "":
                                team_b = teams_register[team_b_name]
                                print(f"✅ Squadra {team_b_name} inserita correttamente!")
                                break
                            else: print(NAME_NOT_VALID)
                        try:
                            new_match = Match(team_a, team_b)
                            matches_register[new_match.get_name()] = new_match
                        except:
                            print("Errore!")
                        else:
                            print(f"✅ Nuova partita creata {new_match}")

                elif submenu == "2":
                    print(" || ELENCO PARTITE E STATISTICHE || ")
                    for name in matches_register:
                        print(matches_register[name])
                # EDIT/DELETE MATCH
                elif submenu == "3":
                    print(" || MODIFICA O ELIMINA PARTITA || ")
                # BACK TO MAIN MENU
                elif submenu == "4": 
                    break
                else: print(ENTER_VAL_RANGE)
        
        # MENU IMPORT/EXPORT FILE
        elif sel_menu == "4":
            while True:
                show_save_menu()
                submenu = input("Seleziona il sottomenu: ").strip()
                # IMPORT FILE
                if submenu == "1":
                    print(" || IMPORTA FILE SALVATAGGIO || ")
                # EXPORT FILE
                elif submenu == "2":
                    print(" || ESPORTA FILE SALVATAGGIO || ")
                # BACK TO MAIN MENU
                elif submenu == "3": 
                    break
                else:
                    print("⚠️ Inserisci un valore tra 1 e 3")
                





if __name__ == "__main__":
    main()



