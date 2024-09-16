""" 
    Program name: Ship.py
    Description: defines the ship type
    Inputs: a list of locations
    Outputs: a ship object 
    Sources of code: None
    Authors: Connor Bennudriti, Brinley Hull, Gianni Louisa, Kyle Moore, Ben Renner
    Creation Date: 9/7/2024
"""

class Ship:
    def __init__(self, locations: list):
        """
            __init__(self, locations: list)

            Sources: Team authored

            Initalized the Ship class

            Returns None

            Parameters:
                locations: A list of board locations where ship segments are located
        """
        self.locations = locations # A list of board locations where ship segments are located
        self.hit_segments = [] # A list containing the locations of ship segments that have been hit
        self.destroyed: bool = False # A bool to sinify if the ship has been destroyed (all segments hit)
