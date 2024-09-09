"""
    Program name: Player.py
    Description: Creates a class to hold Player object information
    Inputs: 
    Outputs: 
    Sources of code: Team authored
    Authors: Connor Bennudriti, Brinley Hull, Gianni Louisa, Kyle Moore, Ben Renner
    Creation Date: 9/7/2024
"""

from Ship import Ship # Import from Ship class

class Player:
    def __init__(self, number: int):
        """
            __init__(self, number: int)

            Initializes player class instance

            Returns nothing

            Parameters
                number: an integer to identify different players
        """
        self.number = number # An integer for player identification
        self.ships = [] # A list of the player's ship objects
        self.strike_attempts = [] # A list containing a player's strikes

    def getShipLocations(self):
        """
            getShipLocations(self)

            Returns list of string ship locations/coordinates

            Parameters
                None
        """
        coordinates = [] # Initialize the locations/coordinates list

        for ship in self.ships: # For each ship in the player's ship list
            for coordinate in ship.locations: # For each coordinate in the ship's location list
                coordinates.append(coordinate) # Add it to the coordinates list

        return coordinates # Return the coordinates list