"""
    Prologue Comment

    Author(s): Brinley Hull (if anyone adds to this file, add your name here)
    Creation Date: 9/7/2024
"""

from Ship import Ship # This may not be needed

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