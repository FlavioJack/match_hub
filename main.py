

def main():
    print("Selezionare una scelta dal menu: ")
    print("""
            1. Area tornei
            2. Partite
            3. Classifica
            4. Giocatori """)

    selection = int(input())
    
    while(selection > 4 or selection < 1):
        print("!!! Hai inserito un valore errato !!!")
        selection = int(input())
    
    return







if __name__ == "__main__":
    main()



