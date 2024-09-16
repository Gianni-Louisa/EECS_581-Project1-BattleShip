"""
    Program name: Player.py
    Description: Creates a class to hold Player object information
    Inputs:
    * __init__
        -number: (int) Player's identification number.
        -color: (str) The color associated with the player, should be either 'blue' or 'green'.
        -header: (str) Header string representing column labels for the game board.
        -columns: (list of str) List of strings representing the columns on the board.
        -rows: (list of int) List of integers representing the row numbers on the board.
    * convertTextToColor
        -text: (str) The string that will be colored.
        -color: (str) A string representing the color, must be one of ['green', 'blue', 'red'].
    * printStrikeBoard
        -opponent: (Player object) The opponent player, whose ships and strike attempts will be displayed.
    * printBoard
        -opponent: (Player object) The opponent player, whose strike attempts will be considered while displaying the current player's board.
    Outputs:
    * convertTextToColor
        -Returns a string wrapped in the appropriate ANSI escape code for the specified color.
    * getShipLocations
        -Returns a list of strings where each string represents the location of one of the player's ships on the board.
    Sources of code: Chat GPT
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

    #Gianni and Connor authored
    def convertTextToColor(self, text: str, color: str) -> str:
        """
            convertTextToColor(color: str, text: str)

            Sources: Team authored

            Function to get the ascii for a string to display it as a given color ('green', 'blue', or 'red')

            Parameters:
                text: a string to  convert the the color specifed by 'color'
                color: a string in ['green', 'blue', 'red'] 

            Returns:
                The 'text' string with the appropriate color code around it
        """
        if (color == 'green'): # If the color str is 'green'
            return f'\033[32m{text}\033[0m' # Return the string surrounded by ascii that convert the text to green 
        elif color == 'blue': # If the color str is 'blue'
            return f'\033[34m{text}\033[0m' # Return the string surrounded by ascii that convert the text to blue 
        elif color == 'red': # If the color str is 'red'
            return f'\033[31m{text}\033[0m' # Return the string surrounded by ascii that convert the text to red 
        else: # If the color str is anything other than 'green', 'blue', or 'red'
            raise Exception("ERROR: Invalid color string provided") # Raise an error

    #Gianni Louisa and Connor authored, chatgpt assisted
    def printStrikeBoard(self, opponent) -> None: # Print the board with the opponent's strikes on it
        """
            printStrikeBoard(opponent: Player)

            Sources:

            Prints the board with specified player's strikes on it (misses and hits)

            Parameters:
                opponent: the opponent Player object
        """

        # Print column names
        print(self.convertTextToColor(self.header, self.color)) # Given the header string, print it in the player's color, determined by the object

        # For each row
        for row in self.rows: # For each row in the player's row list
            row_str = f"{row:2} " # Initialize the row string with the row number
            for col in self.columns: # For each column in the player's column list
                cur_pos = col+str(row) # Get the current position on the board
                if cur_pos in self.strike_attempts: # If the current position is in the player's strike attempts
                    hit = False # Initialize hit to False
                    for opponent_ship in opponent.ships: # For each ship in the opponent's ship list
                        if cur_pos in opponent_ship.locations: # If the current position is in the opponent's ship locations
                            if opponent_ship.destroyed: # If the opponent's ship is destroyed
                                row_str += self.convertTextToColor(' #', opponent.color) #show opponents color # for a destroyed ship in that location
                            else:
                                row_str += self.convertTextToColor(' O', opponent.color) #show opponents color O for a hit on a ship in that location
                            hit = True # Set hit to True
                            break # Break out of the loop
                    if not hit: # If no hit was detected
                        row_str += self.convertTextToColor(' X', 'red')  # Red X on strike for a miss
                else: # If the current position is not in the player's strike attempts
                    row_str += self.convertTextToColor(' .', self.color)  # Print a '.' in the player's color
            print(self.convertTextToColor(row_str, self.color)) # Print the row string in the player's color

    #Gianni Louisa and Connor authored, chatgpt assisted
    def printBoard(self, opponent) -> None: # Print the board with the player's ships on it, this is the normal board(bottom board)
        """
            printBoard()

            Sources:

            Prints player's board with their ships on it

            Parameters
                None
        """
        print(self.convertTextToColor(self.header, self.color)) # Print the header string in the player's color, uses objects color attribute
        for row in self.rows: # For each row in the player's row list
            row_str = self.convertTextToColor( f"{row:2} ", self.color) # Initialize the row string with the row number in the player's color
            for col in self.columns: # For each column in the player's column list
                cur_pos = col+str(row) # Get the current position on the board
                if cur_pos in opponent.strike_attempts: # If the current position is in the opponent's strike attempts
                    hit = False # Initialize hit to False
                    for my_ship in self.ships: # For each ship in the player's ship list
                        if cur_pos in my_ship.locations: # If the current position is in the player's ship locations
                            if my_ship.destroyed: # If the player's ship is destroyed
                                row_str += self.convertTextToColor(' #', 'red')  # Red # for a destroyed ship on my board. 
                            else: # If the player's ship is not destroyed
                                row_str += self.convertTextToColor(' O', 'red')  # Red O for a hit on a ship on my board
                            hit = True # Set hit to True
                            break # Break out of the loop
                    # If no hit was detected, it's a miss
                    if not hit:
                        row_str += self.convertTextToColor(' X', 'red')  # Red X for a miss on my board
                elif cur_pos in self.getShipLocations(): # If the current position is in the player's ship locations
                    row_str += self.convertTextToColor(' +', self.color) # Print a '+' in the player's color
                else: # If the current position is not in the player's strike attempts or the player's ship locations
                    row_str += self.convertTextToColor(' .', self.color) # Print a '.' in the player's color
            print(row_str) # Print the row string
        

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