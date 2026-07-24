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

def player_registration(name, register):
    new_player = Player(name)
    register[name] = new_player
    # return new_player

def team_registration(name, register):
    new_team = Team(name)
    register[name] = new_team
    return new_team

def available_players(players_register):
    players_list = ", ".join(players_register)+";"
    return players_list
    
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
    print(" 3  -  Aggiungi Giocatore a Squadra")
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

                # BACK TO MAIN MENU  
                if not submenu:
                    break

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
                            player_registration(player_name, players_register)
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

                        # BACK TO PLAYER MENU
                        if not player_name:
                            break
                        if player_name in players_register:
                            player = players_register[player_name]
                            show_player_modify_menu()
                            submenu = input(SELECT_SUBMENU).strip()

                            # RETURN TO PLAYER MENU
                            if not submenu:
                                break

                            # CHANGE NAME
                            if submenu == "1":
                                new_name = input(ENTER_NEW_NAME)
                                try:
                                    player.set_name(new_name)
                                    players_register.pop(player_name)
                                    players_register[new_name] = player
                                    print(f"✅ Nome \"{player_name}\" -> \"{new_name}\" modificato correttamente!")
                                except Exception as e:
                                    print(GENERIC_ERR, e)
                                    
                            # RESET STATS
                            elif submenu == "2":
                                try:
                                    player.reset_stats()
                                    print(f"✅ Statistiche di \"{player_name}\" resettate correttamente!")
                                except Exception as e:
                                    print(GENERIC_ERR, e)
                                    
                            # DELETE PLAYER
                            elif submenu == "3":
                                choice = input(f"Sei sicuro di voler eliminare il giocatore \"{player_name}\"? s/n: ").strip().lower()
                                if choice == "s":
                                    try:
                                        players_register.pop(player_name)
                                        print(f"✅ Giocatore \"{player_name}\" eliminato con successo!")
                                    except Exception as e:
                                        print(GENERIC_ERR, e)       
                                else: print(CANCELLED_OPERATION)

                            else: print(VAL_RANGE_ERR)
                        else: print(NAME_NOT_VALID)
                else: print(VAL_RANGE_ERR)

        # MENU TEAMS
        elif sel_menu == "2":
            while True:
                show_team_menu()
                submenu = input(SELECT_SUBMENU).strip()

                # BACK TO MAIN MENU
                if not submenu:
                    break

                # CREATE TEAM
                if submenu == "1":
                    print("\nCREAZIONE SQUADRA ")
                    while True:
                        team_name = input("Inserisci il nome della squadra da creare + Enter o premi Enter per annullare/terminare: ").strip()

                        # BACK TO TEAM MENU
                        if not team_name:
                            break

                        if team_name not in teams_register:
                            try:
                                new_team = team_registration(team_name, teams_register)
                                print("✅ Creazione squadra avvenuta con successo")
                            except Exception as e: print(GENERIC_ERR, e)
                        else: 
                            print("⚠️ Nome squadra già presente!")
                            continue

                        print("Giocatori disponibili: ", end="")
                        print(available_players(players_register))
                        print("Adesso aggiungi alla tua squadra i nomi dei giocatori tra quelli disponibili.")
                        temp_players_list = []
                        
                        while True:
                            sel_name = input(ENTER_NAME_CANCEL).strip()
                            if not sel_name:
                                break
                            if sel_name in players_register:
                                temp_players_list.append(sel_name)
                            else: print(NAME_NOT_VALID)

                        if temp_players_list:
                            try:
                                for player in temp_players_list:
                                    new_team.add_player(players_register[player])
                                print(PLAYERS_ADDED_OK)
                                temp_players_list.clear()
                            except Exception as e: print(GENERIC_ERR, e)
                        else: print("Lista vuota, nessun giocatore aggiunto alla squadra.")
                        
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

                        # BACK TO TEAM MENU
                        if not team_name:
                            break

                        if team_name in teams_register:
                            team = teams_register[team_name]
                            show_team_modify_menu()
                            submenu = input(SELECT_SUBMENU).strip()

                            # RETURN TO TEAM MENU
                            if not submenu:
                                break

                            # CHANGE NAME
                            if submenu == "1":
                                while True:
                                    new_name = input(ENTER_NEW_NAME).strip()
                                    if new_name:
                                        break
                                try:
                                    team.set_name(new_name)
                                    teams_register.pop(team_name)
                                    teams_register[new_name] = team
                                    print(f"✅ Nome team \"{team_name}\" -> \"{new_name}\" modificato correttamente!")
                                except Exception as e: print(GENERIC_ERR, e)
                                    
                            # RESET TEAM STATS
                            elif submenu == "2":
                                try:
                                    team.reset_stats()
                                    print(f"✅ Statistiche di \"{team_name}\" resettate correttamente!")
                                except Exception as e: print(GENERIC_ERR, e)
                                    
                            # ADD PLAYER TO TEAM
                            elif submenu == "3":
                                print("Giocatori disponibili: ", end="")
                                print(available_players(players_register))
                                
                                print("Adesso aggiungi nomi di giocatori tra quelli disponibili da aggiungere alla squadra.")
                                temp_players_list = []
                                
                                while True:
                                    sel_name = input(ENTER_NAME_CANCEL).strip()

                                    # BACK TO "ENTER TEAM NAME" FOR MODIFY TEAM MENU
                                    if not sel_name:
                                        break
                                    if sel_name in players_register:
                                        team_players = team.get_players()
                                        player = players_register[sel_name]
                                        if player not in team_players and sel_name not in temp_players_list:
                                            temp_players_list.append(sel_name)
                                            print("Nome valido, aggiunto alla lista dei nomi da aggiungere alla squadra.")
                                        else: print("Giocatore già in squadra.")
                                    else: print(NAME_NOT_VALID)

                                while temp_players_list:
                                    choice = input("Vuoi aggiungere i nuovi nomi? s/n: ").lower()
                                    if choice == "s":
                                        try:
                                            for player in temp_players_list:
                                                new_team.add_player(players_register[player])
                                            print(PLAYERS_ADDED_OK)
                                            temp_players_list.clear() 
                                            break
                                        except Exception as e: print(GENERIC_ERR, e)
                                    elif choice == "n": 
                                        print(CANCELLED_OPERATION)
                                        temp_players_list.clear()
                                        break
                                    else: print(VAL_TYPE_ERR)
#--------------------------------------------------------------------------------------------------------------------------------
# CONTINUA REFACTORING DA QUI
#   |       |       |
#   V       V       V

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
                            else: print(VAL_RANGE_ERR)
                        else: print(NAME_NOT_VALID)
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



