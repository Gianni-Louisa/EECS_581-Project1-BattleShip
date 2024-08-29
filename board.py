columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rows = range(1, 11)
header = '   ' + ' '.join(columns)


def printBoardPlayer1(shipLocations):#BLUE PLAYER #Prints your board with your ships on it and the enemy's strikes and misses
    print('\033[34m' + header + '\033[0m')
    for row in rows:
        row_str = f"{row:2} "
        for col in columns:
            if col + str(row) in shipLocations:
                row_str += ' +'
            else:
                row_str += ' .'
        print('\033[34m' + row_str + '\033[0m') 

def printBoardPlayer2(shipLocations): #GREEN PLAYER
    print('\033[32m' + header + '\033[0m')
    for row in rows:
        row_str = f"{row:2} "
        for col in columns:
            if col + str(row) in shipLocations:
                row_str += ' +'
            else:
                row_str += ' .'
        print('\033[32m' + row_str + '\033[0m')

def printStrikeBoardPlayer1(shipLocations, strikes): #Prints the board with your strikes on it misses and hits
    print('\033[34m' + header + '\033[0m')
    for row in rows:
        row_str = f"{row:2} "
        for col in columns:
            if col + str(row) in strikes:
                if col + str(row) in shipLocations:
                    row_str += ' \033[31mX\033[0m'  # Red X
                else:
                    row_str += ' \033[32mO\033[0m'  # Green O
            else:
                row_str += ' \033[34m.\033[0m' 
        print('\033[34m' + row_str + '\033[0m')

def printStrikeBoardPlayer2(shipLocations, strikes):
    print('\033[32m' + header + '\033[0m')
    for row in rows:
        row_str = f"{row:2} "
        for col in columns:
            if col + str(row) in strikes:
                if col + str(row) in shipLocations:
                    row_str += ' \033[31mX\033[0m'  # Red X
                else:
                    row_str += ' \033[34mO\033[0m'  # Blue O
            else:
                row_str += ' \033[32m.\033[0m'
        print('\033[32m' + row_str + '\033[0m')
        
    
def shootShip(shipLocations): #ask for input and add to the shot array to show on board, check if hit or miss
    print()
    
def checkWin(): #Check difference between shots and ship locations if all ships are shot return false
    return True
    
def initializeBoard(playerNum): #When a player starts setup where they want their ships located NOT DONE
    if 1 == playerNum: 
        return(["B4","B3","B2","B1","J10","J9"])
    else:
        return(["A4","A3","A2","E1","E10","E9"])

    
    
            
def main():
    
    while(checkWin()):
        printStrikeBoardPlayer1(initializeBoard(2), ["A2","E1","E1","E9","J10","J9"])
        print()
        printBoardPlayer1(initializeBoard(1))
        shootShip(initializeBoard(1))
        input("\nPress Enter to continue...\n")
        
        
        printStrikeBoardPlayer2(initializeBoard(1), ["B4","B3","B2","E1"] )
        print()
        printBoardPlayer2(initializeBoard(2))
        shootShip(initializeBoard(2))
        input("\nPress Enter to continue...\n")
    
    
main()

