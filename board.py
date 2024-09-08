""" PROLOGUE COMMENT 


"""

from Ship import Ship
from Player import Player


columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rows = range(1, 11)
str_rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', "10"]
header = '    ' + ' '.join(columns)
player_zero = Player(0)
player_one = Player(1)


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
        

def checkHit(shot: str, ship_locations: list) -> None: # ADD FUNCTIONALITY FOR SUNK SHIP HERE
    """
        checkHit(shot: str, ship_locations: list)

        Checks whether a shot is a hit or miss and prints the correct message. 
        
        Returns nothing

        Parameters
            shot: a string representing the coordinate of the shot
            ship_locations: a list of Ship locations
    """

    if shot in ship_locations: # Check if the shot hit one of the coordinates held in ship locations
        print("\nHIT!\n") # Print HIT to the console
    else: # If the shot did not hit a ship coordinate
        print("\nMISS!\n") # Print MISS to the console

    # Add condition here to check if ship completely sunk

    
def shootShip(ship_locations: list) -> str: 
    """
        shootShip(ship_locations: list)

        Allows a player to input their desired shot coordinates and returns a string representing the coordinates

        Parameters
            ship_locations: a list of enemy Ship locations
    """

    print("Choose your coordinate to shoot!")

    while True: # Loop to validate the input coordinate
        shot = input("Coordinate: ").upper() # Player inputs coordinate
        if 2 <= len(shot) <= 3 and shot[0] in columns and shot[1] in str_rows: # If the coordinate is 2 or 3 characters long and the first character is a valid column and the second character is a valid row
            if len(shot) == 3 and (shot[1] + shot[2] not in str_rows): # If the coordinate is three characters long and the two characters at the end aren't in the list of valid rows
                continue # Stay in the loop
            break # Break out of the loop

    return shot # Return the coordinate of the shot as a string

    

    
    
def checkWin(): #Check difference between shots and ship locations if all ships are shot return false
    return True
    
def initializeBoard(player_num): # When a player starts setup where they want their ships located NOT DONE
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


def takeTurn(player: Player) -> None:
    """
        turn(player: Player)

        Prints the board and allows the player to take their shot
        
        Returns nothing

        Parameters
            player: a Player instance whose turn it is
    """

    printStrikeBoard(player.number, player.strike_attempts, player.ships)
    print()
    printBoard(player.number, player.ships)
    print(f"\nPlayer {player.number}'s turn!")

    enemy_ship_locations = player_one.getShipLocations() if player.number == 0 else player_zero.getShipLocations() # Determine the ship locations of the other player
    
    while True: # Perform a while loop to avoid duplicate shots
        shot = shootShip(enemy_ship_locations) # Allow the player to choose a coordinate to shoot
        if shot not in player.strike_attempts: # If the shot has not already been taken
            break # Break out of the loop
        print("Shot already taken.\n") # Notify player that the shot was a duplicate
    checkHit(shot, enemy_ship_locations) # Check to see whether the shot was a hit or miss
    player.strike_attempts.append(shot) # Add the shot taken to the player's strike attempts

    input("Press Enter to continue...\n")
    
            
def main():
    
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
            print("Error! Please input a valid number of ships to start.") #print error and try again
    #//Ben R end
          
    while(checkWin()):

        # Initalize
        player_zero.ships = initializeBoard(0)

        player_one.ships = initializeBoard(1)

        # Player 0 turn
        takeTurn(player_zero)
        
        # Player 1 turn
        takeTurn(player_one)
    
    
main()

