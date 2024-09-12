"""
    Program name: Player.py
    Description: Creates a class to hold Player object information
    Inputs: 
    Outputs: 
    Sources of code: Team authored and ?
    Authors: Connor Bennudriti, Brinley Hull, Gianni Louisa, Kyle Moore, Ben Renner
    Creation Date: 9/7/2024
"""


class Player:
    def __init__(self, number: int, color: str, header: str, columns: list, rows: list):
        """
            __init__(self, number: int)

            Sources: Team authored

            Initializes player class instance

            Returns nothing

            Parameters
                number: an integer to identify different players
                color: a str in ['blue', 'green'] for printing a colored player board
                header: the header string of the column labels for printing
                columns: list of column letter strings
                rows: list of the row numbers
        """
        self.number = number # An integer for player identification
        self.color = color # Color of the player
        self.header = header # Header string for column labels
        self.columns = columns # List of column letters
        self.rows = rows # The row numbers

        self.ships = [] # A list of the player's ship objects
        self.strike_attempts = [] # A list containing a player's strikes

    def convertTextToColor(self, text: str, color: str) -> str:
        """
            convertTextToColor(color: str, text: str)

            Sources: 

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

    def printStrikeBoard(self, opponent) -> None: 
        """
            printStrikeBoard(opponent: Player)

            Sources:

            Prints the board with specified player's strikes on it (misses and hits)

            Parameters:
                opponent: the opponent Player object
        """

        # Print column names
        print(self.convertTextToColor(self.header, self.color))

        # For each row
        for row in self.rows:
            row_str = f"{row:2} "

            # For each column
            for col in self.columns:
                cur_pos = col+str(row)
                # If the current position has been shot at by the player
                if cur_pos in self.strike_attempts:
                    # Go through the opponent ships 
                    hit = False
                    for opponent_ship in opponent.ships:
                        # Check if opponent has guessed where our ship is 
                        if cur_pos in opponent_ship.locations:
                            # If the ship is destroyed, print a # in the color of the player
                            if opponent_ship.destroyed:
                                row_str += self.convertTextToColor(' #', opponent.color) # Opponent's color for a destroyed ship
                            else:
                                row_str += self.convertTextToColor(' O', opponent.color) # Opponent's color for a hit
                            hit = True
                            break
                    # If no hit was detected, it's a miss
                    if not hit:
                        row_str += self.convertTextToColor(' X', 'red')  # Red X for a miss
                # If position has not been shot at by player, print a '.'
                else:
                    row_str += self.convertTextToColor(' .', self.color) 
            # Print the created string for the current row
            print(self.convertTextToColor(row_str, self.color))

    def printBoard(self, opponent) -> None:
        """
            printBoard()

            Sources:

            Prints player's board with their ships on it

            Parameters
                None
        """
        # Print column names
        print(self.convertTextToColor(self.header, self.color))

        # For each row
        for row in self.rows:
            row_str = self.convertTextToColor( f"{row:2} ", self.color)
            # For each column
            for col in self.columns:
                # Get current location on board
                cur_pos = col+str(row)
                # If position contains a ship
                if cur_pos in opponent.strike_attempts:
                   
                    hit = False
                    for my_ship in self.ships:
                       
                        if cur_pos in my_ship.locations:

                            if my_ship.destroyed:
                                row_str += self.convertTextToColor(' #', 'red') 
                            else:
                                row_str += self.convertTextToColor(' O', 'red') 
                            hit = True
                            break
                    # If no hit was detected, it's a miss
                    if not hit:
                        row_str += self.convertTextToColor(' X', 'red')  # Red X for a miss
                #print a + if a ship is there
                elif cur_pos in self.getShipLocations():
                    # Print a '+' 
                    row_str += self.convertTextToColor(' +', self.color)
                # If position has not been shot at by player, print a '.'
                else:
                    # Print a '.'
                    row_str += self.convertTextToColor(' .', self.color)
            print(row_str)
        

    def getShipLocations(self) -> None:
        """
            getShipLocations(self)

            Sources: Team authored

            Returns list of string ship locations/coordinates

            Parameters
                None
        """
        coordinates = [] # Initialize the locations/coordinates list

        for ship in self.ships: # For each ship in the player's ship list
            for coordinate in ship.locations: # For each coordinate in the ship's location list
                coordinates.append(coordinate) # Add it to the coordinates list

        return coordinates # Return the coordinates list