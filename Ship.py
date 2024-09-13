""" 
    Program name: Ship.py
    Description: defines the ship type
    Inputs: a list of locations
    Outputs: a ship object 
    Sources of code: None
    Authors: Connor Bennudriti, Brinley Hull, Gianni Louisa, Kyle Moore, Ben Renner
    Creation Date: 
"""

class Ship:
    def __init__(self, locations: list):
        self.locations = locations
        self.hit_segments = []
        self.destroyed: bool = False

    def hit(self):
        '''
        isDestroyed = True
        for i in self.locations:
            if i in self.hit_segments:
                isDestoryed = True
            else:
                break
        '''
        
        self.destroyed = True