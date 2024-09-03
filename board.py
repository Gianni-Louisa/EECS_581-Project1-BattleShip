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

def printStrikeBoard(player_num: int, player_strike_attempts: list, opponent_ship_locations: list) -> None: 
    """
        printStrikeBoard(player_num: int, player_strike_attempts: list, opponent_ship_locations: list)

        Prints the board with specified player's strikes on it misses and hits

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
                if cur_pos in opponent_ship_locations:
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




def printBoard(player_num: int, ship_locations: list):
    """
        printBoard(player_num: int, ship_locations: list)

        Prints your board with your ships on it and the enemy's strikes and misses

        Parameters
            player_num: an int specifying the number of the player
            ship_locations: a list of strings specifying where the player's ships are
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
            if cur_pos in ship_locations:
                # Print a + 
                row_str += ' +'
            # If position does not contain a ship
            else:
                # Print a .
                row_str += ' .'
        print(convertTextToColor(row_str, player_color_dict[player_num]))
        



    
def shootShip(ship_locations): #ask for input and add to the shot array to show on board, check if hit or miss
    print()
    
def checkWin(): #Check difference between shots and ship locations if all ships are shot return false
    return True
    
def initializeBoard(player_num): #When a player starts setup where they want their ships located NOT DONE
    if player_num == 0: 
        # return(["B4","B3","B2","B1","J10","J9"])
        return(["B4","B3","B2","B1", 'F5', 'F6'])
    elif player_num == 1:
        # return(["A4","A3","A2","E1","E10","E9"])
        return(["A4","A3","A2","E1", 'E2', 'E3'])
    else:
        raise Exception("ERROR: invalid player_num")

    
    
            
def main():
    while(checkWin()):

        # Initalize
        player_zero_ship_locations = initializeBoard(0)
        player_zero_strike_attempts = ["A2", 'A3', "E1","E2","E9","J10","J9"]
        player_one_ship_locations = initializeBoard(1)
        player_one_strike_attempts = ["B4","B3","B2","E1"]

        # Player 0 turn
        printStrikeBoard(0, player_zero_strike_attempts, player_one_ship_locations)
        print()
        printBoard(0, player_zero_ship_locations)
        # shootShip(player_zero_ship_locations)
        input("\nPress Enter to continue...\n")
        

        # Player 1 turn
        printStrikeBoard(1, player_one_strike_attempts, player_zero_ship_locations)
        print()
        printBoard(1, player_one_ship_locations)
        # shootShip(player_one_ship_locations)
        input("\nPress Enter to continue...\n")
    
    
main()

