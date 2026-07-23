from models import Player, Team, Match

SELECT_SUBMENU = "Seleziona il sottomenu o premi Enter per tornare indietro: "
ENTER_NAME_CANCEL = "Inserisci il nome del giocatore o premi Enter per annullare/terminare: "
ENTER_NEW_NAME = "Inserisci il nuovo nome: "
VAL_RANGE_ERR = "⚠️ Il valore deve essere compreso nel range."
VAL_TYPE_ERR = "⚠️ Hai inserito un valore non consentito."
GENERIC_ERR = "⚠️ Errore!"
NAME_NOT_VALID = "❌ Nome non presente tra quelli disponibili, controlla maiuscole e minuscole."
PLAYERS_ADDED_OK = "✅ Giocatori inseriti correttamente!"
ACTION_EXECUTED_NOERR = "✅ Azione eseguita correttamente!"
CANCELLED_OPERATION = "Operazione annullata!"

def registration(name, register, regtype):
    if regtype == 1:
        new_player = Player(name)
        register[name] = new_player
        return new_player
    elif regtype == 2:
        new_team = Team(name)
        register[name] = new_team
        return new_team
    
def get_player(players_register, player_name):
    return players_register[player_name]

def get_team(teams_register, team_name):
    return teams_register[team_name]

def get_match(match_register, match_name):
    return match_register[match_name]
        
def show_main_menu():
    print("\n\n########## MAIN MENU ##########")
    print(" 1  -  Giocatori")
    print(" 2  -  Squadre")
    print(" 3  -  Partite")
    print(" 4  -  Salvataggi")
    print(" 5  -  Esci")

def show_player_menu():
    print("\n\n===== GIOCATORI =====")
    print(" 1  -  Inserisci Giocatore")
    print(" 2  -  Mostra Giocatori e loro Statistiche")
    print(" 3  -  Modifica Giocatore") 

def show_player_modify_menu():
    print("\n\n===== GIOCATORI >> MODIFICA GIOCATORE =====")
    print(" 1  -  Cambia Nome")
    print(" 2  -  Reset Statistiche Giocatore")
    print(" 3  -  Elimina Giocatore")

def show_team_menu():
    print("\n\n===== SQUADRE =====")
    print(" 1  -  Inserisci Squadra")
    print(" 2  -  Mostra Squadre e loro Statistiche")
    print(" 3  -  Modifica Squadra")

def show_team_modify_menu():
    print("\n\n===== SQUADRE >> MODIFICA SQUADRA =====")
    print(" 1  -  Cambia Nome")
    print(" 2  -  Reset Statistiche Squadra")
    print(" 3  -  Aggiungi Giocatore da Squadra")
    print(" 4  -  Rimuovi Giocatore da Squadra")
    print(" 5  -  Elimina Squadra")

def show_match_menu():
    print("\n\n===== PARTITE =====")
    print(" 1  -  Inserisci Partita")
    print(" 2  -  Mostra Partite e loro Statistiche")
    print(" 3  -  Elimina Partita")

def show_save_menu():
    print("\n\n===== IMPORTA/ESPORTA FILE SALVATAGGIO =====")
    print(" 1  -  Importa file")
    print(" 2  -  Esporta file")
        
##################################################################################################
##################################################################################################
############################################## MAIN ##############################################
##################################################################################################
##################################################################################################

def main():

    # data structures containing main objects: players, teams and matches
    players_register = {}
    teams_register = {}
    matches_register = []

    while True:
        show_main_menu()
        sel_menu = input("Seleziona il numero del menu: ").strip()
        
        # MENU PLAYERS
        if sel_menu == "1":
            while True:
                show_player_menu()
                submenu = input(SELECT_SUBMENU).strip()

                # CREATE PLAYER
                if submenu == "1":
                    print("\nCREAZIONE GIOCATORI ")
                    while True:
                        player_name = input(ENTER_NAME_CANCEL).strip()
                        if not player_name:
                            break
                        if player_name in players_register:
                            print("❌ Nome già in uso, scegline un altro!")
                            continue
                        try: 
                            registration(player_name, players_register, 1)
                            print(f"✅ Nome \"{player_name}\" inserito correttamente!")
                        except Exception as e: 
                            print(f"⚠️ Errore, registrazione giocatore fallita: {e}")
             
                # SHOW PLAYERS STATS   
                elif submenu == "2":
                    print("\nELENCO GIOCATORI E STATISTICHE ")
                    for name in players_register:
                        print(players_register[name])

                # EDIT/DELETE PLAYER
                elif submenu == "3":
                    print("\nMODIFICA O ELIMINA GIOCATORE ")
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
                                new_name = input(ENTER_NEW_NAME)
                                try:
                                    player.set_name(new_name)
                                    players_register.pop(player_name)
                                    players_register[new_name] = player
                                except:
                                    print(GENERIC_ERR)
                                else:
                                    print(f"✅ Nome \"{player_name}\" -> \"{new_name}\" modificato correttamente!")
                            # RESET STATS
                            elif submenu == "2":
                                try:
                                    player.reset_stats()
                                except:
                                    print(GENERIC_ERR)
                                else:
                                    print(f"✅ Statistiche di \"{player_name}\" resettate correttamente!")
                            # DELETE PLAYER
                            elif submenu == "3":
                                choice = input(f"Sei sicuro di voler eliminare il giocatore \"{player_name}\"? s/n: ").strip().lower()
                                if choice == "s":
                                    try:
                                        players_register.pop(player_name)
                                    except:
                                        print(GENERIC_ERR)
                                    else:
                                        print(f"✅ Giocatore \"{player_name}\" eliminato con successo!")
                                else: print(CANCELLED_OPERATION)
                            # RETURN TO NAME INSERTION
                            elif submenu == "4":
                                break
                            else: print(VAL_RANGE_ERR)
                        else: print(NAME_NOT_VALID)
                # BACK TO MAIN MENU  
                elif submenu == "": 
                    break
                else: print(VAL_RANGE_ERR)

        # MENU TEAMS
        elif sel_menu == "2":
            while True:
                show_team_menu()
                submenu = input(SELECT_SUBMENU).strip()
                # CREATE TEAM
                if submenu == "1":
                    print("\nCREAZIONE SQUADRA ")
                    while True:
                        team_name = input("Inserisci il nome della squadra da creare + Enter o premi Enter per annullare/terminare: ").strip()
                        if team_name == "":
                            break
                        new_team = registration(team_name, teams_register, 2)
                        print("Giocatori disponibili: ", end="")
                        for player in players_register.keys():
                            print(player, end=" ")
                        print("\n")
                        # choose names, append to list and foreach list's element (player name) 
                        # pick from the player objects register and add to the team object
                        print("Adesso aggiungi nomi di giocatori tra quelli disponibili da aggiungere alla squadra creata.")
                        players_for_team = []
                        sel_name = input(ENTER_NAME_CANCEL).strip()
                        while sel_name != "":
                            if sel_name in players_register.keys():
                                players_for_team.append(sel_name)
                            else: print(NAME_NOT_VALID)
                            sel_name = input(ENTER_NAME_CANCEL).strip()
                        try:
                            for player in players_for_team:
                                new_team.add_player(players_register[player])
                        except: print(GENERIC_ERR)
                        else: print(PLAYERS_ADDED_OK)
                        
                # SHOW TEAMS STATS
                elif submenu == "2":
                    print("\nELENCO SQUADRE E STATISTICHE ")
                    for name in teams_register:
                        print(teams_register[name])
                # EDIT/DELETE TEAM
                elif submenu == "3":
                    while True:
                        print("\nMODIFICA O ELIMINA SQUADRA ")
                        team_name = input("Inserisci il nome della squadra da modificare + Enter o premi Enter per annullare/terminare: ").strip()
                        if team_name == "":
                            break
                        elif team_name in teams_register:
                            team = teams_register[team_name]
                            show_team_modify_menu()
                            submenu = input(SELECT_SUBMENU).strip()
                            # CHANGE NAME
                            if submenu == "1":
                                new_name = input(ENTER_NEW_NAME)
                                try:
                                    team.set_name(new_name)
                                    teams_register.pop(team_name)
                                    teams_register[new_name] = team
                                except:
                                    print(GENERIC_ERR)
                                else:
                                    print(f"✅ Nome \"{team_name}\" -> \"{new_name}\" modificato correttamente!")
                            # RESET TEAM STATS
                            elif submenu == "2":
                                try:
                                    team.reset_stats()
                                except:
                                    print(GENERIC_ERR)
                                else:
                                    print(f"✅ Statistiche di \"{team_name}\" resettate correttamente!")
                            # ADD PLAYER TO TEAM
                            elif submenu == "3":
                                print("Giocatori disponibili: ", end="")
                                for player in players_register.keys():
                                    print(player, end=" ")
                                print("\n")
                                print("Adesso aggiungi nomi di giocatori tra quelli disponibili da aggiungere alla squadra.")
                                
                                players_for_team = []
                                sel_name = input(ENTER_NAME_CANCEL).strip()
                                while sel_name != "":
                                    if sel_name in players_register:
                                        players_list = team.get_players()
                                        player = players_register[sel_name]
                                        if player not in players_list:
                                            players_for_team.append(sel_name)
                                            print("Nome valido.")
                                        else: print("Giocatore già in squadra.")
                                    else: print(NAME_NOT_VALID)
                                    sel_name = input(ENTER_NAME_CANCEL).strip()
                                try:
                                    for player in players_for_team:
                                        new_team.add_player(players_register[player])
                                except: print(GENERIC_ERR)
                                else: print(PLAYERS_ADDED_OK)
                            # DELETE PLAYER FROM TEAM
                            elif submenu == "4":
                                player_name = input("Inserisci il nome del giocatore da rimuovere + Enter o premi Enter per annullare/terminare: ").strip()
                                # get player func
                                if player_name in players_register:
                                    player = players_register[player_name]
                                    if player in team.get_players():
                                        choice = input(f"Sei sicuro di voler eliminare il giocatore \"{player_name}\" dalla squadra? s/n: ").strip().lower()
                                        if choice == "s":
                                            try:
                                                team.remove_player(player)
                                            except:
                                                print(GENERIC_ERR)
                                            else:
                                                print(f"✅ Giocatore \"{player_name}\" eliminato dalla squadra con successo!")
                                        else: print(CANCELLED_OPERATION)
                                    else: print("Giocatore non presente in squadra!")
                                else: print(NAME_NOT_VALID)
                            # DELETE TEAM
                            elif submenu == "5":
                                choice = input(f"Sei sicuro di voler eliminare la squadra \"{team_name}\"? s/n: ").strip().lower()
                                if choice == "s":
                                    try:
                                        teams_register.pop(team_name) # team.remove_player(team_name)
                                    except:
                                        print(GENERIC_ERR)
                                    else:
                                        print(f"✅ Giocatore \"{player_name}\" eliminato con successo!")
                                else: print(CANCELLED_OPERATION)
                            # RETURN TO TEAM MENU
                            elif submenu == "6":
                                break
                            else: print(VAL_RANGE_ERR)
                        else: print(NAME_NOT_VALID)
                # BACK TO MAIN MENU
                elif submenu == "": 
                    break
                else: print(VAL_RANGE_ERR)
        
        # MENU MATCH
        elif sel_menu == "3":
            while True:
                show_match_menu()
                submenu = input(SELECT_SUBMENU).strip()
                # CREATE MATCH
                if submenu == "1":
                    while True:
                        print("\nCREAZIONE PARTITE")
                        choice = input("Premi 1 per l'elenco delle squadre presenti o premi Enter per annullare/terminare: ")
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
                        
                        while True:
                            try:
                                score_a = int(input(f"Inserisci il punteggio di {team_a_name}: "))
                                score_b = int(input(f"Inserisci il punteggio di {team_b_name}: "))
                                break
                            except ValueError:
                                print(VAL_TYPE_ERR)

                        try:
                            new_match = Match(team_a, team_b, score_a, score_b)
                            matches_register.append(new_match)
                            #matches_register[new_match.get_name()] = new_match # only for dict
                        except:
                            print(GENERIC_ERR)
                        else:
                            print(f"✅ Nuova partita creata {new_match}")
                # SHOW MATCH STATS
                elif submenu == "2":
                    print("\nELENCO PARTITE E STATISTICHE ")
                    for name in matches_register:
                        print(name) # matches_register[name] for dict insert in print
                # DELETE MATCH
                elif submenu == "3":
                    while True:
                        print("\nELIMINA PARTITA ")
                        print("Elenco partite")
                        counter = 0
                        for match in matches_register:
                            counter += 1
                            print(f"{counter}. {match}") #matches_register[match] for dict insert in print
                        match_sel = input("Inserisci il numero della partita da cancellare o premi Enter per annullare/terminare: ").strip() 
                        if match_sel == "":
                            break
                        if match_sel.isdigit():
                            match_number = int(match_sel)
                            print(match_number)
                        else:
                            print(VAL_TYPE_ERR)
                            break
                        if match_number <= counter and match_number > 0:
                            match_to_delete = matches_register[match_number-1]
                            choice = input(f"Sei sicuro di voler eliminare la partita \"{match_to_delete.get_name()}\" del {match_to_delete.get_date()}? s/n: ").strip().lower()
                            if choice == "s":
                                try: matches_register.remove(match_to_delete) #matches_register.pop(match_to_delete)
                                except: print(GENERIC_ERR)
                                else: print(f"✅ Partita \"{match_to_delete}\" eliminata con successo!")
                            elif choice == "no": print(CANCELLED_OPERATION)
                            else: print(VAL_TYPE_ERR)
                        else: print(VAL_RANGE_ERR)
                # BACK TO MAIN MENU
                elif submenu == "": 
                    break
                else: print(VAL_RANGE_ERR)
        
        # MENU IMPORT/EXPORT FILE
        elif sel_menu == "4":
            while True:
                show_save_menu()
                submenu = input(SELECT_SUBMENU).strip()
                # IMPORT FILE
                if submenu == "1":
                    print("\nIMPORTA FILE SALVATAGGIO ")
                # EXPORT FILE
                elif submenu == "2":
                    print("\nESPORTA FILE SALVATAGGIO ")
                # BACK TO MAIN MENU
                elif submenu == "": 
                    break
                else:
                    print(VAL_RANGE_ERR)
        
        elif sel_menu == "5":
            break

        else: print(VAL_RANGE_ERR)
                





if __name__ == "__main__":
    main()



