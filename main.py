from models import Player, Team, Match

ENTER_NAME_CANCEL = "Inserisci il nome del giocatore + Enter o premi Enter per annullare/terminare: "
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
    print(" 1  -  Giocatori")
    print(" 2  -  Squadre")
    print(" 3  -  Partite")
    print(" 4  -  Salvataggi")

def show_player_menu():
    print("\n\n===== MAIN MENU >> GIOCATORI =====")
    print(" 1  -  Inserisci Giocatore")
    print(" 2  -  Mostra Giocatori e loro Statistiche")
    print(" 3  -  Modifica Giocatore")
    print(" 4  -  Torna al Menu Principale")      

def show_player_modify_menu():
    print("\n\n===== GIOCATORI >> MODIFICA GIOCATORE =====")
    print(" 1  -  Cambia Nome")
    print(" 2  -  Reset Statistiche Giocatore")
    print(" 3  -  Elimina Giocatore")
    print(" 4  -  Torna al Menu Giocatori")  

def show_team_menu():
    print("\n\n===== SQUADRE =====")
    print(" 1  -  Inserisci Squadra")
    print(" 2  -  Mostra Squadre e loro Statistiche")
    print(" 3  -  Modifica Squadra")
    print(" 4  -  Torna al Menu Principale")   

def show_team_modify_menu():
    print("\n\n===== SQUADRE >> MODIFICA SQUADRA =====")
    print(" 1  -  Cambia Nome")
    print(" 2  -  Reset Statistiche Squadra")
    print(" 3  -  Elimina Squadra")
    print(" 4  -  Torna al Menu Squadre")  

def show_match_menu():
    print("\n\n===== PARTITA =====")
    print(" 1  -  Inserisci Partita")
    print(" 2  -  Mostra Partite e loro Statistiche")
    print(" 3  -  Modifica Partite")
    print(" 4  -  Torna al Menu Principale")  

def show_save_menu():
    print("\n\n===== IMPORTA/ESPORTA FILE SALVATAGGIO =====")
    print(" 1  -  Importa file")
    print(" 2  -  Esporta file")
    print(" 3  -  Torna al Menu Principale")  
        





def main():

    players_register = {}
    teams_register = {}
    matches_register = {}

    #match1 = Match(team_a, team_b)
   
    sel_menu = "0"
    while sel_menu.strip()!="":
        show_main_menu()

        sel_menu = input("Seleziona il numero del menu + Enter o premi Enter per uscire: ").strip()

        # MENU PLAYERS
        if sel_menu == "1":
            while True:
                show_player_menu()
                submenu = input("Seleziona il sottomenu: ").strip()
                # CREATE PLAYER
                if submenu == "1":
                    print("\nCREAZIONE GIOCATORI ")
                    while True:
                        player_name = input(ENTER_NAME_CANCEL).strip()
                        if player_name not in players_register and player_name != "":
                            registration(player_name, players_register, 1)
                            print(f"✅ Nome \"{player_name}\" inserito correttamente!")
                        elif player_name.strip() != "":
                            print("❌ Nome già in uso, scegline un altro!")
                        else:
                            break
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
                                    print(f"✅ Statistiche di \"{player_name}\" resettate correttamente!")
                            # DELETE PLAYER
                            elif submenu == "3":
                                choice = input(f"Sei sicuro di voler eliminare il giocatore \"{player_name}\"? s/n: ").strip().lower()
                                if choice == "s":
                                    try:
                                        players_register.pop(player_name)
                                    except:
                                        print("Errore!")
                                    else:
                                        print(f"✅ Giocatore \"{player_name}\" eliminato con successo!")
                                else: print("Operazione annullata!")
                            # RETURN TO NAME INSERTION
                            elif submenu == "4":
                                break
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
                        for player in players_for_team:
                            new_team.add_player(players_register[player])
                        
                # SHOW TEAMS STATS
                elif submenu == "2":
                    print("\nELENCO SQUADRE E STATISTICHE ")
                    for name in teams_register:
                        print(teams_register[name])
                # EDIT/DELETE TEAM
                elif submenu == "3":
                    print("\nMODIFICA O ELIMINA SQUADRA ")
                    while True:
                        team_name = input("Inserisci il nome della squadra + Enter o premi Enter per annullare/terminare: ").strip()
                        if team_name == "":
                            break
                        elif team_name in teams_register:
                            team = teams_register[team_name]
                            show_team_modify_menu()
                            submenu = input(SELECT_SUBMENU).strip()
                            # CHANGE NAME
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
                        print("\nCREAZIONE PARTITE ")
                        choice = input("Premi 1 + Enter per l'elenco delle squadre presenti o premi Enter per annullare/terminare: ")
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
                    print("\nELENCO PARTITE E STATISTICHE ")
                    for name in matches_register:
                        print(matches_register[name])
                # EDIT/DELETE MATCH
                elif submenu == "3":
                    print("\nMODIFICA O ELIMINA PARTITA ")
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
                    print("\nIMPORTA FILE SALVATAGGIO ")
                # EXPORT FILE
                elif submenu == "2":
                    print("\nESPORTA FILE SALVATAGGIO ")
                # BACK TO MAIN MENU
                elif submenu == "3": 
                    break
                else:
                    print("⚠️ Inserisci un valore tra 1 e 3")
                





if __name__ == "__main__":
    main()



