from Ship import Ship


columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rows = range(1, 11)
header = '    ' + ' '.join(columns)


def convertTextToColor(text: str, color: str) -> str:
    """
        convertTextToColor(color: str, text: str)

        Function to get the ascii for a string to display it as a given color ('green', 'blue', or 'red')

        Parameters:
            text: a string to  convert the the color specifed by 'color'
            color: a string in ['green', 'blue', 'red'] 

        Returns:
            The 'text' string with the appropriate color code around it
    """
    if (color == 'green'):
        return f'\033[32m{text}\033[0m'
    elif color == 'blue':
        return f'\033[34m{text}\033[0m'
    elif color == 'red':
        return f'\033[31m{text}\033[0m'
    else:
        raise Exception("ERROR: Invalid color string provided")


# Dict to associate players' numbers with their colors 
player_color_dict = {
    0: 'blue',
    1: 'green'
}

def printStrikeBoard(player_num: int, player_strike_attempts: list, opponent_ships: list) -> None: 
    """
        printStrikeBoard(player_num: int, player_strike_attempts: list, opponent_ships: list)

        Prints the board with specified player's strikes on it (misses and hits)

        Parameters:
            player_num: an integer specifying which player's strike board to print
            player_strike_attempts: a list of strings specifying where player has shot
            opponent_ship_locations: a list of strings specifying where the enemy ships are
    """

    # Print column names
    print(convertTextToColor(header, player_color_dict[player_num]))

    # For each row
    for row in rows:
        row_str = f"{row:2} "
        # For each column
        for col in columns:
            cur_pos = col+str(row)
            # If the current position has been shot at by the player
            if cur_pos in player_strike_attempts:
                # Check if that position contains an enemy ship
                if cur_pos in [loc for ship in opponent_ships for loc in ship.locations]:
                    # Print an 'O' in the opponents color for a hit
                    row_str += convertTextToColor(' O', player_color_dict[abs(player_num-1)]) # abs(player_num-1) gets opponents player_num (eg for player 0 -> abs(0-1) = 1)
                # If position does not have an enemy ship, print a red X
                else:
                    row_str += convertTextToColor(' X', 'red')  # Red X
            # If position has not been shot at by player, print a '.' in the color of the player
            else:
                row_str += convertTextToColor(' .', player_color_dict[player_num]) 
        # Print the created string for the current row
        print(convertTextToColor(row_str, player_color_dict[player_num]))




def printBoard(player_num: int, ships: list):
    """
        printBoard(player_num: int, ship_locations: list)

        Prints player's board with their ships on it

        Parameters
            player_num: an int specifying the number of the player
            ships: a list of Ship objects for the player
    """
    # Print column names
    print(convertTextToColor(header, player_color_dict[player_num]))

    # For each row
    for row in rows:
        row_str = f"{row:2} "
        # For each column
        for col in columns:
            # Get current location on board
            cur_pos = col+str(row)
            # If position contains a ship
            if cur_pos in [loc for ship in ships for loc in ship.locations]:
                # Print a '+' 
                row_str += ' +'
            # If position does not contain a ship
            else:
                # Print a '.'
                row_str += ' .'
        print(convertTextToColor(row_str, player_color_dict[player_num]))
        

def checkHit(shot, ship_locations): # Check whether a shot is a hit or miss and print the correct message
    if shot in ship_locations: # Check whether the shot hit one of the coordinates held in ship locations
        print("\nHIT!\n")
    else:
        print("\nMISS!\n")

    
def shootShip(ship_locations): # Ask for input coordinates and add to the shot array to show on board, check if hit or miss
    print("\nChoose your coordinate to shoot!")

    column = input("Enter a valid column (A-J): ").upper() # Player inputs column

    # Input validation loop. If not valid, continue to ask for a valid column
    while column not in columns: 
        column = input("Enter a valid column (A-J): ").upper() # Player inputs column
    
    validRow = False # Loop condition variable

    # Input validation loopa. If not valid, continue to ask for a valid row
    while not validRow:
        row = input("Enter a valid row (1-10): ") # Player inputs row
        for i in rows:
            if row == str(i): # If the input is a valid input, break the loop
                validRow = True 
                break

    shot = column + row # Combine column and row to make a valid coordinate

    checkHit(shot, ship_locations) # Check to see whether the shot was a hit or miss

    return shot

    

    
    
def checkWin(): #Check difference between shots and ship locations if all ships are shot return false
    return True
    
def initializeBoard(player_num): #When a player starts setup where they want their ships located NOT DONE
    if player_num == 0: 
        return [
            Ship(['B4','B3','B2','B1']), 
            Ship(['F1','F2','F3'])
        ]
    elif player_num == 1:
        return [
            Ship(['A1','A2']), 
            Ship(['G4','G5','G6']), 
            Ship(['F1','F2'])
        ]
    else:
        raise Exception("ERROR: invalid player_num")

    
    
            
def main():
    # Initialize Variables
    player_zero_strike_attempts = []
    player_one_strike_attempts = []
    player_zero_ship_locations = []
    player_one_ship_locations = []
    #//Ben R start
    valid_num_ships = ['1','2','3','4','5'] #used to check if user chose the correct number of ships
    goodInput = False #used for while loop to check for a correct input num of ships
    
    #choosing the number of ships 
    print("Welcome to Battle Ship!")
    while goodInput == False: #runs until we get a good input
        numShips = input("Choose the number of ships you wish to play with! (1-5): ") #inputted number of ships for the game
        if numShips in valid_num_ships: #used to break the loop if numShips in valid_num_ships
            goodInput = True #break loop
            numShips = int(numShips) #now we want it to be a type int for later
        else:
            print("Error! Please input a valid number of ships to start.")
    #//Ben R end
          
    while(checkWin()):

        # Initalize
        player_zero_ships = initializeBoard(0)

        player_one_ships = initializeBoard(1)

        # Player 0 turn
        printStrikeBoard(0, player_zero_strike_attempts, player_one_ships)
        print()
        printBoard(0, player_zero_ships)
        player_zero_strike_attempts.append(shootShip(player_zero_ship_locations))
        input("Press Enter to continue...\n")
        

        # Player 1 turn
        printStrikeBoard(1, player_one_strike_attempts, player_zero_ships)
        print()
        printBoard(1, player_one_ships)
        player_one_strike_attempts.append(shootShip(player_one_ship_locations))
        input("Press Enter to continue...\n")
    
    
main()

